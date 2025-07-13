from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from app import recommend_sabzi
from typing import List
from datetime import date, datetime
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Sabzi(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    date_cooked: date = Field(default_factory=lambda: datetime.today().date())


class SabziCreate(SQLModel):
    name: str


app = FastAPI()

@app.on_event("startup")
def startup():
    pass

@app.get("/sabzis", response_model = List[Sabzi])
def get_all(session: Session = Depends(get_session)):
    return session.exec(select(Sabzi)).all()

@app.post("/cook", response_model = Sabzi)
def add_or_update_sabzi(sabzi_data: SabziCreate, session: Session = Depends(get_session)):
    today = datetime.today().date()

    existing = session.exec(select(Sabzi).where(Sabzi.name == sabzi_data.name)).first()
    if existing:
        existing.date_cooked = today
        session.add(existing)
    else:
        existing = Sabzi(name = sabzi_data.name, date_cooked = today)
        session.add(existing)

    session.commit()
    session.refresh(existing)
    return existing

@app.get("/recommend")
def recommend(session: Session = Depends(get_session)):
    sabzis = session.exec(select(Sabzi)).all()
    name, days = recommend_sabzi(sabzis)
    return {"recommendation": name, "days_since_last_cooked": days}


@app.delete('/sabzi/{sabzi_id}', response_model = Sabzi)
def delete_sabzi(sabzi_id: int, session: Session = Depends(get_session)):
    sabzi = session.get(Sabzi, sabzi_id)
    if not sabzi:
        raise HTTPException(status_code = 404, detail = "Not Found!")
    
    session.delete(sabzi)
    session.commit()
    return sabzi