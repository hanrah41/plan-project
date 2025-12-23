# fastapi_app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI 앱이 정상 작동 중입니다."}
