from core.grid import Grid
from core.layer import Layer 

class Planet: 
    def __init__(self, name: str, grid: Grid, radius_km: int, rotation_hours: int, axial_tilt_deg:float, gravity:float):
        self.name = name
        self.grid = grid 
        self.radius_km = radius_km 
        self.rotation_hours = rotation_hours
        self.axial_tilt_deg = axial_tilt_deg
        self.gravity = gravity 
        self.height = Layer("Height", grid)
        self.temperature = Layer("Temperature", grid)

    