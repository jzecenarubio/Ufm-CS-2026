"""
Ejemplo vanilla: Gemini API con requests
Para probar la capa gratuita antes de decidir si se usa en clase.

A diferencia de PokeAPI, esta API si pide autenticacion. Para conseguir
una API key gratuita (sin tarjeta):

1. Entrar a https://aistudio.google.com
2. Iniciar sesion con una cuenta de Google normal
3. Click en "Get API key" y copiar la key que genera

Documentacion oficial: https://ai.google.dev/gemini-api/docs
"""

from api_key import API_KEY
import requests

# Pega aqui tu API key (la que copiaste de Google AI Studio).
VERBOSE = False
MODEL = "gemini-3.6-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

# Print configuración API
if VERBOSE:
    print(f'\n===========================')
    print(f'GEMINI MODEL: {MODEL}')
    print(f'API KEY: {API_KEY}')
    print(f'\n===========================')

# A diferencia de PokeAPI, aqui la key no va en la URL: va en un header.
# Poner credenciales en la URL es mala practica (queda en logs, historial
# del navegador, etc.), asi que Gemini pide mandarla en un header aparte.
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY,
}

while True:
    print(f'==GEMINI==')

    user_prompt = (
        'En que piensas? (ingresa tu prompt o "salir" para terminar la sesión): ')

    # Revisa si el usuario desea salir
    if user_prompt.lower().strip() == 'salir':
        print('\n Hasta luego!!!')
        break

    # El "cuerpo" (body) de la peticion: aqui va el prompt.
    # Fijate que ya no es una URL con datos pegados, es JSON de verdad.
    body = {
        "contents": [
            {
                "parts": [
                    {'text': user_prompt}
                ]
            }
        ]
    }

    # Como el body no es un simple GET, usamos requests.post() y le pasamos
    # el diccionario de Python directo en json=... (requests lo convierte
    # a JSON por nosotros).
    respuesta = requests.post(URL, headers=headers, json=body)

    if VERBOSE:
        print("Status code:", respuesta.status_code)

    if respuesta.status_code != 200:
        print("\nAlgo salio mal:")
        print(respuesta.text)
    else:
        datos = respuesta.json()

        # La respuesta de Gemini viene anidada varios niveles:
        # datos -> candidates -> [0] -> content -> parts -> [0] -> text
        respuesta_gemini = datos["candidates"][0]["content"]["parts"][0]["text"]
        print("\nRespuesta de Gemini:\n")
        print(respuesta_gemini)
