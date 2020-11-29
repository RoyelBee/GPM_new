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
                    }

                    #number_style2{
                        padding-right: 3px;
                        text-align: right;
                        font-size: 10px;   
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
                    <th colspan='38' style="background-color: #f5f681;text-align: center; font-size:20px;"> 
                    Brand Wise SKU Wise Stock Aging Report Status Summary : In between 90 Days to Expiry Days
                    </th> 
                </tr>
                    <tr>

                        <th rowspan="2" class="style1" style="text-align: left; width:8%;">Aging Days</th>
                        <th rowspan="2" class="style1" style="text-align: left;"> Product Brand </th>
                        <th rowspan="2" class="style1" style="width: 4%;text-align: center;">SL</th>
                        <th rowspan="2"class="style1" style="width: 20%;text-align: left;" >Item Description</th>
                        <th rowspan="2"class="style1">BOG</th>
                        <th rowspan="2"class="style1">BSL</th>
                        <th rowspan="2"class="style1">COM</th>
                        <th rowspan="2"class="style1">COX</th>
                        <th rowspan="2"class="style1">CTG</th>
                        <th rowspan="2"class="style1">CTN</th>
                        <th rowspan="2"class="style1">DNJ</th>
                        <th rowspan="2"class="style1">FEN</th>
                        <th rowspan="2"class="style1">FRD</th>
                        <th rowspan="2"class="style1">GZP</th>
                        <th rowspan="2"class="style1">HZJ</th>
                        <th rowspan="2"class="style1">JES</th>
                        <th rowspan="2"class="style1">KHL</th>
                        <th rowspan="2"class="style1">KRN</th>
                        <th rowspan="2"class="style1">KSG</th>
                        <th rowspan="2"class="style1">KUS</th>
                        <th rowspan="2"class="style1">MHK</th>
                        <th rowspan="2"class="style1">MIR</th>
                        <th rowspan="2"class="style1">MLV</th>
                        <th rowspan="2"class="style1">MOT</th>
                        <th rowspan="2"class="style1">MYM</th>
                        <th rowspan="2"class="style1">NAJ</th>
                        <th rowspan="2"class="style1">NOK</th>
                        <th rowspan="2"class="style1">PAT</th>
                        <th rowspan="2"class="style1">PBN</th>
                        <th rowspan="2"class="style1">RAJ</th>
                        <th rowspan="2"class="style1">RNG</th>
                        <th rowspan="2"class="style1">SAV</th>
                        <th rowspan="2"class="style1">SYL</th>
                        <th rowspan="2"class="style1">TGL</th>
                        <th rowspan="2"class="style1">VRB</th>
                        <th colspan="3" >SK+F Plant</th>


                   </tr>  
                   <tr> 
                        <th class="style1">Rupganj </th>
                        <th class="style1">Mirpur </th>
                        <th class="style1">Tongi </th>
                   </tr>



                 """ + aging_summary.aging_stock_summary_status(gpm_name) + """


            </table>  <br><br>


            

            <table border="1px solid gray" width='300%'>
                <tr> 
                    <th colspan='38' style="background-color: #f5f681;text-align: center; font-size:20px;"> Branch - Brand - SKU wise Stock Aging Status: Detailed</th> 
                </tr>
                    <tr>

                        <th rowspan="2"class="style1" style="text-align: center; width:8%;">SL</th>
                        <th rowspan="2" class="style1" style="text-align: left;"> Product Brand </th>
                        <th rowspan="2" class="style1" style="width: 5%;text-align: center;">SL</th>
                        <th rowspan="2"class="style1" style="width: 30%;text-align: left;" >Item Description</th>
                        <th rowspan="2"class="style1">BOG</th>
                        <th rowspan="2"class="style1">BSL</th>
                        <th rowspan="2"class="style1">COM</th>
                        <th rowspan="2"class="style1">COX</th>
                        <th rowspan="2"class="style1">CTG</th>
                        <th rowspan="2"class="style1">CTN</th>
                        <th rowspan="2"class="style1">DNJ</th>
                        <th rowspan="2"class="style1">FEN</th>
                        <th rowspan="2"class="style1">FRD</th>
                        <th rowspan="2"class="style1">GZP</th>
                        <th rowspan="2"class="style1">HZJ</th>
                        <th rowspan="2"class="style1">JES</th>
                        <th rowspan="2"class="style1">KHL</th>
                        <th rowspan="2"class="style1">KRN</th>
                        <th rowspan="2"class="style1">KSG</th>
                        <th rowspan="2"class="style1">KUS</th>
                        <th rowspan="2"class="style1">MHK</th>
                        <th rowspan="2"class="style1">MIR</th>
                        <th rowspan="2"class="style1">MLV</th>
                        <th rowspan="2"class="style1">MOT</th>
                        <th rowspan="2"class="style1">MYM</th>
                        <th rowspan="2"class="style1">NAJ</th>
                        <th rowspan="2"class="style1">NOK</th>
                        <th rowspan="2"class="style1">PAT</th>
                        <th rowspan="2"class="style1">PBN</th>
                        <th rowspan="2"class="style1">RAJ</th>
                        <th rowspan="2"class="style1">RNG</th>
                        <th rowspan="2"class="style1">SAV</th>
                        <th rowspan="2"class="style1">SYL</th>
                        <th rowspan="2"class="style1">TGL</th>
                        <th rowspan="2"class="style1">VRB</th>
                        <th colspan="3" >SK+F Plant</th>

                   </tr>  
                   <tr> 
                        <th class="style1">Rupganj </th>
                        <th class="style1">Mirpur </th>
                        <th class="style1">Tongi </th>
                   </tr>



                    </tr>  """ + branch_aging.get_branch_aging_stock_status(gpm_name) + """


            </table>  <br><br>

                <table border="1px solid black" style="width: 300%;">

    <tr>
        <th colspan='53' style="background-color: #f5f681;text-align: center; font-size:20px;"> Branch - Brand - SKU
            wise Stock Information: Detailed
        </th>
    </tr>
    <tr>
        <th colspan="20" class="info" style="text-align: left"> """ + gpm.getGPMNFullInfo(gpm_name) + """
        </th>
        <th rowspan="3" style="background-color: #fed8b1;font-size: 12px;text-align:center">
            <div>TDCL <br> Central <br> WH
            </div>
        </th>
        <th rowspan="3" style="background-color: #fed8b1; font-size: 12px;">Total <br> Branch  <br> Qty</th>
        <th colspan="5" style="background-color: #ff2300" class="color_style"> Nill</th>
        <th colspan="5" style="background-color: #ff971a" class="color_style">Super Under Stock</th>
        <th colspan="5" style="background-color: #eee298;" class="color_style">Under Stock</th>
        <th colspan="5" class="color_style">Normal Stock</th>
        <th colspan="5" style="background-color: #cbe14c; color: black" class="color_style">Over Stock</th>
        <th colspan="6" style="background-color: #fff900; color: black" class="color_style">Super Over Stock</th>
    </tr>

    <tr>
        <th rowspan="2" class="style1" style="font-size: 12px;background-color: #d7fed7;">SL &nbsp&nbsp</th>
        <th rowspan="2" class="brand" style="font-size: 12px;font-weight: bolder; background-color: #d7fed7;"> 
        Product Brand

        </th>
        <th rowspan="2" class="item_sl" style="font-size: 12px;background-color: #d7fed7;"> SL

        </th>
        <th rowspan="2" class="description" style="width:14%;font-weight: bolder; font-size: 12px;background-color: #d7fed7;text-align: 
        left;">Item
            <br> Description
        </th>
        <th rowspan="2" class="uom3" style="font-size: 12px;background-color: #d7fed7; text-align:left"> UOM</th>
        <th rowspan="2" class="colors" style="font-size: 12px;padding: 0;text-align: center;">LD <br> Sales
            <br>Qty
        </th>
        <th rowspan="2" class="colors" style="font-size: 12px;padding-left: 0;">Avg Sales/ <br> Day</th>
        <th rowspan="2" class="colors" style="font-size: 12px;padding-left: 0;">TM <br> Sales <br> Target
        </th>
        <th rowspan="2" class="colors" style="font-size: 12px;">
            <div>MTD <br> Sales <br> Target</div>
        </th>
        <th rowspan="2" class="colors" style="font-size: 12px;">
            <div>MTD <br> Sales <br> Actual</div>
        </th>
        <th rowspan="2" class="colors" style="font-size: 12px;">
            <div>MTD <br> Sales <br> Achv%</div>
        </th>
        <th rowspan="2" class="colors" style="font-size: 12px;">
            <div>TM <br>Sales <br> Achv%
            </div>
        </th>
        <th rowspan="2" class="colors" style="font-size: 12px;">
            <div>TM <br> Sales <br> Trend
            </div>
        </th>
        <th rowspan="2" class="colors" style="font-size: 12px;">
            <div>TM Trend <br> Achv%
            </div>
        </th>
        <th rowspan="2" class="remaining" style="font-size: 12px;padding-left: 0; background-color:#c8f22b ;">
            <div>Remaining<br> TM Sales <br> Qty
            </div>
        </th>
        <th rowspan="2" class="nation_wide" style="font-size: 12px;padding-left: 0;background-color:#f0e713;">
            <div>Nationwide <br> Total <br> Stock</div>
        </th>
        <th rowspan="2" class="nation_wide" style="font-size: 12px;padding-left: 0;background-color: #fed8b1;">
            <div>Total <br> SK+F <br> Qty</div>
        </th>
        <th colspan="3" style="font-weight: bolder; font-size: 12px;">SKF Plant</th>


        <th colspan="31" style="font-weight: bolder; font-size: 14px;"> TDCL Branches</th>
    </tr>
    <tr>
        <th class="branch_plant_color" rowspan="" style="font-size: 12px;text-align: center; ">Mirpur</th>
        <th class="branch_plant_color" rowspan="" style="font-size: 12px;text-align: center; ">Tongi</th>
        <th class="branch_plant_color" rowspan="" style="font-size: 12px;padding: 0; text-align: center; ">Rupganj</th>


        <th class="branch_plant_color" style="font-size:9px; ">BOG</th>
        <th class="branch_plant_color" style="font-size:9px; ">BSL</th>
        <th class="branch_plant_color" style="font-size:9px; ">COM</th>
        <th class="branch_plant_color" style="font-size:9px; ">COX</th>
        <th class="branch_plant_color" style="font-size:9px; ">CTG</th>
        <th class="branch_plant_color" style="font-size:9px; ">CTN</th>
        <th class="branch_plant_color" style="font-size:9px; "> DNJ</th>
        <th class="branch_plant_color" style="font-size:9px; ">FEN</th>
        <th class="branch_plant_color" style="font-size:9px; ">FRD</th>
        <th class="branch_plant_color" style="font-size:9px;">GZP</th>
        <th class="branch_plant_color" style="font-size:9px;">HZJ</th>
        <th class="branch_plant_color" style="font-size:9px;">JES</th>
        <th class="branch_plant_color" style="font-size:9px;">KHL</th>
        <th class="branch_plant_color" style="font-size:9px;">KRN</th>
        <th class="branch_plant_color" style="font-size:9px;">KSG</th>
        <th class="branch_plant_color" style="font-size:9px;">KUS</th>
        <th class="branch_plant_color" style="font-size:9px;">MHK</th>
        <th class="branch_plant_color" style="font-size:9px;">MIR</th>
        <th class="branch_plant_color" style="font-size:9px;">MLV</th>
        <th class="branch_plant_color" style="font-size:9px;">MOT</th>
        <th class="branch_plant_color" style="font-size:9px;">MYM</th>
        <th class="branch_plant_color" style="font-size:9px;">NAJ</th>
        <th class="branch_plant_color" style="font-size:9px;">NOK</th>
        <th class="branch_plant_color" style="font-size:9px;">PAT</th>
        <th class="branch_plant_color" style="font-size:9px;">PBN</th>
        <th class="branch_plant_color" style="font-size:9px;">RAJ</th>
        <th class="branch_plant_color" style="font-size:9px;">RNG</th>
        <th class="branch_plant_color" style="font-size:9px;">SAV</th>
        <th class="branch_plant_color" style="font-size:9px;">SYL</th>
        <th class="branch_plant_color" style="font-size:9px;">TGL</th>
        <th class="branch_plant_color" style="font-size:9px;">VRB</th>

    </tr>

                    """ + SalesStock.get_Sales_and_Stock_Records() + """
                </table> <br>


                </body>
            </html>
        """
    return results

# # ------------  ---------
