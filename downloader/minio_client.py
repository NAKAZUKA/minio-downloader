import os
from datetime import timezone
from minio import Minio
from minio.error import S3Error
from downloader.config import Config
from downloader.logger import logger

class MinioDownloader:
    def __init__(self):
        try:
            self.client = Minio(
                Config.MINIO_ENDPOINT,
                access_key=Config.MINIO_ACCESS_KEY,
                secret_key=Config.MINIO_SECRET_KEY,
                secure=False
            )
            logger.info("MINIO: Connection initialized")
        except Exception as e:
            logger.error(f"MINIO: Failed to initialize client - {e}")
            raise

        if not os.path.exists(Config.DOWNLOAD_DIR):
            os.makedirs(Config.DOWNLOAD_DIR)

    def download_tif_files(self):
        try:
            logger.info("MINIO: Starting to list objects")
            objects = self.client.list_objects(Config.MINIO_BUCKET, prefix=Config.MINIO_PREFIX, recursive=True)
            for obj in objects:
                if not obj.object_name.lower().endswith(".tiff"):
                    continue

                if obj.last_modified is None:
                    continue

                obj_time = obj.last_modified.astimezone(Config.MOSCOW_TZ)

                if not (Config.START_DATE <= obj_time <= Config.END_DATE):
                    continue

                file_path = os.path.join(Config.DOWNLOAD_DIR, os.path.basename(obj.object_name))
                logger.info(f"MINIO: Downloading {obj.object_name} to {file_path}")
                self.client.fget_object(Config.MINIO_BUCKET, obj.object_name, file_path)
        except S3Error as e:
            logger.error(f"MINIO: Error accessing object - {e}")
            raise
        except Exception as e:
            logger.error(f"MINIO: Unknown error during download - {e}")
            raise
