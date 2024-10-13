import numpy as np
import pickle

file_path="/home/jamie/Projects/AI-Automobility-Class/MNIST"
key_file = {
	'train_img':'train-images-idx3-ubyte',
	'train_label':'train-labels-idx1-ubyte',
	'test_img':'t10k-images-idx3-ubyte',
	'test_label':'t10k-labels-idx1-ubyte'
}

class NeuralNetwork:
	def __init__(self):
		with open("MNIST/sample_weight.pkl", 'rb') as f:
			self.network= pickle.load(f)

	sigmoid=	lambda self, x: 1/(1+np.exp(-x))
	reLU=		lambda self, x: np.maximum(0, x)

	def softmax(self, a):
		exp_a=np.exp(a-np.max(a))
		sum_exp_a=np.sum(exp_a)
		return exp_a/sum_exp_a

	def predict(self, x, activation):
		W1, W2, W3 = self.network['W1'], self.network['W2'], self.network['W3']
		b1, b2, b3 = self.network['b1'], self.network['b2'], self.network['b3']

		if activation == 'reLU':	act_func=self.reLU
		else:						act_func=self.sigmoid

		self.a1=np.dot(np.float128(x), W1)+b1
		self.z1=act_func(self.a1)
		self.a2=np.dot(self.z1, W2)+b2
		self.z2=act_func(self.a2)
		self.a3=np.dot(self.z2, W3)+b3
		self.y=self.softmax(self.a3)

		return self.y

class MNIST_dataset:
	def __init__(self):
		self.offset_val={'label':8, 'img':16}

		self.train_img	=self._load_image(key_file['train_img'])
		self.train_label=self._load_label(key_file['train_label'])
		self.test_img	=self._load_image(key_file['test_img'])
		self.test_label	=self._load_label(key_file['test_label'])

	def _load_image(self, file):
		with open(file_path+"/"+file, 'rb') as f:
			self.image=np.frombuffer(f.read(), np.uint8, offset=self.offset_val['img'])
		return self.image.reshape(-1, 784)

	def _load_label(self, file):
		with open(file_path+"/"+file, 'rb') as f:
			self.label=np.frombuffer(f.read(), np.uint8, offset=self.offset_val['label'])
		return self.label

NN=NeuralNetwork()
mnist_data=MNIST_dataset()

batch_size=100

#train image+sigmoid
accuracy_count=0
activation=input('Activation functions list: \n\'sigmoid\'\n\'reLU\'\nChoose function:')
for i in range(0, len(mnist_data.train_img), batch_size):
	y=NN.predict(mnist_data.train_img[i:i+batch_size], activation)
	p=np.argmax(y, axis=1)
	accuracy_count += np.sum(p == mnist_data.train_label[i:i+batch_size])

print("%-25s" % "train image Accuracy with "+activation+": ", "%-0.5f" % float(accuracy_count/len(mnist_data.train_img)))
