from pyspark import *
from pyspark.sql import SparkSession
from graphframes import *


sc = SparkContext()
spark = SparkSession.builder.appName('fun').getOrCreate()


def get_shortest_distances(graphframe, dst_id):
    # TODO
    # Find shortest distances in the given graphframe to the vertex which has id `dst_id`
    # The result is a dictionary where key is a vertex id and the corresponding value is
    # the distance of this node to vertex `dst_id`.
    result = graphframe.shortestPaths(landmarks=[dst_id])
    result = result.select("id", "distances").collect()

    distances = {}
    for row in result:
        if len(row['distances']) > 0:
            distances[row['id']]=row['distances'][dst_id]
        else:
            distances[row['id']] = -1

    return distances


if __name__ == "__main__":
    vertex_list = []
    edge_list = []
    with open('dataset/graph.data') as f:
        for line in f:
            line = line.split()
            src = line[0]  # TODO: Parse src from line
            if len(line) > 1:
                dst_list = line[1:]  # TODO: Parse dst_list from line
            else:
                dst_list = []
            vertex_list.append((src,))
            edge_list += [(src, dst) for dst in dst_list]

    vertices = spark.createDataFrame(vertex_list, ['id'])  # TODO: Create dataframe for vertices
    edges = spark.createDataFrame(edge_list, ['src', 'dst'])  # TODO: Create dataframe for edges

    g = GraphFrame(vertices, edges)
    sc.setCheckpointDir("/tmp/shortest-paths")

    # We want the shortest distance from every vertex to vertex 1
    for k, v in get_shortest_distances(g, '1').items():
        print(k, v)
