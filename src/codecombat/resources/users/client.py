# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import CodeCombatEnvironment
from ..commons.types.classroom_response_with_code import ClassroomResponseWithCode
from ..commons.types.object_id_string import ObjectIdString
from ..commons.types.user_response import UserResponse
from .types.hero_config import HeroConfig
from .types.user_role import UserRole


class UsersClient:
    def __init__(
        self,
        *,
        environment: CodeCombatEnvironment = CodeCombatEnvironment.PRODUCTION,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
    ):
        self._environment = environment
        self._username = username
        self._password = password

    def create(
        self,
        *,
        name: str,
        email: str,
        role: typing.Optional[UserRole] = None,
        preferred_language: typing.Optional[str] = None,
        hero_config: typing.Optional[HeroConfig] = None,
        birthday: typing.Optional[str] = None,
    ) -> None:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "users"),
            json=jsonable_encoder(
                {
                    "name": name,
                    "email": email,
                    "role": role,
                    "preferredLanguage": preferred_language,
                    "heroConfig": hero_config,
                    "birthday": birthday,
                }
            ),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, handle: str, *, include_play_time: typing.Optional[str] = None) -> UserResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}"),
            params={"includePlayTime": include_play_time},
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, handle: str, *, name: str, birthday: typing.Optional[str] = None) -> UserResponse:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}"),
            json=jsonable_encoder({"name": name, "birthday": birthday}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_classrooms(
        self, handle: str, *, ret_member_limit: typing.Optional[float] = None
    ) -> typing.List[ClassroomResponseWithCode]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/classrooms"),
            params={"retMemberLimit": ret_member_limit},
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ClassroomResponseWithCode], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_hero(self, handle: str, *, thang_type: typing.Optional[ObjectIdString] = None) -> UserResponse:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/hero-config"),
            json=jsonable_encoder({"thangType": thang_type}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def set_ace_config(
        self,
        handle: str,
        *,
        live_completion: typing.Optional[bool] = None,
        behaviors: typing.Optional[bool] = None,
        language: typing.Optional[str] = None,
    ) -> UserResponse:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/ace-config"),
            json=jsonable_encoder({"liveCompletion": live_completion, "behaviors": behaviors, "language": language}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def add_o_auth_identity(
        self,
        handle: str,
        *,
        provider: str,
        access_token: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
    ) -> UserResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/o-auth-identities"),
            json=jsonable_encoder({"provider": provider, "accessToken": access_token, "code": code}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_subscription(self, handle: str, *, ends: dt.datetime) -> UserResponse:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/subscription"),
            json=jsonable_encoder({"ends": ends}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def shorten_subscription(self, handle: str, *, ends: dt.datetime) -> UserResponse:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/shorten-subscription"),
            json=jsonable_encoder({"ends": ends}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def grant_license(self, handle: str, *, ends: dt.datetime) -> UserResponse:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/license"),
            json=jsonable_encoder({"ends": ends}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def shorten_license(self, handle: str, *, ends: dt.datetime) -> UserResponse:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/shorten-license"),
            json=jsonable_encoder({"ends": ends}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def find_user(self, property: str, value: str) -> None:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"user-lookup/{property}/{value}"),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncUsersClient:
    def __init__(
        self,
        *,
        environment: CodeCombatEnvironment = CodeCombatEnvironment.PRODUCTION,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
    ):
        self._environment = environment
        self._username = username
        self._password = password

    async def create(
        self,
        *,
        name: str,
        email: str,
        role: typing.Optional[UserRole] = None,
        preferred_language: typing.Optional[str] = None,
        hero_config: typing.Optional[HeroConfig] = None,
        birthday: typing.Optional[str] = None,
    ) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "users"),
                json=jsonable_encoder(
                    {
                        "name": name,
                        "email": email,
                        "role": role,
                        "preferredLanguage": preferred_language,
                        "heroConfig": hero_config,
                        "birthday": birthday,
                    }
                ),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, handle: str, *, include_play_time: typing.Optional[str] = None) -> UserResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}"),
                params={"includePlayTime": include_play_time},
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(self, handle: str, *, name: str, birthday: typing.Optional[str] = None) -> UserResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}"),
                json=jsonable_encoder({"name": name, "birthday": birthday}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_classrooms(
        self, handle: str, *, ret_member_limit: typing.Optional[float] = None
    ) -> typing.List[ClassroomResponseWithCode]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/classrooms"),
                params={"retMemberLimit": ret_member_limit},
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ClassroomResponseWithCode], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_hero(self, handle: str, *, thang_type: typing.Optional[ObjectIdString] = None) -> UserResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/hero-config"),
                json=jsonable_encoder({"thangType": thang_type}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def set_ace_config(
        self,
        handle: str,
        *,
        live_completion: typing.Optional[bool] = None,
        behaviors: typing.Optional[bool] = None,
        language: typing.Optional[str] = None,
    ) -> UserResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/ace-config"),
                json=jsonable_encoder(
                    {"liveCompletion": live_completion, "behaviors": behaviors, "language": language}
                ),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def add_o_auth_identity(
        self,
        handle: str,
        *,
        provider: str,
        access_token: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
    ) -> UserResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/o-auth-identities"),
                json=jsonable_encoder({"provider": provider, "accessToken": access_token, "code": code}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_subscription(self, handle: str, *, ends: dt.datetime) -> UserResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/subscription"),
                json=jsonable_encoder({"ends": ends}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def shorten_subscription(self, handle: str, *, ends: dt.datetime) -> UserResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/shorten-subscription"),
                json=jsonable_encoder({"ends": ends}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def grant_license(self, handle: str, *, ends: dt.datetime) -> UserResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/license"),
                json=jsonable_encoder({"ends": ends}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def shorten_license(self, handle: str, *, ends: dt.datetime) -> UserResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(f"{self._environment.value}/", f"users/{handle}/shorten-license"),
                json=jsonable_encoder({"ends": ends}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def find_user(self, property: str, value: str) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"user-lookup/{property}/{value}"),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)