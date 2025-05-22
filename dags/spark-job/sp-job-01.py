from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("MyApp") \
        .enableHiveSupport() \
        .config("hive.metastore.uris", "thrift://172.18.0.5:9083") \
        .config("spark.hadoop.fs.s3a.endpoint", "http://172.18.0.4:9000") \
        .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()
    
    print("=== DATABASES ===")
    spark.sql("SHOW DATABASES").show()
    
    print("=== TABLES IN DEFAULT DATABASE ===")
    spark.sql("USE default")    
    spark.sql("SHOW TABLES").show()

    # Optional: stop the session
    spark.stop()

if __name__ == "__main__":
    main()
