import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import Functions.db_connection as dbc
def thousand_converter(number):
    number = int(number / 1000)
    number = format(number, ',')
    number = number + 'K'
    return number

def executives_brand_target_sales_chart(name):
    sql = """
        DECLARE @cols NVARCHAR (MAX)
    
        SELECT @cols = COALESCE (@cols + ',[' + [executive shortname] + ']', '[' + [executive shortname] + ']')
                       FROM
                       (
                            SELECT distinct [executive shortname] from [dbo].[GPMExecutive_ShortName] where gpmname 
                             LIKE ?) PV
                       ORDER BY [executive shortname]
        DECLARE @query NVARCHAR(MAX)
        SET @query ='Select * from
                (select *
                from
                (
              select sum(extinvmisc) as sale,Item.brand,[Executive ShortName] as Exe from
        (select * from oesalesdetails where  
        transtype =1 and transdate between convert(varchar(8),DATEADD(month, DATEDIFF(month, 0,  GETDATE()), 0),112) and 
		 convert(varchar(8),getdate(), 112)) as Sale
        left join
        (select * from prinfoskf ) as Item
        on sale.item=item.itemno
        
        left join
        (select * from [GPMExecutive_ShortName]) as Exe on
        exe.ExecutiveName=item.cp01
        group by [Executive ShortName],item.exid,item.brand
                ) src
                pivot
                (Max(Sale)
               for EXE in (' + @cols + ')) AS piv
                ) as TblSale
                      left join
                    (select *
                from
        (select [Executive ShortName] as Exe,item.brand,(sum(trgval)/30)*RIGHT(convert(varchar(8),getdate()-1, 112),2) as Target from
        (select * from [ARCSECONDARY].[dbo].[PRODUCT_WISE_TRG] where yrm=convert(varchar(6),getdate(), 112)) as Tar
        right join
        (select * from prinfoskf) as Item
        on tar.exid=item.exid
        and item.itemno=tar.item
        left join
        (select * from [GPMExecutive_ShortName]) as Exe on
        exe.ExecutiveName=item.cp01
        group by tar.exid,[Executive ShortName] ,item.Brand
                ) src
                pivot
                (
                sum(Target)
                for EXE in (' + @cols + '
                 )
                ) AS piv) as tblsTarget
                on (tblsTarget.brand=TblSale.brand)'
        
        EXEC SP_EXECUTESQL @query
        """

    df = pd.read_sql(sql, dbc.connection, params={name})

    df.to_csv('./Data/initialdata.csv', index=False)

    df = pd.read_csv('./Data/initialdata.csv')

    df = df.reindex(sorted(df.columns), axis=1)
    df1 = df[['brand'] + [col for col in df.columns if col != 'brand']]

    # print(df1.columns)
    df1 = df1.iloc[:, :-1]
    master_col = []
    coluns = df1.columns.tolist()[1:][::-1]

    # # Arrange columns name with .S for sales and .T for Target
    for i in range(len(coluns)):
        if i % 2 == 0:
            col = coluns[i].replace(".1", "")  + ' .T'
            master_col.append(col)
        else:
            col = coluns[i].replace(".1", "") + ' .S'
            master_col.append(col)

    # print(master_col)


    threshLinit = (len(df1.columns)) - 3
    # print(threshLinit)
    df1 = df1[df1.isnull().sum(axis=1) <= threshLinit]
    df1.to_csv('./Data/master_executive_target_sales_data.csv', index=False)

    # # Fill all blank cell with 0
    df = df1.fillna(0)

    # # Short data by values (All Sales and Target)
    colv = df.columns.tolist()
    Colvalues = colv[1::]
    # print(Colvalues)
    df.sort_values(by=Colvalues, inplace=True) # For Largest to smallest

    df.to_csv('./Data/master_executive_target_sales_data.csv', index=False)

    # # Now append all data in a list and process it for stacked barchart
    data = pd.read_csv('./Data/master_executive_target_sales_data.csv')
    all_data = []
    for i in range(data.shape[0]):
        all_data.append((data.loc[i].tolist())[1:])

    # print(all_data)
    # print(len(all_data))
    writer = pd.ExcelWriter('./Data/new_testdata2.xlsx', engine='xlsxwriter')
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

    new_data = pd.read_excel('./Data/new_testdata2.xlsx')
    new_all_data = []

    for i in range(new_data.shape[0]):
        new_all_data.append((new_data.loc[i].tolist()[0:]))

    # # # --------------------- Creating fig-----------------------------------------

    barWidth = 0.90
    executive_names = data.columns.tolist()[1:]
    exe = executive_names[::-1]

    def zero_label_checker(val, label):
        if val == 0.0:
            lable = ''
        else:
            lable = label + '\n' + str(int(val/1000)) + 'K'
            # lable =  str(round(val, 2)) #+ '%'
        return lable

    plt.subplots(figsize=(18, 9))


    def plot_stacked_bar(data, brands, category_labels=None,
                         show_values=True, value_format="{}", y_label=None,
                         colors=None, grid=True, reverse=True):
        ny = len(data[0])
        ind = list(range(ny))

        axes = []
        cum_size = np.zeros(ny)

        data = np.array(data)

        if reverse:
            data = np.flip(data, axis=1)
            category_labels = reversed(category_labels)

        for i, row_data in enumerate(data):
            # color = colors[i] if colors is not None else None
            axes.append(plt.bar(ind, row_data, bottom=cum_size,
                                label=brands[i]
                                # , color=color
                                ))
            cum_size += row_data

        if category_labels:
            plt.xticks(ind, master_col, rotation=45, fontsize=14, fontweight='bold')

        if show_values:
            i = 0
            for axis in axes:

                for bar in axis:
                    w, h = bar.get_width(), bar.get_height()
                    plt.text(bar.get_x() + w / 2, bar.get_y() + h / 2,
                             zero_label_checker(h, brands[i]), ha="center",
                             va="center", rotation=0, fontsize=12)
                i = i + 1

    brands = data['brand'].tolist()

    plot_stacked_bar(
        all_data,
        brands,
        category_labels=exe,
        show_values=True,
        value_format='{:.1f}' + '%'
        # ,colors=colors

    )

    plt.xlabel("Executive Name", fontweight='bold', fontsize=14)
    plt.ylabel("Amounts (K)", fontweight='bold', fontsize=14)
    plt.title('Executives Brand wise MTD Target and Sales', fontsize=16, fontweight='bold', color='#3e0a75')
    # plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.085),
    #                fancybox=True, shadow=True, ncol=7)

    # plt.show()
    plt.tight_layout()
    plt.savefig('./Images/mainexecutive.png')
    print('6. Brand wise Executives Target & Sales Figure Generated')
