from fastapi import FastAPI
from routers import participant_manager_api
app = FastAPI(tags=["MIGx"])

app.include_router(participant_manager_api.router, tags=["Participant"])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)