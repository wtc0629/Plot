import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
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

    # Return the LineCollection object for creating a legend
    return lc

def make_segments(x, y):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments

tester_name = ["PHD","Dennis","DRP","Philipp","QXR","TMZ","TYT","WTC","WTC2","ZC","YKD","WTC3"]
for k in range(12):
    data = pd.read_csv("C:\\Users\\51004\\Desktop\\MergeCSV\\"+tester_name[k] +"\\gaze_merged.csv")
    gestures = ["horizontally", "horizontally fast", "vertically", "vertically fast", "near to far", "near to far fast",
                "square", "square fast", "left circle (anticlockwise)", "right circle (clockwise)",
                "large right circle (clockwise)"]

    # Define custom colormap with Red, Yellow, Blue, Green, Pink
    colors = [(1, 0, 0), (1, 1, 0), (0, 0, 1), (0, 1, 0), (1, 0.71, 0.76)]
    cmap = LinearSegmentedColormap.from_list('CustomMap', colors, N=5)

    # Create legend lines for Red, Yellow, Blue, Green, Pink
    legend_lines = [
        Line2D([0], [0], color=colors[0], linewidth=2),
        Line2D([0], [0], color=colors[1], linewidth=2),
        Line2D([0], [0], color=colors[2], linewidth=2),
        Line2D([0], [0], color=colors[3], linewidth=2),
        Line2D([0], [0], color=colors[4], linewidth=2),
    ]

    for j in gestures:
        fig, axs = plt.subplots(2, 4, figsize=(18, 8), constrained_layout=True)
        axs = axs.flatten()

        # Store LineCollection objects for creating legend
        lc_legend = []

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
                # Use colorline and store the LineCollection objects
                lc = colorline(axs[i], x, y, z, cmap=cmap, linewidth=2, alpha=0.7)
                lc_legend.append(lc)
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
                # Use colorline and store the LineCollection objects
                lc = colorline(axs[i], x, y, z, cmap=cmap, linewidth=2, alpha=0.7)
                lc_legend.append(lc)
                axs[i].set_title(nowGesture)
                axs[i].set_xlabel('gaze_point_3d_x')
                axs[i].set_ylabel('gaze_point_3d_y')

        # Add a common legend for each color
        axs[3].legend(legend_lines, ['0-2sec', '2-4sec', '4-6sec', '6-8sec', '8-10sec'], bbox_to_anchor=(1.05, 1),
                      loc='best', borderaxespad=0.)

        # Create a legend for the LineCollection objects
        # axs[0].legend(lc_legend, [f'Gesture {i + 1}' for i in range(8)], bbox_to_anchor=(1.05, 0.5), loc='center left', borderaxespad=0.)

        plt.savefig("C:\\Users\\51004\\Desktop\\MergeCSV\\"+tester_name[k]+"\\" + j + '.png', bbox_inches='tight')
        plt.close('all')

