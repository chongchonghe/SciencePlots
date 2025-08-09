import numpy as np
import matplotlib.pyplot as plt
import scienceplots as sp

import os

# Check we are in examples dir
current_dir = os.getcwd().lower()
if current_dir.endswith("scienceplots"):
    os.chdir("./examples")
# Create 'figures' folder if it does not exist
if not os.path.exists("./figures"):
    os.makedirs("figures")

def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))

def main():
    print("sp.figsize = ", sp.figsize)

    pparam = dict(xlabel="Voltage (mV)", ylabel=r"Current ($\mu$A)")

    x = np.linspace(0.75, 1.25, 201)

    def plot_my(figname, nlines=6):
        fig, ax = plt.subplots()
        ps = [10, 15, 20, 30, 50, 100]
        for p in ps[:nlines]:
            ax.plot(x, model(x, p), label=p)
        ax.legend(title="Order")
        ax.autoscale(tight=True)
        ax.set(**pparam)
        fig.savefig(figname, dpi=300)
        plt.close()

    # with plt.style.context(["science", "nature"]):
    #     plot_my("fig-my.jpg")
    with plt.style.context(["my"]):
        plot_my("fig-my-my.jpg")
    with plt.style.context(["poster"]):
        plot_my("fig-my-poster.jpg", nlines=2)
    with plt.style.context(["poster-bigger"]):
        plot_my("fig-my-poster-bigger.jpg", nlines=6)

if __name__ == "__main__":
    main()