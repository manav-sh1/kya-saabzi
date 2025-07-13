from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import json
from app import recommend_sabzi
from sqlmodel import Session, select

app = FastAPI()
DATA_FILE = 'data.json'

class Sabzi(BaseModel):
    name: str 

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    
def save_data(sabzi_list):
    with open(DATA_FILE, 'w') as f:
        json.dump(sabzi_list, f, indent = 4)

@app.get('/')
def home():
    sabzi_list = load_data()
    recommend_name, days_ago = recommend_sabzi(sabzi_list)
    return {
        "recommendation": recommend_name,
        "days_since_last_cooked": days_ago
    }

@app.post('/cook')
def cook(sabzi: Sabzi):
    sabzi_list = load_data()
    today = datetime.today().strftime('%Y-%m-%d')

    # Update if exists
    for s in sabzi_list:
        if s['name'].lower() == sabzi.name.lower():
            s['date_cooked'] == today
            save_data(sabzi_list)
            return {'message': f"Updated {sabzi.name}"}
        
    # Add a new one
    sabzi_list.append({'name': sabzi.name, 'date_cooked': today})
    save_data(sabzi_list)
    return {'message': f'Added {sabzi.name}'}

@app.get('/sabzis')
def get_sabzi():
    return load_data()