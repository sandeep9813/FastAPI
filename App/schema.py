from pydantic import BaseModel


class Cardio(BaseModel):
    age: int
    height: int
    weight: float
    ap_hi: int
    ap_lo: int
    cholesterol: int
    gluc: int
    smoke: int
    alco: int
    active: int