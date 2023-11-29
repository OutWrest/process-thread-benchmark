import fastapi
import uvicorn

app = fastapi.FastAPI()

targets_index = 0

@app.get("/target")
async def read_target():
    global targets_index
    targets_index += 1
    if targets_index > 500:
        targets_index = -1
    return targets_index

def main():
    uvicorn.run(app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()