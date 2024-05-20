from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import restaurants, neighborhoods

app = FastAPI()

# CORS Middleware ekleme
origins = [
    "http://localhost:3000",  # Frontend'in çalıştığı URL
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(restaurants.router, prefix='/api')
app.include_router(neighborhoods.router, prefix='/api')
