
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.finance_rates import get_rate

class CurrencyConvertRequest(BaseModel):
    amount: float
    from_currency: str
    to_currency: str

class CurrencyConvertResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    converted: float
    rate: float

router = APIRouter()

@router.post("/convert", response_model=CurrencyConvertResponse)
def convert_currency(request: CurrencyConvertRequest):
    try:
        rate = get_rate(request.from_currency, request.to_currency)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    converted = request.amount * rate
    return CurrencyConvertResponse(
        from_currency=request.from_currency,
        to_currency=request.to_currency,
        amount=request.amount,
        converted=converted,
        rate=rate
    )
