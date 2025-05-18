import matplotlib.pyplot as plt
import numpy as np

def plot_entropy(entropy_log):
    plt.figure(figsize=(10, 5))
    plt.plot(entropy_log, label="Entropy")
    plt.title("Entropy Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Entropy")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_bitstring_history(bit_history):
    array = np.array([[int(bit) for bit in state] for state in bit_history])
    plt.figure(figsize=(10, 5))
    plt.imshow(array.T, cmap="binary", aspect="auto", interpolation="nearest")
    plt.title("Bitstring State Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Bit Index")
    plt.tight_layout()
    plt.show()
