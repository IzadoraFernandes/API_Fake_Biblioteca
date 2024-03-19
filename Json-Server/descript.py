import requests

def update_book_description():
    url_api_livros = "http://localhost:3000/livros"
    response_livros = requests.get(url_api_livros)
    if response_livros.status_code == 200:
        data = response_livros.json()
        for book_obj in data:
            url = f"https://www.googleapis.com/books/v1/volumes?q={book_obj['nome']}&maxResults=1"
            response = requests.get(url)
            if response.status_code == 200:
                book_info = response.json().get('items', [])
                if book_info:
                    volume_info = book_info[0].get('volumeInfo', {})
                    description = volume_info.get("description", "")
                    book_obj["descricao"] = description  # Update the description field
                    put_url = f"{url_api_livros}/{book_obj['id']}"
                    response_put = requests.put(put_url, json=book_obj)
                    if response_put.status_code == 200:
                        print(f"Descrição atualizada para {book_obj['nome']}")
                    else:
                        print(f"Falha ao atualizar a descrição para {book_obj['nome']}")

# Chamada da função para atualizar as descrições de todos os livros na API
update_book_description()
