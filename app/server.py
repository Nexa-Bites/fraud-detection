from fastapi import FastAPI, WebSocket
from app.fraud_detection import fraud_detector  # Import model from ml_model.py
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#Data for the ML model to predict on
# num_verifications (integer, 1 to 50)
# num_failed_verifications (integer, 0 to 10)
# num_revocations (integer, 0 to 5)
# num_dids (integer, 1 to 3)
# key_rotations (integer, 0 to 5)



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()
    print("Client connected!")
    await websocket.send_json({"message": "WebSocket connected!"})

    while True:
        try:
            data = await websocket.receive_json()  # Receive data from Node.js
            print(f"📩 Received data: {data}")
            
            if "features" not in data:
                await websocket.send_json({"error": "Missing 'features' key in data"})
                continue
            
            prediction = fraud_detector.predict(data["features"])  # Use ML model
            await websocket.send_json({"prediction": prediction})  # Send prediction
            await websocket.send_json(prediction)
            print(f"📤 Sent response: {prediction}")
        except Exception as e:
            print(f"Websocket error: {e}")
            break
        
    print("Client disconnected")


@app.get("/")
def home():
    return {"message": "FastAPI is running!"}


#This FastAPI app will expose REST API endpoints (e.g., POST /predict) that your Node.js backend can call using HTTP requests.
# config.py
# tests