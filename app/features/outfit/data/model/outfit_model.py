from typing import Literal

from pydantic import BaseModel, Field


# Caps on LLM text: a longer answer fails validation and the rules answer instead.
_ITEM_MAX = 60
_REASON_MAX = 300


class OutfitModel(BaseModel):
    """What a datasource returns. Text fields are in the requested language."""

    top: str = Field(max_length=_ITEM_MAX)
    bottom: str = Field(max_length=_ITEM_MAX)
    shoes: str = Field(max_length=_ITEM_MAX)
    jacket: str | None = Field(
        max_length=_ITEM_MAX, description="null when no jacket is needed"
    )
    umbrella: bool
    sunscreen: bool
    reason: str = Field(max_length=_REASON_MAX)


class OutfitResponseModel(OutfitModel):
    # Tells the app (and us while debugging) whether the LLM answered
    # or the rule-based fallback did.
    source: Literal["llm", "fallback"]
