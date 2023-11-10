import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.collections as mcoll
import matplotlib.path as mpath
from matplotlib.colors import LinearSegmentedColormap

def colorline(ax, x, y, z=None, cmap=plt.get_cmap('jet'), norm=plt.Normalize(0.0, 1.0),
              linewidth=2, alpha=1.0):
    if z is None:
        z = np.linspace(0.0, 1.0, len(x))

    if not hasattr(z, "__iter__"):
        z = np.array([z])

    z = np.asarray(z)

    segments = make_segments(x, y)
    lc = mcoll.LineCollection(segments, array=z, cmap=cmap, norm=norm,
                              linewidth=linewidth, alpha=alpha)

    ax.add_collection(lc)

def make_segments(x, y):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments

data = pd.read_csv('C:\\Users\\51004\\Desktop\\MergeCSV\\Dennis\\gaze_merged.csv')
gestures = ["horizontally", "horizontally fast", "vertically", "vertically fast", "near to far", "near to far fast",
            "square", "square fast", "left circle (anticlockwise)", "right circle (clockwise)",
            "large right circle (clockwise)"]

# Define custom colormap with Red, Yellow, Blue, Green, Pink
colors = [(1, 0, 0), (1, 1, 0), (0, 0, 1), (0, 1, 0), (1, 0.41, 0.71)]
cmap = LinearSegmentedColormap.from_list('CustomMap', colors, N=5)

for j in gestures:
    fig, axs = plt.subplots(2, 4, figsize=(12, 6), constrained_layout=True)

    axs = axs.flatten()

    for i in range(8):
        nowGesture = j + '_GestureTime' + str(i)
        subset = data.loc[data['process'] == nowGesture]
        if j == "near to far" or j == "near to far fast":
            x = subset['gaze_point_3d_y']
            y = subset['gaze_point_3d_z']
            axs[i].plot(x, y, label="Original", color='black')
            z = np.linspace(0, 1, len(x))
            path = mpath.Path(np.column_stack([x, y]))
            verts = path.interpolated(steps=3).vertices
            x, y = verts[:, 0], verts[:, 1]
            colorline(axs[i], x, y, z, cmap=cmap, linewidth=2, alpha=0.7)
            axs[i].set_title(nowGesture)
            axs[i].set_xlabel('gaze_point_3d_y')
            axs[i].set_ylabel('gaze_point_3d_z')

        else:
            x = subset['gaze_point_3d_x']
            y = subset['gaze_point_3d_y']
            axs[i].plot(x, y, label="Original", color='black')

            z = np.linspace(0, 1, len(x))
            path = mpath.Path(np.column_stack([x, y]))
            verts = path.interpolated(steps=3).vertices
            x, y = verts[:, 0], verts[:, 1]
            colorline(axs[i], x, y, z, cmap=cmap, linewidth=2, alpha=0.7)
            axs[i].set_title(nowGesture)
            axs[i].set_xlabel('gaze_point_3d_x')
            axs[i].set_ylabel('gaze_point_3d_y')


    plt.savefig('C:\\Users\\51004\\Desktop\\MergeCSV\\Dennis\\' + j + '.png')
    plt.close('all')
