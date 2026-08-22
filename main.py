from fastapi import FastAPI,UploadFile,File
import pandas as pd
from database import process

app=FastAPI()

@app.get("/")
def Greetings():
    return "Hello my Nigga"

@app.post("/upload")
def Upload_Here(thefile: UploadFile = File(...)):
    result=process(thefile.file)
    return result
