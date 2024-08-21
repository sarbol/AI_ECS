import pickle

def get_optimal_settings(env_data):
    # Load the trained model
    with open('src/ai/models/model_v1.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    
    # Example: Predict optimal settings based on input data
    input_features = [
        env_data.temperature,
        env_data.humidity,
        env_data.air_quality
    ]
    predicted_settings = model.predict([input_features])
    
    return {
        "temperature": predicted_settings[0],
        "lighting": predicted_settings[1]
    }
