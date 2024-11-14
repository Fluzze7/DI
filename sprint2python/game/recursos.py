import requests
from PIL import Image,ImageTk
from requests import HTTPError, RequestException
from io import BytesIO


def descargar_imagen(url,size):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        image = image.resize((size, size), Image.Resampling.LANCZOS)
        print(f"La imagen  {url}  se descarga")
        return ImageTk.PhotoImage(image)
    except (HTTPError, RequestException, IOError):
        return None