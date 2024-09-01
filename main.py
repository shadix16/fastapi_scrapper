from fastapi import FastAPI
from module_scrapper.urls import router

app = FastAPI()

app.include_router(router, prefix="/scrape", tags=["scrape"])
