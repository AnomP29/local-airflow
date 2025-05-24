from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("MyApp") \
        .enableHiveSupport() \
        .config("hive.metastore.uris", "thrift://172.18.0.4:9083") \
        .config("spark.hadoop.fs.s3a.endpoint", "http://172.18.0.2:9000") \
        .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
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
