from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import (
    participant_manager_api
)


app = FastAPI(tags=["MIGx"])
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(participant_manager_api.router, tags=["Participant"])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)