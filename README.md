# CodeCombat Python Library

[![pypi](https://img.shields.io/pypi/v/codecombat.svg)](https://pypi.python.org/pypi/codecombat)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Documentation

API documentation is available at https://codecombat.com/api-docs.

## Installation

Add this dependency to your project's build file:

```bash
pip install codecombat
# or
poetry add codecombat
```

## Usage

```python
from codecombat.client import CodeCombatApi

client = CodeCombatApi(
  username="CLIENT_ID", password="CLIENT_SECRET")

const response = client.users.set_ace_config(
  document_id="document_id",
  live_completion=True,
  language="python"
);

print('Received response from Code Combat', response);
```

## Async client

This SDK also includes an async client, which supports the `await` syntax:

```python
from codecombat.client import AsyncCodeCombatApi

raven = AsyncRavenApi(
  username="CLIENT_ID", password="CLIENT_SECRET")

async def set_ace_config() -> None:
  await client.users.set_ace_config(
    document_id="document_id",
    live_completion=True,
    language="python"
  );
```

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your build.gradle file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest [opening an issue](https://github.com/ravenappdev/raven-java) first to discuss with us!

On the other hand, contributions to the README are always very welcome!
