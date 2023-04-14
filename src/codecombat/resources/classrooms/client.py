# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import CodeCombatEnvironment
from ..commons.types.classroom_response import ClassroomResponse
from ..commons.types.classroom_response_with_code import ClassroomResponseWithCode
from ..commons.types.object_id_string import ObjectIdString
from .types.ace_config import AceConfig
from .types.level_session_response import LevelSessionResponse
from .types.member_stat import MemberStat


class ClassroomsClient:
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

    def get(self, *, code: str, ret_member_limit: typing.Optional[float] = None) -> ClassroomResponseWithCode:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "classrooms"),
            params={"code": code, "retMemberLimit": ret_member_limit},
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClassroomResponseWithCode, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, name: str, owner_id: ObjectIdString, ace_config: AceConfig) -> None:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "classrooms"),
            json=jsonable_encoder({"name": name, "ownerID": owner_id, "aceConfig": ace_config}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def upsert_from_classroom(
        self, handle: str, *, code: str, user_id: str, ret_member_limit: typing.Optional[float] = None
    ) -> ClassroomResponse:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment.value}/", f"classrooms/{handle}/members"),
            json=jsonable_encoder({"code": code, "userId": user_id, "retMemberLimit": ret_member_limit}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClassroomResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_user_from_classroom(
        self, handle: str, *, user_id: str, ret_member_limit: typing.Optional[float] = None
    ) -> ClassroomResponse:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.value}/", f"classrooms/{handle}/members"),
            json=jsonable_encoder({"userId": user_id, "retMemberLimit": ret_member_limit}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClassroomResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def enroll_user_in_course(
        self,
        classroom_handle: str,
        course_handle: str,
        *,
        ret_member_limit: typing.Optional[float] = None,
        user_id: ObjectIdString,
    ) -> ClassroomResponse:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"classrooms/{classroom_handle}/courses/{course_handle}/enrolled"
            ),
            params={"retMemberLimit": ret_member_limit},
            json=jsonable_encoder({"userId": user_id}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClassroomResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remove_user_from_classroom(
        self,
        classroom_handle: str,
        course_handle: str,
        *,
        ret_member_limit: typing.Optional[float] = None,
        user_id: ObjectIdString,
    ) -> ClassroomResponse:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"classrooms/{classroom_handle}/courses/{course_handle}/remove-enrolled"
            ),
            params={"retMemberLimit": ret_member_limit},
            json=jsonable_encoder({"userId": user_id}),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClassroomResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_members_stats(
        self,
        classroom_handle: str,
        *,
        project: typing.Optional[str] = None,
        member_limit: typing.Optional[float] = None,
        member_skip: typing.Optional[float] = None,
    ) -> typing.List[MemberStat]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"classrooms/{classroom_handle}/stats"),
            params={"project": project, "memberLimit": member_limit, "memberSkip": member_skip},
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[MemberStat], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_level_session(self, classroom_handle: str, member_handle: str) -> typing.List[LevelSessionResponse]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"classrooms/{classroom_handle}/members/{member_handle}/sessions"
            ),
            auth=(self._username, self._password),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[LevelSessionResponse], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncClassroomsClient:
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

    async def get(self, *, code: str, ret_member_limit: typing.Optional[float] = None) -> ClassroomResponseWithCode:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "classrooms"),
                params={"code": code, "retMemberLimit": ret_member_limit},
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClassroomResponseWithCode, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, name: str, owner_id: ObjectIdString, ace_config: AceConfig) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "classrooms"),
                json=jsonable_encoder({"name": name, "ownerID": owner_id, "aceConfig": ace_config}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def upsert_from_classroom(
        self, handle: str, *, code: str, user_id: str, ret_member_limit: typing.Optional[float] = None
    ) -> ClassroomResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(f"{self._environment.value}/", f"classrooms/{handle}/members"),
                json=jsonable_encoder({"code": code, "userId": user_id, "retMemberLimit": ret_member_limit}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClassroomResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_user_from_classroom(
        self, handle: str, *, user_id: str, ret_member_limit: typing.Optional[float] = None
    ) -> ClassroomResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment.value}/", f"classrooms/{handle}/members"),
                json=jsonable_encoder({"userId": user_id, "retMemberLimit": ret_member_limit}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClassroomResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def enroll_user_in_course(
        self,
        classroom_handle: str,
        course_handle: str,
        *,
        ret_member_limit: typing.Optional[float] = None,
        user_id: ObjectIdString,
    ) -> ClassroomResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"classrooms/{classroom_handle}/courses/{course_handle}/enrolled"
                ),
                params={"retMemberLimit": ret_member_limit},
                json=jsonable_encoder({"userId": user_id}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClassroomResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remove_user_from_classroom(
        self,
        classroom_handle: str,
        course_handle: str,
        *,
        ret_member_limit: typing.Optional[float] = None,
        user_id: ObjectIdString,
    ) -> ClassroomResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(
                    f"{self._environment.value}/",
                    f"classrooms/{classroom_handle}/courses/{course_handle}/remove-enrolled",
                ),
                params={"retMemberLimit": ret_member_limit},
                json=jsonable_encoder({"userId": user_id}),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ClassroomResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_members_stats(
        self,
        classroom_handle: str,
        *,
        project: typing.Optional[str] = None,
        member_limit: typing.Optional[float] = None,
        member_skip: typing.Optional[float] = None,
    ) -> typing.List[MemberStat]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"classrooms/{classroom_handle}/stats"),
                params={"project": project, "memberLimit": member_limit, "memberSkip": member_skip},
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[MemberStat], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_level_session(self, classroom_handle: str, member_handle: str) -> typing.List[LevelSessionResponse]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"classrooms/{classroom_handle}/members/{member_handle}/sessions"
                ),
                auth=(self._username, self._password),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[LevelSessionResponse], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
