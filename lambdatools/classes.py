from dataclasses import dataclass
from typing import Any


@dataclass
class LambdaClientContextMobileClient:
    installation_id: str
    app_title: str
    app_version_name: str
    app_version_code: str
    app_package_name: str


@dataclass
class LambdaCognitoIdentity:
    cognito_identity_id: str
    cognito_identity_pool_id: str


@dataclass
class LambdaClientContext:
    client: LambdaClientContextMobileClient
    custom: dict[str, Any]
    env: dict[str, Any]

@dataclass
class LambdaContext:
    function_name: str
    function_version: str
    invoked_function_arn: str
    memory_limit_in_mb: int
    aws_request_id: str
    log_group_name: str
    log_stream_name: str
    identity: LambdaCognitoIdentity
    client_context: LambdaClientContext

    @staticmethod
    def get_remaining_time_in_millis() -> int:
        # placeholder for typing
        return 0
