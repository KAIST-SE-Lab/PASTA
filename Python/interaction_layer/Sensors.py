from typing import List

from interaction_layer.Sensor import Sensor
from specification.EnvironmentData import EnvironmentData


class Sensors:

    # TODO: Specify your sensors
    def __init__(self):
        self._sensors: List[Sensor] = []
        pass

    # TODO: Monitor environment
    def monitor(self) -> EnvironmentData:
        monitoredData = EnvironmentData()
        return monitoredData
