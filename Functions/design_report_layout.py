import Functions.item_wise_yesterday_sales as yesterday
import Functions.no_sales_record as noSales
import Functions.no_stock_record as noStock
import Functions.branch_stock_summery as bs
import Functions.branch_wise_stock_aging as branch_aging
import Functions.aging_summary as aging_summary

# import Functions.read_gpm_info as gpm
# import Functions.sales_and_stock_record as SalesStock
# import Functions.branch_wise_stocks as branch_stock
# import Functions.item_wise_stock_days as item_day

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
            <img src="cid:banner_ai" width="90%"> <br>
                <img src="cid:dash" width="90%"> <br>
                <img src="cid:cm" width="90%"> <br>
                <img src="cid:executive" width="90%"> <br>
                <img src="cid:executive_main" width="100%" height="90%"> <br>
                <img src="cid:brand"> <br>
                <img src="cid:aging" width="100%"> <br> <br> <br> <br>
                
            
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
                        <th rowspan="2"class="style1">CND</th>
                        <th rowspan="2"class="style1">JES</th>
                        <th rowspan="2"class="style1">KHL</th>
                        <th rowspan="2"class="style1">KRN</th>
                        <th rowspan="2"class="style1">KSG</th>
                        <th rowspan="2"class="style1">KUS</th>
                        <th rowspan="2"class="style1">TEJ</th>
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
                        <th rowspan="2"class="style1">BBR</th>
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
                        <th colspan='15' style=" background-color: #bcf19f; font-size: 18px;"> Item wise Sales : 
                        Yesterday </th> 
                    </tr>
                    <tr>
                         <th  class="brandsl" style="font-size: 14px;">SL</th>
                         <th class="brand" style="font-size: 14px;"> Product Brand </th>
                         <th  class="item_sl" style="text-align: center; font-size: 14px;">SL</th>
                         <th  class="description1" style="text-align: left; font-size: 14px; width:20%;">Item 
                              <br> Description</th>
                         <th  class="uom" style="text-align: right; font-size: 14px;"> UOM</th>
                         <th  class="uom" style="text-align: right; font-size: 14px;"> Sales <br> Quantity</th>
                         <th  class="uom" style="text-align: right; font-size: 14px;"> Sales <br> Quantity%</th>
                         <th  class="uom" style="text-align: right; font-size: 14px;"> Monthly Target </th>
                         <th  class="uom" style="text-align: right; font-size: 14px;"> MTD Target </th>
                         <th  class="uom" style="text-align: right; font-size: 14px;"> TP </th>
                         <th  class="uom" style="text-align: right; font-size: 14px;"> TP Sales Value </th>
                         <th  class="uom" style="text-align: right ; font-size: 14px;"> Net Sales Value</th>
                         <th  class="uom" style="text-align: right ; font-size: 14px;"> Net Sales %</th>
                         <th  class="uom" style="text-align: right ; font-size: 14px;"> Discount</th>
                         <th  class="uom" style="text-align: right ; font-size: 14px;"> LD Target <br> Qty/Day</th>
                    </tr>



                   """ + yesterday.item_wise_yesterday_sales_Records()  +  yesterday.grandtotal() + """
                </table>  <br> 
            
                
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
                
            <table border="1px solid gray" width='300%'> 
                   <tr> 
                        <th colspan='5' style=" background-color: #ffc994; font-size: 20px; "> No Sales Item: Yesterday </th> 
                    </tr>

                    <tr>
                        <th  class="brandsl" style="font-size: 14px;">SL</th>
                        <th class="brand" style="font-size: 14px;"> Product Brand</th>
                        <th  class="brandsl" style="text-align: center; font-size: 14px;">SL</th>
                        <th  class="description1" style="text-align: left; font-size: 14px;">Item Description</th
                        <th class="uom" style="text-align: right;  font-size: 14px;"> UOM</th>

                    </tr>

                  """ + yesterday.item_wise_yesterday_no_sales_Records() + """
                </table>  <br> <br>

                <table border="1px solid gray" width='300%'>
                    <tr> 
                        <th colspan='5' style=" background-color: #f4d3b5 ;font-size: 20px;"> No Sales Item: Last 3 Months </th> 
                    </tr>

                    <tr>
                        <th  class="brandsl" style="font-size: 14px;">SL</th>
                        <th class="brand" style="font-size: 14px;"> Product Brand </th>
                        <th  class="brandsl" style="text-align: center; font-size: 14px;">SL</th>
                        <th  class="description1" style="text-align: left; font-size: 14px;">Item Description</th
                        <th class="uom" style="text-align: right;  font-size: 14px;"> UOM</th>
                    </tr>

                     """ + noSales.get_No_Sales_Records() + """
                </table>  <br> 


                <table border="1px solid black" width='300%'> 
                    <tr> 
                        <th colspan='7' style=" background-color: #f4d3b5; font-size: 20px;"> No Stock Item: Last 3 Months </th> 
                    </tr>

                    <tr>
                        <th  class="brandsl" style="font-size: 14px;">SL</th>
                        <th class="brand" style="font-size: 14px;"> Brand </th>
                        <th  class="brandsl" style="text-align: center; font-size: 14px;"> SL</th>
                        <th  class="description1" style="text-align: left; font-size: 14px;">Item Description</th
                        <th class="uom" style="text-align: right;  font-size: 14px;"> UOM</th>
                        <th class="uom" style="text-align: right;  font-size: 14px;">Total Ordered</th>
                        <th class="uom" style="text-align: right; font-size: 14px;"> Estimated Sales</th>
                    </tr>
                    """ + noStock.get_No_Stock_Records() + """  </tr>
                </table>  <br> 

                <table border="1px solid black" width='300%'> 
                    <tr> 
                        <th colspan='8' style=" background-color: #f4d3b5;text-align: center; font-size: 20px; "> 
                        Branch Wise Item Stock Category </th> 
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

                </table> <br> <br>  
            
                 <table  style="border-style:none" width='300%'>
                    <tr style="border-style:none;float: right;"> 
                        <th colspan='1' style=" font-size: 14px;width: 1000px;text-align: left;padding-left: 15px; border-style:none"></th>
                        <th colspan='1' style=" background-color: #f40d0d;font-size: 14px; width: 60px; border-style:1px solid black;"></th> 
                        <th colspan='1' style=" font-size: 14px;width: 200px;text-align: left;padding-left: 15px;border-style:none">Expired</th> 
                        <th colspan='1' style=" background-color:#fd8947;font-size: 14px; width: 60px; border-style:1px solid black;"></th> 
                        <th colspan='1' style=" font-size: 14px;width: 200px;text-align: left;padding-left: 15px; border-style:none"> 0 - 15 Days </th>
                        <th colspan='1' style=" background-color: #eaff3d ;font-size: 14px; width: 60px; border-style:1px solid black;"></th> 
                        <th colspan='1' style=" font-size: 14px;width: 200px;text-align: left;padding-left: 15px; border-style:none"> 16 - 30 Days  </th> 
                        <th colspan='1' style=" background-color: #e1e300 ;font-size: 14px; width: 60px; border-style:1px solid black;"></th>
                        <th colspan='1' style=" font-size: 14px;width: 200px;text-align: left;padding-left: 15px;border-style:none">31 - 60 Days </th> 
                        <th colspan='1' style=" background-color: #b2eb05 ;font-size: 14px; width: 60px; border-style:1px solid black;"></th>
                        <th colspan='1' style=" font-size: 14px;width: 200px;text-align: left;padding-left: 15px;border-style:none">61 - 90 Days </th> 
                        <th colspan='1' style=" background-color: #629B00;font-size: 14px; width: 60px; border-style:1px solid black;"></th> 
                        <th colspan='1' style=" font-size: 14px;width: 250px;text-align: left;padding-left: 15px;border-style:none"> 91 - 180 Days</th>
                        <th colspan='1' style=" background-color: #124B00;font-size: 14px; width: 60px; border-style:1px solid black;"></th> 
                        <th colspan='1' style=" font-size: 14px;width: 250px;text-align: left;padding-left: 15px;border-style:none"> 181 - 210 Days</th>
                        <th colspan='1' style=" background-color: #ffffff;font-size: 14px; width: 60px; border-style:1px solid black;"></th> 
                        <th colspan='1' style=" font-size: 14px;width: 250px;text-align: left;padding-left: 15px;border-style:none"> >210 Days</th> 
                    </tr>
                </table>
            <br> <br>
            
            <table border="1px solid gray" width='300%'>
                <tr> 
                    <th colspan='38' style="background-color: #f5f681;text-align: center; font-size:20px;"> Branch - Brand - SKU wise Stock Aging Status: Detailed</th> 
                </tr>
                    <tr>
                        
                        <th rowspan="2" class="style1" style="text-align: center; width:8%;">SL</th>
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
                        <th rowspan="2"class="style1">CND</th>
                        <th rowspan="2"class="style1">JES</th>
                        <th rowspan="2"class="style1">KHL</th>
                        <th rowspan="2"class="style1">KRN</th>
                        <th rowspan="2"class="style1">KSG</th>
                        <th rowspan="2"class="style1">KUS</th>
                        <th rowspan="2"class="style1">TEJ</th>
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
                        <th rowspan="2"class="style1">BBR</th>
                        <th colspan="3" >SK+F Plant</th>

                   </tr>  
                   <tr> 
                        <th class="style1">Rupganj </th>
                        <th class="style1">Mirpur </th>
                        <th class="style1">Tongi </th>
                   </tr>
                        
                
                
                    </tr>  """ + branch_aging.get_branch_aging_stock_status(gpm_name) + """
                    
 
            </table>  <br><br>
                
                
                
            </html>
        """
    return results

# # ------------  ---------
