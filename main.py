from typing import Union
from insert_data import insert_data,get_contact,validate_input,sanitize_input
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/form/contact")
async def read_root(request: Request):
        data =await request.json()
        if not data:
            return JSONResponse({"message": "INVALID"}, status_code=400)

        
        sanitized_data = sanitize_input(data)
        
        if not validate_input(sanitized_data):
            print("returned from validate_input")
            return JSONResponse({"message": "INVALID"}, status_code=400)
        
        insert_data(sanitized_data)
        
        return JSONResponse({"message": "Ok"}, status_code=200)

@app.get("/api/v1/form/detail")
async def read_item():
   return get_contact()