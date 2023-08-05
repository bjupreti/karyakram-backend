from sqlmodel import  Session, SQLModel, create_engine
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

conn_str = "sqlite:///" + os.path.join(BASE_DIR, "db", "karyakram.db")
print("Base",conn_str)

engine = create_engine(conn_str, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session



