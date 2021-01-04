
-- Cumulative MTD Sales in value
select  right(TRANSDATE, 2) as Date, isnull(sum(EXTINVMISC),0) as ItemSales from OESalesDetails
left join PRINFOSKF
on OESalesDetails.ITEM = PRINFOSKF.ITEMNO
where left(TRANSDATE,6) = convert(varchar(6),getdate(), 112)
and PRINFOSKF.GPMNAME ='Mr. Mohammad Akhter Alam Khan'
and prinfoskf.BRAND in (select distinct brand from GPMBRAND where Name = 'Mr. Mohammad Akhter Alam Khan')
group by right(TRANSDATE, 2)
order by right(TRANSDATE, 2)


-- Cumulative MTD Target in value
Declare @CurrentMonth NVARCHAR(MAX);
Declare @DaysInMonth NVARCHAR(MAX);
SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
SET @DaysInMonth = DAY(EOMONTH(GETDATE()))
select  isnull(sum(VALUE),0)/@DaysInMonth as MonthsTargetQty
from ARCSECONDARY.dbo.RfieldForceProductTRG
left join PRINFOSKF
on RfieldForceProductTRG.ITEMNO = PRINFOSKF.ITEMNO
where YEARMONTH=CONVERT(varchar(6), dateAdd(month,0,getdate()), 112) and GPMNAME = 'Mr. Mohammad Akhter Alam Khan'
and prinfoskf.BRAND in (select distinct brand from GPMBRAND where Name = 'Mr. Mohammad Akhter Alam Khan')


-- Executive Sales Target - KPI 05 ------------------
Declare @CurrentMonth NVARCHAR(MAX);
Declare @DaysInMonth NVARCHAR(MAX);
Declare @DaysInMonthtilltoday NVARCHAR(MAX);
SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
SET @DaysInMonth = DAY(EOMONTH(GETDATE()))
SET @DaysInMonthtilltoday = right(convert(varchar(8), GETDATE(),112),2)

select exe_sales.ExecutiveName as ExecutiveName,exe_sales.shortname as shortname,exe_sales.ItemSales as ItemSales,
isnull(exe_target.MTDTargetVal, 0) as MTDTargetQty from
(select CP01 as ExecutiveName,b.[Executive ShortName] as shortname,cast(isnull(sum(EXTINVMISC),
0)/1000 as int) as ItemSales from OESalesDetails
left join PRINFOSKF
on OESalesDetails.ITEM = PRINFOSKF.ITEMNO
left join
(select * from GPMExecutive_ShortName) as b
on b.[ExecutiveName]=PRINFOSKF.cp01
where left(TRANSDATE,10) between  convert(varchar(10),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),112)
        and convert(varchar(10),getdate()-1, 112)
and PRINFOSKF.GPMNAME  = 'Mr. Mohammad Akhter Alam Khan'
and prinfoskf.BRAND in (select distinct brand from GPMBRAND where Name  = 'Mr. Mohammad Akhter Alam Khan')
group by CP01,b.[Executive ShortName]) as exe_sales
left join
(select CP01 as ExecutiveName, cast(((sum(VALUE)/@DaysInMonth)*@DaysInMonthtilltoday)/1000 as int) as MTDTargetVal
from PRINFOSKF
left join ARCSECONDARY.dbo.RfieldForceProductTRG
on RfieldForceProductTRG.ITEMNO = PRINFOSKF.ITEMNO
where YEARMONTH = CONVERT(varchar(6), dateAdd(month,0,getdate()),
112) and GPMNAME  = 'Mr. Mohammad Akhter Alam Khan'
and prinfoskf.BRAND in (select distinct brand from GPMBRAND where Name  = 'Mr. Mohammad Akhter Alam Khan')
group by CP01) as exe_target
on exe_sales.ExecutiveName = exe_target.ExecutiveName
order by exe_sales.ItemSales desc

------- executives_brand_target_sales_chart KPI 6 --------
DECLARE @cols NVARCHAR (MAX)

        SELECT @cols = COALESCE (@cols + ',[' + [executive shortname] + ']', '[' + [executive shortname] + ']')
                       FROM
                       (
                            select [executive shortname] from(
SELECT distinct [executive shortname] as [executive shortname], ExecutiveName from [dbo].[GPMExecutive_ShortName] a left join PRINFOSKF b
on a.ExecutiveName=b.CP01
where a.GPMNAME LIKE ? and b.BRAND in (select distinct brand from GPMBRAND where Name like ?)) as ttt) PV
                       ORDER BY [executive shortname]
        DECLARE @query NVARCHAR(MAX)
        SET @query ='Select * from
                (select *
                from
                (
        select b.[Executive ShortName] as exe,PRINFOSKF.brand as brand,sum(EXTINVMISC) as sale from OESalesDetails
left join PRINFOSKF
on OESalesDetails.ITEM = PRINFOSKF.ITEMNO
left join
(select * from GPMExecutive_ShortName) as b
on b.[ExecutiveName]=PRINFOSKF.cp01
where transtype =1 and transdate between convert(varchar(8),DATEADD(month, DATEDIFF(month, 0,  GETDATE()), 0),112) and
		 convert(varchar(8),getdate(), 112)
and prinfoskf.BRAND in (select distinct brand from GPMBRAND )
group by b.[Executive ShortName],PRINFOSKF.brand
                ) src
                pivot
                (Max(Sale)
               for EXE in (' + @cols + ')) AS piv
                ) as TblSale
                      left join
                    (select *
                from
        (
select [Executive ShortName] as Exe,prinfoskf.brand as brand, sum(TRGVAL)/ DAY(EOMONTH(GETDATE()))*RIGHT(convert(varchar(8),getdate()-1, 112),2) as Target
from PRINFOSKF
left join ARCSECONDARY.dbo.[PRODUCT_WISE_TRG]
on [PRODUCT_WISE_TRG].ITEM = PRINFOSKF.ITEMNO
 left join
        (select distinct [Executive ShortName],ExecutiveName from [GPMExecutive_ShortName]) as Exe on
        exe.ExecutiveName=PRINFOSKF.cp01
where yrm=CONVERT(varchar(6), dateAdd(month,0,getdate()),
112)
and prinfoskf.BRAND in (select distinct brand from GPMBRAND )
group by [Executive ShortName],prinfoskf.brand

                ) src
                pivot
                (
                sum(Target)
                for EXE in (' + @cols + '
                 )
                ) AS piv) as tblsTarget
                on (tblsTarget.brand=TblSale.brand)'

        EXEC SP_EXECUTESQL @query