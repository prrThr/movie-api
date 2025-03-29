import requests

TOKEN = ""

url = "https://api.themoviedb.org/3/movie/27205/reviews?language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(url, headers=headers)


if response.status_code == 200:
    data = response.json()
    reviews = data.get("results", [])[:3]  # Pega no máximo os 3 primeiros reviews

    for review in reviews:
        author = review.get("author", "Desconhecido")
        rating = review.get("author_details", {}).get("rating", "Sem nota")
        content = review.get("content", "Sem descrição")

        print(f"Autor: {author}\nNota: {rating}\nDescrição: {content}\n")
        print(f"--------------------------------------------------------------------------")
else:
    print("Erro na requisição:", response.status_code, response.text)
