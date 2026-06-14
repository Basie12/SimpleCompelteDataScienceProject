import joblib
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self):                                              # was __nit__
        self.model = joblib.load(Path("artifact/model_trainer/model.joblib"))   # was model.jobib

    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction