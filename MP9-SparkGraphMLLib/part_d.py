from pyspark.ml.classification import RandomForestClassifier
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.linalg import Vectors

sc = SparkContext()
sqlContext = SQLContext(sc)


def predict(df_train, df_test):
    # TODO: Train random forest classifier

    # Hint: Column names in the given dataframes need to match the column names
    # expected by the random forest classifier `train` and `transform` functions.
    # Or you can alternatively specify which columns the `train` and `transform`
    # functions should use

    # Result: Result should be a list with the trained model's predictions
    # for all the test data points
    rf = RandomForestClassifier()
    model = rf.fit(df_train)
    pred = model.transform(df_test)
    
    return pred.prediction

def parse_line(line):
    # TODO: Parse data from line into an RDD
    line = line.split(',')
    label = line[-1] 
    features = line[:-1] 
    features = Vectors.dense(features)
    return [features, label]


def main():
    raw_training_data = sc.textFile("dataset/training.data")

    # TODO: Convert text file into an RDD which can be converted to a DataFrame
    # Hint: For types and format look at what the format required by the
    # `train` method for the random forest classifier
    # Hint 2: Look at the imports above
    rdd_train = raw_training_data.map(parse_line)

    # TODO: Create dataframe from the RDD
    df_train = sqlContext.createDataFrame(rdd_train, ['features','label'])

    raw_test_data = sc.textFile("dataset/test-features.data")

    # TODO: Convert text file lines into an RDD we can use later
    rdd_test =raw_test_data.map(lambda line: Vectors.dense(line.split(',')))

    # TODO:Create dataframe from RDD
    df_test = sqlContext.createDataFrame(rdd_test, ['features'])

    predictions = predict(df_train, df_test)

    # You can take a look at dataset/test-labels.data to see if your
    # predictions were right
    for pred in predictions:
        print(int(pred))


if __name__ == "__main__":
    main()
