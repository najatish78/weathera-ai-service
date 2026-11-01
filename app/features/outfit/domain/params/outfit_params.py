"""What the app sends to /suggest-outfit (the request side of the API contract)."""

from typing import Literal

from pydantic import BaseModel, Field

# OpenWeather's `weather[0].main` values, sent by the app as-is.
WeatherCondition = Literal[
    "Clear", "Clouds", "Rain", "Drizzle", "Thunderstorm", "Snow",
    "Mist", "Smoke", "Haze", "Dust", "Fog", "Sand", "Ash", "Squall", "Tornado",
]


class WeatherSummary(BaseModel):
    """Weather for the chosen time window, summarised by the app."""

    temp_min: float = Field(description="°C")
    temp_max: float = Field(description="°C")
    feels_like: float = Field(description="°C")
    # OpenWeather's `pop` is 0..1; the app sends it as a whole percent (0.8 -> 80).
    rain_chance: int = Field(ge=0, le=100, description="Percent, 0-100")
    wind_speed: float = Field(ge=0, description="m/s")
    condition: WeatherCondition


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
