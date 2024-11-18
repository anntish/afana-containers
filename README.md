# RUN
## docker-compose up --build

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


# LAB_1
# BAD PRACTICE OF USING CONTAINERIZATION

Лучше использовать монолит в следующих случаях:

1) Когда быстро нужно получить MVP, работа над стартапами
2) Должно быть легкое тестирование
3) В некоторых областях в принципе лучше использовать именно монолит (сфера телефонии, как пример из лекции)
4) Нужно исходить из принципов работы команды, а не только от архитектуры приложения (команда сплоченная, видят общую архитектуру, для них нет необходимости изоляции модулей) 
5) Более высокая производительность по сравнению с микросервисами

# DESCRIPTION OF GOOD DOCKERFILE

- IMAGE python с тегом 3.9 (используем питоновский образ)
- создаем рабочую директорию внутри контейнера (это как cd для терминала ОС, влияет на то, как выполнятся нижеследующие команды в докерфайле)
- копируем то, что у нас лежит в проекте в текущую директорию /app контейнера (потому что ".")
- выполняем команду ВНУТРИ контейнера (не сохраняем кэш, устанавливаем перечисленные зависимости)
- копируем все, что есть в локальных файлах в наш контейнер
- команда, которая выполняется при запуске контейнера (не путать с RUN, который нужен для выполнения команд в ПРОЦЕССЕ сборки) не забываем указывать хосты и порты, где будет запущен контейнер ;)

# DESCRIPTION OF BAD DOCKERFILE

- В плохом докерфайле можно заметить, что мы используем образ Python без явного указания конкретной версии образа
- Все наши команды выполняются в корне, копируем ВСЕ файлы сразу (теряется возможность кеширования отдельных файлов, возможно нужно игнорировать некоторые файлы при помощи dockerignore)
- Мы не используем requirements.txt, что КРАЙНЕ неудобно, если зависимостей довольно много
- Не указываем конкретный порт, на котором будет работать контейнер (может привести к проблемам)

# LAB_2
# HOW TO LIMIT RESOURCES?

Да, можно ограничивать ресурсы для сервисов. Можно написать так:

![image](https://github.com/user-attachments/assets/57de3001-4922-4cb9-8f72-7733a374ac8c)

          
limits - максимум, сколько получит сервис. В данном случае 50% от одного ядра процессора и 512 мб оперативной памяти\
reservations - минимум, который предоставлен сервису

# DOCKER-COMPOSE UP FOR ONLY CERTAIN CONTAINERS

При запуске композа можно указать, какой именно сервис запускать. К примеру, запустим на фоне сервис fastapi:

docker-compose up fastapi

Почитать: https://stackoverflow.com/questions/30233105/docker-compose-up-for-only-certain-containers
