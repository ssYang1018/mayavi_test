from mayavi import mlab

from import_npy import get_data


def main():
    numpy_data = get_data()
    # mlab.contour3d(numpy_data, opacity=1)
    mlab.volume_slice(numpy_data,plane_orientation='x_axes', slice_index=0)
    mlab.volume_slice(numpy_data,plane_orientation='y_axes', slice_index=0)
    mlab.volume_slice(numpy_data,plane_orientation='z_axes', slice_index=0)
    mlab.show()


if __name__ == '__main__':
    main()