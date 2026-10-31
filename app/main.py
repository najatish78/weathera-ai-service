from fastapi import FastAPI

from app.features.health.presentation import routes as health
from app.features.outfit.presentation import routes as outfit

app = FastAPI(
    title="Weathera AI Service",
    description="Turns a weather forecast and a user profile into outfit advice.",
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(outfit.router)
