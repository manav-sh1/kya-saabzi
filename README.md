# 🍛 Sabzi Tracker API

A simple FastAPI-based backend application to track cooked sabzis (vegetables) and recommend what to cook next based on how long ago it was last cooked.

## 🚀 Features

- Add or update sabzis with the current cooking date
- Retrieve a list of all cooked sabzis
- Get a recommendation for what to cook next based on recency
- Delete entries by name

## 🛠️ Tech Stack

- **FastAPI** for building the API
- **SQLModel** + **PostgreSQL** for ORM and database
- **Supabase** as the cloud-hosted database
- **Render** for deployment

## 📦 Endpoints

| Method | Endpoint       | Description                        |
|--------|----------------|------------------------------------|
| GET    | `/sabzis`      | Fetch all cooked sabzis            |
| POST   | `/cook`        | Add or update a sabzi              |
| GET    | `/recommend`   | Recommend what to cook next        |
| DELETE | `/sabzis/{name}` | Delete a sabzi by its name         |

## 📄 Example Request

```json
POST /cook
{
  "name": "Aloo Gobi"
}
