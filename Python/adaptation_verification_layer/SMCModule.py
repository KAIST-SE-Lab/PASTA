from adaptation_verification_layer.SampleGenerator import SampleGenerator
from adaptation_verification_layer.Simulator import Simulator
from adaptation_verification_layer.Verifier import Verifier
from specification.AdaptationGoal import AdaptationGoal
from specification.AdaptationTactic import AdaptationTactic
from specification.EnvironmentPrediction import EnvironmentPrediction
from specification.SystemModel import SystemModel
from specification.VerificationResult import VerificationResult


class SMCModule:

    def __init__(self):
        self._sampler = SampleGenerator()
        self._simulator = Simulator()
        self._verifier = Verifier()

    # TODO: Specify your SMC algorithms (SMCS, SSP, SPRT, etc.)
    def verifyAdaptationTactic(self, sys: SystemModel, tactic: AdaptationTactic, prediction: EnvironmentPrediction,
                               goal: AdaptationGoal) -> VerificationResult:
        simResults = []

        while not self._isSufficient():
            # Iterate sample generation, simulation, and addition of the simulation result
            # Step 3
            sample = self._sampler.generateSample(prediction)

            # Step 4
            simResults.append(self._simulator.simulate(sys, tactic, sample))

        # Step 5
        return self._verifier.verify(simResults, goal)

    # TODO: Implement SMC algorithm's sample-sufficiency-checking method
    def _isSufficient(self) -> bool:
        return True
