import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('testdata.xlsx')
all_data = []
for i in range(data.shape[0]):
    all_data.append((data.loc[i].tolist())[1:])

print(all_data)
# # # --------------------- Creating fig-----------------------------------------
# # # From raw value to percentage


# plot
barWidth = 0.75
executive_names = data.columns.tolist()[1:]
# print(executive_names)

plt.subplots(figsize=(12.8, 6))

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


series_labels = data['Brands'].tolist()

plot_stacked_bar(
    all_data,
    series_labels,
    category_labels=executive_names,
    show_values=True,
    value_format='{:.0f}',
    colors=['#31c377', '#f4b300', 'red', '#96ff00', '#0089ff', '#e500ff', '#00ffd8','red', '#96ff00', '#0089ff', '#e500ff', '#00ffd8']
)

# plt.xlabel("Branch Name", fontweight='bold', fontsize=12)
plt.ylabel("Target", fontweight='bold', fontsize=14)
plt.title('Executives Brand wise Sales', fontsize=16, fontweight='bold', color='#3e0a75')
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.085),
#                fancybox=True, shadow=True, ncol=7)

# plt.show()
plt.savefig('testfig.png')
