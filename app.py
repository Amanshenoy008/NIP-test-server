from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
import uuid

app = FastAPI(title="NewsinPixels API", version="0.1")

# iOS app doesn't need CORS, but keeping it open helps when you test in a browser.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def item(topic: str, title: str, subtitle: str, system_image: str, image_url: str) -> Dict:
    return {
        "id": str(uuid.uuid4()),
        "topic": topic,
        "title": title,
        "subtitle": subtitle,
        "systemImage": system_image,
        "imageURL": image_url,
    }

# ✅ Replace these with your real meme images + headlines later.
TECH = [
    item("Tech", "Apple teases new AI features", "Here’s what’s rumored and what’s real.", "cpu", "https://picsum.photos/seed/tech1/1200/800"),
    item("Tech", "Open-source devs ship faster", "Tooling is getting wild in 2026.", "hammer", "https://picsum.photos/seed/tech2/1200/800"),
]
SPORTS = [
    item("Sports", "Underdog wins the final", "A comeback nobody expected.", "sportscourt", "https://picsum.photos/seed/sports1/1200/800"),
]
ENT = [
    item("Entertainment", "Streaming wars continue", "New shows, higher prices, more drama.", "film", "https://picsum.photos/seed/ent1/1200/800"),
]
FINANCE = [
    item("Finance", "Markets swing on new data", "Volatility returns this week.", "chart.line.uptrend.xyaxis", "https://picsum.photos/seed/fin1/1200/800"),
]
WORLD = [
    item("World", "Global summit highlights", "Key takeaways in 30 seconds.", "globe.asia.australia", "https://picsum.photos/seed/world1/1200/800"),
]
GAMING = [
    item("Gaming", "New game breaks records", "Players love it, speedrunners destroy it.", "gamecontroller", "https://picsum.photos/seed/gaming1/1200/800"),
]

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/api/tech")
def tech() -> List[Dict]:
    return TECH

@app.get("/api/sports")
def sports() -> List[Dict]:
    return SPORTS

@app.get("/api/entertainment")
def entertainment() -> List[Dict]:
    return ENT

@app.get("/api/finance")
def finance() -> List[Dict]:
    return FINANCE

@app.get("/api/world")
def world() -> List[Dict]:
    return WORLD

@app.get("/api/gaming")
def gaming() -> List[Dict]:
    return GAMING

@app.get("/api/feed")
def feed() -> List[Dict]:
    # Your “Your Feed” can be a mix
    return TECH + SPORTS + ENT + FINANCE + WORLD + GAMING
