# Amazon data science book visualizations

## Build from Sources
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
Tableau Public View: https://public.tableau.com/app/profile/tasfiq.kamran/viz/amzn_ds_books_dashboard/Dashboard1