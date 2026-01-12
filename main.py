from fastapi import FastAPI, HTTPException
from Route.user_route import user_route

app = FastAPI()
app.include_router(user_route)

