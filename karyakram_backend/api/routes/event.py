from fastapi import APIRouter,Depends,status,HTTPException
from ...models.event import Event
from sqlmodel import Session
from ...db.database import get_session,create_db_and_tables

router = APIRouter(
    prefix="/event",
    tags=['EVENT']
)

get_db = create_db_and_tables()

# function is the path operation function and .get("/events ") is the operation path and @app is the path operation decorator
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_event(request: Event, db: Session = Depends(get_session)):
    new_event = Event(title=request.title, description=request.description, address_line_1=request.address_line_1, address_line_2=request.address_line_2)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

@router.delete("/{event_id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db: Session = Depends(get_session)):
    event = db.query(Event).filter(Event.event_id == id)
    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} is not available")
    event.delete(synchronize_session=False)
    db.commit()
    return 'Event deleted'

@router.put("/{event_id}",status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: Event, db: Session = Depends(get_session)):
    event = db.query(Event).filter(Event.event_id == id)
    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} is not available")
    
    #update only the fields that are passed in the request
    for attr,value in request.dict().items():
        if value:
            setattr(event,attr,value)
    # event.update(request)
    db.commit()
    return 'Event updated'

@router.get("/",status_code=status.HTTP_200_OK)
def get_events(db: Session = Depends(get_session)):
    blogs = db.query(Event).all()
    return blogs



@router.get("/{event_id}",status_code=200)
def show(event_id, db: Session = Depends(get_session)):
    event = db.query(Event).filter(Event.event_id == event_id).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {event_id} is not available")
    return event

