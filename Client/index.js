const WebSocket = require('ws');
const express = require('express');

const app = express();
app.use(express.json());


async function incrementVerification(userId) {
    const query = `
      UPDATE fraud_detection 
      SET num_verifications = num_verifications + 1 
      WHERE user_id = $1 
      RETURNING *;  -- Return updated row
    `;

    try {
        const res = await client.query(query, [userId]);
        return res.rows[0]; // Return updated fraud data for that user
    } catch (err) {
        console.error("Error updating verification count:", err);
        return null;
    }
}



// Connect to FastAPI WebSocket server
const ws = new WebSocket('wss://fraud-detection-sc7s.onrender.com/ws');

// When WebSocket opens, send test fraud detection request
ws.on('open', async function open() {
    console.log("Connected to FastAPI WebSocket");

    const testData = {
        features: [40, 8, 2, 3, 4]  // Example fraud detection input
    };

    const updatedFraudData = await incrementVerification(userId);

    if (updatedFraudData) {
        ws.send(JSON.stringify({ features: Object.values(updatedFraudData) }));
    }

    ws.send(JSON.stringify(testData));  // Send data to FastAPI
});

// Receive prediction response from FastAPI
ws.on('message', function incoming(data) {
    console.log("Received response from FastAPI:", data.toString());
    let info = data.toString().prediction;
    console.log(info);
});

ws.on("error", (error) => {
    console.error("❌ WebSocket error:", error);
});

// Handle WebSocket close event
ws.on('close', function close() {
    console.log("Disconnected from FastAPI WebSocket");
});


app.listen(5000, () => {
    console.log("Server is running! Finally!!!")
})