class RedundantAmmoReloadException(Exception):
    """Exception raised when reloading a drone with full ammo."""

    def __init__(self, message="Redundant ammo reload detected. The drone already has full ammo."):
        self.message = message
        super().__init__(self.message)
