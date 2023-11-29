import fastapi
import uvicorn
import asyncio

app = fastapi.FastAPI()


@app.get("/exploit/{target}")
async def read_target(target: int):
    await asyncio.sleep(1)
    return "Exploited " + str(target) + " successfully!"

def main():
    uvicorn.run(app, host='0.0.0.0', port=9000)

if __name__ == '__main__':
    main()