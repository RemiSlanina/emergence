import numpy as np 
import matplotlib.pyplot as plt 

from core.grid import Grid
from core.layer import Layer
from render.renderer import Renderer 

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


