from typing import List

from interaction_layer.Actuator import Actuator
from specification.AdaptationTactic import AdaptationTactic


class Actuators:

    # TODO: Specify your actuators
    def __init__(self):
        self._actuators: List[Actuator] = []
        pass

    # TODO: How to execute adaptation
    def execute(self, tactic: AdaptationTactic):
        pass
