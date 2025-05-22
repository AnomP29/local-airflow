from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("MyApp") \
        .enableHiveSupport() \
        .getOrCreate()

    print("=== DATABASES ===")
    spark.sql("SHOW DATABASES").show()
    
    # Show Hive tables
    spark.sql("SHOW TABLES").show()

    # Optional: stop the session
    spark.stop()

if __name__ == "__main__":
    main()
