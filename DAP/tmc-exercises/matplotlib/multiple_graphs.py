#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def main():
    x1=np.array([2,4,6,7])
    y1=np.array([4,3,5,1])
    x2=np.array([1,2,3,4])
    y2=np.array([4,2,3,1])
    plt.plot(x1, y1, label='Line 1')
    plt.plot(x2, y2, label='Line 2')
    plt.title("My first figure") 
    plt.xlabel("My x-axis")       
    plt.ylabel("My y-axis")  
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
