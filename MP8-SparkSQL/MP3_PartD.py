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
# 4. MapReduce (10 points): List the three most frequent 'word' with their count of appearances
####

# Spark SQL
gb_df.registerTempTable("gbooks")
results = sqlContext.sql("SELECT word, COUNT(*) FROM gbooks GROUP BY word ORDER BY COUNT(*) DESC")
results.show(3)



# There are 18 items with count = 425, so could be different 
# +---------+--------+
# |     word|count(1)|
# +---------+--------+
# |  all_DET|     425|
# | are_VERB|     425|
# |about_ADP|     425|
# +---------+--------+

