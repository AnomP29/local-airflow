import io
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

def main():
    # Create Spark session with Hive support
    spark = SparkSession.builder \
        .appName("MyApp") \
        .enableHiveSupport() \
        .getOrCreate()

    df = spark.read.table("default.nyc_taxi_trip_yellow")
    df = df.filter(col("pickup_date").cast("string") == "2021-01-30")
    df = df.groupBy("pickup_date").count().orderBy("pickup_date")

    # Capture df.show() output
    print('capture output')
    # buf = io.StringIO()
    # sys_stdout = sys.stdout  # Backup original stdout
    # sys.stdout = buf
    
    print('df.show')
    # df.show(20, truncate=False)  # Show up to 20 rows, no truncation

    print('Restore stdout')
    # sys.stdout = sys_stdout  # Restore stdout
    # output = buf.getvalue()
    
    # print(output)  # This will go to the Airflow task log
    
    sp_sql = '''
    select 
    --*
    pickup_date 
    ,count(1)
    from default.nyc_taxi_trip_yellow ntty
    where 9=9
    and pickup_date = '2021-01-30'
    group by 1
    order by 1
    limit 10
    ;
    '''
    # print(sp_sql)
    # q01 = spark.sql(sp_sql)
    # oq01 = q01._jdf.showString(20, 20, False)
    # print(oq01)
    # print("=== DATABASES ===")
    # sdb = spark.sql("SHOW DATABASES")
    # odb = sdb._jdf.showString(20, 20, False)
    # print(odb)
    
    # print("=== TABLES IN DEFAULT DATABASE ===")
    # spark.sql("USE default")    
    # stb = spark.sql("SHOW TABLES")
    # otb = stb._jdf.showString(20, 20, False)
    # print(otb)
    
    # Optional: stop the session
    spark.stop()

if __name__ == "__main__":
    main()
