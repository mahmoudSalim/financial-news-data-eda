from typing import Optional

from pydantic import BaseModel, Field

class Predict(BaseModel):
    text: str = Field(..., description="The input text.")
    confidence_threshold: Optional[float] = Field(0.0, title="The minimum accepted score.")

