from app.features.outfit.data.model.outfit_model import OutfitResponseModel
from app.features.outfit.domain.params.outfit_params import OutfitParams
from app.features.outfit.domain.repository.outfit_repository import OutfitRepository


class SuggestOutfitUseCase:
    def __init__(self, repository: OutfitRepository):
        self._repository = repository

    async def __call__(self, params: OutfitParams) -> OutfitResponseModel:
        return await self._repository.suggest_outfit(params)
