# Reference - https://fastapi.tiangolo.com/tutorial/
# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
# Important: fastAPI looks in a chronological order from top to bottom to see what matches the URL so, try to write the function and endpoints by small to large urls, specially in case of path parameters

# It uses ASGI (Asynchronous Server Gateway Interface) which is a spiritual successor of WSGI (Web Server Gateway Interface) 

# The key difference between ASGI (Asynchronous Server Gateway Interface) and WSGI (Web Server Gateway Interface) is how they handle requests, specifically synchronous vs. asynchronous requests.


# To run the FastAPI code, we need to run the command-
# uvicorn filename:object(instance name) --reload
# in this case, uvicorn main:app --reload
# here --reload means when we make any change to our fastapi code it will automaticaally detect the changes and restart the server
# Also there is another way to run fastapi app as-
# fastapi run filename.py  -- to run at production level mode
# fastapi dev filename-py -- to run at development level mode

# pydantic enforces type hints at runtime, and provides user friendly error when data is invalid
# this is used to get the data from ui in case of post method
# defines how data should be in pure, canonical python and validate it with pydantic
# FastAPI is now compatible with both Pydantic v1 and Pydantic v2.
# Based on how new the version of FastAPI you are using, there could be small method name changes.
# The three biggest are:
# 1- .dict() function is now renamed to .model_dump()
# 2- schema_extra function within a Config class is now renamed to json_schema_extra
# 3- Optional variables need a =None example: id: Optional[int] = None

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List , Optional


app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str 
    origin: str

teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"message": "welcome to blr"}

@app.get("/teas")
def get_teas():
    return teas 


@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea


@app.put("/teas/{tea_id}")
def update_tea(tea_id:int, updated_tea: Tea):
    for index,tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = update_tea
            return update_tea
        
    return {"error": "tea not found"}


@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index,tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)
            return deleted
        
    return {"error": "tea not found"}




# run http://127.0.0.1:8000/docs on browser, it will show the document for APIs
#  It will display the complete code in ui for testing our written APIs 
# similar we have /redoc
# this is what called as "Swagger UI"