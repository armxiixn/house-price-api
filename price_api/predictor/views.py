from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import joblib
import numpy as np


model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

print("✅ Model and Scaler loaded successfully!")
print(model)



@api_view(['POST'])
def predict_price(request):
    try:
        data = request.data

       
        Area = float(data['Area'])
        Room = int(data['Room'])
        Parking = int(data['Parking'])
        Warehouse = int(data['Warehouse'])
        Elevator = int(data['Elevator'])
        Region_mean_price = float(data['Region_mean_price'])
        majmooe_emkanat = int(data['majmooe_emkanat'])
        # nesbat_otagh_be_area=float(data['nesbat_otagh_be_area'])

       
        Area_log = np.log1p(Area)
        X = np.array([[Area_log, Room, Parking, Warehouse, Elevator,Region_mean_price,majmooe_emkanat]])
        X_scaled = scaler.transform(X)

        
        y_pred = model.predict(X_scaled)
        y_pred_real = np.expm1(y_pred)

        return Response({'predicted_price': round(float(y_pred_real[0]), 2)})

    except Exception as e:
        return Response({'error': str(e)})




from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

@api_view(['GET'])
def get_region_prices(request):
    try:
        with open('region_map.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return Response(data)
    except Exception as e:
        return Response({'error': str(e)})


