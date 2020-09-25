from specification.SystemModel import SystemModel


class SystemModelManager:

    def __init__(self, sys: SystemModel):
        self.sysModel = sys

    def updateModel(self):
        # TODO: Specify how to update model
        pass

    def getSysModel(self) -> SystemModel:
        return self.sysModel
