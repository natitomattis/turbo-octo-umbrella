"""
This module contains a class that conforms to the Seldon core interface
for ML model.
"""

from sklearn.externals import joblib
from typing import Iterable


class MLTitanic:
    """
    Model template. You can load your model parameters in __init__ from
    a location accessible at runtime
    """

    def __init__(self):
        """
        Add any initialization parameters. These will be passed at
        runtime from the graph definition parameters defined in your
        seldondeployment kubernetes resource manifest.
        """
        self.clf = joblib.load('sk.pkl') 
        print("Initializing")

    def predict(self, X, features_names):
        """
        Return a prediction.

        Parameters
        ----------
        X : array-like
        feature_names : array of feature names (optional)
        """
        print("Predict called - will run identity function")
        predictions = self.clf.predict(X)
        return predictions
        
    def send_feedback(self,features,feature_names,reward,truth):
        print("Send feedback called")
        return []

    def metrics(self):
        return [
            {"type":"COUNTER","key":"mycounter","value":1}, # a counter which will increase by the given value
            {"type":"GAUGE","key":"mygauge","value":100}, # a gauge which will be set to given value
            {"type":"TIMER","key":"mytimer","value":20.2}, # a timer which will add sum and count metrics - assumed millisecs
        ]

