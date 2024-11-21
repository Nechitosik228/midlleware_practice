from typing import Awaitable, Callable
from fastapi import Request, Response, status
from starlette.middleware.base import BaseHTTPMiddleware


class CustomMidlleware(BaseHTTPMiddleware):
    def __init__(self, app: BaseHTTPMiddleware):
        super().__init__(app)

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        if "route" in request.url.path:
            if not request.headers.get("custom-header"):
                print(request.headers.get("custom-header"))
                return Response(
                    content="Bad request", status_code=status.HTTP_400_BAD_REQUEST
                )
        response = await call_next(request)
        return response


class CheckBodyMidlleware(CustomMidlleware):
    def __init__(self, app: BaseHTTPMiddleware):
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ):
        if "route" in request.url.path:
            if request.method == "POST":
                body = {}
                try:
                    body = await request.json()
                except Exception:
                    return Response(
                        status_code=status.HTTP_400_BAD_REQUEST, content="No JSON Body"
                    )
                if "test" not in body:
                    return Response(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        content="Invalid JSON Body",
                    )

        response = await super().dispatch(request, call_next)
        return response
