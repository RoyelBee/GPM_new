import pyodbc as db

connection = db.connect('DRIVER={SQL Server};'
                            'SERVER=137.116.139.217;'
                            'DATABASE=ARCHIVESKF;'
                            'UID=rptuser;PWD=Rpt@1729')