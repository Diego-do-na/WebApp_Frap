from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importa tus routers
from app.routers.pacientes_r import router as paciente_router
from app.routers.reportes_r import router as reportes_router
from app.routers.usuarios_r import router as usuarios_router
from app.routers.insumo_medicamentos_r import router as insumos_router
from app.routers.catalogos_r import router as catalogos_router

app = FastAPI(
    title="API de Expedientes Médicos",
    version="1.0.0"
)

# Configuración de CORS (permite acceso desde cualquier frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Puedes cambiarlo si quieres limitarlo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(paciente_router)
app.include_router(reportes_router)
app.include_router(usuarios_router)
app.include_router(insumos_router)
app.include_router(catalogos_router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente 🚀"}