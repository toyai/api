from typing import Any, List

from fastapi import APIRouter

router = APIRouter()

# http://0.0.0.0:8000/api/v1/
@router.get('/')
async def detect():
    return {
        "message": "Hello World"
    }
    