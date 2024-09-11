from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat,PositiveInt
from enum import Enum



class ProdutoEnum(str,Enum):
    produto1 = "Zapflow com Gemini"
    produto2 = "Zapflow com ChatGPT"
    produto3 = "Zapflow com LLama 3.0"
    
class vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
    
