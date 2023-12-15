# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import Optional

#from config.database import engine, Base

#from middlewares.error_handler import ErrorHandler

#from router.movie import movie_router
#from router.auth import auth_router

# Crear una instancia de FastAPI (aplicacion)
app = FastAPI()


# Cambio en la documentacion
app.title = "local lujos"
app.version = "1.0.0"

#app.add_middleware(ErrorHandler)
#app.include_router(movie_router)
#app.include_router(auth_router)

#Base.metadata.create_all(bind=engine)

class Libro(BaseModel):
    titulo:str
    autor:str
    paginas: int
    editorial: Optional[str]

@app.get("/", tags=['home'])
def message():
    return HTMLResponse(content="<h1>Hola Mundo !!!!</h1>")

@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return {"data": id}

@app.post("/libros")
def insertar_libro(libro: Libro):
    return {"message":f"libro {libro,titulo} insertado"}
