# This file was auto-generated by Fern from our API Definition.

import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import CodeCombatEnvironment
from .types.clan_response import ClanResponse


class ClansClient:
    def __init__(
        self, *, environment: CodeCombatEnvironment = CodeCombatEnvironment.PRODUCTION, username: str, password: str
    ):
        self._environment = environment
        self._username = username
        self._password = password

    def upsert_clan(self, handle: str, *, user_id: str) -> ClanResponse:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment.value}/", f"clan/{handle}/members"),
            json=jsonable_encoder({"userId": user_id}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClanResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncClansClient:
    def __init__(
        self, *, environment: CodeCombatEnvironment = CodeCombatEnvironment.PRODUCTION, username: str, password: str
    ):
        self._environment = environment
        self._username = username
        self._password = password

    async def upsert_clan(self, handle: str, *, user_id: str) -> ClanResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(f"{self._environment.value}/", f"clan/{handle}/members"),
                json=jsonable_encoder({"userId": user_id}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClanResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
