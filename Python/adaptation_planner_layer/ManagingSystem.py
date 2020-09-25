from typing import Dict

from adaptation_verification_layer.SMCModule import SMCModule
from data_analysis_layer.ForecastingEngine import ForecastingEngine
from interaction_layer.Actuators import Actuators
from interaction_layer.Sensors import Sensors
from knowledge_layer.AdaptationGoalManager import AdaptationGoalManager
from knowledge_layer.EnvironmentDatabase import EnvironmentDatabase
from knowledge_layer.SystemModelManager import SystemModelManager
from knowledge_layer.TacticRepository import TacticRepository
from specification.AdaptationGoal import AdaptationGoal
from specification.AdaptationTactic import AdaptationTactic
from specification.SystemModel import SystemModel
from specification.VerificationResult import VerificationResult


class ManagingSystem:

    # TODO: Initialize your SAS
    def __init__(self):
        # Knowledge
        self._envDB = EnvironmentDatabase()
        SASmodel = SystemModel()
        self._sysModelManager = SystemModelManager(SASmodel)
        tactics = []
        self._tacticRepo = TacticRepository(tactics)
        goal = AdaptationGoal()
        self._goalManager = AdaptationGoalManager(goal)

        # Data Analysis Layer
        self._forecaster = ForecastingEngine()

        # Interaction Layer
        self._sensors = Sensors()
        self._actuators = Actuators()

        # Adaptation Verification Layer
        self._SMC = SMCModule()

    def adaptManagedSystem(self):
        # Step 1
        monitoredData = self._sensors.monitor()
        self._envDB.addEnvironmentData(monitoredData)
        self._sysModelManager.updateModel()

        # Step 2
        prediction = self._forecaster.forecast(self._envDB.getHistoricalEnvironmentData())

        # Step 3, 4, and 5 - work as "Optimal adaptation tactic searching module"
        evaluations = {}
        sys = self._sysModelManager.getSysModel()
        goal = self._goalManager.getGoal()
        for tactic in self._tacticRepo.getPossibleTactics():
            evaluations[tactic] = self._SMC.verifyAdaptationTactic(sys, tactic, prediction, goal)

        # Step 6
        selectedTactic = self._getOptimalTactic(evaluations)

        # Step 7
        self._actuators.execute(selectedTactic)

    # TODO: Implement how to find optimal tactic
    def _getOptimalTactic(self, evaluations: Dict[AdaptationTactic, VerificationResult]) -> AdaptationTactic:
        optimalTactic = None
        # Find optimal one among evaluation sheets

        return optimalTactic
