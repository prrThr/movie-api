import httpx
import requests

OMDB_KEY = ""
TMDB_KEY = ""
TMDB_TOKEN = ""


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



async def fetch_tmdb(title:str):
    url_search = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }

    response = requests.get(url_search, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            movie_id = data["results"][0]["id"]
            #return movie_id
            url_reviews = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?language=en-US&page=1"
            response = requests.get(url_reviews, headers=headers)

            if response.status_code == 200:
                data = response.json()
                reviews = data.get("results", [])[:3]  # Pega os 3 primeiros reviews

                for review in reviews:
                    author = review.get("author", "Desconhecido")
                    rating = review.get("author_details", {}).get("rating", "Sem nota")
                    content = review.get("content", "Sem descrição")

                    print(f"Autor: {author}\nNota: {rating}\nDescrição: {content}\n")
                    print(f"--------------------------------------------------------------------------")
            else:
                print("Erro na requisição:", response.status_code, response.text)

        else:
            print("Nenhum filme encontrado")
    else:
        print("Erro na requisição:", response.status_code, response.text)

    


"""
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
"""

