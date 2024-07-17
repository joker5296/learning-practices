from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("Day-1 Learning").getOrCreate()

print(spark)

data  = [1,2,3,4,5,6,7,8,9,10,11,12]

rdd = spark.sparkContext.parallelize(data, 10)

print(rdd.getNumPartitions())