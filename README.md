# MinIO TIF Downloader

Скрипт для скачивания `.tif` файлов из MinIO-бакета по префиксу и временному диапазону.
---
## Структура проекта
```
.
├── download_tifs.py
├── downloader/
│ ├── init.py
│ ├── config.py
│ ├── logger.py
│ └── minio_client.py
├── .env
├── uv_requirements.txt
├── README.md
└── Makefile
```