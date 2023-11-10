import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

test = pd.read_csv('C:\\Users\\51004\\Desktop\\MergeCSV\\Dennis\\gaze_merged.csv')
gestures = ["horizontally", "horizontally fast", "vertically", "vertically fast", "near to far", "near to far fast",
            "square", "square fast", "left circle (anticlockwise)", "right circle (clockwise)",
            "large right circle (clockwise)"]


# print(test)



def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()


colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
for j in gestures:
    nowGestures = ''
    newtest = []
    for i in range(8):
        nowGestures = j + '_GestureTime' + str(i)
        newtest = test.loc[test['process'] == nowGestures]
        if j == 'near to far' or j == 'near to far fast':
            newtest.plot(x='gaze_point_3d_y', y='gaze_point_3d_z', title=j + ' y-z ' + str(i))
         #  newtest.plot(x='gaze_point_3d_x', y='gaze_point_3d_z', title=j + ' x-z ' + str(i))
        else:
            newtest.plot(x='gaze_point_3d_x', y='gaze_point_3d_y', title=j + ' x-y ' + str(i))


    filename = 'C:\\Users\\51004\\Desktop\\MergeCSV\\Dennis\\' + j + '.pdf'
    save_multi_image(filename)
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
