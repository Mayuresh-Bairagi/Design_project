# 🍌 Banana Crop Yield Prediction & Recommendation System

A deep learning-powered system that predicts banana crop count and quality, recommends farming decisions, and aims to forecast real-time crop pricing — all wrapped into a FastAPI backend for integration.

---

## 🎯 Project Objective

This project is focused on building an end-to-end solution for **banana crop yield prediction** by:

- Counting the number of bananas using **YOLO object detection**
- Assessing banana quality using a **MobileNet CNN (pretrained)**
- Providing intelligent crop recommendations using a **Groq model**
- (Upcoming) Predicting approximate market price using **web scraping** and **real-time price analysis**

---

## 🔍 Key Features

- 🍌 **Banana Counting with YOLO** – Detects and counts bananas in real-world images  
- ✅ **Banana Quality Classification** – Uses a MobileNet-based CNN to classify quality levels  
- 📈 **Crop Recommendation Engine** – Leverages Groq’s high-speed model inference  
- 🌐 **Real-Time Price Forecasting (Upcoming)** – Uses web scraping to suggest market price for harvested crops  
- ⚡ **FastAPI Backend** – Provides APIs to integrate model predictions with frontend or dashboards  

---

## 🧠 Tech Stack

| Layer             | Tech Used                  |
|------------------|----------------------------|
| Detection        | YOLO (You Only Look Once)  |
| Quality Analysis | MobileNet CNN              |
| Recommendation   | Groq Model                 |
| Backend          | FastAPI                    |
| Upcoming         | Web Scraping (BeautifulSoup / Selenium), Price Prediction Model |

---

## 📁 Project Structure (Example)

```
Design_project/
├── yolo_model/            # YOLO model for banana counting
├── quality_model/         # MobileNet-based quality classification
├── groq_model/            # Groq model for recommendations
├── app/                   # FastAPI backend logic
│   ├── main.py
│   └── routes/
├── utils/                 # Preprocessing, postprocessing scripts
├── data/                  # Sample images and datasets
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/Mayuresh-Bairagi/Design_project.git
   cd Design_project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run FastAPI backend**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 📊 Future Plans

- ✅ Real-time banana price prediction  
- ✅ Web scraping from agri-market sites  
- ✅ Integration with user dashboard / frontend  
- ✅ Model optimization for deployment on edge devices  

---

