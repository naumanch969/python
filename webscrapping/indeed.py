import requests
from bs4 import BeautifulSoup
import time

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.google.com/'  # Replace with an appropriate referer
    }

    base_url = 'https://uk.indeed.com/jobs?q=part+time&l=London%2C+Greater+London&start='
    url = f'{base_url}{page * 10}&pp=gQAPAAAAAAAAAAAAAAACGAubHQAxAQABRe7ioyH43k6JNoDPRr9cg8zhXkMITC352Xe4MP3Ag4XhH7Nd6SQPc5bbfd9AHgAA&vjk=8182c432223c7d8f'

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad requests

        # Add a delay to avoid making too many requests in a short time
        time.sleep(2)

        soup = BeautifulSoup(response.content, 'lxml')
        # Your scraping logic here using BeautifulSoup on 'soup'

        header = soup.find('header')
        print(header.attrs)

        return response.status_code

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Example usage
print(extract(1))  # Adjust the page number as needed
