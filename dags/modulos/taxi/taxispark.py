from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
 
conf = (
    SparkConf().setMaster("k8s://https://10.96.0.1:443")
    .set('spark.hadoop.fs.s3a.endpoint', 'http://10.107.212.209:9000')
    .set('spark.hadoop.fs.s3a.access.key', 'SZ3l7o2oBqA0b9te')
    .set('spark.hadoop.fs.s3a.secret.key', 'KFPNBiX6fCQGGzDE8pAy5kr1kVrKX4gj')
    .set('spark.hadoop.fs.s3a.path.style.access', True)
    .set('spark.hadoop.fs.s3a.fast.upload', True)
    .set('spark.hadoop.fs.s3a.connection.maximum', 100)
    .set('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
    .set('spark.delta.logStore.class', 'org.apache.spark.sql.delta.storage.S3SingleDriverLogStore')
    .set('spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionsExtension')
    .set('spark.sql.catalog.spark_catalog', 'org.apache.spark.sql.delta.catalog.DeltaCatalog')
)

sc = SparkContext(conf=conf).getOrCreate()

if __name__ == '__main__':

     spark = SparkSession.builder.appName('test-dag-airflow-spark').getOrCreate()
     
     schema = spark.read.format('json').option('inferSchema', 'true').json('s3a://bronze/teste/*json')

     schema.write.format("csv").save("s3a://bronze/save")
     
     schema.show()
     
     schema.printSchema()
     
     spark.stop()