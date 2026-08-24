from dotenv import load_dotenv
import os
from google import genai
from database import process

load_dotenv('key.env')
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def sql_qr(column):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f""" The table is called sales.
        The columns are:{column}.
        Generate only SQL query.
        Question:What are the total sales by region?"""
    )
    print(response.text)