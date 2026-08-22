import sqlite3 as sql
import pandas as pd
#-
conn=sql.connect('SalesData.db',check_same_thread=False)
cursor=conn.cursor()

def process(file):
    data=pd.read_csv(file)
    data['Date'] = data['Date'].str.strip()
    data.to_sql('sales',conn,if_exists='replace',index=False)

    cursor.execute("PRAGMA table_info(sales)")
    result=cursor.fetchall()

    columns= [row[1] for row in result]
    cursor.execute("SELECT COUNT(*) FROM sales")
    rows=cursor.fetchone()[0]

    return { "message": "File uploaded successfully",
             "table": "sales",
             "columns": columns, 
             "rows": rows 
            }

#-
def main():
    print(">>>Sales-Analyzer")
    print("1. What is the total sales?")
    print("2. What are the total sales by region?")
    print("3. What are the top 5 products?")
    print("4. What is the average sales per region?")
    print("5. What was the monthly sold trend?")

    reply=input("What do you want to check? : ")

    if reply=='1':
        Total_Sales()
    elif reply=='2':
        Region_Sales()
    elif reply=='3':
        Top_Products()
    elif reply=='4':
        Avrg_Sale()
    elif reply=='5':
        Sale_Trend()
#-
def Total_Sales():
    cursor.execute("SELECT SUM(Sales) FROM sales")
    result=cursor.fetchone()
    print("Total Sales =",result[0])

def Region_Sales():
    cursor.execute("""
        SELECT Region,SUM(Sales)
        FROM sales
        GROUP BY Region
    """)
    result=cursor.fetchall()

    for row in result:
        print(row)

def Top_Products():
    cursor.execute("""
        SELECT Product,COUNT(Product)
        FROM sales
        GROUP BY Product
        ORDER BY COUNT(Product) DESC
        LIMIT 5
    """)
    result=cursor.fetchall()

    for row in result:
        print(row)

def Avrg_Sale():
    cursor.execute("""
        SELECT Region,AVG(Sales)
        FROM sales
        GROUP BY Region
    """)
    result=cursor.fetchall()

    for row in result:
        print(row)

def Sale_Trend():
    cursor.execute("""
        SELECT strftime('%m',Date),COUNT(Product)
        FROM sales
        GROUP BY strftime('%m',Date)
    """)
    result=cursor.fetchall()

    for row in result:
        print(row)

#-