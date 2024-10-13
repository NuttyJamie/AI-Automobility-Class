import numpy as np
import pickle

file_path="/home/jamie/Projects/AI-Automobility-Class/MNIST"
key_file = {
	'train_img':'train-images-idx3-ubyte',
	'train_label':'train-labels-idx1-ubyte',
	'test_img':'t10k-images-idx3-ubyte',
	'test_label':'t10k-labels-idx1-ubyte'
}

def init_network():
	with open("MNIST/sample_weight.pkl", 'rb') as f:
		return pickle.load(f)

def load_mnist_label(file):
	with open(file_path+"/"+file, 'rb') as f:
		return np.frombuffer(f.read(), np.uint8, offset=8)

def load_mnist_images(file):
	with open(file_path+"/"+file, 'rb') as f:
		images=np.frombuffer(f.read(), np.uint8, offset=16)
		return images.reshape(-1, 784)

def softmax(a):
	exp_a=np.exp(a-np.max(a))
	sum_exp_a=np.sum(exp_a)
	return exp_a/sum_exp_a

def predict_sigmoid(network, x):
	W1, W2, W3 = network['W1'], network['W2'], network['W3']
	b1, b2, b3 = network['b1'], network['b2'], network['b3']

	a1=np.dot(np.float128(x), W1)+b1
	z1=sigmoid(a1)
	a2=np.dot(z1, W2)+b2
	z2=sigmoid(a2)
	a3=np.dot(z2, W3)+b3
	y=softmax(a3)

	return y

def predict_reLU(network, x):
	W1, W2, W3 = network['W1'], network['W2'], network['W3']
	b1, b2, b3 = network['b1'], network['b2'], network['b3']

	a1=np.dot(np.float128(x), W1)+b1
	z1=reLU(a1)
	a2=np.dot(z1, W2)+b2
	z2=reLU(a2)
	a3=np.dot(z2, W3)+b3
	#y=softmax(a3)
	y=a3

	return y

sigmoid=	lambda x: 1/(1+np.exp(-x))
reLU=		lambda x: np.maximum(0, x)

dataset = {}
dataset['train_img']= load_mnist_images(key_file['train_img'])
dataset['train_label'] = load_mnist_label(key_file['train_label'])	
dataset['test_img'] = load_mnist_images(key_file['test_img'])
dataset['test_label'] = load_mnist_label(key_file['test_label'])

network=init_network()

(train_img, train_label), (test_img, test_label) = \
		(dataset['train_img'], dataset['train_label']), (dataset['test_img'], dataset['test_label'])

batch_size=100

#train image+sigmoid
accuracy_count=0
for i in range(0, len(train_img), batch_size):
	y=predict_sigmoid(network, train_img[i:i+batch_size])
	p=np.argmax(y, axis=1)
	accuracy_count += np.sum(p == train_label[i:i+batch_size])

print("%-35s" % "train image Accuracy with sigmoid:", "%-0.5f" % float(str(float(accuracy_count)/len(train_img))))

#train image+reLU
accuracy_count=0
for i in range(0, len(train_img), batch_size):
	y=predict_reLU(network, train_img[i:i+batch_size])
	p=np.argmax(y, axis=1)
	accuracy_count += np.sum(p == train_label[i:i+batch_size])

print("%-35s" % "train image Accuracy with reLU:", "%-0.5f" % float(str(float(accuracy_count)/len(train_img))))

#test image+sigmoid
accuracy_count=0
for i in range(0, len(test_img), batch_size):
	y=predict_sigmoid(network, test_img[i:i+batch_size])
	p=np.argmax(y, axis=1)
	accuracy_count += np.sum(p == test_label[i:i+batch_size])

print("%-35s" % "test image Accuracy with sigmoid:", "%-0.5f" % float(str(float(accuracy_count)/len(test_img))))

#test image+reLU
accuracy_count=0
for i in range(0, len(test_img), batch_size):
	y=predict_reLU(network, test_img[i:i+batch_size])
	p=np.argmax(y, axis=1)
	accuracy_count += np.sum(p == test_label[i:i+batch_size])

print("%-35s" % "test image Accuracy with reLU:", "%-0.5f" % float(str(float(accuracy_count)/len(test_img))))
