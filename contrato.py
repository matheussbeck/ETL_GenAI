from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr, validate_call
from enum import Enum

class ProdutoEnum(str,Enum)
    
class vendas(BaseModel):
    email: Emailstr
    data: datetime
    valor: float
    quantidade: int
    produto: str