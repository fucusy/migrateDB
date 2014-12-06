script usage
>>python  ProcessSqlServerInsertSqlToOracleInsertSql.py {SqlServerInsertSqlFileName.sql} {OracleInsertSqlFileName.sql}
you need replace {SqlServerInsertSqlFileName.sql} with real filename path
and replace {OracleInsertSqlFileName.sql} with the output sql name what you want
if you do not specify the output file name, the default name "OracleInsertOutput.sql" will be used
for example if the python script and SqlFile is under the same directory you can run under command
to transfer  SqlServerInsertSqlFile.sql to OracleInsertSqlFile.sql
>>python ProcessSqlServerInsertSqlToOracleInsertSql.py SqlServerInsert.sql