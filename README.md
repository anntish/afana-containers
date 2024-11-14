# RUN
## sudo docker-compose -f docker-compose.yml up --build

# TEST
## Open URL http://localhost:8000/docs 
## You'll see the swagger, change the strings

{
  "user_name": "Ivan",
  "user_surname": "Ivanov",
  "user_job": "Data Scientist"
}

## Execute Postgres container
docker exec -it postgres-container psql -U myuser -d mydatabase

## Check your written data out!
SELECT * FROM users;
