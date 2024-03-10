from fastapi import APIRouter, Response

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/")
async def health():
    return Response(status_code=204)
