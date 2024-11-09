from fastapi import FastAPI
from routes import get_user_info
from models.init_db import init_db

app = FastAPI()

app.include_router(get_user_info.router)

init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
