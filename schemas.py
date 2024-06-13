from typing import List, Optional
from pydantic import BaseModel

# A base model defining the structure for configuration data
class ConfigurationBase(BaseModel):
    country_id: int
    identity: str
    identity_type: str
    is_required: bool

# Inherits from ConfigurationBase. Used for creating new configurations
class ConfigurationCreate(ConfigurationBase):
    pass

# Inherits from ConfigurationBase. Used for creating new configurations
class ConfigurationUpdate(ConfigurationBase):
    pass

# Extends ConfigurationBase to include additional fields "id" and enables orm_mode:
class Configuration(ConfigurationBase):
    id: int
    class Config:
        orm_mode: True

# A base model defining the structure for country data
class CountryBase(BaseModel):
    country_name: str
    country_code: str
# Inherits from CountryBase. Used for creating new countries:
class CountryCreate(CountryBase):
    pass

# Extends CountryBase to include an id and a list of configurations, and enables orm_mode:
class Country(CountryBase):
    id: int

    class Config:
        orm_mode: True