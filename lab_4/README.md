# Lab_4

## Ход работы:

1) Запускаем minikube и прогоняем манифесты и проверяем запущены ли поды

<img width="589" alt="Снимок экрана 2024-12-15 в 16 58 43" src="https://github.com/user-attachments/assets/f14f50a2-42ad-489d-875f-a36c05a375d7" />

2) По состояниям подов все ок, но также проверим логи с основных контейнеров:

**MinIO:**
<img width="798" alt="Снимок экрана 2024-12-15 в 17 39 34" src="https://github.com/user-attachments/assets/44e87ec0-08ab-4ee1-84e3-5502f287d31e" />
    
**Postgres:**
<img width="843" alt="Снимок экрана 2024-12-15 в 17 43 23" src="https://github.com/user-attachments/assets/bb918b8c-3c74-4b1d-a407-076884e7f514" />
**MLflow:**
<img width="571" alt="Снимок экрана 2024-12-15 в 17 44 10" src="https://github.com/user-attachments/assets/47442778-31a1-4b73-8151-474bff886ae6" />

**Init (контейнер с обучением модели, логированием метаданных и сохранением модели посредством mlflow; реализовано как Job, чтобы отработало единожды):**
<img width="651" alt="Снимок экрана 2024-12-15 в 17 47 26" src="https://github.com/user-attachments/assets/504cc12a-6b76-44ea-94b1-97d2ed567ecb" />
<img width="652" alt="Снимок экрана 2024-12-15 в 17 48 01" src="https://github.com/user-attachments/assets/e83c9996-372b-465e-9de1-7766465dddbd" />

**API:**
<img width="653" alt="Снимок экрана 2024-12-15 в 17 49 05" src="https://github.com/user-attachments/assets/c88337b6-415e-4e85-991b-28efb2788039" />

3) Сделаем туннелирование трафика и проверим, что MLFlow UI и MiniO UI корректно работают:
<img width="750" alt="Снимок экрана 2024-12-15 в 16 57 17" src="https://github.com/user-attachments/assets/17243246-7011-45c3-8eb1-b0dc902051e0" />


**MLflow**:
<img width="1422" alt="Снимок экрана 2024-12-15 в 16 52 58" src="https://github.com/user-attachments/assets/9ecf3f72-2468-4729-b27b-7aa143446d4b" />


<img width="1425" alt="Снимок экрана 2024-12-15 в 16 53 37" src="https://github.com/user-attachments/assets/abf46a39-e7d3-43bf-b64a-f6f426c9a51d" />


**MinIO**:
<img width="1435" alt="Снимок экрана 2024-12-15 в 16 55 07" src="https://github.com/user-attachments/assets/df954473-913a-4ba0-9c12-91eff0629604" />


<img width="1433" alt="Снимок экрана 2024-12-15 в 16 55 58" src="https://github.com/user-attachments/assets/f65824d4-b1df-4ded-bea8-d80f9d3f7ff5" />
