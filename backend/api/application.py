from importlib import metadata
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.api.modules.router import api_router
from backend.api.lifetime import register_shutdown_event, register_startup_event

APP_ROOT = Path(__file__).parent.parent

APP_VERSION = "1.0.0"

def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="backend",
        version=APP_VERSION,
        docs_url=None,
        redoc_url=None,
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # # Adds startup and shutdown events.
    # register_startup_event(app)
    # register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api/v1")
    # Adds static directory.

    return app
