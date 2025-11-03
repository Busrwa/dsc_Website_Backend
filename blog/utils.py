from dsc_website.firebase_config import bucket

def upload_file_to_firebase(local_path, filename):
    """Yüklenen dosyayı Firebase Storage'a gönderir ve erişim URL'sini döner."""
    blob = bucket.blob(f"uploads/{filename}")
    blob.upload_from_filename(local_path)
    blob.make_public()  # herkese açık hale getir
    return blob.public_url
