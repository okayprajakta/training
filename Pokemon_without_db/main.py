from typing import List, Optional
import json
from fastapi import FastAPI, HTTPException, Query, status
from schemas import Pokemon
app = FastAPI()

# List to store Pokemon data
POKEMON_URL = "pokedex_raw_array.json"
pokemon_list=[]


# def read_data():
#     with open(POKEMON_URL, 'r') as file:
#         return json.load(file)
    
# def write_data(data):
#     with open(POKEMON_URL,'w') as file:
#         json.dump(data, file, indent=4)

# pokemon_list = read_data()

def extend_pokemons():
    """Load Pokemon data from a JSON file."""
    with open(POKEMON_URL, 'r') as file:
        data = json.load(file)
        pokemon_list.extend(data)
# Load Pokemon data at startup
extend_pokemons()

def save_pokemons():
    """Save Pokemon data to a JSON file."""
    with open(POKEMON_URL,"w") as file:
        json.dump(pokemon_list, file, indent=4)

@app.get("/pokemon")
def pokemon(
    name:Optional[str] = Query(None, description="Search by name"),
    min_height : Optional[int] = Query(None, description="Search ny Minimun Height",gt=0),
    max_height : Optional[int] = Query(None, description="Search by Maximum Height",gt=0),
    min_weight : Optional[int] = Query(None, description="Search by Minimum Weight", gt=0),
    max_weight : Optional[int] = Query(None, description="Search by Maximum weight", gt=0),
    limit: int = Query(10, description="Number of results per page", gt=0),
    offset: int = Query(0, description="Offset for pagination", ge=0)
):
    
    search_result= pokemon_list

    if name is not None:
        search_result = [
            pokemon for pokemon in search_result
            if name.lower() in pokemon['name'].lower()
        ]

    if min_height is not None:
        search_result = [
            pokemon for pokemon in search_result 
            if pokemon['height'] >= min_height]
        
    if max_height is not None:
        search_result = [
            pokemon for pokemon in search_result 
            if pokemon['height'] <= max_height]
    
    if min_weight is not None:
        search_result = [
            pokemon for pokemon in search_result
            if pokemon['weight'] >= min_weight]
        
    if max_weight is not None:
        search_result = [
            pokemon for pokemon in search_result 
            if pokemon['weight'] <= max_weight]
    
    paginated_result = search_result[offset:offset + limit]

    if paginated_result:
        return paginated_result
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= "Pokemon NOT Found"
    )
    


@app.get("/pokemon/{pokemon_id}", status_code=status.HTTP_200_OK)
def get_pokemon_by_id(pokemon_id: int):
    """
    Get a Pokemon by its ID.
    
    Args:
        pokemon_id (int): The ID of the Pokemon.
    
    Returns:
        dict: The Pokemon with the specified ID.
    """
    for pokemon in pokemon_list:
        if pokemon["id"] == pokemon_id:
            return pokemon
    raise HTTPException(status_code=404, detail="Pokemon not found")



@app.post("/pokemon", status_code=status.HTTP_201_CREATED)
def create_pokemon(pokemon: Pokemon):
    """
    Create a new Pokemon.
    
    Args:
        pokemon (Pokemon): The Pokemon data.
    
    Returns:
        dict: A message and the created Pokemon.
    """
    for p in pokemon_list:
        if p["id"] == pokemon.id :
            raise HTTPException(status_code=400, detail="Pokemon already exists")
    pokemon_list.append(pokemon.model_dump())
    save_pokemons()
    return {"message": "Pokemon created successfully", "pokemon": pokemon}

# @app.put("/pokemon/{pokemon_id}")
# def update_pokemon(pokemon_id: int, pokemon: Update):
#     """
#     Update an existing Pokemon.
    
#     Args:
#         pokemon_id (int): The ID of the Pokemon to update.
#         pokemon (Update): The updated Pokemon data.
    
#     Returns:
#         dict: A message and the updated Pokemon.
#     """
#     for p in pokemon_list:
#         if p["id"] == pokemon_id:
#             p["name"] = pokemon.name
#             p["height"] = pokemon.height
#             p["weight"] = pokemon.weight
#             p["xp"] = pokemon.xp
#             p["image_url"] = pokemon.image_url
#             p["pokemon_url"] = pokemon.pokemon_url
#             p["ability"] = pokemon.ability
#             p["stats"] = pokemon.stats
#             p["type"] = pokemon.type
#             save_pokemons()
#             return {"message": "Pokemon updated successfully", "pokemon": p}
        
#     raise HTTPException(status_code=404, detail="Pokemon not found")

@app.delete("/pokemon/{pokemon_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pokemon(pokemon_id: int):
    """
    Delete a Pokemon by its ID.
    
    Args:
        pokemon_id (int): The ID of the Pokemon to delete.
    
    Returns:
        dict: A message indicating the deletion status.
    """
    for pokemon in pokemon_list:
        if pokemon["id"] == pokemon_id:
            pokemon_list.remove(pokemon)
            save_pokemons()
            return {"message": "Pokemon deleted successfully"}
    raise HTTPException(status_code=404, detail="Pokemon not found")

@app.patch("/pokemon/{pokemon_id}", status_code=status.HTTP_200_OK)
def patch_pokemon(pokemon_id: int, update: dict):
    pokemon = next((p for p in pokemon_list if p["id"]==pokemon_id),None)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    
    for key, value in update.items():
        if key in pokemon:
            pokemon[key]=value
        else:
            raise HTTPException(status_code=400, detail=f"Invalid key:{key}")
        save_pokemons()
        return {"message":"Pokemon updated successfully","Pokemon":pokemon}