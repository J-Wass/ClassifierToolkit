import numpy as np
import random

class NeuralNet:
    def _init_(self):
        pass
    def train(self, data, labels, layers, learning_rate = 0.5):
        self.edge_layers = []
        self.node_layers = []
        self.data = data
        self.labels = labels

        # create first layer for input, input nodes don't have biases so don't populate them
        self.edge_layers.insert(0, [])
        self.node_layers.insert(0, [])
        # iterate each node in input layer
        for n in range(len(data[0])):
            # iterate each weight in each node of the input layer
            self.edge_layers[0].insert(n, [])
            for w in range(layers[0]):
                self.edge_layers[0][n].insert(w,random.uniform(-2,3))
        # iterate each layer to build our matrices and initial weights/biases
        for i in range(1, len(layers)+1):
            self.edge_layers.insert(i, [])
            self.node_layers.insert(i, [])
            # iterate each node in the layer
            for j in range (layers[i-1]):
                if i == 1: # initialize the random biases
                    self.node_layers[i].insert(j,random.uniform(-2,3))
                else:
                    self.node_layers[i].insert(j,random.uniform(-2,3))
                self.edge_layers[i].insert(j, [])
                # iterate each edge in the node to initialize the random weights, hidden layers only
                for k in range(layers[i-1]):
                    if i == 0: # edge_layers[i][j][k] means the k'th edge in the j'th node in the i'th layers
                        self.edge_layers[i][j].insert(k, random.uniform(-2,3))
                    else:
                        self.edge_layers[i][j].insert(k, random.uniform(-2,3))
        #create output biases
        self.node_layers.insert(len(layers)+2, [])
        for l in range(len(set(labels))):
            self.node_layers[len(layers)+1].insert(l, random.uniform(-2,3))
        for datapoint in data:
            self.train_datapoint(datapoint)
    def train_datapoint(self, datapoint):
        pass
    def predict(self, datapoint):
        pass
