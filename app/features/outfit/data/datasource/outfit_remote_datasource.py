from abc import ABC, abstractmethod

from app.features.outfit.data.model.outfit_model import OutfitModel
from app.features.outfit.domain.params.outfit_params import OutfitParams


class OutfitRemoteDataSource(ABC):
    @abstractmethod
    async def suggest_outfit(self, params: OutfitParams) -> OutfitModel:
        """Raises on network errors or an invalid answer."""
