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

    wb2 = xlrd.open_workbook('Data/item_wise_stock_days.xlsx')
    sh2 = wb2.sheet_by_name('Sheet1')

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
            # NationwideStock
            NationwideStock = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td class=\"nation_wide\">" + str(ofn.number_style(str(NationwideStock))) + "</td>\n"

        for j in range(16, 17):
            # SKF Mirpur Plant
            mirpur = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(mirpur))) + "</td>\n"

        for j in range(17, 18):
            # SKF Rupganje
            Rupganje = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(Rupganje))) + "</td>\n"

        for j in range(18, 19):
            # SKF Tongi Plant
            tongi = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(tongi))) + "</td>\n"

        for j in range(19, 20):
            bog = int(sh.cell_value(i, j))

        for j in range(20, 21):
            bsl = int(sh.cell_value(i, j))

        for j in range(21, 22):
            com = int(sh.cell_value(i, j))

        for j in range(22, 23):
            cox = int(sh.cell_value(i, j))

        for j in range(23, 24):
            ctg = int(sh.cell_value(i, j))

        for j in range(24, 25):
            ctn = int(sh.cell_value(i, j))

        for j in range(25, 26):
            dnj = int(sh.cell_value(i, j))

        for j in range(26, 27):
            fen = int(sh.cell_value(i, j))

        for j in range(27, 28):
            frd = int(sh.cell_value(i, j))

        for j in range(28, 29):
            gzp = int(sh.cell_value(i, j))

        for j in range(29, 30):
            hzj = int(sh.cell_value(i, j))

        for j in range(30, 31):
            jes = int(sh.cell_value(i, j))

        for j in range(31, 32):
            khl = int(sh.cell_value(i, j))

        for j in range(32, 33):
            krn = int(sh.cell_value(i, j))

        for j in range(33, 34):
            ksg = int(sh.cell_value(i, j))

        for j in range(34, 35):
            kus = int(sh.cell_value(i, j))

        for j in range(35, 36):
            mhk = int(sh.cell_value(i, j))

        for j in range(36, 37):
            mir = int(sh.cell_value(i, j))

        for j in range(37, 38):
            mlv = int(sh.cell_value(i, j))

        for j in range(38, 39):
            mot = int(sh.cell_value(i, j))

        for j in range(39, 40):
            mym = int(sh.cell_value(i, j))

        for j in range(40, 41):
            naj = int(sh.cell_value(i, j))

        for j in range(41, 42):
            nok = int(sh.cell_value(i, j))

        for j in range(42, 43):
            pat = int(sh.cell_value(i, j))

        for j in range(43, 44):
            pbn = int(sh.cell_value(i, j))

        for j in range(44, 45):
            raj = int(sh.cell_value(i, j))

        for j in range(45, 46):
            rng = int(sh.cell_value(i, j))

        for j in range(46, 47):
            sav = int(sh.cell_value(i, j))

        for j in range(47, 48):
            syl = int(sh.cell_value(i, j))

        for j in range(48, 49):
            tgl = int(sh.cell_value(i, j))

        for j in range(49, 50):
            vrb = int(sh.cell_value(i, j))

        for j in range(50, 51):
            # TDCL Central
            tdcl_val = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(tdcl_val))) + "</td>\n"

        for j in range(51, 52):
            # Branch Total
            tdcl_val = int(sh.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\">" + str(ofn.number_style(str(tdcl_val))) + "</td>\n"

        for j in range(52, 53):
            bog1 = int(sh.cell_value(i, j))

        for j in range(53, 54):
            bsl1 = int(sh.cell_value(i, j))

        for j in range(54, 55):
            com1 = int(sh.cell_value(i, j))

        for j in range(55, 56):
            cox1 = int(sh.cell_value(i, j))

        for j in range(56, 57):
            ctg1 = int(sh.cell_value(i, j))

        for j in range(57, 58):
            ctn1 = int(sh.cell_value(i, j))

        for j in range(58, 59):
            dnj1 = int(sh.cell_value(i, j))

        for j in range(59, 60):
            fen1 = int(sh.cell_value(i, j))

        for j in range(60, 61):
            frd1 = int(sh.cell_value(i, j))

        for j in range(61, 62):
            gzp1 = int(sh.cell_value(i, j))

        for j in range(62, 63):
            hzj1 = int(sh.cell_value(i, j))

        for j in range(63, 64):
            jes1 = int(sh.cell_value(i, j))

        for j in range(64, 65):
            khl1 = int(sh.cell_value(i, j))

        for j in range(65, 66):
            krn1 = int(sh.cell_value(i, j))

        for j in range(66, 67):
            ksg1 = int(sh.cell_value(i, j))

        for j in range(67, 68):
            kus1 = int(sh.cell_value(i, j))

        for j in range(68, 69):
            mhk1 = int(sh.cell_value(i, j))

        for j in range(69, 70):
            mir1 = int(sh.cell_value(i, j))

        for j in range(70, 71):
            mlv1 = int(sh.cell_value(i, j))

        for j in range(71, 72):
            mot1 = int(sh.cell_value(i, j))

        for j in range(72, 73):
            mym1 = int(sh.cell_value(i, j))

        for j in range(73, 74):
            naj1 = int(sh.cell_value(i, j))

        for j in range(74, 75):
            nok1 = int(sh.cell_value(i, j))

        for j in range(75, 76):
            pat1 = int(sh.cell_value(i, j))

        for j in range(76, 77):
            pbn1 = int(sh.cell_value(i, j))

        for j in range(77, 78):
            raj1 = int(sh.cell_value(i, j))

        for j in range(78, 79):
            rng1 = int(sh.cell_value(i, j))

        for j in range(79, 80):
            sav1 = int(sh.cell_value(i, j))

        for j in range(80, 81):
            syl1 = int(sh.cell_value(i, j))

        for j in range(82, 83):
            tgl1 = int(sh.cell_value(i, j))

        for j in range(83, 84):
            vrb1 = int(sh.cell_value(i, j))

        for j in range(5, 6):
            BOG = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(bog,bog1, BOG)) + "\">" + str(BOG) + "</td>\n"

        for j in range(6, 7):
            BSL = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\" style=\"background-color:" + \
                      str(ofn.warning(bsl,bsl1, BSL)) + "\">" + str(BSL) + "</td>\n"

        for j in range(7, 8):
            COM = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(com,com1, COM)) + "\">" + str(COM) + "</td>\n"

        for j in range(8, 9):
            COX = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(cox,cox1, COX)) + "\">" + str(COX) + "</td>\n"

        for j in range(9, 10):
            CTG = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(ctg,ctg1, CTG)) + "\">" + str(CTG) + "</td>\n"

        for j in range(10, 11):
            CTN = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(ctn,ctn1, CTN)) + "\">" + str(CTN) + "</td>\n"

        for j in range(11, 12):
            DNJ = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(dnj,dnj1, DNJ)) + "\">" + str(DNJ) + "</td>\n"

        for j in range(12, 13):
            FEN = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(fen,fen1, FEN)) + "\">" + str(FEN) + "</td>\n"

        for j in range(13, 14):
            FRD = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(frd,frd1, FRD)) + "\">" + str(FRD) + "</td>\n"

        for j in range(14, 15):
            GZP = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(gzp,gzp1, GZP)) + "\">" + str(GZP)+ "</td>\n"

        for j in range(15, 16):
            HZJ = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(hzj,hzj1, HZJ)) + "\">" + str(HZJ) + "</td>\n"

        for j in range(16, 17):
            JES = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(jes,jes1, JES)) + "\">" + str(JES)+ "</td>\n"

        for j in range(17,18):
            KHL = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(khl,khl1, KHL)) + "\">" + str(KHL) + "</td>\n"

        for j in range(18, 19):
            KRN = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(krn,krn1, KRN)) + "\">" + str(KRN) + "</td>\n"

        for j in range(19, 20):
            KSG = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(ksg,ksg1, KSG)) + "\">" + str(KSG) + "</td>\n"

        for j in range(20, 21):
            KUS = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(kus,kus1, KUS)) + "\">" + str(KUS) + "</td>\n"

        for j in range(21, 22):
            MHK = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(mhk,mhk1, MHK)) + "\">" + str(MHK) + "</td>\n"

        for j in range(22, 23):
            MIR = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(mir,mir1, MIR)) + "\">" + str(MIR) + "</td>\n"

        for j in range(23, 24):
            MLV = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(mlv,mlv1, MLV)) + "\">" + str(MLV)+ "</td>\n"

        for j in range(24, 25):
            MOT = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(mot,mot1, MOT)) + "\">" + str(MOT) + "</td>\n"

        for j in range(25, 26):
            MYM = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(mym,mym1, MYM)) + "\">" + str(MYM) + "</td>\n"

        for j in range(26, 27):
            NAJ = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(naj,naj1, NAJ)) + "\">" + str(NAJ)+ "</td>\n"

        for j in range(27, 28):
            NOK = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(nok,nok1, NOK)) + "\">" + str(NOK)+ "</td>\n"

        for j in range(28, 29):
            PAT = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(pat,pat1, PAT)) + "\">" + str(PAT) + "</td>\n"

        for j in range(29, 30):
            PBN = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(pbn,pbn1, PBN)) + "\">" + str(PBN) + "</td>\n"

        for j in range(30, 31):
            RAJ = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(raj,raj1, RAJ)) + "\">" + str(RAJ)+ "</td>\n"

        for j in range(31, 32):
            RNG = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(rng,rng1, RNG)) + "\">" + str(RNG) + "</td>\n"

        for j in range(32, 33):
            SAV = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(sav,sav1, SAV)) + "\">" + str(SAV) + "</td>\n"

        for j in range(33, 34):
            SYL = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + str(ofn.warning(
                syl,syl1, SYL)) + "\">" + str(SYL) + "</td>\n"

        for j in range(34, 35):
            TGL = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(tgl,tgl1, TGL)) + "\">" + str(TGL) + "</td>\n"

        for j in range(35, 36):
            VRB = str(sh2.cell_value(i, j))
            tabletd = tabletd + "<td id=\"number_style2\"style=\"background-color:" + \
                      str(ofn.warning(vrb,vrb1, VRB)) + "\">" + str(VRB)+ "</td>\n"

        # for j in range(83, 84):
        #     VRB = int(sh.cell_value(i, j))
        #     tabletd = tabletd + "<td class=\"remarks\"style=\"background-color:" + \
        #               str(ofn.warning(vrb, VRB)) + "\">" + str(ofn.number_style(str(VRB))) + "</td>\n"

        table = tabletd + "</tr>\n"
    print("Master Table Created")
    return table

