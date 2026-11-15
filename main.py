# python -m uvicorn main:app --reload
# git status
# git add .
# git commit -m "message"
# git push origin main

from fastapi import FastAPI,UploadFile,File,Form
from fastapi.responses import PlainTextResponse
import pandas as pd
from database import process
from database import run_sql
from database import clean_sql
from database import validate_sql
from test import sql_qr

app=FastAPI()

@app.get("/", response_class=PlainTextResponse)
def Greetings():
    return "Hello.\nTo analyze your data enter (/docs) in the end of url.\nThank-You:)"

@app.post("/upload")
def Upload_Here(thefile: UploadFile = File(...),question: str = Form(...)):
    result=process(thefile.file)

    column=result['columns']
    final_sql=sql_qr(column,question)
    clean=clean_sql(final_sql)

    if(validate_sql(clean)):
        answer=run_sql(clean)
    else:
        answer="Bande da putar ban te seedha swal pooch."

    return {
        "Data": result,
        "generated_sql": clean,
        "Answer": answer
    }
