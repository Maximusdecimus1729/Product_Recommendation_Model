---
title: Product Recommendation
emoji: 🎯
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

# 🎯 Product Recommendation App

A Flask web application that serves real-time product recommendations using a trained **SVD (Singular Value Decomposition)** collaborative filtering model built with `scikit-surprise`.

---

## 📁 Project Structure

```
App/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container image definition
├── docker-compose.yml      # Multi-container orchestration
├── model/
│   └── svd_model.pkl       # Pre-trained SVD model
└── templates/
    ├── index.html          # Input form
    └── result.html         # Prediction result page
```

---

## ⚙️ Requirements

- Python 3.10+
- Docker & Docker Compose

---

## 🚀 Getting Started

### Option 1 — Run with Docker (recommended)

```bash
docker-compose up --build
```

Then open your browser at [http://localhost:5000](http://localhost:5000).

To stop the app:

```bash
docker-compose down
```

### Option 2 — Run locally

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the app
flask run --host=0.0.0.0 --port=5000
```

---

## 🔌 API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Renders the recommendation form |
| `POST` | `/recommend` | Returns a predicted rating for a user/product pair |

### POST `/recommend` — Form Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `user_id` | integer | User ID (1 – 1000) |
| `product_id` | integer | Product ID (1 – 500) |

---

## 🧠 Model

The SVD model was trained on a synthetic user–product interaction dataset (5,000 interactions, 1,000 users, 500 products) using `scikit-surprise`. The serialized model is loaded from `model/svd_model.pkl` at startup.

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `Flask` | Web framework |
| `scikit-surprise` | SVD recommendation model |
| `numpy` | Numerical operations |

---

## 🐳 Docker Notes

- The image is based on `python:3.10-slim`.
- Build dependencies (`gcc`, `build-essential`) are installed to compile `scikit-surprise` and then cleaned up to keep the image lean.
- The app listens on port **5000** inside the container, mapped to port **5000** on the host.
