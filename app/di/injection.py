"""Wires the layers together, like `di/injection.dart` (get_it) in the app.

Routes ask for what they need with `Depends(...)`; tests swap any piece
with `app.dependency_overrides`.
"""

from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from openai import AsyncOpenAI

from app.core.config import Settings, get_settings
from app.features.outfit.data.datasource.outfit_local_datasource import (
    OutfitLocalDataSource,
)
from app.features.outfit.data.datasource.outfit_remote_datasource import (
    OutfitRemoteDataSource,
)
from app.features.outfit.data.datasource.outfit_remote_datasource_impl import (
    OutfitRemoteDataSourceImpl,
)
from app.features.outfit.data.repository.outfit_repository_impl import (
    OutfitRepositoryImpl,
)
from app.features.outfit.domain.repository.outfit_repository import OutfitRepository
from app.features.outfit.domain.usecase.suggest_outfit_usecase import (
    SuggestOutfitUseCase,
)


@lru_cache
def _llm_client(base_url: str, api_key: str) -> AsyncOpenAI:
    # One client (and its connection pool) per process, like a @singleton.
    return AsyncOpenAI(base_url=base_url, api_key=api_key)


def get_outfit_remote_datasource(
    settings: Annotated[Settings, Depends(get_settings)],
) -> OutfitRemoteDataSource:
    client = _llm_client(settings.llm_base_url, settings.llm_api_key)
    return OutfitRemoteDataSourceImpl(client, settings.llm_model)


def get_outfit_local_datasource() -> OutfitLocalDataSource:
    return OutfitLocalDataSource()


def get_outfit_repository(
    remote: Annotated[OutfitRemoteDataSource, Depends(get_outfit_remote_datasource)],
    local: Annotated[OutfitLocalDataSource, Depends(get_outfit_local_datasource)],
) -> OutfitRepository:
    return OutfitRepositoryImpl(remote, local)


def get_suggest_outfit_usecase(
    repository: Annotated[OutfitRepository, Depends(get_outfit_repository)],
) -> SuggestOutfitUseCase:
    return SuggestOutfitUseCase(repository)
