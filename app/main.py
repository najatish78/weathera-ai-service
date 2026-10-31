from fastapi import FastAPI

from app.api import health

app = FastAPI(
    title="Weathera AI Service",
    description="Turns a weather forecast and a user profile into outfit advice.",
    version="0.1.0",
)

app.include_router(health.router)
