import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('testdata.xlsx')
# print(data.columns)
print(data.shape)

name1val = (data.loc[0].tolist())[1:]
name2val = (data.loc[1].tolist())[1:]
name3val = (data.loc[2].tolist())[1:]
name4val = (data.loc[3].tolist())[1:]
name5val = (data.loc[4].tolist())[1:]
name6val = (data.loc[5].tolist())[1:]
name7val = (data.loc[6].tolist())[1:]
name8val = (data.loc[7].tolist())[1:]
name9val = (data.loc[8].tolist())[1:]
name10val = (data.loc[9].tolist())[1:]

# # # --------------------- Creating fig-----------------------------------------
# name1val = [600, 500, 330]
# name2val = [700, 500, 660]
# name3val = [450, 500, 34]

r = np.arange(0, 2, 1)
# print(r)

# # # From raw value to percentage

# plot
barWidth = 0.75
names = data.columns.tolist()[1:]


plt.subplots(figsize=(12.8, 9))
#
# labels = names.tolist()
#
#
def plot_stacked_bar(data, series_labels, category_labels=None,
                     show_values=False, value_format="{}", y_label=None,
                     colors=None, grid=False, reverse=False):


    ny = len(data[0])
    ind = list(range(ny))

    axes = []
    cum_size = np.zeros(ny)

    data = np.array(data)

    if reverse:
        data = np.flip(data, axis=1)
        category_labels = reversed(category_labels)

    for i, row_data in enumerate(data):
        color = colors[i] if colors is not None else None
        axes.append(plt.bar(ind, row_data, bottom=cum_size,
                                label=series_labels[i], color=color))
        cum_size += row_data

    if category_labels:
        plt.xticks(ind, category_labels, rotation=0, fontsize=14)

    if y_label:
        plt.ylabel(y_label)

    # plt.legend()

    # if grid:
    #     plt.grid()

    if show_values:
        for axis in axes:
            for bar in axis:
                w, h = bar.get_width(), bar.get_height()
                plt.text(bar.get_x() + w / 2, bar.get_y() + h / 2,
                             value_format.format(h), ha="center",
                             va="center", rotation=0, fontsize=14, fontweight='bold')


series_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
data = [name1val, name2val, name3val, name4val, name5val, name6val, name7val, name8val, name9val, name10val]

plot_stacked_bar(
    data,
    series_labels,
    category_labels=names,
    show_values=True,
    value_format='{:.0f}',
    colors=['#31c377', '#f4b300', 'red', '#96ff00', '#0089ff', '#e500ff', '#00ffd8', '#0089ff', '#e500ff', '#00ffd8']
)

# plt.xlabel("Branch Name", fontweight='bold', fontsize=12)
plt.ylabel("Target", fontweight='bold', fontsize=14)
plt.title('6. Executives Brand wise Sales', fontsize=16, fontweight='bold', color='#3e0a75')
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.085),
#                fancybox=True, shadow=True, ncol=7)

plt.show()
