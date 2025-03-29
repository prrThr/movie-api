import httpx

from load_env import get_env

OMDB_KEY = get_env("OMDB_KEY")
TMDB_KEY = get_env("TMDB_KEY")
TMDB_TOKEN = get_env("TMDB_TOKEN")

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


async def fetch_tmdb(title: str):
    url_search = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url_search, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data.get("results"):
                movie_id = data["results"][0]["id"]

                url_reviews = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?language=en-US&page=1"
                response = await client.get(url_reviews, headers=headers)

                if response.status_code == 200:
                    data = response.json()
                    reviews = data.get("results", [])[:3]

                    return [
                        {
                            "author": review.get("author", "Desconhecido"),
                            "rating": review.get("author_details", {}).get("rating", "Sem nota"),
                            "content": review.get("content", "Sem descrição")
                        }
                        for review in reviews
                    ]
    
    return [{"author": "Nenhum review encontrado", "rating": "-", "content": "-"}]    

