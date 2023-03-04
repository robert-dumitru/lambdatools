from typing import Any
import json
from .classes import LambdaContext


def entrypoint(func: callable) -> callable:
    def wrapper(event: dict, context: LambdaContext) -> Any:
        annotations = func.__annotations__
        # pass through if already a lambda function
        if ["event", "context"] == list(annotations.keys()):
            return func(event, context)

        else:
            # extract function arguments from Lambda event
            func_args = event["body"]
            if isinstance(func_args, str):
                func_args = json.loads(func_args)
            for k, v in func_args.items():
                if not isinstance(v, annotations[k]):
                    # assume pydantic constructor
                    func_args[k] = annotations[k].from_raw(v)

            response: Any = func(**func_args)
            if isinstance(response, list):
                for i, v in enumerate(response):
                    try:
                        response[i] = json.dumps(v)
                    except TypeError:
                        # assume pydantic method
                        response[i] = v.json()
            if isinstance(response, dict):
                for k, v in response.items():
                    try:
                        response[k] = json.dumps(v)
                    except TypeError:
                        response[k] = v.json()
            try:
                return json.dumps(response)
            except TypeError:
                return response.json()

    return wrapper
