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
    # vtk_image_data.SetSpacing(np.array([1.0, 1.0, 1.0])) #间距
    # vtk_image_data.SetOrigin(origin) #起始点
    vtk_image_data.GetPointData().SetScalars(vtk_data)
    # print(vtk_image_data)
    return vtk_image_data


def generateVTK2():
    """
    导入C array
    :return:
    """

    numpy_data = get_data()
    numpy_str = numpy_data.astype(np.int16).tostring()
    x_extent = numpy_data.shape[2]
    y_extent = numpy_data.shape[1]
    z_extent = numpy_data.shape[0]

    image_import = vtk.vtkImageImport()
    image_import.SetImportVoidPointer(numpy_str, len(numpy_str))
    # 也可以使用CopyImportVoidPointer() 会copy一份numpy_str
    image_import.SetWholeExtent(0, x_extent - 1, 0, y_extent - 1, 0, z_extent - 1)
    image_import.SetDataExtent(0, x_extent - 1, 0, y_extent - 1, 0, z_extent - 1)
    image_import.SetDataScalarTypeToShort()  # 根据需求指定数据类型
    image_import.SetNumberOfScalarComponents(1)
    # 如果是RGB数据的话，SetNumberOfScalarComponents(3)
    image_import.Update()

    vtk_image_data = vtk.vtkImageData()
    # vtk_image_data.SetSpacing(spacing)
    # vtk_image_data.SetOrigin(origin)
    return vtk_image_data

