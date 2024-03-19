import requests

def update_book_description():
    url_api_livros = "http://localhost:3000/livros"
    response_livros = requests.get(url_api_livros) #obtendo todos os livros
    if response_livros.status_code == 200:
        data = response_livros.json()
        for book_obj in data:
            url = f"https://www.googleapis.com/books/v1/volumes?q={book_obj['nome']}&maxResults=1"
            response = requests.get(url)
            if response.status_code == 200:
                book_info = response.json().get('items', [])
                if book_info:
                    volume_info = book_info[0].get('volumeInfo', {})
                    print(volume_info)
                    description = volume_info.get("description", "")
                    #authors = ", ".join([author["name"] for author in volume_info.get("authors", [])])
                    # Adiciona a descrição e os autores ao livro no banco de dados
                    put_data = {"descricao": description}
                    id_livro = book_obj["id"]
                    put_url = f"{url_api_livros}/{id_livro}?campos=descricao,autores"
                    requests.put(put_url, json=put_data)
                    
update_book_description()