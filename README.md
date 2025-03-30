## Desenvolvimento de um Serviço Agregador de Dados de APIs Públicas

### Objetivo
- Criar um sistema distribuído que, a partir de uma consulta do usuário, obtenha dados de duas APIs públicas distintas e agregue as informações para compor uma resposta.

### Informações de entrada: 

- Título de um filme (**string**)
- Ano do filme (**int**)

### Informações de saída (JSON)

```json
{
    "titulo": string,
    "ano": int,
    "sinopse": string,
    "reviews": List[string] // lista contendo até 3 reviews
}
```

### Vídeo
[Link do vídeo postado no Youtube](https://youtu.be/Wy2NPFzFFz0)

## Requisitos técnicos

- **Arquitetura cliente-servidor**: o cliente envia a requisição e espera a resposta; o servidor processa a requisição e retorna o dado.
- **O sistema deve consultar duas APIs**: OMDB e TMDB. A informação da sinopse deve vir do OMDB e os reviews do TMDB.
- **Comunicação**: utilizar protocolos como HTTP/REST para comunicação entre cliente e servidor.
- **Concorrência**: as requisições para as  duas APIs (OMDB e TMDB) deverão serem feitas paralelamente.

### Dependências
- As dependências estão no arquivo `requirements.txt`.
- Para instalar as dependências, crie um ambiente virtual no diretório do projeto com `python -m venv venv`
- Utilize `source venv/bin/activate` para ativar o ambiente virtual
- Execute `pip install -r requirements.txt` para instalar as dependências

### Funcionamento
1. Via termina, execute `python main.py`
2. Será requisitado o nome do filme, insira-o em inglês (Ex: Inception, Lord of The Rings, etc...)
3. Será requisitado o ano. Caso o título do filme sejá `Lord of The Rings` com o ano  `2001` será retornado `The Fellowship of the Ring`, caso o ano for 2002 será retornado `The Two Towers` e assim por diante
4. O retorno será o título, ano, sinopse e os 3 primeiros reviews retornados pela API

