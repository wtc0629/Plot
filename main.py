import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\51004\\Desktop\\MergeCSV\\Dennis\\gaze_merged.csv')
gestures = ["horizontally", "horizontally fast", "vertically", "vertically fast", "near to far", "near to far fast",
            "square", "square fast", "left circle (anticlockwise)", "right circle (clockwise)",
            "large right circle (clockwise)"]



for j in gestures:
    fig, axs = plt.subplots(2, 4, figsize=(12, 6), constrained_layout=True)

    # 将axs展平，方便后续使用
    axs = axs.flatten()
    nowGestures = ''
    for i in range(8):

        nowGesture = j + '_GestureTime' + str(i)
        subset = data.loc[data['process'] == nowGesture]
        axs[i].plot(subset['gaze_point_3d_x'], subset['gaze_point_3d_y'])
        axs[i].set_title(nowGesture)
        axs[i].set_xlabel('gaze_point_3d_x')
        axs[i].set_ylabel('gaze_point_3d_y')
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
