import os
import json
import firebase_admin
from firebase_admin import credentials, storage

firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

if firebase_credentials:
    try:
        cred_dict = json.loads(firebase_credentials)
        cred = credentials.Certificate(cred_dict)
    except json.JSONDecodeError:
        raise ValueError("Invalid FIREBASE_CREDENTIALS JSON format.")
else:
    cred_path = os.path.join(os.path.dirname(__file__), "dscwebsite-812fe-firebase-adminsdk-fbsvc-14b74f787d.json")
    if not os.path.exists(cred_path):
        raise FileNotFoundError("Firebase credentials not found. Please set FIREBASE_CREDENTIALS.")
    cred = credentials.Certificate(cred_path)

firebase_admin.initialize_app(cred, {
    'storageBucket': 'dscwebsite-812fe.appspot.com'
})

bucket = storage.bucket()
