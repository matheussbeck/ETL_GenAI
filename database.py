import psycopg2
from psycopg2 import sql
from contrato import vendas
import streamlit as st
from dotenv import load_dotenv
import os

#carregar variaveis do arquivo .env
load_dotenv()

#Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')






>>> from sqlalchemy import select, bindparam
>>> scalar_subq = (
...     select(user_table.c.id)
...     .where(user_table.c.name == bindparam("username"))
...     .scalar_subquery()
... )

>>> with engine.connect() as conn:
...     result = conn.execute(
...         insert(address_table).values(user_id=scalar_subq),
...         [
...             {
...                 "username": "spongebob",
...                 "email_address": "spongebob@sqlalchemy.org",
...             },
...             {"username": "sandy", "email_address": "sandy@sqlalchemy.org"},
...             {"username": "sandy", "email_address": "sandy@squirrelpower.org"},
...         ],
...     )
...     conn.commit()