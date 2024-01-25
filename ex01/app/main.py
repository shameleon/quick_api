from fastapi import FastAPI, APIRouter, Query
from app.schemas import RecipeSearchResults, Recipe, RecipeCreate
from app.recipe_data import RECIPES
# from schemas import RecipeSearchResults, Recipe, RecipeCreate
# from recipe_data import RECIPES
from typing import Optional


"""
tutorial
code from 
https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-4-pydantic-schemas/
https://github.com/ChristopherGS/ultimate-fastapi-tutorial/blob/main/part-04-pydantic-schemas/app/main.py

Recipe response model is imported from a new schemas.py file.

"""

# instantiate a FastAPI app object, which is a Python class that provides all the functionality for your API.
app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

# instantiate an APIRouter which is how we can group our API endpoints (and specify versions and other config which we will look at later)
api_router = APIRouter()

# basic GET endpoint for our API.
@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, World!"}


# Uses a response_model
# https://fastapi.tiangolo.com/tutorial/response-model/
@api_router.get("/recipe/{recipe_id}", status_code=200, response_model=Recipe)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a single recipe by ID
    """
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if result:
        return result[0]


# Updated using the FastAPI parameter validation `Query` class
# # https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
@api_router.get("/search/", status_code=200, response_model=RecipeSearchResults)
def search_recipes(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="chicken"),
    max_results: Optional[int] = 10
) -> dict:
    """
    Search for recipes based on label keyword
    """
    if not keyword:
        # we use Python list slicing to limit results
        # based on the max_results query parameter
        return {"results": RECIPES[:max_results]}
    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)
    return {"results": list(results)[:max_results]}


# New addition, using Pydantic model `RecipeCreate` to define
# the POST request body
@api_router.post("/recipe/", status_code=201, response_model=Recipe)
def create_recipe(*, recipe_in: RecipeCreate) -> dict:
    """
    Create a new recipe (in memory only)
    """
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url,
    )
    RECIPES.append(recipe_entry.model_dump())

    return recipe_entry

# We use the include_router method of the app object 
# to register the router we created in step 2 on the FastAPI object.
app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    # wwith module called directly
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")