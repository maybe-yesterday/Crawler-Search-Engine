import os
import meilisearch
from crawler import crawl_page
from dotenv import load_dotenv

# Load variables from the .env file into the environment
load_dotenv()

# --- Configuration ---
MEILI_URL = "http://127.0.0.1:7700"
MEILI_MASTER_KEY = os.getenv("MEILI_MASTER_KEY")
if not MEILI_MASTER_KEY:
    raise ValueError("MEILI_MASTER_KEY not found. Please create a .env file.")

URLS_TO_INDEX = [
    "https://courses.cs.washington.edu/courses/cse446/",
    "https://courses.cs.washington.edu/courses/cse446/25au/"
]

def run_indexer():
    """Crawls a list of URLs and adds them to the Meilisearch index."""
    client = meilisearch.Client(MEILI_URL, MEILI_MASTER_KEY)
    index = client.index('pages')
    
    documents = []
    for url in URLS_TO_INDEX:
        page_data = crawl_page(url)
        if page_data:
            documents.append(page_data)
    print("\n--- DATA BEING SENT TO MEILISEARCH ---")
    print(documents)

    if documents:
        task = index.add_documents(documents)
        print(f"Documents sent for indexing. Task UID: {task.task_uid}")
    else:
        print("No documents were indexed.")

if __name__ == "__main__":
    run_indexer()