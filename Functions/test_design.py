import Functions.item_wise_yesterday_sales as yesterday
import Functions.no_sales_record as noSales
import Functions.no_stock_record as noStock
import Functions.read_gpm_info as gpm
import Functions.sales_and_stock_record as SalesStock

import Functions.branch_wise_stocks as branch_stock
import Functions.branch_stock_summery as bs
import Functions.item_wise_stock_days as item_day
import Functions.branch_wise_stock_aging as branch_aging
import Functions.aging_summary as aging_summary


def generate_layout(gpm_name):
    results = """ <!DOCTYPE html>
            <html>
            <head>
                <style>
                    table, th, td {
                        border: 1px solid black;
                        border-collapse: collapse;
                    }

                    table {
                        border: 1px solid black;
                        table-layout: fixed;
                        width: 20000px;
                    }

                    th, td {
                        border: 1px solid black;
                        width: 150px;
                        overflow: hidden;
                    }

                    .central{
                        text-align: center;
                    }

                    th.style1{
                        background-color: #e5f0e5;
                        padding-left: 2px;
                        padding-right: 5px;
                        text-align: right;
                    }
                    .style1{
                        padding-right: 3px;
                        text-align: right;


                    }
                    .number_style{
                        padding-right: 3px;
                        text-align: right;
                        font-size: 12px;   
                        height: 40px;
                    }

                    #number_style2{
                        padding-right: 3px;
                        text-align: right;
                        font-size: 10px;
                        height: 40px;   
                    }

                    .item_sl{
                        width: 60px !important; 
                        background-color: #e5f0e5;
                        padding-right: 3px;
                        text-align: center;
                    }
                    td.serial{
                        width: 60px !important;
                        padding-left: 5px;
                        text-align: center;
                        font-size: 12px;
                    }
                    serial1{
                        padding-left: 5px;
                        text-align: left;
                        font-size: 16px;
                    }
                    .sl_center{
                        padding-left: 5px;
                        text-align: center;
                        font-size: 12px;
                    }

                    #sss{

                        padding-left: 5px;
                        text-align: center;
                        font-size: 10px;
                    }
                    #ssstd{

                        padding-left: 3px;
                        padding-right: 3px;
                        text-align: right;
                        font-size: 10px;
                    }
                    #padding{

                        padding-left: 5px;
                        text-align: right;
                        font-size: 5px;
                    }

                    .serialno{
                        width: 30px !important;
                        padding-left: 5px;
                        text-align: center;
                        font-size: 12px;
                    }
                    .brand {
                        width: 70px !important;
                        background-color: #e5f0e5;
                        font-weight: bold;
                        color: black;
                        text-align: left;
                    }
                    .brandsl {
                        width: 30px !important;
                        background-color: #e5f0e5;
                        font-weight: bold;
                        color: black;
                        text-align: center;
                    }

                    .brandtd {
                        width: 50px !important;
                        text-align: left;
                        padding-left: 2px;
                        font-weight: bold;
                        font-size: 12px;
                        color: black;
                    }
                    .branch_name{
                        text-align: left;
                        padding-left: 2px;
                        font-weight: bold;
                        font-size: 14px;
                        color: black;
                    }

                    #btd {
                        width: 50px !important;
                        text-align: left;
                        padding-left: 2px;
                        font-weight: bold;
                        font-size: 12px;
                        color: black;
                    }

                    .brandtd1 {
                        width: 40px !important;
                        text-align: left;
                        padding-left: 2px;
                        font-weight: bold;
                        font-size: 14px;
                        color: black;

                    }
                    th.style2{
                        background-color: #faeaca;
                    }
                    .remaining{
                        background-color: #faeaca;
                        padding-left: 20px;
                    }
                    .sales_monthly_trend{
                     background-color: #faeaca;
                     padding-left: 20px;

                    }
                    .style3{
                        background-color: #f7e0b3;
                        padding-left: 5px;
                        padding-right: 2px;

                    }
                    td {
                        font-family: "Tohoma";
                        border: 1px solid gray;
                        font-size: 8px;

                    }
                    .branch_bg_color{
                        font-family: "Tohoma";
                        background-color: #a7c496;
                        padding-left: 5px;
                        color: black;
                        padding-right: 2px;
                        text-align: right;
                        font-size: 8px;

                    }
                    td.num_style {
                        text-align: right;
                        border: 1px solid gray;
                        padding-right: 5px;
                        font-size: 10px;
                    }
                    .color_style{
                        padding-left: 10px;
                        padding-top: 5px;
                        padding-bottom: 5px;
                        padding-right: 10px;
                        color: black;
                        width: 25%
                    }
                    .color_style{
                        width: 16.66%;
                        padding-left: 10px;
                        padding-top: 5px;
                        padding-bottom: 10px;
                        padding-right: 10px;
                        font-size: 14px;
                        font-weight: bolder;
                    }
                      .my_rotate {
                            color: red !important;
                      }
                    .nation_wide{

                        text-align: center;
                        padding-right: 2px;
                        border: 1px solid gray;
                        padding-left: 10px;
                        font-weight: bolder;
                        font-size: 12px;
                        color: black;
                    }
                    .description{
                        width: 900px !important;
                        background-color: #e5f0e5;
                        font-size: 12px;
                        color: black;
                    }
                    .description1{
                        width: 250px !important;
                        background-color: #e5f0e5;
                        font-size: 14px;
                        font-weight: bolder;
                        color: black;
                    }
                    .descriptionmain{
                        width: 250px !important;
                        font-size: 12px;
                        color: black;
                    }

                    #descriptionmain2{
                        width: 280px !important;
                        font-size: 10px;
                        color: black;
                    }

                    .y_desc_sales{
                        width: 250px !important;
                        font-size: 12px;
                        font-weight: bold;
                        color: black;
                    }

                    .grand_total{
                        font-size: 15px;
                        font-weight: bolder;
                        color: black;
                    }

                    .descriptiontd{
                        padding-left: 2px;
                        font-size: 14px;
                        font-weight: bolder;
                    }

                    .descriptionmastertd{
                        padding-left: 2px;
                        font-size: 9px;
                    }

                    .uom{
                        background-color: #e5f0e5;
                        font-size: 11px;
                        color: black;
                        padding-right: 2px;

                    }
                    .uom2{
                        text-align:right;
                        font-size: 10px;
                        color: black;
                    }
                    .uom3{
                        background-color: #faeaca;
                        
                        text-align:right;
                        font-size: 11px;
                        color: black;
                    }


                    .my_margin{
                    margin-right: 220px;
                    color: #E5F0E5 !important;
                    }
                    th.avg_sales{
                        width: 500px !important;
                        background-color: #e5f0e5;
                        font-size: 12px;
                        color: black;
                    }
                     td.avg_sales{
                        width: 100% !important;
                        padding-left:5px;
                    }
                    .remarks{
                    padding-left: 1px;
                    padding-right: 1px;
                    text-align: right;
                    font-size: 10px;
                    }

                    .remarks1{
                    padding-left: 1px;
                    padding-right: 1px;
                    text-align: left;
                    font-size: 10px;
                    }
                    .remarks2{
                    padding-left: 1px;
                    padding-right: 1px;
                    text-align: left;
                    font-size: 12px;
                    }
                    .info{
                        background-color: #a9f2e7;
                        font-size: 13px;
                        text-align: left;
                        text-decoration-line: none;
                        color: black;

                    }

                    .banner{
                    width: 800px !important;
                    height: 200px !important;
                    border: 1px solid #0f6674;
                    }

                .float_left {
                    width: 50%;
                    float: left;
                }

                .colors{
                    background-color: #b7fff8;
                    text-align: center;
                    padding-left: 2px;
                    padding-right: 2px;

                }

            .branch_plant_color{
                background-color: antiquewhite;
                padding-left: 2px;
                padding-right: 2px;
            }

                </style>

            </head>
            <body>
            
            <table border="1px solid gray" width='300%'> 
            <tr> 
                <th colspan='43' style=" background-color: #00ffbb; font-size: 20px; "> Region wise Item Sales : Yesterday</th> 
            </tr>
															
                    <tr>
                        <th class="brand" style="font-size: 14px;">  Brand</th>
                        <th  class="brandsl" style="font-size: 14px; text-align: center">SL</th>
                        <th  class="description" style="width:14%;font-weight: bolder;  left; font-size: 14px;">Item Description</th
                        <th class="uom" style="text-align: right;  font-size: 14px;"> BB</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> BJ</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> BN</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> CD</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> CG</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> CH</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> CL</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> CR</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> CS</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> CT</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> DB</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> DD</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> DK</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> DM</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> DS</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> DT</th> 
                        <th class="uom" style="text-align: right;  font-size: 14px;"> FK</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> FR</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> GK</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> JS</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> KB</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> KC</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> KN</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> MG</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> MH</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> ML</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> MS</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> ND</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> NM</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> PB</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> PS</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> RK</th>										
                        <th class="uom" style="text-align: right;  font-size: 14px;"> RN</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> SB</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> SM</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> SS</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> TJ</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> UM</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> WS</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;"> ZREGION</th>

                    </tr>
                  """ + yesterday.region_wise_yesterday_item_sales(gpm_name) + """
                </table>  <br> <br>

            </html>
        """
    return results

# # ------------  ---------
