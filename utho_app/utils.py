import uuid
import time
import requests
from io import BytesIO
from django.core.files.storage import default_storage
from django.conf import settings

API_KEY = 'iuPxvsDnQpAbNoWFqCKZVjSUeMJBTdXIEmLraglkcwYRGzOfhyHt'
DC_SLUG = 'innoida'  # Data center slug
BUCKET_NAME = 'creap2'  # Your actual bucket name
# UPLOAD_URL = f'https://api.utho.com/v2/objectstorage/{DC_SLUG}/bucket/{BUCKET_NAME}/upload/'
UPLOAD_URL = f'https://api.utho.com/v2/objectstorage/{DC_SLUG}/bucket/{BUCKET_NAME}/upload/'


def upload_image_to_utho(image_file):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }

    unique_filename = f"{uuid.uuid4().hex}_{int(time.time())}.jpg"

    # Save the file temporarily in memory or local storage
    with BytesIO() as temp_file:
        for chunk in image_file.chunks():  # Save file chunks to a temporary in-memory file
            temp_file.write(chunk)
        temp_file.seek(0)

        files = {
            'file': (unique_filename, temp_file, 'image/jpeg')  # Adjust file name and MIME type if necessary
        }

        try:
            response = requests.post(UPLOAD_URL, headers=headers, files=files)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Failed to upload image:", e)
            return None
