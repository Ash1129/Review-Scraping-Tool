import requests
import pandas as pd
from bs4 import BeautifulSoup
import random
import os

reviewlist = []

def get_random_proxy():
    """
    Generate a random proxy for making requests.

    Returns:
        dict: A dictionary containing HTTP and HTTPS proxy configurations.
    """
    proxy = {
        "http": f"http://zven5Vlnewp04Uvk:wifi;;@proxy.soax.com:{9000 + random.randint(0, 9)}",   #add your own proxy here
        "https": f"http://zven5Vlnewp04Uvk:wifi;;@proxy.soax.com:{9000 + random.randint(0, 9)}"   #add your own proxy here
    }
    return proxy

def extract_reviews(review_url):
    """
    Extract reviews from the given URL and append them to the review list.

    Args:
        review_url (str): The URL of the review page.
    """
    print(review_url)
    resp = requests.get(review_url, proxies=get_random_proxy())
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.findAll('div', {'data-hook': "review"})
    
    for item in reviews:
        review = {
            'productTitle': soup.title.text.replace("Amazon.in:Customer reviews: ", "").strip(),
            'Review Title': item.find('a', {'data-hook': "review-title"}).text.strip() if item.find('a', {'data-hook': "review-title"}) else 'N/A',
            'Rating': item.find('i', {'data-hook': 'review-star-rating'}).text.strip() if item.find('i', {'data-hook': 'review-star-rating'}) else 'N/A',
            'Review Body': item.find('span', {'data-hook': 'review-body'}).text.strip() if item.find('span', {'data-hook': 'review-body'}) else 'N/A',
        }
        reviewlist.append(review)

def total_pages(product_url):
    """
    Calculate the total number of review pages for a product.

    Args:
        product_url (str): The URL of the product review page.

    Returns:
        int: The total number of pages.
    """
    resp = requests.get(product_url, proxies=get_random_proxy())
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.find('div', {'data-hook': "cr-filter-info-review-rating-count"})
    
    if reviews:
        total_reviews = int(reviews.text.strip().split()[3].replace(',', ''))
        print(f"Total Reviews: {total_reviews}")
        return (total_reviews // 10) + 1
    
    return 0

def main():
    """
    Main function to extract reviews from all pages of a product and save them to an Excel file.
    """
    product_url = "https://www.amazon.in/Starshine-Storage-Powered-MediaTek-Display/product-reviews/B0CMTZNPXR/"
    total_pg = total_pages(product_url)
    print(f"Total Pages: {total_pg}")

    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    for i in range(1, total_pg + 1):
        print(f"Running for page {i}")
        try:
            review_url = product_url + f"?pageNumber={i}"
            extract_reviews(review_url)
        except Exception as e:
            print(f"Error on page {i}: {e}")

    df = pd.DataFrame(reviewlist)
    df.to_excel('outputs/output1.xlsx', index=False)

if __name__ == "__main__":
    main()
