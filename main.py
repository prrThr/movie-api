from fetcher import fetch_omdb, fetch_tmdb
import asyncio

async def main():
    title = input("Digite o nome do filme (em inglês): ")
    year = int(input("Digite o ano do filmes: "))

    omdb_task = fetch_omdb(title, year)
    tmdb_task = fetch_tmdb(title)

    sinopse, reviews = await asyncio.gather(omdb_task, tmdb_task)

    if sinopse["titulo"] == "Desconhecido" or sinopse["ano"] == 0 or sinopse["sinopse"] == "Sinopse não disponível":
        print("\nFilme não encontrado. Verifique o nome e o ano e tente novamente.")
        return

    print("\n===== Informações do Filme =====")
    print(f"Título: {sinopse['titulo']}")
    print(f"Ano: {sinopse['ano']}")
    print(f"Sinopse: {sinopse['sinopse']}\n")

    print("===== Reviews =====")
    for review in reviews:
        print(f"Autor: {review['author']}")
        print(f"Nota: {review['rating']}")
        print(f"Descrição: {review['content']}\n")
        print("-" * 75)

if __name__ == "__main__":
    asyncio.run(main())

