from pydantic import BaseModel

class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str

class CalculationResponse(BaseModel):
    result: float
