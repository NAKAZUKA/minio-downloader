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

## Запуск 

1) Указываем время начала и конца выгрузки файлов .tiff 
*например* 
START_DATE=2025-07-26T00:00:00
END_DATE=2025-07-28T23:59:59

2) Запускаем скрипт 
```bash
uv run python3 download_tifs.py
```

3) Перехоим в папку ```/downloads```