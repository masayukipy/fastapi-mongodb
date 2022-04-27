from fastapi import FastAPI
from models.Developer import Developer
from fastapi.responses import JSONResponse
import motor.motor_asyncio
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

app = FastAPI()
developers = []

async def connection():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://127.0.0.1:27017')
    db = client['mydb']
    return db

@app.get('/developers')
async def get_developers():
    try:
        db = await connection()
        developers = await db.developers.find().to_list(1000)
        for developer in developers: developer['_id'] = str(developer['_id'])
        return JSONResponse(status_code=200, content={'data': developers})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': 'Ha ocurrido un error'})

@app.get('/developers/{id}')
async def get_developers(id: str):
    try:
        db = await connection()
        developer = await db.developers.find_one({"_id": ObjectId(id)})
        if not developer:
            return JSONResponse(status_code=400, content={'message':'No encontrado'})
        developer['_id'] = str(developer['_id'])
        return JSONResponse(status_code=200, content={'data':developer})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': 'Ha ocurrido un error'})

@app.get('/developers/{id}/skills')
async def get_developers(id: str):
    try:
        db = await connection()
        developer = await db.developers.find_one({"_id": ObjectId(id)})
        if not developer:
            return JSONResponse(status_code=400, content={'message':'No encontrado'})
        developer['_id'] = str(developer['_id'])
        return JSONResponse(status_code=200, content={'data':developer['skills']})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': 'Ha ocurrido un error'})

@app.get('/developers/{id}/experience')
async def get_developers(id: str):
    try:
        db = await connection()
        developer = await db.developers.find_one({"_id": ObjectId(id)})
        if not developer:
            return JSONResponse(status_code=400, content={'message':'No encontrado'})
        developer['_id'] = str(developer['_id'])
        return JSONResponse(status_code=200, content={'data':developer['experience']})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': 'Ha ocurrido un error'})

@app.get('/developers/{id}/languages')
async def get_developers(id: str):
    try:
        db = await connection()
        developer = await db.developers.find_one({"_id": ObjectId(id)})
        if not developer:
            return JSONResponse(status_code=400, content={'message':'No encontrado'})
        developer['_id'] = str(developer['_id'])
        return JSONResponse(status_code=200, content={'data':developer['languages']})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': 'Ha ocurrido un error'})

@app.post('/developers')
async def create_developer(developer: Developer):
    try:
        db = await connection()
        await db.developers.insert_one(jsonable_encoder(developer))
        return JSONResponse(status_code=201, content={'message': "Desarrollador registrado"})
    except:
        return JSONResponse(status_code=500, content={'message': "Ha ocurrido un error"})
    
@app.put('/developers/{id}')
async def update_developer(data: Developer, id: str):
    try:
        db = await connection()
        developer = await db.developers.find_one({"_id": ObjectId(id)})
        if not developer:
            return JSONResponse(status_code=400, content={'message':'No encontrado'})
        await db.developers.update_one({'_id': ObjectId(id)}, {'$set': jsonable_encoder(data)})
        return JSONResponse(status_code=201, content={'message': "Desarrollador modificado"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': "Ha ocurrido un error"})

@app.delete('/developers/{id}')
async def delete_developer(id: str):
    try:
        db = await connection()
        developer = await db.developers.find_one({"_id": ObjectId(id)})
        if not developer:
            return JSONResponse(status_code=400, content={'message':'No encontrado'})
        await db.developers.delete_one({'_id': ObjectId(id)})
        return JSONResponse(status_code=200, content={'message': "Desarrollador eliminado"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': "Ha ocurrido un error"})
