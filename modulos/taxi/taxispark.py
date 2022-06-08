from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf


def run_taxi_pipe():
    
    conf=(SparkConf()
         .setMaster("k8s://https://10.96.0.1:443")
         .set('spark.hadoop.fs.s3a.endpoint','http://10.96.101.36:9000')
         .set('spark.hadoop.fs.s3a.access.key','myaccesskey')
         .set('spark.hadoop.fs.s3a.secret.key','mysecretkey')
         .set('spark.hadoop.fs.s3a.path.style.access',True)
         .set('spark.hadoop.fs.s3a.fast.upload',True)
         .set('spark.hadoop.fs.s3a.connection.maximum',100)
         .set('spark.hadoop.fs.s3a.impl','org.apache.hadoop.fs.s3a.S3AFileSystem')
         .set('spark.delta.logStore.class','org.apache.spark.sql.delta.storage.S3SingleDriverLogStore')
         .set('spark.sql.extensions','io.delta.sql.DeltaSparkSessionsExtension')
         .set('spark.sql.catalog.spark_catalog','org.apache.spark.sql.delta.catalog.DeltaCatalog'))
    sc=SparkContext(conf=conf).getOrCreate()

    
    spark=SparkSession.builder.appName('test-dag-airflow-spark').getOrCreate()
    
    #spark.SparkContext.setLogLevel("INFO")

    schema=spark.read.format('json').option('inferSchema','true').json('s3a://estudos/*json')

    schema.show()

    schema.printSchema()

    spark.stop()
    