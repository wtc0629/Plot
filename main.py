import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.collections as mcoll
import matplotlib.path as mpath

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

for j in gestures:
    fig, axs = plt.subplots(2, 4, figsize=(12, 6), constrained_layout=True)

    axs = axs.flatten()

    for i in range(8):
        nowGesture = j + '_GestureTime' + str(i)
        subset = data.loc[data['process'] == nowGesture]

        x = subset['gaze_point_3d_x']
        y = subset['gaze_point_3d_y']

        # Plot the original line
        axs[i].plot(x, y, label="Original", color='black')

        # Add colored line segments
        z = np.linspace(0, 1, len(x))
        path = mpath.Path(np.column_stack([x, y]))
        verts = path.interpolated(steps=3).vertices
        x, y = verts[:, 0], verts[:, 1]

        colorline(axs[i], x, y, z, cmap=plt.get_cmap('tab10'), linewidth=2, alpha=0.7)

        axs[i].set_title(nowGesture)
        axs[i].set_xlabel('gaze_point_3d_x')
        axs[i].set_ylabel('gaze_point_3d_y')
        axs[i].legend()

    plt.savefig('C:\\Users\\51004\\Desktop\\MergeCSV\\Dennis\\' + j + '.png')
    plt.close('all')



# plt.savefig('C:\\Users\\51004\\Desktop\\MergeCSV\\Dennis\\'+j+str(i)+'.png')
# plt.close()

# print(k)
# x_values = [[1],[3],[5]]
# y_values = [[3],[6],[3]]

# plt.plot(x_values, y_values, 'red')


# list2 = []
# for i in range(8):
#   list2.append('vertically_GestureTime' + str(i))

# test2 = test.loc[test['process'].isin(list2)]

# test2.plot.scatter(x='gaze_normal1_x', y='gaze_normal1_y')

# plt.show()
