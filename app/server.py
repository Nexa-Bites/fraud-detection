from fastapi import FastAPI, WebSocket
from app.fraud_detection import fraud_detector  # Import model from ml_model.py

app = FastAPI()

#Data for the ML model to predict on
# num_verifications (integer, 1 to 50)
# num_failed_verifications (integer, 0 to 10)
# num_revocations (integer, 0 to 5)
# num_dids (integer, 1 to 3)
# key_rotations (integer, 0 to 5)



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")
    
    await websocket.accept()
    await websocket.send_json({"message": "WebSocket connected!"})
    await websocket.close()

    while True:
        try:
            data = await websocket.receive_json()  # Receive data from Node.js
            prediction = fraud_detector.predict(data["features"])  # Use ML model
            await websocket.send_json({"prediction": prediction})  # Send prediction
        except Exception as e:
            print(f"Error: {e}")
            break
        
    print("Client disconnected")


@app.get("/")
def home():
    return {"message": "FastAPI is running!"}


#This FastAPI app will expose REST API endpoints (e.g., POST /predict) that your Node.js backend can call using HTTP requests.
# config.py
# tests