# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...types.clan_response import ClanResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ClansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upsert_member(self, handle: str, *, user_id: str) -> ClanResponse:
        """
        Upserts a user into the clan.

        Parameters:
            - handle: str. The document's `_id` or `slug`.

            - user_id: str. The `_id` or `slug` of the user to add to the clan.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"clan/{handle}/members"),
            json=jsonable_encoder({"userId": user_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClanResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncClansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upsert_member(self, handle: str, *, user_id: str) -> ClanResponse:
        """
        Upserts a user into the clan.

        Parameters:
            - handle: str. The document's `_id` or `slug`.

            - user_id: str. The `_id` or `slug` of the user to add to the clan.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"clan/{handle}/members"),
            json=jsonable_encoder({"userId": user_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClanResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
