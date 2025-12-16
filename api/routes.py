from fastapi import APIRouter, HTTPException
from app.models.schemas import CalculationRequest, CalculationResponse
from app.services.calculator import add, subtract, multiply, divide

router = APIRouter(prefix="/api/v1", tags=["Calculator"])

@router.post("/calculate", response_model=CalculationResponse)
def calculate(payload: CalculationRequest):
    try:
        if payload.operation == "add":
            result = add(payload.a, payload.b)
        elif payload.operation == "subtract":
            result = subtract(payload.a, payload.b)
        elif payload.operation == "multiply":
            result = multiply(payload.a, payload.b)
        elif payload.operation == "divide":
            result = divide(payload.a, payload.b)
        else:
            raise ValueError("Invalid operation")

        return CalculationResponse(result=result)

    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero not allowed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
