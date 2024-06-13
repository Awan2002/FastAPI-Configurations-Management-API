from sqlalchemy.orm import Session
import models, schemas


# The create_configuration function creates a new Configuration record in the database using attributes from configuration, 
# including country_id, identity, identity_type, and is_required, then returns the newly created Configuration object after committing it to the database session.
def create_configuration(db: Session, configuration: schemas.ConfigurationCreate):
    db_configuration = models.Configuration(
        country_id=configuration.country_id,
        identity=configuration.identity,
        identity_type=configuration.identity_type,
        is_required=configuration.is_required
    )
    db.add(db_configuration)
    db.commit()
    db.refresh(db_configuration)
    return db_configuration




# The get_configurations_by_country_code function retrieves all Configuration records associated with a Country identified by country_code from 
# the database session (db) by performing a join operation between Configuration and Country tables based on the matching country code.
def get_configurations_by_country_code(db: Session, country_code: str):
    return db.query(models.Configuration).join(models.Country).filter(models.Country.code == country_code).all()






# The update_configuration function retrieves a Configuration record by configuration_id from the database session (db), 
# updates its attributes based on the provided configuration object, commits the changes to the database, refreshes db_configuration to reflect any updates, and returns the updated Configuration object.
def update_configuration(db: Session, configuration_id: int, configuration: schemas.ConfigurationUpdate):
    db_configuration = db.query(models.Configuration).filter(models.Configuration.id == configuration_id).first()
    if db_configuration:
        for key, value in configuration.dict().items():
            setattr(db_configuration, key, value)
        db.commit()
        db.refresh(db_configuration)
    return db_configuration





# The delete_configuration function deletes a Configuration record identified by configuration_id from the database session (db), 
# commits the deletion operation if the record exists, and returns the deleted Configuration object if found.
def delete_configuration(db: Session, configuration_id: int):
    db_configuration = db.query(models.Configuration).filter(models.Configuration.id == configuration_id).first()
    if db_configuration:
        db.delete(db_configuration)
        db.commit()
    return db_configuration
