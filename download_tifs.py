from downloader.minio_client import MinioDownloader
from downloader.logger import logger

def main():
    try:
        downloader = MinioDownloader()
        downloader.download_tif_files()
    except Exception as e:
        logger.error(f"SYSTEM: Unhandled exception occurred: {e}")

if __name__ == "__main__":
    main()
