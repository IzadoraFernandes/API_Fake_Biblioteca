import requests

def update_book_covers():
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
                    image_links = volume_info.get('imageLinks', {})
                    thumbnail_link = image_links.get('thumbnail') if 'thumbnail' in image_links else None
                    if thumbnail_link:
                        book_obj['foto'] = thumbnail_link
                        response_image_link = requests.put(f"{url_api_livros}/{book_obj['id']}", json=book_obj)
                        if response_image_link.status_code == 200:
                            print(f"Capa atualizada para {book_obj['nome']}")
                        else:
                            print(f"Falha ao atualizar a capa para {book_obj['nome']}")
                    else:
                        print(f"Capa não encontrada para {book_obj['nome']}")
                else:
                    print(f"Capa não encontrada para {book_obj['nome']}")
            else:
                print(f"Falha ao buscar a capa para {book_obj['nome']}")
    else:
        print("Falha ao obter a lista de livros")

# Chamada da função para atualizar as capas de todos os livros na API
update_book_covers()
