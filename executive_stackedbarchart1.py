import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import xlrd

import pandas as pd
import path as dir
import Functions.db_connection as dbc

sql = """
DECLARE @cols NVARCHAR (MAX)

SELECT @cols = COALESCE (@cols + ',[' + [executive shortname] + ']', '[' + [executive shortname] + ']')
               FROM
               (
                    SELECT distinct [executive shortname] from [dbo].[GPMExecutive_ShortName] where gpmname= 'Mr. Fazal Mohammad Tanim'
               ) PV
               ORDER BY [executive shortname]
DECLARE @query NVARCHAR(MAX)
SET @query ='Select * from
        (select *
        from
        (
      select sum(extinvmisc) as sale,Item.brand,item.itemno,[Executive ShortName] as Exe from
(select * from oesalesdetails where  
transtype =1 and transdate>=convert(varchar(8),getdate(), 112)) as Sale
left join
(select * from prinfoskf ) as Item
on sale.item=item.itemno

left join
(select * from [GPMExecutive_ShortName]) as Exe on
exe.ExecutiveName=item.cp01
group by [Executive ShortName],item.exid,item.brand,item.ITEMno
        ) src
        pivot
        (Max(Sale)
       for EXE in (' + @cols + ')) AS piv
        ) as TblSale
              left join
            (select *
        from
(select [Executive ShortName] as Exe,item.brand,item.itemno as itemno,sum(trgval) as Target from
(select * from [ARCSECONDARY].[dbo].[PRODUCT_WISE_TRG] where yrm=convert(varchar(6),getdate(), 112)) as Tar
right join
(select * from prinfoskf  ) as Item
on tar.exid=item.exid
and item.itemno=tar.item
left join
(select * from [GPMExecutive_ShortName]) as Exe on
exe.ExecutiveName=item.cp01
group by tar.exid,item.itemno,[Executive ShortName] ,item.Brand
        ) src
        pivot
        (
        sum(Target)
        for EXE in (' + @cols + '
         )
        ) AS piv) as tblsTarget
        on (tblsTarget.itemno=TblSale.itemno)'

EXEC SP_EXECUTESQL @query
"""

df = pd.read_sql(sql, dbc.connection)

df.to_csv('initialdata.csv', index=False)
coluns = df.columns.tolist()[1:]

df = pd.read_csv('initialdata.csv')
# print('Total col = ', len(df.columns))

df = df.reindex(sorted(df.columns), axis=1)



df1 = df[['brand'] + [col for col in df.columns if col != 'brand']]


# print(df1.columns)
df1 = df1.iloc[:, :-3]
master_col = []
coluns = df1.columns.tolist()[1:]

# # Arrange columns name with .S for sales and .T for Target
for i in range(len(coluns)):
    if i%2 == 0:
        col = coluns[i]+' .S'
        master_col.append(col)
    else:
        col = coluns[i].replace(".1", "")+' .T'
        master_col.append(col)

# print(master_col)


threshLinit = (len(df1.columns)) - 3
print(threshLinit)
df1 = df1[df1.isnull().sum(axis=1) <= threshLinit]
df1.to_csv('master_executive_target_sales_data.csv', index=False)

# df = pd.read_csv('master_executive_target_sales_data.csv')
df = df1.fillna(0)
l = df.columns.tolist()
Colvalues = l[1:]

df.sort_values(by=Colvalues, inplace=True)

df.to_csv('master_executive_target_sales_data.csv', index=False)
# print('Executive Stacked Bar-chart Initial Data Saved ')


data = pd.read_csv('master_executive_target_sales_data.csv')
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

barWidth = 0.90
executive_names = data.columns.tolist()[1:]


# print(executive_names)
def zero_checker(val):
    if val == 0.0:
        val = ''
    else:
        val = str(val) #+ '%'
    return val


def zero_label_checker(val, label):
    if val == 0.0:
        lable = ''
    else:
        lable = label # + '\n' + str(round(val, 2)) + '%'
        # lable =  str(round(val, 2)) #+ '%'
    return lable


plt.subplots(figsize=(20, 8))


def plot_stacked_bar(data, series_labels, category_labels=None,
                     show_values=True, value_format="{}", y_label=None,
                     colors=None, grid=True, reverse=False):
    ny = len(data[0])
    ind = list(range(ny))

    axes = []
    cum_size = np.zeros(ny)

    data = np.array(data)

    # if reverse:
    #     data = np.flip(data, axis=1)
    #     category_labels = reversed(category_labels)

    for i, row_data in enumerate(data):
        # color = colors[i] if colors is not None else None
        axes.append(plt.bar(ind, row_data, bottom=cum_size,
                            label=series_labels[i]
                            # , color=color
                            ))
        cum_size += row_data

    if category_labels:
        plt.xticks(ind, master_col, rotation=90, fontsize=14, fontweight='bold')

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
                # plt.text(bar.get_x() + w / 2, bar.get_y() + h / 2,
                #          zero_label_checker(h, series_labels[i]), ha="center",
                #          va="center", rotation=0, fontsize=14)

                plt.text(bar.get_x() + w / 2, bar.get_y() + h/1.3,
                         zero_label_checker(h, series_labels[i]), ha="center",
                         va="center", rotation=0, fontsize=12)
            i= i+1
            # print(i)


series_labels = data['brand'].tolist()
# print(series_labels)

colors = ['#ff8f00', '#96ff00', '#e4ff00', '#e7bcec', '#b3fff3', '#f1ca97', '#c6ff76', '#6abafe', '#e500ff',
          '#6afeae', '#d8ef3c', '#3cd8ef', '#ffd1dd', '#ff8f00', '#96ff00', '#e4ff00', '#e7bcec', '#b3fff3', '#f1ca97', '#c6ff76', '#6abafe', '#e500ff',
          '#6afeae', '#d8ef3c', '#3cd8ef', '#ffd1dd','#ff8f00', '#96ff00', '#e4ff00', '#e7bcec', '#b3fff3', '#f1ca97', '#c6ff76', '#6abafe', '#e500ff',
          '#6afeae', '#d8ef3c', '#3cd8ef', '#ffd1dd','#ff8f00', '#96ff00', '#e4ff00', '#e7bcec', '#b3fff3', '#f1ca97', '#c6ff76', '#6abafe', '#e500ff',
          '#6afeae', '#d8ef3c', '#3cd8ef', '#ffd1dd']

plot_stacked_bar(
    new_all_data,
    series_labels,
    category_labels=executive_names,
    show_values=True,
    value_format='{:.1f}' + '%'
    # ,colors=colors

)

plt.xlabel("Executive Name", fontweight='bold', fontsize=14)
plt.ylabel("Percent %", fontweight='bold', fontsize=14)
plt.title('Executives Brand wise Sales', fontsize=16, fontweight='bold', color='#3e0a75')
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.085),
#                fancybox=True, shadow=True, ncol=7)

# plt.show()
plt.savefig('mainexecutive.png')
