from ClassifierToolkit import NeuralNet

classifier = NeuralNet()
data = [[0,1], [1,1], [12,12], [10,10]]
labels = [1,2,3,4]
classifier.train(data, labels, (2,2))
