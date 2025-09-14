Customer Churn Prediction (Django + Machine Learning)

This project is an end-to-end churn prediction system that combines Machine Learning with a Django backend API.
The ML model predicts whether a telecom customer is likely to churn (leave the service) based on historical data.

It demonstrates real-world AI integration into web applications.

📂 Project Structure
├── __pycache__/                  # Python cache files
├── churn_app/                    # Django app (API for churn prediction)
├── churn_project/                # Django project (settings & config)
├── churn_model.pkl               # Trained ML model (saved with joblib)
├── colab_requirements.txt        # Dependencies used in Google Colab training
├── compare_requirements.py       # Script to compare Colab vs Django requirements
├── db.sqlite3                    # Django default database
├── django_requirements.txt       # Dependencies for running Django server
├── e.html                        # Example frontend HTML page
├── manage.py                     # Django project entry point
├── ml_utils.py                   # ML utilities (load model, preprocess, predict)
├── train.ipynb                   # Jupyter notebook for model training
└── README.md                     # Project documentation

📊 Dataset

This project uses the Telco Customer Churn Dataset:

🔗 Kaggle - Telco Customer Churn

The dataset includes:

Customer demographics (gender, senior citizen, partner, dependents)

Account information (tenure, contract type, payment method, monthly & total charges)

Services signed up (phone service, internet service, streaming services, etc.)

Target variable: Churn (Yes / No)

🚀 Installation & Setup
1️⃣ Clone this repo
git clone https://github.com/VishnuA02/churn_prediction.git
cd churn_prediction

2️⃣ Install dependencies
pip install -r django_requirements.txt

3️⃣ Run database migrations
python manage.py migrate

4️⃣ Start the Django server
python manage.py runserver

5️⃣ Open in browser
http://127.0.0.1:8000/

📡 API Usage
Endpoint
POST http://127.0.0.1:8000/predict/

Example Request (JSON)
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 5,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 80.5,
  "TotalCharges": 400.0
}

Example Response
{
  "churn": "Yes",
  "churn_probability": 0.87
}

🛠 Tech Stack

Python (3.x)

Django (REST API)

scikit-learn, XGBoost, RandomForest, LogisticRegression (Stacking Ensemble)

Joblib (for model serialization)

SQLite (default Django database)

Google Colab / Jupyter Notebook (model training)

📌 Notes

train.ipynb contains model training + feature engineering.

ml_utils.py handles model loading & preprocessing inside Django.

You can replace churn_model.pkl with a retrained model if needed.
