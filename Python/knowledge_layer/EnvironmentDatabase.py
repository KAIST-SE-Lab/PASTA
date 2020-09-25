from typing import List

from specification.EnvironmentData import EnvironmentData


class EnvironmentDatabase:

    def __init__(self):
        self._historicalData: List[EnvironmentData] = []

    def addEnvironmentData(self, envData: EnvironmentData):
        self._historicalData.append(envData)

    def getHistoricalEnvironmentData(self) -> List[EnvironmentData]:
        return self._historicalData
