from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from modules.exceptions import PlayerDoesNotExist
from modules.query_mongo import return_player_info

app = FastAPI()

@app.exception_handler(PlayerDoesNotExist)
async def player_dne(request: Request, exc: PlayerDoesNotExist):
    return JSONResponse(
        status_code=404,
        content={
            "message": "No player found."
        }
    )

@app.get("/nba/player/{player_name}")
async def player_exists(player_name: str):
    return return_player_info(player_name.replace("-", " "))