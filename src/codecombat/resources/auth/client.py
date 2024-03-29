# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def login_oauth(
        self,
        *,
        provider: str,
        access_token: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        redirect: typing.Optional[str] = None,
        error_redirect: typing.Optional[str] = None,
    ) -> None:
        """
        Logs a user in. In this example, we call your lookup URL (let's say, `https://oauth.provider/user?t=<%= accessToken %>`) with the access token (`1234`). The lookup URL returns `{ id: 'abcd' }` in this case. We will match this `id` with the OAuthIdentity stored in the user information in our db. If everything checks out, the user is logged in and redirected to the home page.

        Parameters:
            - provider: str. Your OAuth Provider ID

            - access_token: typing.Optional[str]. Will be passed through your lookup URL to get the user ID. Required if no `code`.

            - code: typing.Optional[str]. Will be passed to the OAuth token endpoint to get a token. Required if no `accessToken`.

            - redirect: typing.Optional[str]. Override where the user will navigate to after successfully logging in.

            - error_redirect: typing.Optional[str]. If an error happens, redirects the user to this url, with at least query parameters `code`, `errorName` and `message`.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "auth/login-o-auth"),
            params=remove_none_from_dict(
                {
                    "provider": provider,
                    "accessToken": access_token,
                    "code": code,
                    "redirect": redirect,
                    "errorRedirect": error_redirect,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def login_oauth(
        self,
        *,
        provider: str,
        access_token: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        redirect: typing.Optional[str] = None,
        error_redirect: typing.Optional[str] = None,
    ) -> None:
        """
        Logs a user in. In this example, we call your lookup URL (let's say, `https://oauth.provider/user?t=<%= accessToken %>`) with the access token (`1234`). The lookup URL returns `{ id: 'abcd' }` in this case. We will match this `id` with the OAuthIdentity stored in the user information in our db. If everything checks out, the user is logged in and redirected to the home page.

        Parameters:
            - provider: str. Your OAuth Provider ID

            - access_token: typing.Optional[str]. Will be passed through your lookup URL to get the user ID. Required if no `code`.

            - code: typing.Optional[str]. Will be passed to the OAuth token endpoint to get a token. Required if no `accessToken`.

            - redirect: typing.Optional[str]. Override where the user will navigate to after successfully logging in.

            - error_redirect: typing.Optional[str]. If an error happens, redirects the user to this url, with at least query parameters `code`, `errorName` and `message`.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "auth/login-o-auth"),
            params=remove_none_from_dict(
                {
                    "provider": provider,
                    "accessToken": access_token,
                    "code": code,
                    "redirect": redirect,
                    "errorRedirect": error_redirect,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
