from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.security import require_api_key
from app.di.injection import get_suggest_outfit_usecase
from app.features.outfit.data.model.outfit_model import OutfitResponseModel
from app.features.outfit.domain.params.outfit_params import OutfitParams
from app.features.outfit.domain.usecase.suggest_outfit_usecase import (
    SuggestOutfitUseCase,
)

router = APIRouter(tags=["outfit"], dependencies=[Depends(require_api_key)])


@router.post("/suggest-outfit")
async def suggest_outfit(
    params: OutfitParams,
    suggest: Annotated[SuggestOutfitUseCase, Depends(get_suggest_outfit_usecase)],
) -> OutfitResponseModel:
    """What to wear for the given weather and user. Never fails because of the LLM."""
    return await suggest(params)
