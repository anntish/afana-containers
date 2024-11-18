# RUN
## sudo docker-compose -f docker-compose.yml up --build

# TEST
## Открыть URL http://localhost:8000/docs 

## Вы увидите swagger, поменяйте значения
{
  "user_name": "Ivan",
  "user_surname": "Ivanov",
  "user_job": "Data Scientist"
}

## Запустите контейнер Postgres
docker exec -it postgres-container psql -U myuser -d mydatabase

## Проверь, что получилось!
SELECT * FROM users;


# BAD PRACTICE

1) В плохом докерфайле можно заметить, что мы используем образ Python без явного указания конкретной версии образа
2) Все наши команды выполняются в корне, копируем ВСЕ файлы сразу (теряется возможность кеширования отдельных файлов, возможно нужно игнорировать некоторые файлы при помощи dockerignore)
3) Мы не используем requirements.txt, что КРАЙНЕ неудобно, если зависимостей довольно много
4) Не указываем конкретный порт, на котором будет работать контейнер (может привести к проблемам)
