import matplotlib.pyplot as plt 
from core.layer import Layer
from core.grid import Grid


class Renderer: 
    def show(self, layer:Layer): 
        plt.figure(figsize=(10,5)) # size in inches 
        plt.imshow(layer.data, origin="lower", cmap="terrain") 
        plt.colorbar(label="Elevation")
        plt.savefig("test.png")
        plt.show()