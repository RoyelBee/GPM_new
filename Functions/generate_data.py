import pandas as pd
import pyodbc as db
import numpy as np

import Functions.read_gpm_info as gpm
import Functions.db_connection as conn

def GenerateReport(gpm_name):
    sql_queryes = """
                declare @thismonth varchar(6)
        declare @firstday varchar(8)
        declare @pdatefrom varchar(8)
        declare @pdateTo varchar(8)
        declare @TotalDays int
        declare @MTDdays int=(SELECT DAY(getdate()) )
                        
        if(@MTDdays=1)
        begin
        set @thismonth=convert(varchar(6),getdate()-1,112)
        set @TotalDays=(Select day(dateadd(mm,DateDiff(mm, -1, getdate()-1),0) -1))
        set @MTDdays=(SELECT DAY(getdate()-1)  )
        set @firstday=convert(varchar(6),getdate()-1,112)+'01'
        end
        else
        begin
        set @thismonth=convert(varchar(6),getdate(),112)
        set @TotalDays=(Select day(dateadd(mm,DateDiff(mm, -1, getdate()),0) -1))
        set @firstday=convert(varchar(6),getdate(),112)+'01'
        end
                        
        set @pdateTo= convert(varchar(8),dateadd(Day,-1,getdate()),112)
        --select @pdateTo
        set @pdatefrom= convert(varchar(8),dateadd(Day,-91,getdate()),112)
        --select @mtddays
                        
        select
        dense_rank() OVER (ORDER BY BRAND  ) [BSL NO]
        ,ISNULL(BRAND, 0) BRAND
                        
        ,ROW_NUMBER() OVER (ORDER BY ProductBrand.Brand)   [ISL NO]
        , ISNULL(ProductBrand.Itemname, 'Not Found') [Item Name]
        ,PACKSIZE as UOM
                     
        ,ISNULL(CAST(Sales.YesterdaySales AS INT), 0) YesterdaySalesQty
        ,ISNULL(CAST(Sales.AvgSalesDay AS INT), 0) [Avg Sales/Day]
        ,ISNULL(CAST(ItemTarget.ST AS INT), 0) [Monthly Sales Target]
        ,ISNULL(CAST(ItemTarget.MTDTarget AS INT), 0) [MTD Sales Target]
        ,ISNULL(CAST(Sales.ActualSalesMTD AS INT), 0) [Actual Sales MTD]
        ,ISNULL(CAST(case when ItemTarget.ST>0 then (Sales.ActualSalesMTD/ItemTarget.MTDTarget)* 100 else 0 end AS INT), 0) as [MTD Sales Acv]
        ,ISNULL(CAST(case when ItemTarget.ST>0 then (Sales.ActualSalesMTD/ItemTarget.ST) * 100 else 0 end AS INT), 0) as [Monthly Sales Acv]
        ,ISNULL(cast(Sales.AvgSalesDay*@TotalDays AS INT), 0) as [Monthly Sales Trend]
        ,ISNULL(cast(case when ItemTarget.ST>0 then (Sales.AvgSalesDay*@TotalDays /ItemTarget.ST)*100 else 0 end as int), 0) as [Monthly Sales Trend Achiv]
        ,ISNULL(CAST((NationwideStock-Sales.ActualSalesMTD) AS INT), 0) as [Remaing Stock]
        ,ISNULL(CAST(NationwideStock AS INT), 0) [Nationwide Stock]
        ,isnull(cast([SKF Mirpur Plant] as int), 0) as 'SKF Mirpur Plant'
        ,isnull(cast([SKF Tongi Plant] as int), 0) as 'SKF Tongi Plant'
        ,isnull(cast([SKF Rupganj Plant]as int), 0) as 'SKF Rupganj Plant',
                        
        isnull(AvgSaleBOG, 0) AvgSaleBOG,
        isnull(AvgSaleBSL, 0) AvgSaleBSL,
        isnull(AvgSaleCOM, 0) AvgSaleCOM,
        isnull(AvgSaleCOX, 0) AvgSaleCOX,
        isnull(AvgSaleCTG, 0) AvgSaleCTG,
        isnull(AvgSaleCTN, 0) AvgSaleCTN,
        isnull(AvgSaleDNJ, 0) AvgSaleDNJ,
        isnull(AvgSaleFEN, 0) AvgSaleFEN,
        isnull(AvgSaleFRD, 0) AvgSaleFRD,
        isnull(AvgSaleGZP, 0) AvgSaleGZP,
        isnull(AvgSaleHZJ, 0) AvgSaleHZJ,
        isnull(AvgSaleJES, 0) AvgSaleJES,
        isnull(AvgSaleKHL, 0) AvgSaleKHL,
        isnull(AvgSaleKRN, 0) AvgSaleKRN,
        isnull(AvgSaleKSG, 0) AvgSaleKSG,
        isnull(AvgSaleKUS, 0) AvgSaleKUS,
        isnull(AvgSaleMHK, 0) AvgSaleMHK,
        isnull(AvgSaleMIR, 0) AvgSaleMIR,
        isnull(AvgSaleMLV, 0) AvgSaleMLV,
        isnull(AvgSaleMOT, 0) AvgSaleMOT,
        isnull(AvgSaleMYM, 0) AvgSaleMYM,
        isnull(AvgSaleNAJ, 0) AvgSaleNAJ,
        isnull(AvgSaleNOK, 0) AvgSaleNOK,
        isnull(AvgSalePAT, 0) AvgSalePAT,
        isnull(AvgSalePBN, 0) AvgSalePBN,
        isnull(AvgSaleRAJ, 0) AvgSaleRAJ,
        isnull(AvgSaleRNG, 0) AvgSaleRNG,
        isnull(AvgSaleSAV, 0) AvgSaleSAV,
        isnull(AvgSaleSYL, 0) AvgSaleSYL,
        isnull(AvgSaleTGL, 0) AvgSaleTGL,
        isnull(AvgSaleVRB, 0) AvgSaleVRB,
        --,ISNULL(CAST(((NationwideStock-Sales.ActualSalesMTD)/Sales.AvgSalesDay*3) AS INT), 0) as StockDays
        isnull(cast(TDCLCentralWH as int), 0) as [TDCL Central WH],
        ISNULL((BOG+ BSL+ COM+ COX+ CTG+ CTN+ DNJ+ FEN+ FRD+ GZP+ HZJ+JES+KHL+KRN+KSG + KUS + MHK+ MIR+ MLV+ MOT+ MYM + NAJ+ PAT + PBN+ RAJ
        + RNG + SAV + SYL + TGL+ VRB), 0) AS [Branch Total],
        ISNULL(CAST(BOG AS INT), 0) BOG,
        ISNULL(CAST(BSL AS INT), 0) BSL,
        ISNULL(CAST(COM AS INT), 0) COM,
        ISNULL(CAST(COX AS INT), 0) COX,
        ISNULL(CAST(CTG AS INT), 0) CTG,
        ISNULL(CAST(CTN AS INT), 0) CTN,
        ISNULL(CAST(DNJ AS INT), 0) DNJ,
        ISNULL(CAST(FEN AS INT), 0) FEN,
        ISNULL(CAST(FRD AS INT), 0) FRD,
        ISNULL(CAST(GZP AS INT), 0) GZP,
        ISNULL(CAST(HZJ AS INT), 0) HZJ,
        ISNULL(CAST(JES AS INT), 0) JES,
        ISNULL(CAST(KHL AS INT), 0) KHL,
        ISNULL(CAST(KRN AS INT), 0) KRN,
        ISNULL(CAST(KSG AS INT), 0) KSG,
        ISNULL(CAST(KUS AS INT), 0) KUS,
        ISNULL(CAST(MHK AS INT), 0) MHK,
        ISNULL(CAST(MIR AS INT), 0) MIR,
        ISNULL(CAST(MLV AS INT), 0) MLV,
        ISNULL(CAST(MOT AS INT), 0) MOT,
        ISNULL(CAST(MYM AS INT), 0) MYM,
        ISNULL(cast(NAJ AS INT), 0) NAJ,
        ISNULL(CAST(NOK AS INT), 0) NOK,
        ISNULL(CAST(PAT AS INT), 0) PAT,
        ISNULL(CAST(PBN AS INT), 0) PBN,
        ISNULL(CAST(RAJ AS INT), 0) RAJ,
        ISNULL(CAST(RNG AS INT), 0) RNG,
        ISNULL(CAST(SAV AS INT), 0) SAV,
        ISNULL(CAST(SYL AS INT), 0) SYL,
        ISNULL(CAST(TGL AS INT), 0) TGL,
        ISNULL(CAST(VRB AS INT), 0) VRB,
        ISNULL(CAST(oeorder.QTYordered AS INT), 0) [Total Ordered],
        ISNULL(EstimateSales, 0) [Estimated Sales]
        ,isnull(TRADEPRICE, 0) as TP, 
        isnull(Sales.YesterdaySales * TRADEPRICE, 0) as [TP Sales Value], 
        isnull(SalesVal, 0) as [Net Sales Value], 
        isnull((Sales.YesterdaySales * TRADEPRICE) - SalesVal, 0) as [Discount]
        
        from
        (select distinct ITEMNO,  TRADEPRICE ,[ITEMNAME] as Itemname, BRAND,PACKSIZE from PRINFOSKF where ITEMNO not like '9%'
        and BRAND IN (SELECT BRAND FROM GPMBRAND WHERE Name like ?)
        ) as ProductBrand
        Left join
        (
        SELECT ITEMNO,sum(QTY) as ST,sum(qty)/@TotalDays as STDay ,(sum(qty)/@TotalDays)*@MTDdays as MTDTarget 
        FROM ARCSECONDARY.dbo.RfieldForceProductTRG where YEARMONTH=@thismonth
        group by ITEMNO) as ItemTarget
        ON ProductBrand.ITEMNO=ItemTarget.ITEMNO
                        
        left join
        (select ITEM
        ,sum(case when transdate between @pdateTo and @pdateTo then QTYSHIPPED else 0 end ) as YesterdaySales
        ,sum(case when transdate between @firstday and @pdateTo then QTYSHIPPED else 0 end ) as ActualSalesMTD
        ,sum(case when transdate between @pdatefrom and @pdateTo then QTYSHIPPED else 0 end)/91  as AvgSalesDay
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='BOGSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleBOG
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='BSLSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleBSL
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='COMSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleCOM
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='COXSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleCOX
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='CTGSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleCTG
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='CTNSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleCTN
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='DNJSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleDNJ
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='FENSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleFEN
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='FRDSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleFRD
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='GZPSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleGZP
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='HZJSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleHZJ
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='JESSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleJES
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='KHLSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleKHL
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='KRNSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleKRN
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='KSGSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleKSG
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='KUSSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleKUS
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='MHKSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleMHK
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='MIRSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleMIR
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='MLVSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleMLV
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='MOTSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleMOT
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='MYMSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleMYM
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='NAJSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleNAJ
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='NOKSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleNOK
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='PATSKF'then QTYSHIPPED else 0 end)/91  as AvgSalePAT
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='PBNSKF'then QTYSHIPPED else 0 end)/91  as AvgSalePBN
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='RAJSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleRAJ
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='RNGSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleRNG
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='SAVSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleSAV
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='SYLSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleSYL
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='TGLSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleTGL
        ,sum(case when transdate between @pdatefrom and @pdateTo and  audtorg='VRBSKF'then QTYSHIPPED else 0 end)/91  as AvgSaleVRB
        ,sum(case when transdate = @pdateTo then EXTINVMISC else 0 end)  as SalesVal
        
                        
        from OESalesDetails where TRANSDATE between @pdatefrom and @pdateTo group by ITEM) as Sales
        on ProductBrand.ITEMNO=sales.ITEM
        left join (
        select ITEMNO,sum(QTYONHAND) as NationwideStock
        ,SUM(case when AUDTORG='MHKSKF' AND LOCATION = '000140' then QTYONHAND else 0 end) as TDCLCentralWH
        ,SUM(case when AUDTORG='BOGSKF' then QTYONHAND else 0 end) as BOG
        ,SUM(case when AUDTORG='BSLSKF' then QTYONHAND else 0 end) as BSL
        ,SUM(case when AUDTORG='COMSKF' then QTYONHAND else 0 end) as COM
        ,SUM(case when AUDTORG='COXSKF' then QTYONHAND else 0 end) as COX
        ,SUM(case when AUDTORG='CTGSKF' then QTYONHAND else 0 end) as CTG
        ,SUM(case when AUDTORG='CTNSKF' then QTYONHAND else 0 end) as CTN
        ,SUM(case when AUDTORG='DNJSKF' then QTYONHAND else 0 end) as DNJ
        ,SUM(case when AUDTORG='FENSKF' then QTYONHAND else 0 end) as FEN
        ,SUM(case when AUDTORG='FRDSKF' then QTYONHAND else 0 end) as FRD
        ,SUM(case when AUDTORG='GZPSKF' then QTYONHAND else 0 end) as GZP
        ,SUM(case when AUDTORG='HZJSKF' then QTYONHAND else 0 end) as HZJ
        ,SUM(case when AUDTORG='JESSKF' then QTYONHAND else 0 end) as JES
        ,SUM(case when AUDTORG='KHLSKF' then QTYONHAND else 0 end) as KHL
        ,SUM(case when AUDTORG='KRNSKF' then QTYONHAND else 0 end) as KRN
        ,SUM(case when AUDTORG='KSGSKF' then QTYONHAND else 0 end) as KSG
        ,SUM(case when AUDTORG='KUSSKF' then QTYONHAND else 0 end) as KUS
        ,SUM(case when AUDTORG='MHKSKF' then QTYONHAND else 0 end) as MHK
        ,SUM(case when AUDTORG='MIRSKF' then QTYONHAND else 0 end) as MIR
        ,SUM(case when AUDTORG='MLVSKF' then QTYONHAND else 0 end) as MLV
        ,SUM(case when AUDTORG='MOTSKF' then QTYONHAND else 0 end) as MOT
        ,SUM(case when AUDTORG='MYMSKF' then QTYONHAND else 0 end) as MYM
        ,SUM(case when AUDTORG='NAJSKF' then QTYONHAND else 0 end) as NAJ
        ,SUM(case when AUDTORG='NOKSKF' then QTYONHAND else 0 end) as NOK
        ,SUM(case when AUDTORG='PATSKF' then QTYONHAND else 0 end) as PAT
        ,SUM(case when AUDTORG='PBNSKF' then QTYONHAND else 0 end) as PBN
        ,SUM(case when AUDTORG='RAJSKF' then QTYONHAND else 0 end) as RAJ
        ,SUM(case when AUDTORG='RNGSKF' then QTYONHAND else 0 end) as RNG
        ,SUM(case when AUDTORG='SAVSKF' then QTYONHAND else 0 end) as SAV
        ,SUM(case when AUDTORG='SYLSKF' then QTYONHAND else 0 end) as SYL
        ,SUM(case when AUDTORG='TGLSKF' then QTYONHAND else 0 end) as TGL
        ,SUM(case when AUDTORG='VRBSKF' then QTYONHAND else 0 end) as VRB
                        
        from ICHistoricalStock where AUDTDATE= convert(varchar(8),getdate()-1,112) AND RIGHT(LOCATION,3) IN ('140','141')
        group by ITEMNO
        ) as Stock
        on ProductBrand.ITEMNO=Stock.ITEMNO
        left join
        (select ITEMNO,sum(case when [location] = ('4001') then QTYAVAIL else 0 end) as 'SKF Mirpur Plant',
        sum(case when [location] = ('4005') then QTYAVAIL else 0 end) as 'SKF Tongi Plant'
        ,sum(case when [location] = ('4016') then QTYAVAIL else 0 end) as 'SKF Rupganj Plant'
        from ICStockStatusCurrentLOT where [location] in ('4001','4005','4016') group by ITEMNO) as currentstock
        on ProductBrand.ITEMNO = currentstock.ITEMNO
                        
        left join
        (select item, SUM(QTYordered) as QTYordered, cast(SUM(QTYordered)*UNITPRICE as int) as EstimateSales from OEOrderDetails
        where ORDERDATE between convert(varchar(10),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),112) 
        and convert(varchar(8),getdate(), 112) 
        group by item, UNITPRICE
                        
        ) as OEOrder
        on Stock.itemno=oeorder.item
                
        """

    df = pd.read_sql_query(sql_queryes, conn.connection, params={gpm_name})
    df.to_excel('Data/gpm_data.xlsx', index=False)
    print('2. Master Dataset Created')

    data_for_html = pd.read_excel('./Data/gpm_data.xlsx')
    data = data_for_html[data_for_html['Avg Sales/Day'] != 0]

    html_data = data.drop(data.columns[[2]], axis=1)
    html_data.insert(loc=2, column='ISL NO', value=np.arange(len(html_data)) + 1)
    html_data.to_excel('./Data/html_data_Sales_and_Stock.xlsx', index=False)
    print('2.1. HTML dataset created for master table ')

    df = pd.read_excel('./Data/gpm_data.xlsx')
    df1 = df.drop(df.columns[[2]], axis=1)
    df0 = df1[df1['Avg Sales/Day'] != 0]
    df0.to_excel('Data/gpm_data1.xlsx', index=False)
    aa = pd.read_excel('./Data/gpm_data1.xlsx')
    aa.insert(loc=2, column='ISL NO', value=np.arange(len(df0)) + 1)
    aa = aa.drop(aa.columns[[18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                             41, 42, 43, 44, 45, 46, 47, 48, 82, 83]], axis=1)
    aa.to_excel('Data/Sales_and_Stock.xlsx', index=False)

    print('2.2. Sales and Stock Dataset Saved')

    df = pd.read_excel('./Data/gpm_data.xlsx')
    df1 = df.drop(df.columns[[2]], axis=1)
    df0 = df1[df1['Avg Sales/Day'] == 0]
    df0 = df0.drop(
        df0.columns[[18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                     41, 42, 43, 44, 45, 46, 47, 48]], axis=1)
    df0.to_excel('./Data/gpm_data1.xlsx', index=False)
    bb = pd.read_excel('./Data/gpm_data1.xlsx')
    bb.insert(loc=2, column='ISL NO', value=np.arange(len(df0)) + 1)
    bb = bb[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM']]
    bb.to_excel('Data/NoSales.xlsx', index=False)
    print('2.3. No sales Dataset Saved')

    all_data = pd.read_excel('./Data/gpm_data.xlsx')
    data = all_data[all_data['Nationwide Stock'] == 0]
    data = data.drop(data.columns[[2]], axis=1)
    data.insert(loc=2, column='ISL NO', value=np.arange(len(data)) + 1)
    noData = data[['BSL NO', 'BRAND', 'ISL NO', 'Item Name', 'UOM', 'Total Ordered', 'Estimated Sales']]
    noData.to_excel('Data/NoStock.xlsx', index=False)
    print('2.4. No Stock Data Saved\n')
