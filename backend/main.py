import os
import meilisearch
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
MEILI_URL = "http://127.0.0.1:7700"
MEILI_MASTER_KEY = os.getenv("MEILI_MASTER_KEY")
if not MEILI_MASTER_KEY:
    raise ValueError("MEILI_MASTER_KEY not found. Please create a .env file.")

app = FastAPI()

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_meilisearch_client():
    app.state.meili_client = meilisearch.Client(MEILI_URL, MEILI_MASTER_KEY)

@app.get("/search")
def search(q: str):
    """Performs a search in the Meilisearch index."""
    index = app.state.meili_client.index('pages')
    search_results = index.search(q)
    return search_results['hits']