import pandas as pd
import path as dir
import Functions.db_connection as dbc
import numpy as np

# executive_df = pd.read_sql_query(""" select [Executive ShortName] from GPMExecutive_ShortName
# where GPMNAME = 'Mr. A. K. M. Nawajesh Hossain' """, dbc.connection)
#
# # print(executive_df['Executive ShortName'].tolist())
#
# a = ['Tanvir', 'Rafi', 'Farhan', 'Alamgir', 'Hrishov', 'Tanmoy', 'Arshiya']
# x = tuple(a)
# x1 = tuple(a)
#
# placeholders = ','.join('?' for i in range(len(x)))
# # print(placeholders)
#
sql = """ DECLARE @cols NVARCHAR (MAX)

SELECT @cols = COALESCE (@cols + ',[' + [executive shortname] + ']', '[' + [executive shortname] + ']')
               FROM
               (
                    SELECT distinct [executive shortname] from [dbo].[GPMExecutive_ShortName] where gpmname like '%A. K. M. Naw%'
               ) PV
               ORDER BY [executive shortname]
DECLARE @query NVARCHAR(MAX)
SET @query ='Select * from
        (select *
        from
        (
       select sale,saleitem.brand,exe from
(select item.brand,sum(extinvmisc) as Sale
--,sum(Value) as Target
--,sum(Value) as Target

from
 (select *,left(transdate,6) as yearmonth from oesalesdetails where transdate>20201201) as sale
left join

(select brand,itemno,gpmname from prinfoskf) as item
on sale.item=item.itemno
group by GPMNAME,Item.brand) as saleItem
left join
(select distinct brand,[Executive ShortName] as EXE from
(select * from GPMBRAND) as gpm
left join
(select * from [GPMExecutive_ShortName]) as exe
on gpm.name=exe.gpmname
) as GPMEXE
on saleItem.brand=GPMEXE.brand


        ) src

        pivot
        (Max(Sale)
       for EXE in (' + @cols + ')) AS piv
        ) as TblSale
              left join
            (select *
        from
(select *
        from
        (select target,targetitem.brand,exe from
(select item.brand,sum(value) as target
--,sum(Value) as Target
--,sum(Value) as Target

from
 (select * from [ARCSECONDARY].[dbo].[RfieldForceProductTRG] where yearmonth=202012) as target
left join

(select brand,itemno,gpmname from prinfoskf) as item
on target.itemno=item.itemno
group by GPMNAME,Item.brand) as TargetItem
left join
(select distinct brand,[Executive ShortName] as EXE from
(select * from GPMBRAND) as gpm
left join
(select * from [GPMExecutive_ShortName]) as exe
on gpm.name=exe.gpmname
) as GPMEXE
on targetitem.brand=GPMEXE.brand
) as T3
        ) src
        pivot
        (
        sum(Target)
        for EXE in (' + @cols + '
         )
        ) AS piv) as tblsTarget
        on (tblsTarget.Brand=TblSale.Brand)'

EXEC SP_EXECUTESQL @query
"""

df = pd.read_sql(sql, dbc.connection)


df.to_csv('initialdata.csv', index=False)

df = pd.read_csv('initialdata.csv')
threshLinit = (len(df.columns)-2)/2
df = df.dropna(thresh=threshLinit)

df = df.reindex(sorted(df.columns), axis=1)
df1 = df[ ['brand'] + [ col for col in df.columns if col != 'brand' ] ]
df1 = df1.iloc[:,:-1]

df1.to_csv('master_executive_target_sales_data.csv', index=False)
print('Executive Stacked Bar-chart Initial Data Saved ')


df = pd.read_csv('master_executive_target_sales_data.csv')
df = df.fillna(0)

df = df.to_csv('master_executive_target_sales_data.csv', index=False)
