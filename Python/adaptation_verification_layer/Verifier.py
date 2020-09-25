from typing import List

from specification.AdaptationGoal import AdaptationGoal
from specification.SimulationResult import SimulationResult
from specification.VerificationResult import VerificationResult


class Verifier:

    # TODO: Specify your goal checker
    def __init__(self):
        pass

    def verify(self, simResults: List[SimulationResult], goal: AdaptationGoal) -> VerificationResult:
        veriResult = VerificationResult()
        return veriResult
