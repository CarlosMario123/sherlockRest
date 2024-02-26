from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sherlock import searchUser

app = FastAPI()

@app.post("/search")
async def handle_post_request(data: dict):
    # Verificar si se proporcionó el nombre en los datos recibidos
    if data and 'name' in data:
        nombre = data['name']
        resultado = await searchUser(nombre)
        response = {'resultados': resultado}
        return JSONResponse(content=response)
    else:
        raise HTTPException(status_code=400, detail="No se proporcionó un nombre válido en la solicitud")

if __name__ == "__main__":
    import uvicorn#para trabajar con asyncronia
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=1200)
