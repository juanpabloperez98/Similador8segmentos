import numpy as np
import Backpropagation as BP


inputs = np.array([
   # 1,2,3,4,5,6,7 
    [1,1,1,1,1,1,0],#0
    [0,0,1,1,0,0,0],#1
    [0,1,1,0,1,1,1],#2
    [0,1,1,1,1,0,1],#3
    [1,0,1,1,0,0,1],#4
    [1,1,0,1,1,0,1],#5
    [1,1,0,1,1,1,1],#6
    [0,1,1,1,0,0,1],#7
    [1,1,1,1,1,1,1],#8
    [1,1,1,1,1,0,1],#9
])

outputs = np.array([
    [0,0,0,0], #0
    [0,0,0,1], #1
    [0,0,1,0],#2
    [0,0,1,1],#3
    [0,1,0,0],#4
    [0,1,0,1],#5
    [0,1,1,0],#6
    [0,1,1,1],#7
    [1,0,0,0],#8
    [1,0,0,1],#9
])


neuron = BP.NeuralNetwork(len(inputs[0]))

n = 2000

def iniciar():
    for e in range(n):
        neuron.train(inputs,outputs)