from pyspark.sql import SparkSession

def main():
    # Create Spark session with Hive support
    spark = SparkSession.builder \
        .appName("MyApp") \
        .enableHiveSupport() \
        .getOrCreate()


    sp_sql = '''
    select 
    --*
    pickup_date 
    ,count(1)
    from default.nyc_taxi_trip_yellow ntty
    where 9=9
    --and cast(ntty.pickup_date as varchar) = '2021-01-30'
    group by 1
    order by 1
    limit 10
    ;
    '''
    q01 = spark.sql(sp_sql)
    oq01 = q01._jdf.showString(20, 20, False)
    print(oq01)
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
