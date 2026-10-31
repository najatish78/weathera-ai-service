import logging

from app.features.outfit.data.datasource.outfit_local_datasource import (
    OutfitLocalDataSource,
)
from app.features.outfit.data.datasource.outfit_remote_datasource import (
    OutfitRemoteDataSource,
)
from app.features.outfit.data.model.outfit_model import OutfitResponseModel
from app.features.outfit.domain.params.outfit_params import OutfitParams
from app.features.outfit.domain.repository.outfit_repository import OutfitRepository

logger = logging.getLogger(__name__)


class OutfitRepositoryImpl(OutfitRepository):
    """Asks the LLM first and falls back to the rules, so it never fails."""

    def __init__(
        self,
        remote_datasource: OutfitRemoteDataSource,
        local_datasource: OutfitLocalDataSource,
    ):
        self._remote = remote_datasource
        self._local = local_datasource

    async def suggest_outfit(self, params: OutfitParams) -> OutfitResponseModel:
        try:
            outfit = await self._remote.suggest_outfit(params)
            source = "llm"
        except Exception:
            logger.exception("LLM suggestion failed, using rule-based fallback")
            outfit = self._local.suggest_outfit(params)
            source = "fallback"
        return OutfitResponseModel(**outfit.model_dump(), source=source)
