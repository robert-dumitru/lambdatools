from typing import Any
from .classes import LambdaContext


def entrypoint(func: callable) -> callable:
    def wrapper(event: dict, context: LambdaContext) -> Any:
        annotations = func.__annotations__
        # pass through if already a lambda function
        if ["event", "context"] == list(annotations.keys()):
            return func(event, context)

        else:
            raise NotImplementedError

    return wrapper
