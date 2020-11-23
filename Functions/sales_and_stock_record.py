import pandas as pd
import xlrd

import Functions.operational_functionality as ofn

def get_Sales_and_Stock_Records():
    excel_data_df = pd.read_excel('Data/html_data_Sales_and_Stock.xlsx', sheet_name='Sheet1',
                                  usecols=['BSL NO', 'BRAND'])
    bslno = ofn.create_dup_count_list(excel_data_df, 'BSL NO')
    brand = ofn.create_dup_count_list(excel_data_df, 'BRAND')

    wb = xlrd.open_workbook('Data/html_data_Sales_and_Stock.xlsx')
    sh = wb.sheet_by_name('Sheet1')

    # wb2 = xlrd.open_workbook('Data/item_wise_stock_days.xlsx')
    # sh = wb2.sheet_by_name('Sheet1')

    # print('GPM Salse and Stock dataset Start printing in HTML')
    tabletd = ""

    for i in range(1, sh.nrows):
        tabletd = tabletd + "<tr>\n"
        for j in range(0, 1):
            # BSL NO
            if (bslno[i - 1] != 0):
                tabletd = tabletd + "<td id=\"sss\" rowspan=\"" + str(bslno[i - 1]) + "\"> " + str(
                    int(sh.cell_value(i, j))) + "</td>\n"

        for j in range(1, 2):
            # Brand
            if (brand[i - 1] != 0):
                tabletd = tabletd + "<td id=\"btd\" rowspan=\"" + str(brand[i - 1]) + "\">" + str(
                    sh.cell_value(i, j)) + "</td>\n"

        for j in range(2, 3):
            # ITemNo
            tabletd = tabletd + "<td id=\"sss\">" + str(int((sh.cell_value(i, j)))) + "</td>\n"

        for j in range(3, 4):
            # item name
            tabletd = tabletd + "<td id=\"descriptionmain2\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(4, 5):
            # unit
            tabletd = tabletd + "<td id=\"number_style2\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(5, 6):
            # avg sales Day
            avg_sales = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(avg_sales))) + "</td>\n"

        for j in range(6, 7):
            # Monthly Sales Target
            msalestar = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(msalestar))) + "</td>\n"

        for j in range(7, 8):
            # MTD sales Target
            mtdsalestar = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(mtdsalestar))) + "</td>\n"

        for j in range(8, 9):
            # actual sales mtd
            mtdsales = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(mtdsales))) + "</td>\n"

        for j in range(9, 10):
            # actual sales mtd
            mtdsales = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(mtdsales))) + "</td>\n"

        for j in range(10, 11):
            # MTD Sales Achv %
            mtd_salesacv = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(str(mtd_salesacv)) + '%' + "</td>\n"

        for j in range(11, 12):
            # Monthly Sales Achv %
            m_salesacv = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(str(m_salesacv)) + '%' + "</td>\n"

        for j in range(12, 13):
            # Monthly Sales Trend
            monthlytrend = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(monthlytrend))) + "</td>\n"

        for j in range(13, 14):
            # monthly sales trend acv
            monthlyachiv = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(monthlyachiv))) + "</td>\n"

        for j in range(14, 15):
            # RemaingStock
            RemaingStock = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(RemaingStock))) + "</td>\n"

        for j in range(15, 16):
            NationwideStock = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"sss\">" + str(ofn.number_style(str(NationwideStock))) + "</td>\n"

        for j in range(16, 17):
            totalskfqty = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"sss\">" + str(ofn.number_style(str(totalskfqty))) + "</td>\n"


        for j in range(17, 18):
            # SKF Mirpur Plant
            mirpur = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(mirpur))) + "</td>\n"

        for j in range(18, 19):
            # SKF Rupganje
            Rupganje = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(Rupganje))) + "</td>\n"

        for j in range(19, 20):
            # SKF Tongi Plant
            tongi = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(tongi))) + "</td>\n"

        for j in range(20, 21):
            bog = sh.cell_value(i, j)

        for j in range(21, 22):
            bsl = sh.cell_value(i, j)

        for j in range(22, 23):
            com = sh.cell_value(i, j)

        for j in range(23, 24):
            cox = sh.cell_value(i, j)

        for j in range(24, 25):
            ctg = sh.cell_value(i, j)

        for j in range(25, 26):
            ctn = sh.cell_value(i, j)

        for j in range(26, 27):
            dnj = sh.cell_value(i, j)

        for j in range(27, 28):
            fen = sh.cell_value(i, j)

        for j in range(28, 29):
            frd = sh.cell_value(i, j)

        for j in range(29, 30):
            gzp = sh.cell_value(i, j)

        for j in range(30, 31):
            hzj = sh.cell_value(i, j)

        for j in range(31, 32):
            jes = sh.cell_value(i, j)

        for j in range(32, 33):
            khl = sh.cell_value(i, j)

        for j in range(33, 34):
            krn = sh.cell_value(i, j)

        for j in range(34, 35):
            ksg = sh.cell_value(i, j)

        for j in range(35, 36):
            kus = sh.cell_value(i, j)

        for j in range(36, 37):
            mhk = sh.cell_value(i, j)

        for j in range(37, 38):
            mir = sh.cell_value(i, j)

        for j in range(38, 39):
            mlv = sh.cell_value(i, j)

        for j in range(39, 40):
            mot = sh.cell_value(i, j)

        for j in range(40, 41):
            mym = sh.cell_value(i, j)

        for j in range(41, 42):
            naj = sh.cell_value(i, j)

        for j in range(42, 43):
            nok = sh.cell_value(i, j)

        for j in range(43, 44):
            pat = sh.cell_value(i, j)

        for j in range(44, 45):
            pbn = sh.cell_value(i, j)

        for j in range(45, 46):
            raj = sh.cell_value(i, j)

        for j in range(46, 47):
            rng = sh.cell_value(i, j)

        for j in range(47, 48):
            sav = sh.cell_value(i, j)

        for j in range(48, 49):
            syl = sh.cell_value(i, j)

        for j in range(49, 50):
            tgl = sh.cell_value(i, j)

        for j in range(50, 51):
            vrb = sh.cell_value(i, j)

        for j in range(51, 52):
            # TDCL Central
            tdcl_val = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(tdcl_val))) + "</td>\n"

        for j in range(52, 53):
            # Branch Total
            tdcl_val = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(tdcl_val))) + "</td>\n"


        for j in range(53, 54):
            BOG = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(bog, BOG)) + "\">" + ofn.day_calculator(bog, BOG) + "</td>\n"

        for j in range(54, 55):
            BSL = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\" style=\"background-color:" + \
                      str(ofn.warning(bsl, BSL)) + "\">" + ofn.day_calculator(bsl, BSL) + "</td>\n"

        for j in range(55, 56):
            COM = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(com, COM)) + "\">" + ofn.day_calculator(com, COM)  + "</td>\n"

        for j in range(56, 57):
            COX = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(cox, COX)) + "\">" + ofn.day_calculator(cox, COX) + "</td>\n"

        for j in range(57, 58):
            CTG = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(ctg, CTG)) + "\">" + ofn.day_calculator(ctg, CTG) + "</td>\n"

        for j in range(58, 59):
            CTN = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(ctn, CTN)) + "\">" + ofn.day_calculator(ctn, CTN) + "</td>\n"

        for j in range(59, 60):
            DNJ = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(dnj, DNJ)) + "\">" + ofn.day_calculator(dnj, DNJ) + "</td>\n"

        for j in range(60, 61):
            FEN = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(fen, FEN)) + "\">" + ofn.day_calculator(fen, FEN) + "</td>\n"

        for j in range(61, 62):
            FRD = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(frd, FRD)) + "\">" + ofn.day_calculator(frd, FRD) + "</td>\n"

        for j in range(62, 63):
            GZP = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(gzp, GZP)) + "\">" + ofn.day_calculator(gzp, GZP) + "</td>\n"

        for j in range(63, 64):
            HZJ = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(hzj, HZJ)) + "\">" + ofn.day_calculator(hzj, HZJ) + "</td>\n"

        for j in range(64, 65):
            JES = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(jes, JES)) + "\">" + ofn.day_calculator(jes, JES) + "</td>\n"

        for j in range(65, 66):
            KHL = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(khl, KHL)) + "\">" + ofn.day_calculator(khl, KHL) + "</td>\n"

        for j in range(66, 67):
            KRN = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(krn, KRN)) + "\">" + ofn.day_calculator(krn, KRN) + "</td>\n"

        for j in range(67, 68):
            KSG = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(ksg, KSG)) + "\">" + ofn.day_calculator(ksg, KSG) + "</td>\n"

        for j in range(68, 69):
            KUS = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(kus, KUS)) + "\">" + ofn.day_calculator(kus, KUS) + "</td>\n"

        for j in range(69, 70):
            MHK = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(mhk, MHK)) + "\">" + ofn.day_calculator(mhk, MHK) + "</td>\n"

        for j in range(70, 71):
            MIR = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(mir, MIR)) + "\">" + ofn.day_calculator(mir, MIR) + "</td>\n"

        for j in range(71, 72):
            MLV = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(mlv, MLV)) + "\">" + ofn.day_calculator(mlv, MLV) + "</td>\n"

        for j in range(72, 73):
            MOT = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(mot, MOT)) + "\">" + ofn.day_calculator(mot, MOT) + "</td>\n"

        for j in range(73, 74):
            MYM = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(mym, MYM)) + "\">" + ofn.day_calculator(mym, MYM) + "</td>\n"

        for j in range(74, 75):
            NAJ = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(naj, NAJ)) + "\">" + ofn.day_calculator(naj, NAJ) + "</td>\n"

        for j in range(75, 76):
            NOK = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(nok, NOK)) + "\">" + ofn.day_calculator(nok, NOK) + "</td>\n"

        for j in range(76, 77):
            PAT = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(pat, PAT)) + "\">" + ofn.day_calculator(pat, PAT) + "</td>\n"

        for j in range(77, 78):
            PBN = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(pbn, PBN)) + "\">" + ofn.day_calculator(pbn, PBN) + "</td>\n"

        for j in range(78, 79):
            RAJ = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(raj, RAJ)) + "\">" + ofn.day_calculator(raj, RAJ) + "</td>\n"

        for j in range(79, 80):
            RNG = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(rng, RNG)) + "\">" + ofn.day_calculator(rng, RNG) + "</td>\n"

        for j in range(80, 81):
            SAV = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(sav, SAV)) + "\">" + ofn.day_calculator(sav, SAV) + "</td>\n"

        for j in range(81, 82):
            SYL = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(syl, SYL)) + "\">" + ofn.day_calculator(syl, SYL) + "</td>\n"

        for j in range(82, 83):
            TGL = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(tgl, TGL)) + "\">" + ofn.day_calculator(tgl, TGL) + "</td>\n"

        for j in range(83, 84):
            VRB = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(vrb, VRB)) + "\">" + ofn.day_calculator(vrb, VRB) + "</td>\n"

        # for j in range(83, 84):
        #     VRB = int(sh.cell_value(i, j))
        #     tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
        #               str(ofn.warning(vrb, VRB)) + "\">" + str(ofn.number_style(str(VRB))) + "</td>\n"

        table = tabletd + "</tr>\n"
    print("18. Master Details Table Created")
    return table

