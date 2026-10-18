# You receive a list of customer records from an upstream source. 
# The same customer_id can appear multiple times with different updated_at values. 
# Write a function dedupe_latest(records) that returns one record per customer_id, 
# keeping only the one with the latest updated_at.


records = [
    {"customer_id": 1, "name": "Asha",  "city": "Pune",   "updated_at": "2026-01-05"},
    {"customer_id": 2, "name": "Ravi",  "city": "Delhi",  "updated_at": "2026-01-03"},
    {"customer_id": 1, "name": "Asha",  "city": "Mumbai", "updated_at": "2026-02-10"},
    {"customer_id": 3, "name": "Meera", "city": "Chennai","updated_at": "2026-01-20"},
    {"customer_id": 2, "name": "Ravi",  "city": "Delhi",  "updated_at": "2025-12-30"},
]

def dedupe(records):
    latest = {}
    for rec in records:
        cid = rec['customer_id']
        if cid not in latest or rec['updated_at'] > latest[cid]['updated_at']:
            latest[cid] = rec

    return list(latest.values())



# spark code
# assume df is the df

from pyspark.sql.window import Window
from pyspark.sql.functions import *

df_unique = df.withColumn("rnk", row_number().over(Window.partitionBy("customer_id").orderBy(col("updated_at").desc())).where("rnk == 1").drop("rnk"))