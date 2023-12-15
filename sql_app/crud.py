from sqlalchemy.orm import Session

from . import model, schemas

def get_schools(db: Session):
    return db.query(model.School).all()

def get_houses(db):
    return db.query(model.House).all()

def get_school_by_id(db, school_id):
    return db.query(model.School).filter(model.School.id == school_id).first()

def get_flats_by_house(db, house_id):
    return db.query(model.Flat).filter(model.Flat.house_id == house_id).first()
