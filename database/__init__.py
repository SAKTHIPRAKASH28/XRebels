import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv()

DATABASE_URL = SQLALCHEMY_DATABASE_URL = f"postgresql://postgres.gtcynoixdpqnbgjdqlxq:{
    os.getenv("DB_PASSWORD")}@aws-0-ap-south-1.pooler.supabase.com:5432/postgres"


engine = create_engine(DATABASE_URL)
