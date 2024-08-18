# FastAPI Hacker News API

## Overview

This project is a Python-based API built using the FastAPI framework. The API interacts with the Hacker News API to fetch and display the top news items. The project also includes caching to reduce the number of API calls and is fully Dockerized for easy deployment.

## Features

- **Retrieve Top News:** Fetch top news items from Hacker News with customizable count.
- **Caching:** Results are cached for 10 minutes to minimize API calls and improve performance.
- **Error Handling:** Graceful handling of errors when the Hacker News API is unavailable.
- **Containerization:** The application is Dockerized for easy setup and deployment.

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- Requests
- Cachetools

## Set Up the Environment

1. **Create a virtual environment and install dependencies:**

   ```bash
   conda create --name venv 
   conda activate venv
   pip install -r requirements.txt
   ```
2. **Running the Application:**

   1. Build the Docker image:

      ```
      docker build -t fastapi-hackernews .
      ```
   2. Run the Docker container:

      ```
      docker run -d -p 8000:8000 fastapi-hackernews
      ```
   3. Lists all containers, including those that are running, restarting, paused, or stopped:

      ```
      docker ps -a
      ```
3. **Example Request:**

   ```
   curl "http://localhost:8000/top-news?count=10"
   ```
4. **Assumptions**: There is a possibility of an error when retrieving data from the cache. To prevent this, the code checks both if the data is present in the cache and whether its length is adequate. Additionally, when data with a higher count is fetched, it overrides any existing data in the cache if the new data is longer.
