from pyspark.sql import SparkSession

def main():
    # Create Spark session with Hive support
    spark = SparkSession.builder \
        .appName("MyApp") \
        .enableHiveSupport() \
        .getOrCreate()


    print("=== DATABASES ===")
    sdb = spark.sql("SHOW DATABASES")
    odb = sdb._jdf.showString(20, 20, False)
    print(odb)
    
    print("=== TABLES IN DEFAULT DATABASE ===")
    # spark.sql("USE default")    
    stb = spark.sql("SHOW TABLES")
    otb = stb._jdf.showString(20, 20, False)
    print(otb)
    
    # Optional: stop the session
    spark.stop()

if __name__ == "__main__":
    main()
