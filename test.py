import numpy as np
import os
# from imageio import imread,imsave
from matplotlib import pyplot as plt

# %matplotlib inline

sourcefolder = r'E:\Desktop\中惠\资源文件\8815029_npy'
# folder_name = '子文件夹'
# sourcefolder = rootfolder +'\\'+ folder_name

img = [] # 设置数组预空间

# r""是防止字符串转译
for subfiles in os.listdir(sourcefolder):
    sourcefiles = sourcefolder +'\\'+ subfiles

    # current_img = imread(sourcefiles)
    current_img = np.load(sourcefiles)
    img.append(current_img)


img_arr = np.array(img)
print(img_arr.shape)
# plt.imshow(img_arr[1,:,:])
plt.imshow(img_arr)
