from typing import Literal

from pydantic import BaseModel, Field


class OutfitModel(BaseModel):
    """What a datasource returns. Text fields are in the requested language."""

    top: str
    bottom: str
    shoes: str
    jacket: str | None = Field(description="null when no jacket is needed")
    umbrella: bool
    sunscreen: bool
    reason: str


class OutfitResponseModel(OutfitModel):
    # Tells the app (and us while debugging) whether the LLM answered
    # or the rule-based fallback did.
    source: Literal["llm", "fallback"]
