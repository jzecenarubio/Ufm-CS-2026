import requests

BASE_URL = "https://api.jikan.moe/v4"

def buscar_anime(nombre):
    """Busca un anime por nombre y devuelve el primer resultado."""
    respuesta = requests.get(f"{BASE_URL}/anime", params={"q": nombre, "limit": 1})
    respuesta.raise_for_status()
    datos = respuesta.json()

    if not datos["data"]:
        print("No se encontró ningún anime con ese nombre.")
        return None

    return datos["data"][0]

def mostrar_info_anime(anime):
    """Imprime la información principal de un anime."""
    print("\n--- Información del Anime ---")
    print(f"Título: {anime['title']}")
    print(f"Episodios: {anime['episodes']}")
    print(f"Rating: {anime['score']}")
    print(f"Estado: {anime['status']}")
    print(f"Sinopsis: {anime['synopsis'][:300]}...")  # solo los primeros 300 caracteres

def mostrar_personajes(anime_id):
    """Consulta y muestra los personajes principales de un anime."""
    respuesta = requests.get(f"{BASE_URL}/anime/{anime_id}/characters")
    respuesta.raise_for_status()
    datos = respuesta.json()

    print("\n--- Personajes principales ---")
    for personaje in datos["data"][:5]:  # solo los primeros 5
        nombre = personaje["character"]["name"]
        rol = personaje["role"]
        print(f"- {nombre} ({rol})")

def main():
    nombre_busqueda = input("Ingresa el nombre de un anime a buscar: ")
    anime = buscar_anime(nombre_busqueda)

    if anime:
        mostrar_info_anime(anime)
        mostrar_personajes(anime["mal_id"])

if __name__ == "__main__":
    main()
    