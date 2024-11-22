# Lab_3

## Ход работы:

1) Запуск minikube


![image](https://github.com/user-attachments/assets/5f21d8cb-c1b3-4d4a-825f-7e398c77b691)


3) Убеждаемся, что контейнер с кубером запустился; смотрим на текущую конфигурацию


![image](https://github.com/user-attachments/assets/80fbf415-9a73-4c12-a5cd-dcb66ed59807)


5) Создаем объекты, чтобы они создались в кластере


![image](https://github.com/user-attachments/assets/dbaa94b0-a0ee-4ba1-8f63-7548907ac1cd)


6) Детально смотрим на описание postgres сервиса


![image](https://github.com/user-attachments/assets/cf5755f2-2c6a-4075-a3d7-9cb924301719)


7) Создаем сикрет и деплой объекты для nextcloud


![image](https://github.com/user-attachments/assets/4fc6ed11-ad58-4a53-a20f-f6e342189cbb)


8) Смотрим на состояние подов и изучаем логи nextcloud deployment (т.к. отсюда как раз отслеживаем ошибки, коих возникало немало)


![image](https://github.com/user-attachments/assets/26be6c96-afe2-4114-9108-9c39e1715648)


9) Создаем объект типа Service для деплоймента nextcloud


![image](https://github.com/user-attachments/assets/ba7dce62-c9ae-4338-b192-02e454aa6e24)


10) Осуществляем туннелирование трафика


![image](https://github.com/user-attachments/assets/b4eaf64b-1484-4393-a61f-c3027fb6786d)
![image](https://github.com/user-attachments/assets/dadf4c0f-aacf-4167-a273-12f3e2052572)


11) Открываем дашборды


![image](https://github.com/user-attachments/assets/699f242b-dc06-4711-8343-b96e3f52f5af)
![image](https://github.com/user-attachments/assets/12b3dc03-25a7-4727-ac34-868352fa7e28)


Последовательность действий для личного задания по сути своей та же. Необходимо было лишь отдельно создать объект Secret для postgres, и то же самое с конфигмапой для nextcloude


## Ответы на вопросы

1) Важен ли порядок выполнения манифестов?

Ответ: да, важен, т.к. деплоймент манифест использует данные с конфигмапа (название бд, имя пользователя, пароль). В случе с сервисами это необязательно, но все же рекомендовано - так мы гарантируем, что сетевая доступность будет настроена до запуска подов

2) Вопрос: что (и почему) произойдет, если отскейлить количество реплик postgres-deployment в 0, затем обратно в 1, после чего попробовать снова зайти на Nextcloud?

При переходе на сервис Nextcloud будет такая надпись в браузере:


![image](https://github.com/user-attachments/assets/78401207-7705-45ae-8515-f7581a80a54d)


После скейла обратно в 1 мы создадим "чистый" под postgres у которого вообще нет никаких данных (вспоминаем, что постргре был в эфемерном поде). Права доступа скорее всего пропадут или база может быть не полностью инициализирована, из-за чего Nextcloud не сможет подключится к БД.





