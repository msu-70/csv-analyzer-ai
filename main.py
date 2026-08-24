from fastapi import FastAPI,UploadFile,File
import pandas as pd
from database import process
from test import sql_qr

app=FastAPI()

@app.get("/")
def Greetings():
    return "Hello my Nigga"

@app.post("/upload")
def Upload_Here(thefile: UploadFile = File(...)):
    result=process(thefile.file)

    column=result['columns']
    print(sql_qr(column))

    return result

