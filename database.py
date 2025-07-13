from sqlmodel import create_engine, Session
from urllib.parse import quote_plus

user = 'manav-sh1'
password = quote_plus('Sparsematrix@1')
host = "db.ildfjmclpeylbedzufgt.supabase.co"
db = 'postgres'

DB_URL = 'postgresql://postgres.ildfjmclpeylbedzufgt:Sparsematrix%401@aws-0-ap-south-1.pooler.supabase.com:5432/postgres'

engine = create_engine(DB_URL, echo = True)

def get_session():
    return Session(engine)
