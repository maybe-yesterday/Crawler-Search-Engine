import React, { useState, useCallback } from 'react';
import './App.css';

function App() {
  const [searchQuery, setSearchQuery] = useState('');
  const [results, setResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const performSearch = useCallback(async (e) => {
    e.preventDefault();
    if (!searchQuery.trim()) {
      setResults([]);
      setError(null);
      return;
    }
    setIsLoading(true);
    setError(null);
    try {
      const response = await fetch(`http://127.0.0.1:8000/search?q=${encodeURIComponent(searchQuery)}`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError("Failed to fetch results. Is the backend running?");
      setResults([]);
    } finally {
      setIsLoading(false);
    }
  }, [searchQuery]);

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>UW CSE Course Material Search</h1>
      </header>
      
      <form onSubmit={performSearch} className="search-form">
        <input
          type="search"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder="Search for something awesome..."
          className="search-input"
          disabled={isLoading}
        />
        <button type="submit" className="search-button" disabled={isLoading}>
          {isLoading ? '...' : 'Search'}
        </button>
      </form>

      {error && <p className="error-message">{error}</p>}
      
      {results.length > 0 && (
        <ul className="results-list">
          {results.map((result) => (
            <li key={result.id} className="result-item">
              <a href={result.url} target="_blank" rel="noopener noreferrer" className="result-title">
                {result.title}
              </a>
              <p className="result-url">{result.url}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;