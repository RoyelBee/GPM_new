import Functions.item_wise_yesterday_sales as yesterday
import Functions.no_sales_record as noSales
import Functions.no_stock_record as noStock
import Functions.read_gpm_info as gpm
import Functions.sales_and_stock_record as SalesStock

import Functions.branch_wise_stocks as branch_stock
import Functions.branch_stock_summery as bs
import Functions.item_wise_stock_days as item_day
import Functions.branch_wise_stock_aging as branch_aging


def generate_layout(gpm_name):
    # print('GPM Name  = ', gpm_name)
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
                    
                    .item_sl{
                        width: 60px !important; 
                        background-color: #e5f0e5;
                        padding-right: 3px;
                        text-align: center;
                    }
                    td.serial{
                        width: 60px !important;
                        padding-left: 5px;
                        text-align: left;
                        font-size: 12px;
                    }
                    .serialno{
                        width: 30px !important;
                        padding-left: 5px;
                        text-align: left;
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
                        text-align: left;
                    }
                    
                    .brandtd {
                        width: 50px !important;
                        text-align: left;
                        padding-left: 2px;
                        font-weight: bold;
                        font-size: 14px;
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
                        background-color: #ddd9d9;
                        text-align: right;
                        padding-right: 2px;
                        border: 1px solid gray;
                        padding-left: 10px;
                        font-weight: bolder;
                        font-size: 12px;
                        color: black;
                    }
                    th.description{
                        width: 900px !important;
                        background-color: #e5f0e5;
                        font-size: 12px;
                        color: black;
                    }
                    .description1{
                        width: 250px !important;
                        background-color: #e5f0e5;
                        font-size: 12px;
                        color: black;
                    }
                    
                    .y_desc_sales{
                        width: 250px !important;
                        font-size: 12px;
                        color: black;
                    }
                    
                    .grand_total{
                        font-size: 15px;
                        font-weight: bolder;
                        color: black;
                    }
                    
                    .descriptiontd{
                        padding-left: 2px;
                        font-size: 12px;
                    }
                    
                    .uom{
                        background-color: #e5f0e5;
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



                </style>

            </head>
            <body>
                <img src="cid:banner_ai" width="90%"> <br>
                <img src="cid:dash" width="90%"> <br>
                <img src="cid:cm" width="90%"> <br>
                <img src="cid:executive" width="90%"> <br>
                <img src="cid:brand"> <br> <br>
                <img src="cid:aging" width="100%"> <br> <br>
                
            <table border="1px solid gray" width="200%">
               <tr>  
               <th colspan='6' style="background-color: #f40d0d;text-align: center; font-size:14px;"> Within 15 
                    Days </th> 
                    <th colspan='6' style="background-color: #ff8600;text-align: center; font-size:14px;"> Within 30 
                    Days </th> 
                    <th colspan='6' style="background-color: #e1e300;text-align: center; font-size:14px;"> Within 60 
                    Days </th> 
                    <th colspan='5' style="background-color: #b2eb05;text-align: center; font-size:14px;"> Within 90 
                    Days </th> 
                    <th colspan='5' style="background-color: #ffffff;text-align: center; font-size:14px;"> More Than 
                    120 Days </th>
                    <th colspan='5' style="background-color: #933636 ;text-align: center; font-size:14px;"> Expired 
                    </th> 
               </tr>
                <tr> 
                    <th colspan='33' style="background-color: #f5f681;text-align: center; font-size:20px;"> Brand 
                    wise Aging Stock Status </th> 
                    
                     
                </tr>
                    <tr>
                        
                        <th class="style1">Brand</th>
                        <th class="style1" style="width: 10%" >Item Description</th>
                        <th class="style1">BOG</th>
                        <th class="style1">BSL</th>
                        <th class="style1">COM</th>
                        <th class="style1">COX</th>
                        <th class="style1">CTG</th>
                        <th class="style1">CTN</th>
                        <th class="style1">DNJ</th>
                        <th class="style1">FEN</th>
                        <th class="style1">FRD</th>
                        <th class="style1">GZP</th>
                        <th class="style1">HZJ</th>
                        <th class="style1">JES</th>
                        <th class="style1">KHL</th>
                        <th class="style1">KRN</th>
                        <th class="style1">KSG</th>
                        <th class="style1">KUS</th>
                        <th class="style1">MHK</th>
                        <th class="style1">MIR</th>
                        <th class="style1">MLV</th>
                        <th class="style1">MOT</th>
                        <th class="style1">MYM</th>
                        <th class="style1">NAJ</th>
                        <th class="style1">NOK</th>
                        <th class="style1">PAT</th>
                        <th class="style1">PBN</th>
                        <th class="style1">RAJ</th>
                        <th class="style1">RNG</th>
                        <th class="style1">SAV</th>
                        <th class="style1">SYL</th>
                        <th class="style1">TGL</th>
                        <th class="style1">VRB</th>
                
                
                    </tr>
                    """ + branch_aging.get_branch_aging_stock_status() + """
 
            </table>  <br>
            
            
            <table border="1px solid gray" width="100%"> 
                   <tr> 
                        <th colspan='10' style=" background-color: #bcf19f; font-size: 18px;"> Item wise Yesterday 
                        Sales Quantity </th> 
                    </tr>

                    <tr>
                        <th  class="brandsl" style="font-size: 14px;">BSL No.</th>
                        <th class="brand" style="font-size: 14px;"> Brand </th>
                        <th  class="item_sl" style="text-align: left; font-size: 14px;">Item SL</th>
                        <th  class="description1" style="text-align: left; font-size: 14px;">Item Description</th>
                        <th  class="uom" style="text-align: right; font-size: 14px;"> UOM</th>
                        <th  class="uom" style="text-align: right; font-size: 14px;"> Sales Quantity</th>
                        <th  class="uom" style="text-align: right; font-size: 14px;"> TP </th>
                        <th  class="uom" style="text-align: right; font-size: 14px;"> TP Sales Value </th>
                        <th  class="uom" style="text-align: right ; font-size: 14px;"> Net Sales Value</th>
                        <th  class="uom" style="text-align: right ; font-size: 14px;"> Discount</th>
                    </tr>

                   """ + yesterday.item_wise_yesterday_sales_Records() + yesterday.grandtotal() + """
                </table>  <br> 

            <table border="1px solid gray" width="100%"> 
                   <tr> 
                        <th colspan='5' style=" background-color: #ffc994; font-size: 20px; "> No Sales Item : 
                        Yesterday </th> 
                    </tr>

                    <tr>
                        <th  class="brandsl" style="font-size: 14px;">BSL No.</th>
                        <th class="brand" style="font-size: 14px;"> Brand </th>
                        <th  class="brandsl" style="text-align: left; font-size: 14px;">Item SL</th>
                        <th  class="description1" style="text-align: left; font-size: 14px;">Item Description</th
                        <th class="uom" style="text-align: right;  font-size: 14px;"> UOM</th>

                    </tr>

                  """ + yesterday.item_wise_yesterday_no_sales_Records() + """
                </table>  <br> <br>

                <table border="1px solid gray" width="100%">
                    <tr> 
                        <th colspan='5' style=" background-color: #f4d3b5 ;font-size: 20px;"> No Sales Item: Last 3 Months </th> 
                    </tr>

                    <tr>
                        <th  class="brandsl" style="font-size: 14px;">BSL No.</th>
                        <th class="brand" style="font-size: 14px;"> Brand </th>
                        <th  class="brandsl" style="text-align: left; font-size: 14px;">Item SL</th>
                        <th  class="description1" style="text-align: left; font-size: 14px;">Item Description</th
                        <th class="uom" style="text-align: right;  font-size: 14px;"> UOM</th>
                    </tr>

                     """ + noSales.get_No_Sales_Records() + """
                </table>  <br> 


                <table border="1px solid black" width="100%"> 
                    <tr> 
                        <th colspan='7' style=" background-color: #f4d3b5; font-size: 20px;"> No Stock Item: Last 3 Months </th> 
                    </tr>

                    <tr>
                        <th  class="brandsl" style="font-size: 14px;">BSL No.</th>
                        <th class="brand" style="font-size: 14px;"> Brand </th>
                        <th  class="brandsl" style="text-align: left; font-size: 14px;">Item SL</th>
                        <th  class="description1" style="text-align: left; font-size: 14px;">Item Description</th
                        <th class="uom" style="text-align: right;  font-size: 14px;"> UOM</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;">Total Ordered</th>
                        <th class="uom" style="text-align: right; font-size: 14px;"> Estimated Sales</th>
                    </tr>
                    """ + noStock.get_No_Stock_Records() + """  </tr>
                </table>  <br> 

                <table border="1px solid black" width="100%"> 
                    <tr> 
                        <th colspan='8' style=" background-color: #f4d3b5;text-align: center; font-size: 20px; "> 
                        Branch 
                        Wise Item Stock Category </th> 
                    </tr>

                    <tr>
                        <th class="brand" >Branch</th>
                        <th class="brand" style="text-align: right; font-size: 14px;"> Total Items</th>
                        <th class="brand" style="text-align: right; font-size: 14px;"> Nill</th>
                        <th class="item_sl" style="text-align: right; font-size: 14px;">Super Under Stock</th>
                        <th class="description1" style="text-align: right; font-size: 14px;">Under Stock</th>
                        <th class="uom" style="text-align: right; font-size: 14px;"> Normal Stock</th>
                        <th class="uom" style="text-align: right; font-size: 14px;">Over Stock</th>
                        <th class="uom" style="text-align: right; font-size: 14px;">Super Over Stock</th>
                    </tr>

                    """ + bs.branch_wise_nil_us_ss() + """ 

                </table> <br> 
                
                <table border="1px solid gray" width="200%">
                    <tr> 
                        <th colspan='16' style="background-color: #f5f681;text-align: left; font-size:20px;"> Brand 
                        wise Items Stock Status </th> 
                        <th colspan='10' style="background-color: #ffba62; font-size:14px;"> Low Stock </th> 
                        <th colspan='10' style="background-color: #80ffff; font-size:14px; "> High Stock </th> 
                    </tr>
                    
                    <tr>
                        <th class="style1">BSL</th>
                        <th class="style1">Brand</th>
                        <th class="style1">Item SL</th>
                        <th class="style1" style="width: 8%" >Item Description</th>
                        <th class="style1">UOM</th>
                        <th class="style1">BOG</th>
                        <th class="style1">BSL</th>
                        <th class="style1">COM</th>
                        <th class="style1">COX</th>
                        <th class="style1">CTG</th>
                        <th class="style1">CTN</th>
                        <th class="style1">DNJ</th>
                        <th class="style1">FEN</th>
                        <th class="style1">FRD</th>
                        <th class="style1">GZP</th>
                        <th class="style1">HZJ</th>
                        <th class="style1">JES</th>
                        <th class="style1">KHL</th>
                        <th class="style1">KRN</th>
                        <th class="style1">KSG</th>
                        <th class="style1">KUS</th>
                        <th class="style1">MHK</th>
                        <th class="style1">MIR</th>
                        <th class="style1">MLV</th>
                        <th class="style1">MOT</th>
                        <th class="style1">MYM</th>
                        <th class="style1">NAJ</th>
                        <th class="style1">NOK</th>
                        <th class="style1">PAT</th>
                        <th class="style1">PBN</th>
                        <th class="style1">RAJ</th>
                        <th class="style1">RNG</th>
                        <th class="style1">SAV</th>
                        <th class="style1">SYL</th>
                        <th class="style1">TGL</th>
                        <th class="style1">VRB</th>
                
                
                    </tr>
                    """ + item_day.item_stock_days() + """
                
                
            </table>  <br>
            

                
                <table border="1px solid gray" cellspacing ="20">
                 <tr>
                    <th colspan="16" class="info" style="text-align: left"> """ + gpm.getGPMNFullInfo(gpm_name) + """
                    </th>
                    <th colspan="3" style="font-weight: bolder; font-size: 12px; background-color: #e6a454 ">SKF Plant</th>
                    <th rowspan="3" style="background-color: #d0ff89"><div>TDCL Central WH</div></th>
                    <th rowspan="3" style="background-color: #95ff89"><div>Branch Total</div></th>
                    <th colspan="5" style="background-color: #ff2300" class="color_style"> Nill</th>
                    <th colspan="5" style="background-color: #ff971a" class="color_style">Super Under Stock</th>
                    <th colspan="5" style="background-color: #eee298;" class="color_style">Under Stock</th>
                    <th colspan="5" class="color_style">Normal Stock</th>
                    <th colspan="5" style="background-color: #cbe14c; color: black"   class="color_style">Over Stock</th>
                    <th colspan="6" style="background-color: #fff900; color: black"  class="color_style">Super Over Stock</th>
                </tr>
    
                <tr>
                    <th rowspan="2" class="style1">BSL<br> No.</th>
                    <th rowspan="2" class="brand"> Brand &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</th>
                    <th rowspan="2" class="item_sl">Item SL</th>
                    <th rowspan="2" class="description"> <div class="my_margin">.</div> Item Description</th>
                    <th rowspan="2" class="uom"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UOM &nbsp;</th>
                    <th rowspan="2" class="sales_monthly_trend">Yesterday Sales </th>
                    <th rowspan="2" class="sales_monthly_trend">Avg Sales Per Day </th>
                    <th rowspan="2" class="sales_monthly_trend">Monthly Sales Target</th>
                    <th rowspan="2" class="style2" ><div>MTD Sales Target</div></th>
                    <th rowspan="2" class="style2"><div>Actual Sales MTD</div></th>
                    <th rowspan="2" class="style2"><div>MTD Sales Achv %</div></th>
                    <th rowspan="2" class="style2"><div>Monthly Sales Achv %</div></th>
                    <th rowspan="2" class="style2"><div>Monthly Sales Trend</div></th>
                    <th rowspan="2" class="style2"> <div>Monthly Sales Trend Achv</div></th>
                    <th rowspan="2" class="remaining"><div>Remaining Quantity</div></th>
                    <th rowspan="2" class="nation_wide"><div>Nationwide Stock</div></th>
                    <th class="style3" rowspan="2">SKF <br>Mirpur </th>
                    <th class="style3" rowspan="2">SKF <br>Tongi </th>
                    <th class="style3" rowspan="2">SKF <br>Rupganje </th>

                    <th colspan="31" style="font-weight: bolder; font-size: 14px"> TDCL Branches</th>
                </tr>
                <tr>
    
                    <th class="branch_bg_color">BOG</th>
                    <th class="branch_bg_color">BSL</th>
                    <th class="branch_bg_color">COM</th>
                    <th class="branch_bg_color">COX</th>
                    <th class="branch_bg_color">CTG</th>
                    <th class="branch_bg_color">CTN</th>
                    <th class="branch_bg_color"> DNJ</th>
                    <th class="branch_bg_color">FEN</th>
                    <th class="branch_bg_color">FRD</th>
                    <th class="branch_bg_color">GZP</th>
                    <th class="branch_bg_color">HZJ</th>
                    <th class="branch_bg_color">JES</th>
                    <th class="branch_bg_color">KHL</th>
                    <th class="branch_bg_color">KRN</th>
                    <th class="branch_bg_color">KSG</th>
                    <th class="branch_bg_color">KUS</th>
                    <th class="branch_bg_color">MHK</th>
                    <th class="branch_bg_color">MIR</th>
                    <th class="branch_bg_color">MLV</th>
                    <th class="branch_bg_color" style="font-size: 8px;"> MOT</th>
                    <th class="branch_bg_color">MYM</th>
                    <th class="branch_bg_color">NAJ</th>
                    <th class="branch_bg_color">NOK</th>
                    <th class="branch_bg_color">PAT</th>
                    <th class="branch_bg_color">PBN</th>
                    <th class="branch_bg_color">RAJ</th>
                    <th class="branch_bg_color" style="font-size: 8px;">RNG</th>
                    <th class="branch_bg_color">SAV</th>
                    <th class="branch_bg_color">SYL</th>
                    <th class="branch_bg_color">TGL</th>
                    <th class="branch_bg_color">VRB</th>
    
                    </tr>
    
                    """ + SalesStock.get_Sales_and_Stock_Records() + """
                </table> <br>



                </body>
            </html>
        """
    return results

# # ------------  ---------
