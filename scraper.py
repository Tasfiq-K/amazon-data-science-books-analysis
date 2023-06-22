from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

columns = ["book_name", "author(s)", "publisher", "#pages", "customer_reviews", "total_ratings", "best_seller_rank", "price_paperback"]

def scrape_data(url):
    url = url
    contents = {}
    contents['book_name'] = 'something'
    pass


def main():
    url = "https://www.amazon.com/s?k=data+science+books&rh=n%3A283155%2Cp_n_feature_browse-bin%3A2656022011&s=exact-aware-popularity-rank&dc&ds=v1%3AKH4YDDHgNreLxOY0lbVzvbRivml8xsWK7Ta3i%2BKuFAc&crid=2YD904R136ZW3&qid=1687341888&rnid=618072011&sprefix=data+science+books%2Caps%2C421&ref=sr_nr_p_n_feature_browse-bin_1"
    webdriver_path = "/usr/local/bin"
    options = Options()
    options.set_preference('profile', webdriver_path)
    driver = Firefox(options=options)
    driver.get(url)

    # books = driver.find_element(By.CLASS_NAME, "sg-col-inner")
    # print(books)
    links = driver.find_elements(By.CSS_SELECTOR, ".a-size-mini > a")
    print(len(links))
    # print(links)
    # for link in links:
    #     print(link.get_attribute('href'))
    # print(links)

    # print(links[0].text)
    hrefs = [link.get_attribute("href") for link in links]
    # print(hrefs)
    # hrefs = []

    for link in hrefs:
        print(link)
        driver.get(link)
        authors = driver.find_element(By.ID, 'productTitle')
        print(authors.text)
        break


    # for link in links:
    #     hrefs.append(link.get_attribute("href"))
    
    # print(hrefs)
        

    driver.close()
    return

if __name__ == "__main__":
    main()