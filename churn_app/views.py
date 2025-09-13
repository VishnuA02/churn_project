# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import sys
import os
import joblib

# ✅ Step 1: Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ✅ Step 2: Import your custom feature engineering method (optional if used externally)
# from ml_utils import add_features  # Optional only if pipeline uses it internally

# ✅ Step 3: Load the trained model pipeline (with internal feature engineering)
try:
    pipeline = joblib.load('churn_model.pkl')
except Exception as e:
    pipeline = None
    load_error = str(e)


@api_view(["GET", "POST"])
def predict_churn(request):
    if pipeline is None:
        return Response({"error": f"Model loading failed: {load_error}"}, status=500)

    if request.method == "GET":
        return Response({"message": "Submit customer data using POST request."})

    elif request.method == "POST":
        try:
            data = request.data
            customer_id = data.get("customerID", "Unknown")

            df = pd.DataFrame([data])

            # Drop customerID if present
            if 'customerID' in df.columns:
                df = df.drop(columns=['customerID'])

            # ✅ Pass to pipeline (with internal feature engineering)
            proba = pipeline.predict_proba(df)[0][1]
            churn = "Yes" if proba >= 0.5 else "No"

            return Response({
                "customerID": customer_id,
                "predicted_churn": churn,
                "churn_probability": round(proba, 2)
            })

        except Exception as e:
            return Response({"error": str(e)}, status=400)

