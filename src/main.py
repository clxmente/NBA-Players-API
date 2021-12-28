from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from modules.exceptions import DoesNotExist
from modules.query_mongo import return_player_info, return_team_info

app = FastAPI()

@app.exception_handler(DoesNotExist)
async def player_dne(request: Request, exc: DoesNotExist):
    return JSONResponse(
        status_code=404,
        content={
            "message": "No record found."
        }
    )

@app.get("/nba/player/{player_name}")
async def player_endpoint(player_name: str):
    return return_player_info(player_name.replace("-", " "))

@app.get("/nba/team/{team_name}")
async def team_endpoint(team_name: str):
    return return_team_info(team_name)