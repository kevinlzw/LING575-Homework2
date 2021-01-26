from DialogActTypes import DialogActTypes


class DialogAct:

    def __init__(self, dialogActType, semantic_frame=None):
        self.DialogActType = dialogActType
        self.semantic_frame = semantic_frame
        self.semantic_intent = self.semantic_frame.Intent if self.semantic_frame else None