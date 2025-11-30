from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

app = FastAPI()

# Load Google FLAN-T5 model
model_name = "google/flan-t5-base"   # You can use small/base/large/xl

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Use text2text-generation pipeline
generator = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1  # CPU
)

class Message(BaseModel):
    message: str

@app.post("/generate")
def generate(data: Message):
    prompt = f"User question: {data.message}"

    output = generator(
        prompt,
        max_length=150,
        temperature=0.7,
        repetition_penalty=1.2,
    )

    reply = output[0]["generated_text"]
    return {"reply": reply.strip()}

