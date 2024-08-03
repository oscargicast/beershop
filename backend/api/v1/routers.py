from fastapi import APIRouter

from api.v1.resources import orders


routers = APIRouter()
router_list = [
    orders.router,
]

for router in router_list:
    routers.tags.append("v1")
    routers.include_router(router)
