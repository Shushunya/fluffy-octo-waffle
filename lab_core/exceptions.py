# TODO: add promotion error

class PromotionError(Exception):
    """Exception raised for custom error scenarios."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
