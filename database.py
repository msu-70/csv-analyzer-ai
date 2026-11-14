import sqlite3 as sql
import pandas as pd
import re
#-
conn=sql.connect('SalesData.db',check_same_thread=False)
cursor=conn.cursor()

#
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

def clean_sql(query):
    query = query.strip()
    query = re.sub(r"```sql\s*", "", query, flags=re.IGNORECASE)
    query = re.sub(r"```", "", query)
    return query.strip()

def validate_sql(final_sql):
    final_sql = final_sql.strip()

    forbidden_words = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE"]
    for i in range(len(forbidden_words)):
        if(forbidden_words[i] in final_sql.upper()):
            return False

    if (final_sql.upper().startswith("SELECT")):
        return True
    else:
        return False

def run_sql(validated_sql):
    result = conn.execute(validated_sql)
    rows = result.fetchall()

    return rows
