from dotenv import load_dotenv
import os
from datetime import datetime, timezone, timedelta
from pathlib import Path

load_dotenv()

geometry_env = Path("/var/app/geometry/.env")
if geometry_env.exists():
    load_dotenv(dotenv_path=geometry_env)
else:
    raise FileNotFoundError("SYSTEM: /var/app/geometry/.env not found")

class Config:
    MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
    MINIO_ACCESS_KEY = os.getenv("CREDENTIAL_S3_ROOT_USER")
    MINIO_SECRET_KEY = os.getenv("CREDENTIAL_S3_ROOT_PASSWORD")
    MINIO_BUCKET = os.getenv("MINIO_BUCKET")
    MINIO_PREFIX = os.getenv("MINIO_PREFIX", "")
    DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "./downloads")

    MOSCOW_TZ = timezone(timedelta(hours=3))
    START_DATE = datetime.strptime(os.getenv("START_DATE"), "%Y-%m-%dT%H:%M:%S").replace(tzinfo=MOSCOW_TZ)
    END_DATE = datetime.strptime(os.getenv("END_DATE"), "%Y-%m-%dT%H:%M:%S").replace(tzinfo=MOSCOW_TZ)
