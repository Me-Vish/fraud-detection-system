# Fraud Detection System using Flask & Machine Learning

A full-stack Fraud Detection web application built using Python, Flask, and Machine Learning.  
The system predicts whether a transaction is **Normal** or **Fraudulent** and provides a simple web interface for real-time testing.

This project was developed as part of hands-on learning in Machine Learning and backend web development.

---

##  Live Demo

https://fraud-detection-system-y9gg.onrender.com

(Note: First load may take a few seconds since Render free services sleep when inactive.)

---

##  Features

- Real-time fraud prediction
- Machine Learning based classification
- Flask backend API
- Web UI for transaction input
- Transaction history logging
- REST API testing support
- Modular project structure

---

##  Technologies Used

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- NumPy  
- HTML / CSS  
- Joblib  

---

##  Project Structure

fraud_detection/  
│  
├── app.py              # Flask application  
├── model.py           # ML model logic  
├── test_api.py        # API testing script  
├── requirements.txt   # Python dependencies  
├── history.csv        # Prediction history  
│  
├── static/  
│   └── bg.jpg         # UI background image  
│  
└── README.md  

---

## How to Run Locally

### 1️ Clone Repository

git clone https://github.com/Me-Vish/fraud-detection-system.git  
cd fraud-detection-system  

---

### 2️ Install Dependencies

pip install -r requirements.txt  

---

### 3️ Run Flask App

python app.py  

---

### 4️ Open in Browser

http://127.0.0.1:5000  

---

##  Machine Learning Workflow

1. Transaction data preprocessing  
2. Feature extraction  
3. Model training  
4. Saving trained model  
5. Flask loads model for prediction  
6. Real-time input → Prediction output  

---

##  Important Note

Large datasets and trained model files are excluded from GitHub due to size limits.  
They are handled locally using `.gitignore`.

---

##  Learning Outcomes

- Flask API development  
- ML model integration with backend  
- Git & GitHub version control  
- Handling large datasets properly  
- End-to-end project deployment using Render  

---
## Author
Vishali M  

Artificial Intelligence & Data Science  
Web Development | Machine Learning | UI/UX  

---
⭐ This project was created for academic learning and internship preparation.
