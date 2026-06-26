import numpy as np

class Grid: 
    def __init__(self, width: int, height: int): 
        self.width = width 
        self.height = height 
        self.shape = (height, width)
    
    def contains(self, x:int, y: int) -> bool: 
        return (
            0 <= x < self.width
            and 
            0 <= y < self.height
        )

# Indixes and Coordinates: 
# a grid stores indices and coordinates and manages conversion between them. 
# array index (120, 340) might equal: 
# latitude = 48.2°
# longitude = 16.3°

# Notes.
# Avoid requiring squares.
# A planet isn't square.
# A common size is something like
# 2048 × 1024
# because longitude wraps all the way around the planet, while latitude 
# only goes from north pole to south pole. 
# That's a natural 2:1 aspect ratio for an equirectangular world map.