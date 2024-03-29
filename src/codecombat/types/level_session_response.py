# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .datetime_string import DatetimeString
from .level_session_response_level import LevelSessionResponseLevel
from .level_session_response_state import LevelSessionResponseState
from .object_id_string import ObjectIdString


class LevelSessionResponse(pydantic.BaseModel):
    state: typing.Optional[LevelSessionResponseState]
    level: typing.Optional[LevelSessionResponseLevel]
    level_id: typing.Optional[str] = pydantic.Field(alias="levelID", description="Level slug like `wakka-maul`")
    creator: typing.Optional[ObjectIdString]
    playtime: typing.Optional[int] = pydantic.Field(description="Time played in seconds.")
    changed: typing.Optional[DatetimeString]
    created: typing.Optional[DatetimeString]
    date_first_completed: typing.Optional[DatetimeString] = pydantic.Field(alias="dateFirstCompleted")
    submitted: typing.Optional[bool] = pydantic.Field(
        description="For arenas. Whether or not the level has been added to the ladder."
    )
    published: typing.Optional[bool] = pydantic.Field(
        description="For shareable projects. Whether or not the project has been shared with classmates."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
