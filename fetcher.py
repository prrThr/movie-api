import httpx

TMDB_KEY = ""
OMDB_KEY = ""

async def fetch_omdb(title: str, year: int):
    url = f"http://www.omdbapi.com/?t={title}&y={year}&apikey={OMDB_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

        return {
            "titulo": data.get("Title", "Desconhecido"),
            "ano": int(data.get("Year", 0)),  # Converte para inteiro
            "sinopse": data.get("Plot", "Sinopse não disponível")
        }

async def fetch_tmdb_reviews(title: str):
    search_url = f"https://api.themoviedb.org/3/search/movie?query={title}&api_key={TMDB_KEY}"
    async with httpx.AsyncClient() as client:
        search_response = await client.get(search_url)
        search_data = search_response.json()
        movie_id = search_data["results"][0]["id"] if search_data["results"] else None

        if not movie_id:
            return []
        
    reviews_url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?api_key={TMDB_KEY}"
    reviews_response = await client.get(reviews_url)
    reviews_data = reviews_response.json()
    return [review["content"] for review in reviews_data.get("results", [])[:3]]

