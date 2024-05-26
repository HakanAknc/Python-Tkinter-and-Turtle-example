from fastapi import (FastAPI, Query)
from pydantic import BaseModel
import csv

app = FastAPI()

# Sporcu modeli
class Player(BaseModel):
    first_name: str
    last_name: str
    position: str

# CSV dosyasından veri okuma
def read_data_from_csv(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Takımdaki tüm sporcuları listeleme
@app.get("/players/")
def list_players():
    return read_data_from_csv("team.csv")

# Yeni bir sporcu eklemek
@app.post("/players/")
def add_player(player: Player):
    with open("team.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=
        [
            "first_name", 
            "last_name", 
            "position"
        ])
        writer.writerow(player.dict())
    return player