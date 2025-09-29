# My Personal Search Engine

This project is a simple, personal search engine. It consists of three main parts: a Python-based web crawler to fetch data, a high-performance Meilisearch instance for indexing and querying, and a modern React user interface for interaction.

## Tech Stack

* **Backend**: Python, FastAPI
* **Search Index**: Meilisearch
* **Web Scraping**: Requests, BeautifulSoup4
* **Frontend**: React
* **Environment Management**: `python-dotenv`

## ⚙️ Setup and Installation

Follow these steps to get your development environment set up.

#### 1. Clone the Repository
```bash
git clone https://github.com/maybe-yesterday/Crawler-Search-Engine.git
cd Crawler-Search-Engine
```

#### 2. Set Up Backend

```
# Navigate to the backend directory
cd backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install the required Python packages
pip install -r requirements.txt
```

#### 3. Set Up Frontend

```
# Navigate to the frontend directory from the root
cd frontend

# Install the required npm packages
npm install
```

#### 4. Configuration

This project required the user to input the websites they want to crawl inside URLS_TO_INDEX in indexer.py. 
The more specific the urls you provided are, the better the search engine will be at answering your questions!

This project requires an API key to communicate with Meilisearch. (Totally free if self-hosted btw)

    Start Meilisearch: Go through [https://www.meilisearch.com/docs/learn/self_hosted/getting_started_with_self_hosted_meilisearch]


    Create your .env file: In the backend/ directory, copy the example file:
    ```
    cp backend/.env.example backend/.env
    ```

    Add your key: Open the newly created backend/.env file and paste your Meilisearch Master Key as the value for MEILI_MASTER_KEY.

    MEILI_MASTER_KEY="your_copied_master_key_goes_here"

#### 5. Running!

```
# Start meilisearch server (in separate terminal)
meilisearch

# Index all files in the website
# You might have to wait a while if the website has too much content
python backend/indexer.py

# Navigate to frontend
cd frontend

# hen this script will do everything for you
npm run dev
```
