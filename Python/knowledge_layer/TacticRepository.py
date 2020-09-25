from typing import List

from specification.AdaptationTactic import AdaptationTactic


class TacticRepository:

    def __init__(self, adaptationTactics: List[AdaptationTactic]):
        self._tactics = adaptationTactics

    def getPossibleTactics(self) -> List[AdaptationTactic]:
        return self._tactics

    def addTactic(self, adaptationTactic: AdaptationTactic):
        self._tactics.append(adaptationTactic)
