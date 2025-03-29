import requests
TOKEN = ""

url = "https://api.themoviedb.org/3/search/movie?query=Inception&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(url, headers=headers)

#print(response.text)

if response.status_code == 200:
    data = response.json()
    if "results" in data and len(data["results"]) > 0:
        first_movie_id = data["results"][0]["id"]
        print("ID do primeiro filme:", first_movie_id)
    else:
        print("Nenhum filme encontrado.")
else:
    print("Erro na requisição:", response.status_code, response.text)

