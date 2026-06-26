import numpy as np
from core.grid import Grid

class Layer: 
    def __init__(self, name: str, grid: Grid, dtype=float): 
        self.name = name 
        self.grid = grid 
        self.data= np.zeros(grid.shape, dtype=dtype)

    def get(self, x: int, y: int): 
        return self.data[y,x]
    
    def set(self, x: int, y: int, value: float): 
        self.data[y,x] = value

    def __repr__(self): 
        return f"Layer(name={self.name}, shape={self.shape})"

    def __str__(self):
        return f"Name: {self.name!r}, size: {self.grid.width} x {self.grid.height}\n" 