#!/bin/sh

# Ждем, пока база данных станет доступной
while ! nc -z $HOST $PORT;
do
    echo "Waiting for database..."
    sleep 1
done

# Запускаем Django сервер
exec "$@"