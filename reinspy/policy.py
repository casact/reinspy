class Policy:
    def __init__(
            self,
            aoi: float,
            premium: float
    ):

        self.aoi = aoi
        self.premium = premium
        self.losses: list = []
