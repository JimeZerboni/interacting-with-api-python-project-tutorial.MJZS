"""
Este módulo interactúa con la API de Spotify para obtener y analizar datos de canciones.
Incluye funciones para autenticarse con la API, recuperar datos de canciones y procesar
la información usando pandas y seaborn.
"""

import os
import base64
import pandas as pd  # Unused import
import seaborn as sns  # pylint: disable=W0611
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

# load the .env file variables
load_dotenv()


# Autenticación con las credenciales de Spotify (client_id, client_secret, redirect_uri)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-library-read"
))

# Ahora puedes realizar solicitudes a la API de Spotify. Ejemplo:
# Obtener información sobre el usuario autenticado
user_info = sp.current_user()
print(user_info)

# Codificar las credenciales como Base64
credentials = f'{SPOTIPY_CLIENT_ID}:{SPOTIPY_CLIENT_SECRET}' # type: ignore
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Configuración de la solicitud para obtener el token
URL = 'https://accounts.spotify.com/api/token'
headers = {
    'Authorization': f'Basic {encoded_credentials}'
}
data = {
    'grant_type': 'client_credentials'
}

# Realizar la solicitud POST
response = requests.post(URL, data=data, headers=headers, timeout=10)  # Timeout de 10 segundos

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    token = response.json().get('access_token')
    print(f'Access Token: {token}')
else:
    print(f'Error: {response.status_code}, {response.text}')
