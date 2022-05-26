import numpy as np
import vtk
from vtk.util import numpy_support
from tvtk.api import tvtk

from import_npy import get_data

def generateVTK():
    numpy_data = get_data()
    # numpy_data is a 3D numpy array
    shape = numpy_data.shape[::-1]
    vtk_data = numpy_support.numpy_to_vtk(numpy_data.ravel(), 1, vtk.VTK_SHORT)

    vtk_image_data = vtk.vtkImageData()
    vtk_image_data.SetDimensions(shape)
    vtk_image_data.SetSpacing(np.array([1.0, 1.0, 1.0])) #间距
    # vtk_image_data.SetOrigin(origin) #起始点
    vtk_image_data.GetPointData().SetScalars(vtk_data)
    # print(vtk_image_data)
    return vtk_image_data


