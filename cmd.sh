#!/bin/bash
set -e
if [ "$ENV" = 'DEV' ]; then
    echo "Running Development Server" # Запуск сервера для разработки
    exec python "app.py"

elif [ "$ENV" = 'UNIT' ]; then
    echo "Running Unit Tests"
    exec python "test.py"

else
    echo "Running Production Server" # Запуск сервера для эксплуатации
    exec python3 /app/app.py 
fi
