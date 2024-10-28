import csv

def load_data(filename='data.csv'):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def calculate_thresholds(data):
    # Calculate separate thresholds for each feature
    thresholds = {}
    features = [
        'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean',
        'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se',
        'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se',
        'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst',
        'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst',
        'fractal_dimension_worst'
    ]

    for feature in features:
        malignant = [float(row[feature]) for row in data if row['diagnosis'] == 'M']
        benign = [float(row[feature]) for row in data if row['diagnosis'] == 'B']
        threshold = (sum(malignant) / len(malignant) + sum(benign) / len(benign)) / 2
        thresholds[feature] = threshold
    return thresholds

def predict_cancer(user_data, thresholds):
    # Compare each feature to its threshold and tally the results
    malignant_count = 0
    benign_count = 0
    for feature, threshold in thresholds.items():
        if float(user_data[feature]) > threshold:
            malignant_count += 1
        else:
            benign_count += 1
    return 'M' if malignant_count > benign_count else 'B'
