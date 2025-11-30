const express = require("express");
const axios = require("axios");
const app = express();
app.use(express.json());

app.post("/chat", async (req, res) => {
  const { message } = req.body;
  try {
    const response = await axios.post("http://127.0.0.1:8001/generate", { message });
    res.json({ reply: response.data.reply });
  } catch (err) {
    console.error(err);
    res.status(500).json({ reply: "Error calling AI service" });
  }
});

app.listen(3001, () => console.log("Node API running on port 3001"));

