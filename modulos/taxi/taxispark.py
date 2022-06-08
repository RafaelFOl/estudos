from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
 

sparkConf = SparkConf()
sparkConf.setMaster("k8s://https://10.96.0.1:443")
sparkConf.setAppName("KUBERNETES-IS-AWESOME")
sparkConf.set("spark.kubernetes.container.image", "itayb/spark:3.1.1-hadoop-3.2.0-aws")
sparkConf.set("spark.kubernetes.namespace", "spark")
sparkConf.set("spark.hadoop.fs.s3a.endpoint", "http://10.96.101.36:9000")
sparkConf.set("spark.hadoop.fs.s3a.access.key", "myaccesskey")
sparkConf.set("spark.hadoop.fs.s3a.secret.key", "mysecretkey")

spark = SparkSession.builder.config(conf=sparkConf).getOrCreate()
sc = spark.sparkContext

df = spark.read.json('s3a://estudos/credentials.json')

df.show()