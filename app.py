#!/usr/bin/python

import fileinput
from random import randint, choice
from termcolor import colored
import time
import os

class Tensor(object):
    def __init__(self, m: int, n: int, p: int):
        '''
        Initialize m x n matrix to random values
        '''
        os.system('clear')
        self.tensor = []
        for i in range(p):
            self.tensor.append([[randint(0,9) for i in range(n)] for j in range(m)])

    def tensor_glow(self):
        '''
        Tensor glow!
        '''
        while True:
            for i in range(len(self.tensor)):
                matrix = self.tensor[i]
                print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) for row in self.brighten_matrix(matrix)]))
                print('\n' + 'matrix: ' + str(i+1))
                time.sleep(0.5)
                os.system('clear')
            i = 0

    def brighten_matrix(self, matrix):
        '''
        Brighten a matrix
        '''
        glowing_matrix = []
        for tensor in matrix:
            glowing_matrix.append(self.brighten_tensor(tensor))
        return glowing_matrix
    
    def brighten_tensor(self, tensor):
        '''
        Brighten a tensor
        '''
        glowing_colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        glowing_tensor = []
        for value in tensor:
            glowing_tensor.append(colored(str(value), choice(glowing_colors), attrs=['bold']))
        return glowing_tensor

if __name__ == '__main__':
    m, n, p = input("Enter dimensions for m x n x p tensor: ").split()
    my_tensor = Tensor(int(m), int(n), int(p))
    my_tensor.tensor_glow()