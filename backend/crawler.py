import requests
from bs4 import BeautifulSoup
import hashlib

def crawl_page(url: str):
    """Fetches the content of a URL and extracts title and text."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title and a clean version of the text content
        title = soup.title.string if soup.title else 'No Title Found'
        content = soup.get_text(separator=' ', strip=True)
        doc_id = hashlib.md5(url.encode()).hexdigest()

        print(f"Crawled: {url}")
        return {
            'id': doc_id, # Use URL as the unique ID
            'url': url,
            'title': title,
            'content': content
        }
    except requests.RequestException as e:
        print(f"Error crawling {url}: {e}")
        return None