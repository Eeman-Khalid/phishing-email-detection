# 📧 Phishing Email Detection using Machine Learning

This project is a **machine learning-based phishing email detection system** built using Python and scikit-learn.  
It classifies emails as:

- **0 → Legitimate Email**
- **1 → Phishing Email**

The model is trained using the Kaggle dataset:
https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset

---

## 📂 Project Structure
# 📧 Phishing Email Detection using Machine Learning

This project is a **machine learning-based phishing email detection system** built using Python and scikit-learn.  
It classifies emails as:

- **0 → Legitimate Email**
- **1 → Phishing Email**

The model is trained using the Kaggle dataset:
https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset

---

## 📂 Project Structure
phishing-email-detection/
│
├── data/ # Dataset (CSV file)
├── models/ # Saved model and vectorizer
├── src/
│ ├── preprocess.py
│ ├── train.py
│ ├── predict.py
│
├── main.py
├── requirements.txt
└── README.md

---

## 🚀 Features

- Text preprocessing using **NLTK**
- TF-IDF vectorization
- Logistic Regression classifier
- Model saving using **joblib**
- Easy prediction system

---

## 📊 Dataset

The dataset contains two main columns:

- `text_combined` → Email text
- `label` → Target variable (0 or 1)

Source:
Kaggle Phishing Email Dataset

---

## 🛠 Technologies Used

- Python 3.10
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Joblib
- Matplotlib
- Seaborn

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/phishing-email-detection.git
cd phishing-email-detection
Install dependencies:

pip install -r requirements.txt

Download NLTK data:

import nltk
nltk.download('punkt')
nltk.download('stopwords')
🏃 How to Run
1️⃣ Train the Model
python src/train.py

This will:

Train the model

Evaluate performance

Save:

models/model.pkl

models/vectorizer.pkl

2️⃣ Run Prediction
python main.py
🧠 Model Details

Algorithm: Logistic Regression

Features: TF-IDF (1-2 grams)

Evaluation: Classification Report

🎯 Example Prediction

Input:

Congratulations! You won a free iPhone. Click the link now.

Output:

Prediction: Phishing Email