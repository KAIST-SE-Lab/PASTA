from specification.AdaptationTactic import AdaptationTactic
from specification.EnvironmentData import EnvironmentData
from specification.SimulationResult import SimulationResult
from specification.SystemModel import SystemModel


class Simulator:

    # TODO: Specify your simulator
    def __init__(self):
        pass

    # TODO: Specify your simulation engine
    def simulate(self, sys: SystemModel, tactic: AdaptationTactic, env: EnvironmentData) -> SimulationResult:
        simResult = SimulationResult()
        return simResult
