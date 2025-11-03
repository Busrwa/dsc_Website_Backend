import uuid
from dsc_website.firebase_config import bucket

def upload_file_to_firebase(file, folder="media"):
    """
    file: Django'dan gelen file objesi (request.FILES['image'] gibi)
    folder: Firebase içinde klasör
    """
    ext = file.name.split('.')[-1]
    filename = f"{folder}/{uuid.uuid4()}.{ext}"  # unique isim
    blob = bucket.blob(filename)
    blob.upload_from_file(file, content_type=file.content_type)
    blob.make_public()  # herkese açık URL için
    return blob.public_url
