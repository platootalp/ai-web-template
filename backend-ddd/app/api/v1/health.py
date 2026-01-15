# genAI_master_start
from fastapi import APIRouter

from app.interfaces.http.schemas import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")
# genAI_master_end
