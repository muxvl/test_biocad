# test_biocad
docker + nginx

Структура
├── demo_service
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src
│       └── server.py
├── docker-compose.yml
└── nginx
    ├── Dockerfile
    └── src
        └── nginx.conf
        
Для запуска необходимо:
  1. Выполнить docker-compose up
  2. Перейти на: 0.0.0.0:80
  3. Готово!
