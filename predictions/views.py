from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Prediction

@api_view(['POST'])
def save_prediction(request):
    # Extract data from the request
    data = {
        'radius_mean': request.data.get('radius_mean'),
        'texture_mean': request.data.get('texture_mean'),
        'perimeter_mean': request.data.get('perimeter_mean'),
        'area_mean': request.data.get('area_mean'),
        'smoothness_mean': request.data.get('smoothness_mean'),
        'compactness_mean': request.data.get('compactness_mean'),
        'concavity_mean': request.data.get('concavity_mean'),
        'concave_points_mean': request.data.get('concave_points_mean'),
        'symmetry_mean': request.data.get('symmetry_mean'),
        'fractal_dimension_mean': request.data.get('fractal_dimension_mean'),
        'radius_se': request.data.get('radius_se'),
        'texture_se': request.data.get('texture_se'),
        'perimeter_se': request.data.get('perimeter_se'),
        'area_se': request.data.get('area_se'),
        'smoothness_se': request.data.get('smoothness_se'),
        'compactness_se': request.data.get('compactness_se'),
        'concavity_se': request.data.get('concavity_se'),
        'concave_points_se': request.data.get('concave_points_se'),
        'symmetry_se': request.data.get('symmetry_se'),
        'fractal_dimension_se': request.data.get('fractal_dimension_se'),
        'radius_worst': request.data.get('radius_worst'),
        'texture_worst': request.data.get('texture_worst'),
        'perimeter_worst': request.data.get('perimeter_worst'),
        'area_worst': request.data.get('area_worst'),
        'smoothness_worst': request.data.get('smoothness_worst'),
        'compactness_worst': request.data.get('compactness_worst'),
        'concavity_worst': request.data.get('concavity_worst'),
        'concave_points_worst': request.data.get('concave_points_worst'),
        'symmetry_worst': request.data.get('symmetry_worst'),
        'fractal_dimension_worst': request.data.get('fractal_dimension_worst'),
        'prediction_result': request.data.get('prediction_result'),
    }

    # Create the Prediction object
    prediction = Prediction.objects.create(**data)

    return Response({"message": "Prediction saved successfully", "id": prediction.id}, status=status.HTTP_201_CREATED)
