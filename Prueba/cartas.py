
## Main
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
# Modelo de datos para una película
class Cartas(BaseModel):
    numero: int
    palo: str
# Base de datos ficticia
cartas_db = [
    {"numero": 1, "palo": "Basto"},
    {"numero": 2, "palo": "Oro"}
]
@app.get("/cartas")
async def get_movies():
    return {"Cartas": cartas_db}

@app.post("/cartas")
async def add_carta(carta: Cartas):
    cartas_db.append(carta.dict())
    return {"message": "Carta agregada con éxito", "Carta:": carta}

@app.delete("/cartas/{title}")
async def delete_movie(numero: int,palo:str):
    for carta in cartas_db:
        if carta["numero"] == numero and carta["palo"] == palo:
            cartas_db.remove(carta)
            return {"message": f"'{carta}' eliminada con éxito"}
    raise HTTPException(status_code=404, detail="Carta no encontrada")

# Para usasrlo es uvicorn cartas:app localhost --port 8000