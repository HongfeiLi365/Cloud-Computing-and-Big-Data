from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType

sc = SparkContext()
sqlContext = SQLContext(sc)

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)


gbook = sc.textFile("gbooks")

gbook = gbook.map(lambda s:s.split()).map(lambda line:[line[0], int(line[1]), int(line[2]), int(line[3])])
# Spark SQL - DataFrame API
fields = [StructField('word', StringType(), True),
          StructField('count1', IntegerType(), True),
          StructField('count2', IntegerType(), True),
          StructField('count3', IntegerType(), True)]
schema = StructType(fields)

gb_df = sqlContext.createDataFrame(gbook, schema)

####
# 2. Counting (10 points): How many lines does the file contains? Answer this question via both RDD api & #Spark SQL
####

# Spark SQL
gb_df.registerTempTable("gbooks")
results = sqlContext.sql("SELECT COUNT(*) FROM gbooks")
results.show()


# +--------+
# |count(1)|
# +--------+
# |86618505|
# +--------+


