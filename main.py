from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Creates a new configuration using data provided in the request body and returns the created configuration.
@app.post("/create_configuration/", response_model=schemas.Configuration)
def create_configuration(configuration: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    return crud.create_configuration(db=db, configuration=configuration)


# Retrieves a list of configurations associated with the specified country_code and returns them as a list of schemas.Configuration.
@app.get("/get_configuration/{country_code}", response_model=list[schemas.Configuration])
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    print(country_code)
    configurations = crud.get_configurations_by_country_code(db, country_code=country_code)
    print(configurations)
    if configurations is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return configurations

# Updates the configuration identified by configuration_id using data provided in the request body and returns the updated configuration.
@app.post("/update_configuration/{configuration_id}", response_model=schemas.Configuration)
def update_configuration(configuration_id: int, configuration: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_configuration = crud.update_configuration(db, configuration_id=configuration_id, configuration=configuration)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

# Deletes the configuration identified by configuration_id and returns the deleted configuration.
@app.delete("/delete_configuration/{configuration_id}", response_model=schemas.Configuration)
def delete_configuration(configuration_id: int, db: Session = Depends(get_db)):
    db_configuration = crud.delete_configuration(db, configuration_id=configuration_id)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration
