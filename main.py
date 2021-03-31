from fastapi import FastAPI
from controllers import router as CitiesRouter


app = FastAPI()


app.include_router(
    CitiesRouter,
    prefix="/api",
    tags=['cities'],
)
