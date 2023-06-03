class OutOfAmmoException(Exception):
    """Exception raised when the drone is out of ammo."""

    def __init__(self, message="Out of ammo. Reload!"):
        self.message = message
        super().__init__(self.message)

