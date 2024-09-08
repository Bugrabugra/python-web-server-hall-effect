from fastapi import FastAPI
from pydantic import BaseModel
import logging

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

class Hall(BaseModel):
    window: str
    state: str

app = FastAPI()

@app.post("/hall")
def hall_handler(hall: Hall):
    logger.debug(hall)
    return hall

@app.get("/healthcheck")
def healthcheck():
    return "OK"