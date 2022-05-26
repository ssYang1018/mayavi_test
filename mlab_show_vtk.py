from mayavi import mlab
from tvtk.api import tvtk
from tvtk.common import configure_input_data

# from import_npy import get_data
from numpy2vtk_test import generateVTK,generateVTK2


def main():
    # data = get_data()
    v = mlab.figure()
    vtk_object = generateVTK()
    con = tvtk.ContourFilter()
    con.set_input_data(vtk_object)
    # con.set_input_data(data)
    sphere_mapper = tvtk.PolyDataMapper()
    configure_input_data(sphere_mapper, con.output)
    con.update()

    p = tvtk.Property(opacity=1, color=(1, 0, 0))
    # The actor is the actually object in the scene.
    sphere_actor = tvtk.Actor(mapper=sphere_mapper, property=p)
    v.scene.add_actor(sphere_actor)

    mlab.show()



if __name__ == "__main__":
    main()