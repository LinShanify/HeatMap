# A Simple Tool for Ploting the Heatmap Overlay Image

### **HeatMap Class**: 3 inputs:
1. **image:** image path *(string)* or image value *(numpy array)*
2. **heatmap:** 2-D numpy value *(no shape restriction)*
3. *(optional)* **gaussian filter**: mosaic smoothing *(gaussian_std, default is 10. when set to 0, means no filter apply)*

```python
from HeatMap import HeatMap
# input a image path and a numpy array heatmap
hm = HeatMap('demo_image.jpg',heat_map)
# or input a numpy array image and heatmap
hm = HeatMap(image,heat_map,gaussian_std=0)
```

### **Method 1 `plot`:** 6 parameters *(all optional)*
1. **transparency:** define the transparency of heamap overlay (lower -> more transparent, default is 0.7)
2. **color_map:** [color map](https://matplotlib.org/examples/color/colormaps_reference.html) style (default is *bwr*)
3. **show_axis:** show axis or not (boolean `True/False`, default is `False`)
4. **show_original:** show original image (boolean `True/False`, default is `False`)
5. **show_colorbar:** show color bar (boolean `True/False`, default is `False`)
6. **width_pad:** the width padding (default is 0, set to negative value for reducing the space between figures)
```python
#simple default plot
hm.plot()
```
![](https://github.com/LinShanify/HeatMap/blob/master/heatmap_result_1.png?raw=true)


```python
#customised plot
hm.plot(transparency=0.6,
        color_map='seismic',
        show_axis=True,
        show_original=True,
        show_colorbar=True,
        width_pad=-10)
```
![](https://github.com/LinShanify/HeatMap/blob/master/heatmap_result_2.png?raw=true)

### **Method 2 `save`:** 9 parameters *(2 required, 7+ optional)*
### **required**
1. **filename:** filename for saved figure *(string)*
2. **formate:** figure saving fomate (**jpg, jpeg, png, pdf, ps, eps** and **svg**)

### **optinal:**
1. **save_path:** firgure saving directory (default is the current working directory)
2. **transparency:** define the transparency of heamap overlay (lower -> more transparent, default is 0.7)
3. **color_map:** [color map](https://matplotlib.org/examples/color/colormaps_reference.html) style (default is *bwr*)
4. **show_axis:** show axis or not (boolean `True/False`, default is `False`)
5. **show_original:** show original image (boolean `True/False`, default is `False`)
6. **show_colorbar:** show color bar (boolean `True/False`, default is `False`)
7. **width_pad:** the width padding (default is 0, set to negative value for reducing the space between figures)
8. other parameters from [pyplot.savefig](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html) can be used here

```python
# simple save
hm.save('heatmap_result_1','png')
```  

```python
# customised save
hm.save('heatmap_result_2','png',
        transparency=0.6,
        color_map='seismic',
        show_axis=True,
        show_original=True,
        show_colorbar=True,
        width_pad=-10)
```

