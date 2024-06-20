## Amazon Product Reviews Scraper

### Overview
This project is a Python script designed to scrape customer reviews from Amazon product pages. It uses web scraping techniques to extract review details and saves them into an Excel file.

### Features
- Extracts product reviews from Amazon.
- Utilizes proxy rotation to avoid getting blocked by Amazon.
- Saves the scraped data into an Excel file for further analysis.

### Requirements
- Python 3.x
- The following Python packages:
  - `requests`
  - `pandas`
  - `beautifulsoup4`
  - `openpyxl`

### Installation

1. **Clone the repository or download the script:**

   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. **Open the script `amazon_reviews_scraper.py` and update the `productUrl` variable with the URL of the Amazon product page you want to scrape:**

   ```python
   productUrl = "https://www.amazon.in/Starshine-Storage-Powered-MediaTek-Display/product-reviews/B0CMTZNPXR/"
   ```

2. **Run the script:**

   ```sh
   main.py
   ```

3. **The script will create an `outputs` directory (if it doesn't exist) and save the scraped reviews into an Excel file named `output.xlsx` within that directory.**

```

### Notes
- Ensure you have the necessary permissions and use proxies responsibly.
- Review scraping may violate Amazon's terms of service, so use this script at your own risk.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.