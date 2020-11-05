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
    # print('GPM Salse and Stock dataset Start printing in HTML')
    tabletd = ""

    for i in range(1, sh.nrows):
        tabletd = tabletd + "<tr>\n"
        for j in range(0, 1):
            # BSL NO
            if (bslno[i - 1] != 0):
                tabletd = tabletd + "<td class=\"serial\" rowspan=\"" + str(bslno[i - 1]) + "\"> " + str(
                    int(sh.cell_value(i, j))) + "</td>\n"

        for j in range(1, 2):
            # Brand
            if (brand[i - 1] != 0):
                tabletd = tabletd + "<td class=\"brandtd\" rowspan=\"" + str(brand[i - 1]) + "\">" + str(
                    sh.cell_value(i, j)) + "</td>\n"

        for j in range(2, 3):
            # ITemNo
            tabletd = tabletd + "<td class=\"central\">" + str(int((sh.cell_value(i, j)))) + "</td>\n"

        for j in range(3, 4):
            # item name
            tabletd = tabletd + "<td class=\"description\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(4, 5):
            # unit
            tabletd = tabletd + "<td class=\"style1\">" + str((sh.cell_value(i, j))) + "</td>\n"

        for j in range(5, 6):
            # avg sales Day
            avg_sales = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(avg_sales))) + "</td>\n"

        for j in range(6, 7):
            # Monthly Sales Target
            msalestar = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(msalestar))) + "</td>\n"

        for j in range(7, 8):
            # MTD sales Target
            mtdsalestar = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(mtdsalestar))) + "</td>\n"

        for j in range(8, 9):
            # actual sales mtd
            mtdsales = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(mtdsales))) + "</td>\n"

        for j in range(9, 10):
            # MTD Sales Achv %
            mtd_salesacv = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(str(mtd_salesacv)) + '%' + "</td>\n"

        for j in range(10, 11):
            # Monthly Sales Achv %
            m_salesacv = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(str(m_salesacv)) + '%' + "</td>\n"

        for j in range(11, 12):
            # Monthly Sales Trend
            monthlytrend = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(monthlytrend))) + "</td>\n"

        for j in range(12, 13):
            # monthly sales trend acv
            monthlyachiv = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(monthlyachiv))) + "</td>\n"

        for j in range(13, 14):
            # RemaingStock
            RemaingStock = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(RemaingStock))) + "</td>\n"

        for j in range(14, 15):
            # NationwideStock
            NationwideStock = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"nation_wide\">" + str(ofn.number_style(str(NationwideStock))) + "</td>\n"

        for j in range(15, 16):
            # SKF Mirpur Plant
            mirpur = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(mirpur))) + "</td>\n"

        for j in range(16, 17):
            # SKF Rupganje
            Rupganje = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(Rupganje))) + "</td>\n"

        for j in range(17, 18):
            # SKF Tongi Plant
            tongi = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(tongi))) + "</td>\n"

        for j in range(18, 19):
            bog = int(sh.cell_value(i, j))
        for j in range(19, 20):
            bsl = int(sh.cell_value(i, j))
        for j in range(20, 21):
            com = int(sh.cell_value(i, j))
        for j in range(21, 22):
            cox = int(sh.cell_value(i, j))
        for j in range(22, 23):
            ctg = int(sh.cell_value(i, j))
        for j in range(23, 24):
            ctn = int(sh.cell_value(i, j))
        for j in range(24, 25):
            dnj = int(sh.cell_value(i, j))
        for j in range(25, 26):
            fen = int(sh.cell_value(i, j))
        for j in range(26, 27):
            frd = int(sh.cell_value(i, j))
        for j in range(27, 28):
            gzp = int(sh.cell_value(i, j))
        for j in range(28, 29):
            hzj = int(sh.cell_value(i, j))
        for j in range(29, 30):
            jes = int(sh.cell_value(i, j))
        for j in range(30, 31):
            khl = int(sh.cell_value(i, j))
        for j in range(31, 32):
            krn = int(sh.cell_value(i, j))
        for j in range(32, 33):
            ksg = int(sh.cell_value(i, j))
        for j in range(33, 34):
            kus = int(sh.cell_value(i, j))
        for j in range(34, 35):
            mhk = int(sh.cell_value(i, j))
        for j in range(35, 36):
            mir = int(sh.cell_value(i, j))
        for j in range(36, 37):
            mlv = int(sh.cell_value(i, j))
        for j in range(37, 38):
            mot = int(sh.cell_value(i, j))
        for j in range(38, 39):
            mym = int(sh.cell_value(i, j))
        for j in range(39, 40):
            naj = int(sh.cell_value(i, j))
        for j in range(40, 41):
            nok = int(sh.cell_value(i, j))
        for j in range(41, 42):
            pat = int(sh.cell_value(i, j))
        for j in range(42, 43):
            pbn = int(sh.cell_value(i, j))
        for j in range(43, 44):
            raj = int(sh.cell_value(i, j))
        for j in range(44, 45):
            rng = int(sh.cell_value(i, j))
        for j in range(45, 46):
            sav = int(sh.cell_value(i, j))
        for j in range(46, 47):
            syl = int(sh.cell_value(i, j))
        for j in range(47, 48):
            tgl = int(sh.cell_value(i, j))
        for j in range(48, 49):
            vrb = int(sh.cell_value(i, j))

        for j in range(49, 50):
            # TDCL Central
            tdcl_val = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(tdcl_val))) + "</td>\n"

        for j in range(50, 51):
            # Branch Total
            tdcl_val = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"num_style\">" + str(ofn.number_style(str(tdcl_val))) + "</td>\n"

        for j in range(51, 52):
            BOG = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(bog, BOG)) + "\">" + str(ofn.number_style(str(BOG))) + "</td>\n"

        for j in range(52, 53):
            BSL = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(bsl, BSL)) + "\">" + str(ofn.number_style(str(BSL))) + "</td>\n"

        for j in range(53, 54):
            COM = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(com, COM)) + "\">" + str(ofn.number_style(str(COM))) + "</td>\n"

        for j in range(54, 55):
            COX = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(cox, COX)) + "\">" + str(ofn.number_style(str(COX))) + "</td>\n"

        for j in range(55, 56):
            CTG = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(ctg, CTG)) + "\">" + str(ofn.number_style(str(CTG))) + "</td>\n"

        for j in range(56, 57):
            CTN = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(ctn, CTN)) + "\">" + str(ofn.number_style(str(CTN))) + "</td>\n"

        for j in range(57, 58):
            DNJ = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(dnj, DNJ)) + "\">" + str(ofn.number_style(str(DNJ))) + "</td>\n"

        for j in range(58, 59):
            FEN = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(fen, FEN)) + "\">" + str(ofn.number_style(str(FEN))) + "</td>\n"

        for j in range(59, 60):
            FRD = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(frd, FRD)) + "\">" + str(ofn.number_style(str(FRD))) + "</td>\n"

        for j in range(60, 61):
            GZP = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(gzp, GZP)) + "\">" + str(ofn.number_style(str(GZP))) + "</td>\n"

        for j in range(61, 62):
            HZJ = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(hzj, HZJ)) + "\">" + str(ofn.number_style(str(HZJ))) + "</td>\n"

        for j in range(62, 63):
            JES = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(jes, JES)) + "\">" + str(ofn.number_style(str(JES))) + "</td>\n"

        for j in range(63, 64):
            KHL = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(khl, KHL)) + "\">" + str(ofn.number_style(str(KHL))) + "</td>\n"

        for j in range(64, 65):
            KRN = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(krn, KRN)) + "\">" + str(ofn.number_style(str(KRN))) + "</td>\n"

        for j in range(65, 66):
            KSG = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(ksg, KSG)) + "\">" + str(ofn.number_style(str(KSG))) + "</td>\n"

        for j in range(66, 67):
            KUS = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(kus, KUS)) + "\">" + str(ofn.number_style(str(KUS))) + "</td>\n"

        for j in range(67, 68):
            MHK = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(mhk, MHK)) + "\">" + str(ofn.number_style(str(MHK))) + "</td>\n"

        for j in range(68, 69):
            MIR = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(mir, MIR)) + "\">" + str(ofn.number_style(str(MIR))) + "</td>\n"

        for j in range(69, 70):
            MLV = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(mlv, MLV)) + "\">" + str(ofn.number_style(str(MLV))) + "</td>\n"

        for j in range(70, 71):
            MOT = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(mot, MOT)) + "\">" + str(ofn.number_style(str(MOT))) + "</td>\n"

        for j in range(71, 72):
            MYM = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(mym, MYM)) + "\">" + str(ofn.number_style(str(MYM))) + "</td>\n"

        for j in range(72, 73):
            NAJ = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(naj, NAJ)) + "\">" + str(ofn.number_style(str(NAJ))) + "</td>\n"

        for j in range(73, 74):
            NOK = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(nok, NOK)) + "\">" + str(ofn.number_style(str(NOK))) + "</td>\n"

        for j in range(74, 75):
            PAT = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(pat, PAT)) + "\">" + str(ofn.number_style(str(PAT))) + "</td>\n"

        for j in range(75, 76):
            PBN = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(pbn, PBN)) + "\">" + str(ofn.number_style(str(PBN))) + "</td>\n"

        for j in range(76, 77):
            RAJ = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(raj, RAJ)) + "\">" + str(ofn.number_style(str(RAJ))) + "</td>\n"

        for j in range(77, 78):
            RNG = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(rng, RNG)) + "\">" + str(ofn.number_style(str(RNG))) + "</td>\n"

        for j in range(78, 79):
            SAV = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(sav, SAV)) + "\">" + str(ofn.number_style(str(SAV))) + "</td>\n"

        for j in range(79, 80):
            SYL = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + str(ofn.warning(
                syl, SYL)) + "\">" + str(ofn.number_style(str(SYL))) + "</td>\n"

        for j in range(80, 81):
            TGL = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(tgl, TGL)) + "\">" + str(ofn.number_style(str(TGL))) + "</td>\n"

        for j in range(81, 82):
            VRB = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(vrb, VRB)) + "\">" + str(ofn.number_style(str(VRB))) + "</td>\n"

        for j in range(82, 83):
            VRB = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
                      str(ofn.warning(vrb, VRB)) + "\">" + str(ofn.number_style(str(VRB))) + "</td>\n"

        table = tabletd + "</tr>\n"
    print("Master Table Created")
    return table
