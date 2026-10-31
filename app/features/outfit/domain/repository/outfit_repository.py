from abc import ABC, abstractmethod

from app.features.outfit.data.model.outfit_model import OutfitResponseModel
from app.features.outfit.domain.params.outfit_params import OutfitParams


class OutfitRepository(ABC):
    @abstractmethod
    async def suggest_outfit(self, params: OutfitParams) -> OutfitResponseModel: ...
