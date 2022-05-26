# import numpy as np
# from mayavi import mlab
#
# load_npy0 = np.load(r"E:\Desktop\中惠\资源文件\8815029_npy\8815029_IM000_PIC.npy")
# load_npy1 = np.load(r"E:\Desktop\中惠\资源文件\8815029_npy\8815029_IM001_PIC.npy")
# load_npy2 = np.load(r"E:\Desktop\中惠\资源文件\8815029_npy\8815029_IM002_PIC.npy")
#
# print(np.shape(load_npy0))
#
# con_npy = np.vstack((load_npy0, load_npy1, load_npy2)).reshape(3, 640, 640)
#
# mlab.plot3d()
# mlab.show()

import numpy as np
import os

def get_data():
    """
    :return:返回三维numpy对象img
    """
    sourcefolder = r'E:\Desktop\中惠\资源文件\8815029_npy'
    img = []# mlab.options.offscreen=True
    for subfiles in os.listdir(sourcefolder):
    # for subfiles in os.listdir(sourcefolder)[0:180]:
        sourcefiles = sourcefolder +'\\'+ subfiles

        # current_img = imread(sourcefiles)
        current_img = np.load(sourcefiles)
        img.append(current_img)
    return np.array(img)