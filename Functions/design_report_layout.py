import Functions.item_wise_yesterday_sales as yesterday
import Functions.no_sales_record as noSales
import Functions.no_stock_record as noStock
import Functions.read_gpm_info as gpm
import Functions.sales_and_stock_record as SalesStock

import Functions.branch_wise_stocks as branch_stock
import Functions.branch_stock_summery as bs
import Functions.branch_stock_demo as bb


def generate_layout():
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
                    .item_sl{
                        background-color: #e5f0e5;
                        padding-right: 3px;
                        text-align: center;
                    }
                    td.serial{
                        padding-left: 5px;
                        text-align: left;
                    }
                    .brand {
                        background-color: #e5f0e5;
                        font-weight: bold;
                        color: black;
                        text-align: left;
                    }
                    .brandtd {
                        text-align: left;
                        padding-left: 2px;
                        font-weight: bold;
                        font-size: 12px;
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
                    .descriptiontd{
                    padding-left: 2px;
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
                <img src="cid:banner_ai"> <br>
                <img src="cid:dash"> <br>
                <img src="cid:cm"> <br>
                <img src="cid:executive"> <br>
                <img src="cid:brand"> <br> <br>
            
            <table border="1px solid gray" width="78.5%"> 
                   <tr> 
                        <th colspan='6' style=" background-color: #bcf19f "> Item wise Yesterday Sales Quantity </th> 
                    </tr>

                    <tr>
                        <th  class="brand">BSL No.</th>
                        <th class="brand"> Brand &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</th>
                        <th  class="item_sl">Item SL</th>
                        <th  class="description1">Item Description</th>
                        <th  class="uom" style="text-align: right"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UOM</th>
                        <th  class="uom" style="text-align: right"> Yesterday Sales</th>
                    </tr>
                
                   """ + yesterday.item_wise_yesterday_sales_Records()+ """
                </table>  <br> 
                
            <table border="1px solid gray" width="78.5%"> 
                   <tr> 
                        <th colspan='5' style=" background-color: #bcf19f "> Item wise Yesterday No Sales </th> 
                    </tr>
                    
                    <tr>
                        <th class="brand">BSL No.</th>
                        <th class="brand"> Brand &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</th>
                        <th class="item_sl">Item SL</th>
                        <th class="description1">Item Description</th>
                        <th class="uom" style="text-align: right"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UOM</th>
                        
                    </tr>
                
                  """ + yesterday.item_wise_yesterday_no_sales_Records()+ """
                </table>  <br> <br>

                <table border="1px solid gray" width="78.5%">
                    <tr> 
                        <th colspan='5' style=" background-color: #f4d3b5 "> No Sales Item: Last 3 Months </th> 
                    </tr>
                    
                    <tr>
                        <th class="brand">BSL No</th>
                        <th class="brand"> Brand &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</th>
                        <th class="item_sl">Item SL</th>
                        <th class="description1">Item Description</th>
                        <th class="uom" style="text-align: right"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UOM</th>
                    </tr>
    
                     """ + noSales.get_No_Sales_Records() + """
                </table>  <br> 
                
                
                <table border="1px solid black" width="78.5%"> 
                    <tr> 
                        <th colspan='7' style=" background-color: #f4d3b5 "> No Sales Item: Last 3 Months </th> 
                    </tr>
                    
                    <tr>
                        <th class="brand">BSL No</th>
                        <th class="brand"> Brand &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</th>
                        <th class="item_sl">Item SL</th>
                        <th class="description1">Item Description</th>
                        <th class="uom" style="text-align: right"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UOM</th>
                        <th class="uom">Total Ordered</th>
                        <th class="uom" style="text-align: right"> Estimated Sales</th>
                    </tr>
                    """ + noStock.get_No_Stock_Records() + """  </tr>
                </table>  <br> 
                
                <table border="1px solid gray" width="78.5%"> 
                    <tr> 
                        <th colspan='7' style=" background-color: #f4d3b5 "> Branch Wise Item Stock Category </th> 
                    </tr>
                
                    <tr>
                        <th class="brand">Branch</th>
                        <th class="brand"> Nill</th>
                        <th class="item_sl">Super Under Stock</th>
                        <th class="description1">Under Stock</th>
                        <th class="uom" style="text-align: right"> Normal Stock</th>
                        <th class="uom" style="text-align: right">Over Stock</th>
                        <th class="uom" style="text-align: right">Super Over Stock</th>
                    </tr>
        
                    """ + bs.branch_wise_nil_us_ss() + """ 
                
                </table> <br> 


            <table border="1px solid gray" width="200%">
                <tr> 
                    <th colspan='36'> Brand wise Items Stock Status </th> 
                </tr>
                <tr>
                    <th class="style1">BSL</th>
                    <th class="style1">Brand</th>
                    <th class="style1">Item SL</th>
                    <th class="style1" style="width: 8%" >Item Description</th>
                    <th class="style1"  >UOM</th>
                    <th class="style1"  >BOG</th>
                    <th class="style1"  >BSL</th>
                    <th class="style1"  >COM</th>
                    <th class="style1"  >COX</th>
                    <th class="style1"  >CTG</th>
                    <th class="style1"  >CTN</th>
                    <th class="style1"  >DNJ</th>
                    <th class="style1"  >FEN</th>
                    <th class="style1"  >FRD</th>
                    <th class="style1"  >GZP</th>
                    <th class="style1"  >HZJ</th>
                    <th class="style1"  >JES</th>
                    <th class="style1"  >KHL</th>
                    <th class="style1"  >KRN</th>
                    <th class="style1"  >KSG</th>
                    <th class="style1"  >KUS</th>
                    <th class="style1"  >MHK</th>
                    <th class="style1"  >MIR</th>
                    <th class="style1"  >MLV</th>
                    <th class="style1"  >MOT</th>
                    <th class="style1"  >MYM</th>
                    <th class="style1"  >NAJ</th>
                    <th class="style1"  >NOK</th>
                    <th >PAT</th>
                    <th >PBN</th>
                    <th >RAJ</th>
                    <th >RNG</th>
                    <th >SAV</th>
                    <th>SYL</th>
                    <th>TGL</th>
                    <th>VRB</th>
 
            
                </tr>
                
                """ + bb.branch_wise_stocks_Records() + """
                
            </table> 
                                
                </body>
            </html>
        """
    return results

# # ------------  ---------
