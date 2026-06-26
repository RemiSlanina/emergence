import numpy as np 
import matplotlib.pyplot as plt 

from core.grid import Grid
from core.layer import Layer
from render.renderer import Renderer 
from core.planet import Planet 

# earth 
# 7000 km ->  2πr ≈ 40,030 km 
# 1024 × 512 
# 40030 / 1024 ≈ 39 km
# Mount Everest 8849 m
# Mariana Trench -11000 m
planet_earth = Planet(
    name="Earth",
    grid=Grid(1024, 512), 
    radius_km=6371,
    rotation_hours=24,
    axial_tilt_deg=23.44,
    gravity=1.0, 
)

# planet b 
# 7000 km ->  2πr ≈ 44,000 km 
# 1024 × 512 
# 44000 / 1024 ≈ 43 km
# Highest  19000 m
# Mariana Trench -2000 m
planet_b = Planet(
    name="Planet B",
    grid=Grid(1024, 512), 
    radius_km=7000,
    rotation_hours=24,
    axial_tilt_deg=23.0,
    gravity=34.0,
)

print(planet_earth)
print("")
print(planet_b)
print("")

grid = Grid(10,5)
height = Layer("Height", grid) 
temperature = Layer("Temperature", grid)
print(height)
print(height.data)
print("")
height.set(5, 2, 100)
height.set(6, 2, 90)
height.set(7, 2, 80)

# height[2, 5] = 100
# height[2, 6] = 90
# height[3, 5] = 80

print(height.data)


renderer = Renderer() 
renderer.show(height) 


# planet_earth = Planet(
#     name="Earth",
#     radius_km=6371,
#     rotation_hours=24,
#     axial_tilt_deg=23.44,
#     gravity=1.0, 
# )

# planet_b = Planet(
#     name="Planet B",
#     radius_km=7000,
#     rotation_hours=24,
#     axial_tilt_deg=23.0,
#     gravity=34.0,
# )

# height = np.zeros((50, 100)) 

# # from 20-30 on y, from 40-60 on x 
# # height[20:30, 40:60] = 1
# # height[20:30, 60:80] = 0.5 
# # height[10:40, 50] = 2

# for y in range(height.shape[0]):
#     height[y, :] = y


# plt.figure(figsize=(10, 5))
# plt.imshow(height, origin="lower", cmap="terrain")
# plt.colorbar(label="Elevation")
# plt.title("Emergence - Heightmap") 
# plt.savefig("test.png")
# plt.show() 


