from pydantic import BaseModel, Field
from typing import List


class Ability(BaseModel):
    """Ability model definition"""
    name : str
    is_hidden : bool

class Stats(BaseModel):
    """Stats model definition"""
    name : str
    base_stat : int = Field(gt=0)

class Type(BaseModel):
    """Type model definition"""
    name : str

class Update(BaseModel):
    """Update model definition"""
    name : str
    height : int
    weight : int
    xp : int
    image_url : str
    pokemon_url : str
    ability : list[Ability]
    stats : list[Stats]
    type : list[Type]

class Pokemon(BaseModel):
    """Pokemon model definition"""
    id : int=Field(gt=0)
    name : str
    height : int = Field(gt=0)
    weight : int = Field(gt=0)
    xp : int
    image_url : str
    pokemon_url : str
    ability : list[Ability]
    stats : list[Stats]
    type : list[Type]

