import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import xlrd

data = pd.read_excel('testdata.xlsx')
all_data = []
for i in range(data.shape[0]):
    all_data.append((data.loc[i].tolist())[1:])



writer = pd.ExcelWriter('new_testdata2.xlsx', engine='xlsxwriter')
for j in range(0, np.shape(all_data)[1]):
    vars()['new_list' + str(j)] = []
    vars()['new_list' + str(j) + 'per'] = []
    vars()['new_list' + str(j) + 'sum'] = 0
    for i in range(0, np.shape(all_data)[0]):
        vars()['new_list' + str(j)].append(all_data[i][j])
    vars()['new_list' + str(j) + 'sum'] = sum(vars()['new_list' + str(j)])
    vars()['new_list' + str(j) + 'per'] = np.divide(vars()['new_list' + str(j)],
                                                    vars()['new_list' + str(j) + 'sum']) * 100
    vars()['new_list' + str(j) + 'df'] = pd.DataFrame(vars()['new_list' + str(j) + 'per'])

    vars()['new_list' + str(j) + 'df'].to_excel(writer, sheet_name='Sheet1', index=False, startcol=j, startrow=0)
writer.save()

new_data = pd.read_excel('new_testdata2.xlsx')
new_all_data = []

for i in range(new_data.shape[0]):
    new_all_data.append((new_data.loc[i].tolist()[0:]))

# # # --------------------- Creating fig-----------------------------------------
# # From raw value to percentage


barWidth = 0.75
executive_names = data.columns.tolist()[1:]


# print(executive_names)
def zero_checker(val):
    if val == 0.0:
        val = ''
    else:
        val = str(val)+'%'
    return val

def zero_label_checker(val, label):
    if val == 0.0:
        lable = ''
    else:
        lable = label
    return lable

plt.subplots(figsize=(12.8, 6))


def plot_stacked_bar(data, series_labels, category_labels=None,
                     show_values=True, value_format="{}", y_label=None,
                     colors=None, grid=False, reverse=False):
    ny = len(data[0])
    ind = list(range(ny))

    axes = []
    cum_size = np.zeros(ny)

    data = np.array(data)

    # if reverse:
    #     data = np.flip(data, axis=1)
    #     category_labels = reversed(category_labels)

    for i, row_data in enumerate(data):
        color = colors[i] if colors is not None else None
        axes.append(plt.bar(ind, row_data, bottom=cum_size,
                            label=series_labels[i], color=color))
        cum_size += row_data

    if category_labels:
        plt.xticks(ind, category_labels, rotation=0, fontsize=14)

    # if y_label:
    #     plt.ylabel(y_label)

    # plt.legend()

    # if grid:
    #     plt.grid()

    if show_values:
        i = 0
        for axis in axes:

            for bar in axis:

                w, h = bar.get_width(), bar.get_height()
                plt.text(bar.get_x() + w / 2, bar.get_y() + h /3,
                         zero_checker(round(h, 2)), ha="center",
                         va="center", rotation=0, fontsize=14, fontweight='bold')

                plt.text(bar.get_x() + w / 2, bar.get_y() + h/1.3,
                         zero_label_checker(h, series_labels[i]), ha="center",
                         va="center", rotation=0, fontsize=14, fontweight='bold')
            i= i+1
            print(i)


series_labels = data['Brands'].tolist()
print(series_labels)


colors = ['#ff8f00', '#96ff00', '#e4ff00', '#e7bcec', '#b3fff3', '#f1ca97', '#c6ff76', '#6abafe', '#e500ff',
          '#6afeae', '#d8ef3c', '#3cd8ef', '#ffd1dd']

plot_stacked_bar(
    new_all_data,
    series_labels,
    category_labels=executive_names,
    show_values=True,
    value_format='{:.2f}' + '%',
    colors=colors


)

plt.xlabel("Executive Name", fontweight='bold', fontsize=14)
plt.ylabel("Percent %", fontweight='bold', fontsize=14)
plt.title('Executives Brand wise Sales', fontsize=16, fontweight='bold', color='#3e0a75')
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.085),
#                fancybox=True, shadow=True, ncol=7)

plt.show()
# plt.savefig('testfig.png')
