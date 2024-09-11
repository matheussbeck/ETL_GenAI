from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat,PositiveInt
from enum import Enum



class ProdutoEnum(str,Enum):
    produto1 = "Zapflow com Gemini"
    produto2 = "Zapflow com ChatGPT"
    produto3 = "Zapflow com LLama 3.0"
    
class vendas(BaseModel):
    """
    Modelo de dados para as vendas.
    
    Args: 
        email (EmailStr): email do comprador
        data (datetime): data da venda
        valor (PositiveFloat): valor total da venda
        quantidade (PositiveFloat): quantidade total da venda
        produto (ProdutoEnum): nome do produto vendido   
    
    """

    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
    
