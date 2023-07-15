# Amazon data science book visualizations

## Problem statement
The goal of this project is to gather information of Data Science realted books from amazon. There are total of 1351 entries in the `amazon_data_science_books.csv` file. </br>
Later we utlizied the scrape data to understand the following demographics and correlations using [Tableau](https://www.tableau.com/) Dashboard: </br>
1. A pie chart showing the number of books published by the top 15 publishers and the others.
2. A barchart of top 15 publisher by the amount of books published
3. Average price of books by the top 15 publishers
4. Price range of books
5. Pages vs Price trend
6. Top 100 books by user reviews (rating 4.0 - 5.0)
7. Average reviews of Top 15 publishers </br>

## Findings and Observations from the [Dashboard](https://public.tableau.com/app/profile/tasfiq.kamran/viz/AmazonDataScienceBooksDashboard/Dashboard1)
1. Among the 1324 books (after preprocessing the data) 948 of them are published by only 15 publications.
1. Packt has the highest publication of books
2. Springer has the highest average price 
3. As the pages increase the price of the books is increased
4. Price of the most books fall around the range between (25.00 - 65-00) USD

You can visit the public dashboard [here](https://public.tableau.com/app/profile/tasfiq.kamran/viz/AmazonDataScienceBooksDashboard/Dashboard1): 


## Build from Sources and run the selenium driver
1. Clone the repo
```bash
git clone https://github.com/Tasfiq-K/amazon-data-science-books.git
```
2. Initiaize and activate virtual environment </br> 
If you are running Python 3.4+, you can use the venv module baked into Python:
```bash
python -m venv <directory name>
```
for example, if you name your directory 'venv', then run this command:
```bash
python -m venv venv
```
For activating the virtual environmet run:
On Windows:
```bash
# In cmd.exe
venv\Scripts\activate.bat
# In Powershell
venv\Scripts\activate.psl
```
On Linux or MacOs
```bash
$ source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Download Webdriver </br>
Download the web driver at your convenience, I've used the geckodriver to use it with the Firefox browser. You can download it from [here](https://github.com/mozilla/geckodriver/releases) 

5. Run the scraper
```bash
python scraper.py --geckodriver_path <path_to_chromedriver>
```
6. You will get a file with the following name `amazon_data_science_books.csv` containing all the required fields and data. Alternatively, check the scraped data [here](https://github.com/Tasfiq-K/amazon-data-science-books/blob/main/amazon_data_science_books.csv)

## Analytics
Tableau Public View: https://public.tableau.com/app/profile/tasfiq.kamran/viz/AmazonDataScienceBooksDashboard/Dashboard1