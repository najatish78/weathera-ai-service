"""Asks the LLM through any OpenAI-compatible API (Gemini by default)."""

import json

from openai import AsyncOpenAI

from app.features.outfit.data.datasource.outfit_remote_datasource import (
    OutfitRemoteDataSource,
)
from app.features.outfit.data.model.outfit_model import OutfitModel
from app.features.outfit.domain.params.outfit_params import OutfitParams

_LANGUAGE = {"ar": "Arabic", "en": "English"}

_SYSTEM_PROMPT = """You are a practical stylist inside a weather app.
Given the weather and the user's profile, decide what they should wear.
Pick concrete items that fit the weather, the user's gender, style and cold
sensitivity: for example waterproof boots in rain, sandals on a hot beach day.

Answer ONLY with a JSON object matching this schema:
{schema}

Write every text value in {language}. Use null for "jacket" when none is needed."""


class OutfitRemoteDataSourceImpl(OutfitRemoteDataSource):
    def __init__(self, client: AsyncOpenAI, model: str):
        self._client = client
        self._model = model

    async def suggest_outfit(self, params: OutfitParams) -> OutfitModel:
        system = _SYSTEM_PROMPT.format(
            schema=json.dumps(OutfitModel.model_json_schema()),
            language=_LANGUAGE[params.lang],
        )
        user = params.model_dump_json(include={"weather", "profile"})

        completion = await self._client.chat.completions.create(
            model=self._model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            response_format={"type": "json_object"},
            temperature=0.4,
        )
        return OutfitModel.model_validate_json(completion.choices[0].message.content or "")
