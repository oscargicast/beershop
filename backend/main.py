from fastapi import FastAPI

from api.v1.routers import routers
from core.config import settings
from fastapi_versioning import VersionedFastAPI

from populate import make_orders


app = FastAPI(title=settings.PROJECT_NAME)


origins = [
    "*",
]


app.include_router(routers)
app = VersionedFastAPI(
    app,
    enable_latest=True,
    version_format="{major}",
    prefix_format="/api/v{major}",
)

make_orders()
