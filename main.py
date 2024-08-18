from fastapi import FastAPI, HTTPException, Query
import requests
from cachetools import TTLCache

app = FastAPI()

cache = TTLCache(maxsize=10, ttl=600)

@app.get("/top-news")
async def get_top_news(count: int = Query(10, gt=0)):
    if "top_news" in cache and len(cache["top_news"]) >= count:
        return cache["top_news"][:count]
    
    try:
        response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
        response.raise_for_status()
        top_story_ids = response.json()[:count]
        top_stories = []
        
        for story_id in top_story_ids:
            story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
            story_response.raise_for_status()
            top_stories.append(story_response.json())
            
        cache["top_news"] = top_stories
        return top_stories
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Error fetching data from Hacker News: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
