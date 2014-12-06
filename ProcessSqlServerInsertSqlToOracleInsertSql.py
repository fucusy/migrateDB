__author__ = 'fucus'

# script usage
# >>python  ProcessSqlServerInsertSqlToOracleInsertSql.py {SqlServerInsertSqlFileName.sql} {OracleInsertSqlFileName.sql}
# you need replace {SqlServerInsertSqlFileName.sql} with real filename path
# and replace {OracleInsertSqlFileName.sql} with the output sql name what you want
# if you do not specify the output file name, the default name "OracleInsertOutput.sql" will be used
# for example if the python script and SqlFile is under the same directory you can run under command
# to transfer  SqlServerInsertSqlFile.sql to OracleInsertSqlFile.sql
# >>python ProcessSqlServerInsertSqlToOracleInsertSql.py SqlServerInsert.sql



# config
default_out_put_file_name = "OracleInsertOutput.sql"



import sys
import re


if len(sys.argv) < 2:
    print "please input the SqlServerInsertSqlFileName path"
    exit(0)
input_file_path = sys.argv[1]
output_file_path = default_out_put_file_name

if len(sys.argv) >= 3:
    output_file_path = sys.argv[2]


input_f = open(input_file_path,"r")
output_f = open(output_file_path,"w")

for row in input_f:
    if row[:2] == "GO" or row[:3] == "USE" \
        or row[:3] == "SET" or row[:2] == "/*"\
        or row[:5] == "print":
        continue

    out_row = re.sub(r'\[([a-zA-Z_]*)\]',r'\1',row)
    out_row = re.sub(r'N\'([^\']*)\'',r"'\1'",out_row)
    out_row = out_row.replace("dbo.","")
    out_row = out_row.replace("INSERT","INSERT INTO")
    out_row = out_row.replace("\n",";\n")
    output_f.write(out_row)





input_f.close()
output_f.close()


