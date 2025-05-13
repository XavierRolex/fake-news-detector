from pydantic import BaseModel

class NewsInput(BaseModel):
    text: str

class PredictionResult(BaseModel):
    label: str
    probability: float | str