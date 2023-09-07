from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
app = FastAPI()
now = datetime.now()

#basemodel for log object
class Log(BaseModel):
    id: str
    time_of_log: now
    body:str

#simple get route to get to landing page
@app.get("/")
def log_main():
    return{"Welcome to Landing Page: Hello Log"}

#get route to pull specific log file
@app.get("/logs/{log_id}")
def get_log(log:Log):
    return log

#POST route to add log to repository
@app.post("/logs")
async def create_log(log:Log):
    return log

#Put to edit specific log
@app.put("logs//update{log_id}")
async def update_log(log: Log):
    return log

#Delete to remove log
@app.delete("/logs/delete{log_id}")
async def delete_log(log:Log):
    return log