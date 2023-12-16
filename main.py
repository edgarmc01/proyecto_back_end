# main.py
from fastapi import FastAPI
from router.filament import filament_router
import json
from fastapi.responses import JSONResponse
from typing import Optional
import uvicorn
from fastapi import status
from config.database import engine, Base, session
from models.filaments import Filament as FilamentModels
from fastapi.encoders import jsonable_encoder
from schema.filament import Filament, ListFilaments, UpdateFilament

app = FastAPI() #usamos el modulo de fastapi

# Cambio en la documentacion
app.title = "Filamentos para impresoras 3D"
app.version = "1.0.0"

Base.metadata.create_all(bind=engine)
app.include_router(filament_router)

tabla_filamentos = []

@app.get("/all_filaments", status_code=status.HTTP_200_OK, response_model=ListFilaments, tags=['home'])#pasar a router
def mostrar_todos_filamentos():
    """
    ## Response
        - filament:List(Filament)
    """
    db = session()
    result =db.query(FilamentModels).all()

    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonable_encoder(result))

@app.get("/{id}", status_code=status.HTTP_200_OK,response_model=Filament, tags=['home'])
def mostrar_filamento(id: int):
    db = session()
    result = db.query(FilamentModels).filter(FilamentModels.id == id).first()
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"message":"el filamento no fue encontrado con ese id"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))

@app.post("/create_filament",status_code=status.HTTP_201_CREATED,response_model=Filament, tags=['home'])
def agregar_filamento(filament: Filament):
    """
    ## Args
        - filaments: Filament
    ## Response
        - filaments: Filament
    """
#   tabla_filamentos.append(Filament)
    db = session()
    new_filament = FilamentModels(**filament.dict())
    db.add(new_filament)
    db.commit()
    return filament.dict()

@app.delete("/{id}",status_code=status.HTTP_200_OK, tags=['home'])
def eliminar_filamento(id: int):
    db = session()
    result = db.query(FilamentModels).filter(FilamentModels.id == id).first()
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"message":"el filamento no fue encontrado con ese id para eliminar"})
    result_return = result
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result_return))
        
@app.patch("/{id}",status_code=status.HTTP_200_OK, tags=['home'])
def modificar_filamento(filament: UpdateFilament):
    db = session()
    result = db.query(FilamentModels).filter(FilamentModels.id == filament.id).first()
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"message":"el filamento no fue encontrado con ese id para actualizar"})
    filament_data = filament.dict(exclude_unset=True)#quita elementos
    for key, value in filament_data.items():
        setattr(result, key, value)
    result_return = result
    db.add(result)
    db.commit()
    db.refresh(result)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result_return))
