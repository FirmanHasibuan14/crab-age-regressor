import joblib
import pandas as pd
from schemas.predict import PredictionRequest

class MLServices:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)

        self.sex_mapping = {'F': 0, 'I': 1, 'M': 2}

        self.features = [
            'Sex', 'Length', 'Diameter', 'Height', 'Weight',
            'Shucked Weight', 'Viscera Weight', 'Shell Weight'
        ]

    def _preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        df_copy = df.copy()

        df_copy['Sex'] = df_copy['Sex'].map(self.sex_mapping)

        return df_copy
    
    def predict(self, request_data: PredictionRequest):
        input_dict = {
            'Sex': request_data.sex,
            'Length': request_data.length,
            'Diameter': request_data.diameter,
            'Height': request_data.height,
            'Weight': request_data.weight,
            'Shucked Weight': request_data.shucked_weight,
            'Viscera Weight': request_data.viscera_weight,
            'Shell Weight': request_data.shell_weight
        }

        df = pd.DataFrame([input_dict])

        processed_data = self._preprocess(df)

        prediction = processed_data[self.features]

        predicted_age = self.model.predict(prediction)[0]

        return {"age": int(round(predicted_age))}

ml_service = MLServices(model_path="../ML/Model/xgb_regressor_model.pkl")