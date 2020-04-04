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
# 5. Joining (10 points): The following program construct a new dataframe out of 'df' with a much smaller size.
####

df2 = gb_df.select("word", "count1").distinct().limit(1000)
df2.createOrReplaceTempView('gbooks2')

# Now we are going to perform a JOIN operation on 'df2'. Do a self-join on 'df2' in lines with the same #'count1' values and see how many lines this JOIN could produce. Answer this question via DataFrame API and #Spark SQL API
# Spark SQL API
results = sqlContext.sql("SELECT g1.word AS word1, g2.word AS word2 FROM gbooks2 g1, gbooks2 g2 WHERE g1.count1 = g2.count1")
print(results.count())

# output: 9658

