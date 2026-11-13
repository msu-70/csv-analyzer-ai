# python -m uvicorn main:app --reload

from fastapi import FastAPI,UploadFile,File,Form
from fastapi.responses import PlainTextResponse
import pandas as pd
from database import process
from test import sql_qr

app=FastAPI()

@app.get("/", response_class=PlainTextResponse)
def Greetings():
    return "Hello.\nTo analyze your data enter (/docs) in the end of url.\nThank-You:)"

@app.post("/upload")
def Upload_Here(thefile: UploadFile = File(...),question: str = Form(...)):
    result=process(thefile.file)

    column=result['columns']
    print(sql_qr(column,question)) 

    return result

