# Python Question 9: Process a Large CSV Efficiently
# You have a CSV file containing 20 million rows with these columns:

# customer_id, amount
# 101, 500
# 102, 300
# 101, 200
# 103, 400
# 102, 100

# i will use the pyspark

# df = spark.read.format("csv").schema(_schema).option("header",True).load(pathtocsv)
# df_clean = df.filter("customer is not null & amount is not null")  #--> now its corrrect
# df_clean = df.filter((F.col("customer_id").isNotNull()) & (F.col("amount").isNotNull()))
# df_agg = df_clean.groupBy("customer_id").agg(sum("amount").alias("revenue"))

# the real python code, using chunking


import pandas as pd 
import numpy as np 

def process_large_csv(path):
    totals = {}

    for chunk in pd.read_csv(path, chunksize = 100_000):
        # first make the dtype constant
        chunk["customer_id"] = chunk["customer_id"].astype('string').str.strip()
        chunk["amount"] = pd.to_numeric(chunk["amount"],errors='coerce')

        #  remove the nulls and nan
        chunk = chunk.dropna(subset=['customer_id','amount'])   
        #here, it will drop rows if any column have null, 
        # Remember: By default, dropna() uses how="any", meaning drop the row if any specified column is null.
        # If you wanted to drop rows only when both columns are null, use how="all".
        chunk = chunk[chunk["customer_id"] !=""]

        #  aggregate for each chunk
        chunk_totals = chunk.groupby("customer_id")["amount"].sum()

        # accumulate total aross chunk_totals

        for customer_id, amount in chunk_totals.items():
            totals[customer_id] = totals.get(customer_id,0) + amount

    df = pd.DataFrame(list(totals.items()), columns=['customer_id','revenue'])
    return df

        



