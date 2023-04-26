class Action:
    """
    simply represents the actions to be taken by objects of the Player type
    """
    def __init__(self, rotate: int = 0, forward: int = 0, spin: int = 0) -> None:
        self.rotate = rotate
        self.forward = forward
        self.spin = spin
