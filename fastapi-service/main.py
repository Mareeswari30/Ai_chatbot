from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

app = FastAPI()

# Load model & tokenizer
model_name = "stabilityai/stablelm-2-1b-chat"  # smaller, CPU-friendly
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create a text generation pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1  # CPU only
)

# Request model
class Message(BaseModel):
    message: str

@app.post("/generate")
def generate(data: Message):
    prompt = f"User: {data.message}\nAssistant:"
    output = generator(
        prompt,
        max_length=100,          # limit reply length
        do_sample=True,          # add randomness for varied responses
        temperature=0.7,         # control creativity
        repetition_penalty=1.5,  # avoid repeated text
        num_return_sequences=1
    )
    return {"reply": output[0]["generated_text"].strip()}
