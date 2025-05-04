import sys

from pandas import DataFrame
from sklearn.pipeline import Pipeline

from customer_churn_prediction.exception import CustomerChurnException
from customer_churn_prediction.logger import logging

class TargetValueMapping:
    def __init__(self):
        self.No:int = 0
        self.Yes:int = 1
    def _asdict(self):
        return self.__dict__
    def reverse_mapping(self):
        mapping_response = self._asdict()
        return dict(zip(mapping_response.values(),mapping_response.keys()))