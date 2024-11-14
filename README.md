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
