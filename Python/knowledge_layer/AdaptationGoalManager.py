from specification.AdaptationGoal import AdaptationGoal


class AdaptationGoalManager:

    def __init__(self, adaptationGoal: AdaptationGoal):
        self._goal = adaptationGoal

    def getGoal(self) -> AdaptationGoal:
        return self._goal

    def setGoal(self, newGoal: AdaptationGoal):
        self._goal = newGoal
