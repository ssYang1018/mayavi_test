# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/13 20:17
@Author  : LIN
@File    : tvtk_example01.py
@IDE     : PyCharm
"""
from tvtk.api import tvtk
from tvtk.tools import mlab
import numpy as np

from numpy2vtk_test import generateVTK


def depth_peeling(scene):
    rw = scene.render_window
    renderer = scene.renderer
    rw.alpha_bit_planes = 1
    rw.multi_samples = 0
    renderer.use_depth_peeling = 1
    renderer.maximum_number_of_peels = 100
    renderer.occlusion_ratio = 0.1


def ivtk_scene(actors):
    from tvtk.tools import ivtk

    window = ivtk.IVTKWithCrustAndBrowser(size=(800, 600))
    window.title = 'TVTKImageWindow'  # TVTKImageWindow
    window.open()
    depth_peeling(window.scene)
    window.scene.add_actors(actors)
    window.scene.background = .5, .5, .5
    # fix problem when run in IPython
    dialog = window.control.centralWidget().widget(0).widget(0)
    from pyface.qt import QtCore

    dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
    dialog.show()
    return window


def event_loop():
    from pyface.api import GUI
    gui = GUI()
    gui.start_event_loop()


def main():
    # 创建一个圆锥数据源对象，并且同时设置其高度、底面半径和底面圆的分辨率(底面边数)（用36边形近似）
    # cs = tvtk.CylinderSource(height=3.0, radius=1.0, resolution=36)  # 2
    stl = tvtk.STLReader(file_name=r"E:\Desktop\HUA_implant_001.stl")

    # 图像对象：使用PolyDataMapper将数据转换为图形数据
    # m = tvtk.PolyDataMapper(input_connection=cs.output_port)  # 3 映射器
    m = tvtk.PolyDataMapper(input_connection=stl.output_port)  # 3 映射器

    # 创建一个Actor场景的实体，实体中是图像对象
    a = tvtk.Actor(mapper=m)
    win = ivtk_scene(a)
    win.scene.isometric_view()

    # 开始界面消息循环
    event_loop()


def test():
    from tvtk.tools import ivtk
    # from pyface.api import GUI
    # gui = GUI()
    # Create and open an application window.
    window = ivtk.IVTKWithCrustAndBrowser(size=(800, 600))
    window.open()
    f = mlab.Figure(window.scene)

    # Create an outline.
    # o = mlab.Outline()
    # f.add(o)
    # mlab.test_imshow(f)
    z_large = np.random.random((1024, 512))
    i = mlab.ImShow(z_large)
    f.add(i)



def test_show_vtkData():
    vtk_object = generateVTK()

    # con = tvtk.StructuredGridOutlineFilter()
    con = tvtk.ContourFilter()
    con.set_input_data(vtk_object)
    # con.generate_values(10, grid.point_data.scalars.range)
    m = tvtk.PolyDataMapper(input_connection=con.output_port)  # 3 映射器
    # m = tvtk.PolyDataMapper(scalar_range=vtk_object.GetPointData().scalars.range,
    #                     input_connection = con.output_port)  # 3 映射器

    # 创建一个Actor场景的实体，实体中是图像对象
    a = tvtk.Actor(mapper=m)
    a.property.opacity = 1 #透明度0.1
    a.property.color = 0, 0, 0
    win = ivtk_scene(a)
    win.scene.isometric_view()

    # 开始界面消息循环
    event_loop()



if __name__ == '__main__':
    # test()
    # main()
    # mlab.main()
    test_show_vtkData()
