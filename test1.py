import numpy as np
from mayavi import mlab
import os

# load_npy0 = np.load(r"E:\Desktop\中惠\资源文件\8815029_npy\8815029_IM000_PIC.npy")
sourcefolder = r'E:\Desktop\中惠\资源文件\8815029_npy'
img = []
# mlab.options.offscreen=True
for subfiles in os.listdir(sourcefolder)[150:180]:
    sourcefiles = sourcefolder +'\\'+ subfiles

    # current_img = imread(sourcefiles)
    current_img = np.load(sourcefiles)
    img.append(current_img)
    # mlab.points3d(current_img, mode="point")
    # mlab.contour3d(current_img)



img_arr = np.array(img)
mlab.points3d(img_arr, mode="point", opacity=0.5, line_width=0.02)

mlab.show()