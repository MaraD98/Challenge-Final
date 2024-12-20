from fastapi import FastAPI
from app.routers.router import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir cualquier origen. Cambia esto a dominios específicos para mayor seguridad.
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluye los endpoints definidos en endpoints.py
app.include_router(router)

