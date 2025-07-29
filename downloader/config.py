from dotenv import load_dotenv
import os
from datetime import datetime, timezone, timedelta

load_dotenv()

class Config:
    MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
    MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
    MINIO_BUCKET = os.getenv("MINIO_BUCKET")
    MINIO_PREFIX = os.getenv("MINIO_PREFIX", "")
    DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "./downloads")

    MOSCOW_TZ = timezone(timedelta(hours=3))
    
    START_DATE = datetime.strptime(os.getenv("START_DATE"), "%Y-%m-%dT%H:%M:%S").replace(tzinfo=MOSCOW_TZ)
    END_DATE = datetime.strptime(os.getenv("END_DATE"), "%Y-%m-%dT%H:%M:%S").replace(tzinfo=MOSCOW_TZ)
