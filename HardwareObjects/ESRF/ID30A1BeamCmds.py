from . import ID30BeamCmds


class ID30A1BeamCmds(ID30BeamCmds.ID30BeamCmds):
    def __init__(self, *args):
        ID30BeamCmds.ID30BeamCmds.__init__(self, *args)

    def init(self):
        controller = self.getObjectByRole("controller")
        self.centrebeam = ID30BeamCmds.ControllerCommand(
            "Centre beam", controller.centrebeam
        )

    def getCommands(self):
        return [self.centrebeam]
