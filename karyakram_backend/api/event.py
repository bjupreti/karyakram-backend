from fastapi import APIRouter, Depends, status, HTTPException, Response
from models.event import Event
from sqlmodel import Session, select
from db.database import get_session, engine
from schemas.event import EventCreate, EventResponse
from sqlmodel import Session

router = APIRouter(prefix="/events", tags=["Events"])


@router.get("/", response_model=list[EventResponse])
def get_events(db: Session = Depends(get_session)):
    events = db.query(Event).all()
    return events


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=EventResponse)
def create_event(request: EventCreate, db: Session = Depends(get_session)):
    new_event = Event(**request.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


@router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, db: Session = Depends(get_session)):
    event = db.query(Event).filter(Event.event_id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with id {event_id} is not available",
        )
    return event


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_session)):
    event_query = db.query(Event).filter(Event.event_id == id)
    event = event_query.first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with id {id} is not available",
        )
    event_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{event_id}", status_code=status.HTTP_200_OK, response_model=EventResponse)
def update(id: int, request: Event, db: Session = Depends(get_session)):
    event_query = db.query(Event).filter(Event.event_id == id)
    event = event_query.first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with id {id} is not available",
        )
    event_query.update(request.dict(), synchronize_session=False)
    db.commit()
    return event_query.first()
