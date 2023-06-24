from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re
import time
import pandas as pd

columns = ["book_name", "author(s)", "publisher", "language", "#pages", "customer_reviews", "total_ratings", "best_seller_rank", "price_paperback"]

def scrape_data(driver, url):
    # url = url
    contents = {}
    driver.get(url)

    # get book data
    book_name = driver.find_element(By.ID, 'productTitle').text

    # get author(s) name, if more than 1 author join them with comma (,)
    try:
        author = driver.find_element(By.ID, "moreAboutTheAuthorCard_feature_div").find_elements(By.TAG_NAME, 'h2')[1:]
        if len(author) >= 2:
            authors = ','.join([auth.text for auth in author])
        else:
            authors = [auth.text for auth in author][0]
    
    except IndexError:
        author = driver.find_element(By.ID, 'bylineInfo').find_elements(By.CSS_SELECTOR, 'span.author.notFaded')
        if len(author) > 1:
            authors = ','.join([auth.text.replace(' (Author),', '') for auth in author if "Author" in auth.text])
        else:
            authors = [auth.text.replace(' (Author)') for auth in author][0]

    # get book details
    details = [d.text for d in driver.find_element(By.ID, "detailBulletsWrapper_feature_div").find_elements(By.TAG_NAME, 'li')]

    # get book price
    try:
        price = driver.find_element(By.ID, 'price')
    
    except NoSuchElementException:
        price = driver.find_element(By.CSS_SELECTOR, 'span.a-price.a-text-price.header-price.a-size-base.a-text-normal') # working

    # update the dictionary
    contents['book_name'] = book_name
    contents['author(s)'] = authors
    contents['publisher'] = [re.split(pattern=r"[;:(]", string=details[0])[1].strip()\
                             if "Publisher" in details[0] else "Self Publication"][0]
    contents['Language'] = [re.split(pattern=r"[;:(]", string=details[1])[1].strip()\
                            if "Language" in details[1] else "Null"][0]
    contents['#pages'] = [re.split(pattern=r"[;:(]", string=details[2])[1].split(' ')[1].strip()\
                            if "Paperback" in details[2] else "Null"][0]
    contents['best_seller_rank'] = [re.split(pattern=r"[:;#( ]", string=details[-5])[5].replace(',', '').strip()\
                                   if "Best Sellers Rank" in details[-5] else "Null"][0]
    
    contents['customer_reviews'] = [re.split(pattern="[:\n]", string=details[-1])[1].strip()\
                                    if "Customer Reviews" in details[-1] else "0"]
    contents['total_ratings'] = [re.split(pattern="[:\n]", string=details[-1])[2].split(' ')[0]\
                                 if "ratings" in details[-1] else "0"]
    contents['url'] = url
    contents['price($)'] = float(price.text.replace("$", ''))
    

    return contents


def main():
    # initializing the driver and firefox profile
    webdriver_path = "/usr/local/bin"
    options = Options()
    options.set_preference('profile', webdriver_path)
    driver = Firefox(options=options)

    # The main page
    main_page = "https://www.amazon.com/s?k=data+science+books&rh=n%3A283155%2Cp_n_feature_browse-bin%3A2656022011&s=exact-aware-popularity-rank&dc&ds=v1%3AKH4YDDHgNreLxOY0lbVzvbRivml8xsWK7Ta3i%2BKuFAc&crid=2YD904R136ZW3&qid=1687341888&rnid=618072011&sprefix=data+science+books%2Caps%2C421&ref=sr_nr_p_n_feature_browse-bin_1"
    # next_page = "https://www.amazon.com/s?k=data+science+books&i=stripbooks&rh=n%3A283155%2Cp_n_feature_browse-bin%3A2656022011&s=exact-aware-popularity-rank&dc&page=2&crid=2YD904R136ZW3&qid=1687598450&rnid=618072011&sprefix=data+science+books%2Caps%2C421&ref=sr_pg_2"

    
    data_rows = []  # data will be stored in this list as dictionary
    
    for page in range(1, 51):
        if page > 1:
            page = f"https://www.amazon.com/s?k=data+science+books&i=stripbooks&rh=n%3A283155%2Cp_n_feature_browse-bin%3A2656022011&s=exact-aware-popularity-rank&dc&page={page}&crid=2YD904R136ZW3&qid=1687598450&rnid=618072011&sprefix=data+science+books%2Caps%2C421&ref=sr_pg_{page}"
            driver.get(page)
            hrefs = [link.get_attribute('href') for link in driver.find_elements(By.CSS_SELECTOR, ".a-size-mini > a")]
            for link in hrefs:
                data_rows.append(scrape_data(driver, link))
        else:
            page = main_page
            driver.get(page)
            hrefs = [link.get_attribute('href') for link in driver.find_elements(By.CSS_SELECTOR, ".a-size-mini > a")]
            for link in hrefs:
                data_rows.append(scrape_data(driver, link))
    
    # print(data_rows)        

    driver.close()

    df = pd.DataFrame(data=data_rows, columns=columns)
    df.to_csv('amazon_data_science_books.csv', index=False)
    
    return

if __name__ == "__main__":
    main()