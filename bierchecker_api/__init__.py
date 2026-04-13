from fastapi import FastAPI


app = FastAPI()


@app.get("/health", status_code=204)
async def health_check() -> None:
    return


@app.get("/ada")
async def isadacool() -> dict:
    return {"is_ada_cool": True}
