import os
import numpy as np
from PIL import  Image
import matplotlib
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage

class HeatMap_Image:
    def __init__(self,image_path,heat_map,gaussian_std=10):
        image = Image.open(image_path)
        width, height = image.size
        self.image = image
        
        heatmap_image = Image.fromarray(heat_map*255)
        heatmap_image_resized = heatmap_image.resize((width,height))
        heatmap_image_resized = ndimage.gaussian_filter(heatmap_image_resized, sigma=(gaussian_std, gaussian_std), order=0)
        heatmap_image_resized = np.asarray(heatmap_image_resized)
        self.heat_map = heatmap_image_resized
    
    def plot(self,transparency=0.7,color_map='bwr',show_axis=False, show_colorbar=False):
        if not show_axis:
            plt.axis('off')
        plt.imshow(self.image)
        plt.imshow(self.heat_map/255, alpha=transparency, cmap=color_map)
        if show_colorbar:
            plt.colorbar()
        plt.show()
    
    def save(self,filename,format='eps',save_path=os.getcwd(),transparency=0.7,color_map='bwr',show_axis=False, show_colorbar=False):
        if not show_axis:
            plt.axis('off')
        plt.imshow(self.image)
        plt.imshow(self.heat_map, alpha=transparency, cmap=color_map)
        if show_colorbar:
            plt.colorbar()
        plt.savefig(os.path.join(save_path,filename), format=format, bbox_inches='tight',pad_inches = 0)