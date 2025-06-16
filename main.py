
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Allow requests from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Sentiment API is live!"}

@app.get("/sentiment")
def get_sentiment():
    try:
        df = pd.read_csv("enriched_sentiment.csv")
        df["publishedAt"] = pd.to_datetime(df["publishedAt"]).astype(str)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
