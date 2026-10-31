"""What the app sends to /suggest-outfit.

First draft: the exact fields are still open and will be refined with the
Flutter side.
"""

from typing import Literal

from pydantic import BaseModel, Field


class WeatherSummary(BaseModel):
    """Weather for the chosen time window, summarised by the app."""

    temp_min: float = Field(description="°C")
    temp_max: float = Field(description="°C")
    feels_like: float = Field(description="°C")
    rain_chance: int = Field(ge=0, le=100, description="Percent")
    wind_speed: float = Field(ge=0, description="m/s")
    condition: str = Field(description="OpenWeather main condition, e.g. Rain, Clear")


class UserProfile(BaseModel):
    age: int = Field(ge=1, le=120)
    gender: Literal["male", "female"]
    height_cm: int = Field(ge=50, le=250)
    weight_kg: int = Field(ge=10, le=300)
    cold_sensitivity: Literal["low", "normal", "high"] = "normal"
    style: Literal["casual", "formal", "sporty"] = "casual"


class OutfitParams(BaseModel):
    weather: WeatherSummary
    profile: UserProfile
    lang: Literal["ar", "en"] = "en"
