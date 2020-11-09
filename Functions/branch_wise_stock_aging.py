import pyodbc as db
import pandas as pd
import Functions.operational_functionality as ofn
import xlrd

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')




def get_branch_aging_stock_status():
    df = pd.read_sql_query("""
        Select * from

        (select *
        from
        (
        Select * from
        (select  BRAND,ITEMNAME,AUDTORG, Max(AGEING) AS AGEING   from
        (select ITEMNO,AUDTORG,AGEING,QTYAVAIL,EXPIRYDATE from ICStockCurrent_Lot) as T1
        LEFT JOIN
        (select ITEMNO,ITEMNAME,BRAND,PACKSIZE,GPMNAME from PRINFOSKF)as T2
        ON (T1.ITEMNO=T2.ITEMNO)
        WHERE T2.GPMNAME = 'Mr. A. K. M. Nawajesh Hossain'
        Group by  BRAND,ITEMNAME,AUDTORG ) as T3
        ) src
        pivot
        (Max(AGEING)
        for AUDTORG in ([BOGSKF],[BSLSKF],[COMSKF],[COXSKF],[CTGSKF],[CTNSKF],[DNJSKF],[FENSKF],[FRDSKF],[GZPSKF],[HZJSKF],[JESSKF],[KHLSKF],[KRNSKF],[KSGSKF],[KUSSKF],[MHKSKF],[MIRSKF],[MLVSKF],[MOTSKF],[MYMSKF],[NAJSKF],[NOKSKF],[PATSKF],[PBNSKF],[RAJSKF],[RNGSKF],[SAVSKF],[SKFDAT],[SYLSKF],[TGLSKF],[VRBSKF]
         )) AS piv
        ) as TblAging
        left join
        (select *
        from
        (Select * from
        (select  BRAND,ITEMNAME,AUDTORG, Sum(QTYAVAIL) AS TotalStock   from
        (select ITEMNO,AUDTORG,AGEING,QTYAVAIL,EXPIRYDATE from ICStockCurrent_Lot) as T1
        LEFT JOIN
        (select ITEMNO,ITEMNAME,BRAND,PACKSIZE,GPMNAME from PRINFOSKF)as T2
        ON (T1.ITEMNO=T2.ITEMNO)
        WHERE T2.GPMNAME ='Mr. A. K. M. Nawajesh Hossain'
        Group by  BRAND,ITEMNAME,AUDTORG ) as T3
        ) src
        pivot
        (
        sum(TotalStock)
        for AUDTORG in ([BOGSKF],[BSLSKF],[COMSKF],[COXSKF],[CTGSKF],[CTNSKF],[DNJSKF],[FENSKF],[FRDSKF],[GZPSKF],[HZJSKF],[JESSKF],[KHLSKF],[KRNSKF],[KSGSKF],[KUSSKF],[MHKSKF],[MIRSKF],[MLVSKF],[MOTSKF],[MYMSKF],[NAJSKF],[NOKSKF],[PATSKF],[PBNSKF],[RAJSKF],[RNGSKF],[SAVSKF],[SKFDAT],[SYLSKF],[TGLSKF],[VRBSKF]
         )
        ) AS piv) as tblsStock
        on (tblsStock.ITEMNAME=TblAging.ITEMNAME) """, connection)

    df.to_excel('Data/branch_wise_aging_stock.xlsx', index=False)
    print('Aging Stock data saved')
    excel_data_df = pd.read_excel('Data/branch_wise_aging_stock.xlsx', sheet_name='Sheet1',
                                  usecols=['BRAND', 'ITEMNAME'])
    bslno = ofn.create_dup_count_list(excel_data_df, 'BRAND')
    brand = ofn.create_dup_count_list(excel_data_df, 'ITEMNAME')

    wb = xlrd.open_workbook('Data/branch_wise_aging_stock.xlsx')
    sh = wb.sheet_by_name('Sheet1')

    tabletd = ""

    for i in range(1, sh.nrows):
        tabletd = tabletd + "<tr>\n"
        for j in range(0, 1):
            # BSL NO
            if (bslno[i - 1] != 0):
                tabletd = tabletd + "<td class=\"serial\" rowspan=\"" + str(bslno[i - 1]) + "\"> " + str(
                    (sh.cell_value(i, j))) + "</td>\n"

        for j in range(1, 2):
            # Brand
            if (brand[i - 1] != 0):
                tabletd = tabletd + "<td class=\"brandtd\" rowspan=\"" + str(brand[i - 1]) + "\">" + str(
                    sh.cell_value(i, j)) + "</td>\n"

        for j in range(2, 3):
            bog = sh.cell_value(i, j)

        for j in range(3, 4):
            bsl = sh.cell_value(i, j)

        for j in range(4, 5):
            com = sh.cell_value(i, j)

        for j in range(5, 6):
            cox = sh.cell_value(i, j)

        for j in range(6, 7):
            ctg = sh.cell_value(i, j)

        for j in range(7, 8):
            ctn = sh.cell_value(i, j)

        for j in range(8, 9):
            dnj = sh.cell_value(i, j)

        for j in range(9, 10):
            fen = sh.cell_value(i, j)

        for j in range(10, 11):
            frd = sh.cell_value(i, j)

        for j in range(11, 12):
            gzp = sh.cell_value(i, j)

        for j in range(12, 13):
            hzj = sh.cell_value(i, j)

        for j in range(13, 14):
            jes = sh.cell_value(i, j)

        for j in range(14, 15):
            khl = sh.cell_value(i, j)

        for j in range(15, 16):
            krn = sh.cell_value(i, j)

        for j in range(16, 17):
            ksg = sh.cell_value(i, j)

        for j in range(17, 18):
            kus = sh.cell_value(i, j)

        for j in range(18, 19):
            mhk = sh.cell_value(i, j)

        for j in range(19, 20):
            mir = sh.cell_value(i, j)

        for j in range(20, 21):
            mlv = sh.cell_value(i, j)

        for j in range(21, 22):
            mot = sh.cell_value(i, j)

        for j in range(22, 23):
            mym = sh.cell_value(i, j)

        for j in range(23, 24):
            naj = sh.cell_value(i, j)

        for j in range(24, 25):
            nok = sh.cell_value(i, j)

        for j in range(25, 26):
            pat = sh.cell_value(i, j)

        for j in range(26, 27):
            pbn = sh.cell_value(i, j)

        for j in range(27, 28):
            raj = sh.cell_value(i, j)

        for j in range(28, 29):
            rng = sh.cell_value(i, j)

        for j in range(29, 30):
            sav = sh.cell_value(i, j)

        for j in range(47, 48):
            syl = sh.cell_value(i, j)

        for j in range(48, 49):
            tgl = sh.cell_value(i, j)

        for j in range(49, 50):
            vrb = sh.cell_value(i, j)


        for j in range(36, 37):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(bog)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(37, 38):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(bsl)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(38, 39):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(com)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(39, 40):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(cox)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(40, 41):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(ctg)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(41, 42):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(ctn)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(42, 43):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(dnj)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(43, 44):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(fen)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(44, 45):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(frd)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(45, 46):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(gzp)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(46, 47):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(hzj)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(47, 48):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(jes)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(48, 49):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(khl)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(49, 50):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(krn)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(50, 51):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(ksg)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(51, 52):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(kus)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(52, 53):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(mhk)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(53, 54):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(mir)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(54, 55):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(mlv)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(55, 56):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(mot)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(56, 57):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(mym)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(57, 58):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(naj)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(58, 59):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(nok)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(59, 60):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(pat)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(60, 61):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(pbn)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(61, 62):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(raj)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(62, 63):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(rng)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(63, 64):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(sav)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(65, 66):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(syl)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(66, 67):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(tgl)) + "\">"+ str(sh.cell_value(i, j)) + "</td>\n"

        for j in range(67, 68):
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.status_color(vrb)) + "\">" + str(sh.cell_value(i, j)) + "</td>\n"


        table = tabletd + "</tr>\n"
    print("Branch wise aging stock table Created")
    return table
