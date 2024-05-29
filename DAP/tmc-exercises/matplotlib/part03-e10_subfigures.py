import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    _, ax = plt.subplots(1, 2)

    ax[0].plot(a[:, 0], a[:, 1])
    ax[0].set_title("Line plot")
    ax[0].set_xlabel("X")
    ax[0].set_ylabel("Y")

    ax[1].scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3])
    ax[1].set_title("Scatter plot")
    ax[1].set_xlabel("X")
    ax[1].set_ylabel("Y")

    plt.show()


def main():
    pass

if __name__ == "__main__":
    main()
