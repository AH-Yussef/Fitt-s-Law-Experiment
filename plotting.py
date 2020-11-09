import matplotlib.pyplot as plt
import numpy as np

def plot_ID_vs_MT(event):
    all_data = np.genfromtxt("data/all_data.csv", names=True, dtype="float", delimiter=",")

    x = all_data["ID"]
    y = all_data["MT"]

    fig = plt.figure()
    axes = fig.gca()
    plt.plot(x, y, "o")
    plt.grid()
    plt.xlabel("index of difficulty")
    plt.ylabel("movement time (sec)")


    m, c = np.polyfit(x, y, 1)
    b = float("{0:.3f}".format(m))
    a = float("{0:.3f}".format(c))

    plt.title("ID vs MT \n (a={}, b={})".format(a, b), fontsize=15)

    plt.plot(x, m*x + c, c="red")
    plt.show()

def plot_D_vs_MT(event):
    all_data = np.genfromtxt("data/all_data.csv", names=True, dtype="float", delimiter=",")

    x = all_data["D"]
    y = all_data["MT"]

    fig = plt.figure()
    axes = fig.gca()
    plt.plot(x, y, "o")
    plt.title("D vs MT ", fontsize=15)
    plt.grid()
    plt.title("D vs MT", fontsize=18)
    plt.xlabel("distance (px)")
    plt.ylabel("movement time (sec)")

    m, c = np.polyfit(x, y, 1)
    plt.plot(x, m*x + c, c="red")

    plt.show()

def plot_W_vs_MT(event):
    all_data = np.genfromtxt("data/all_data.csv", names=True, dtype="float", delimiter=",")

    x = all_data["W"]
    y = all_data["MT"]

    fig = plt.figure()
    axes = fig.gca()
    plt.plot(x, y, "o")
    plt.grid()
    plt.title("W vs MT", fontsize=18)
    plt.xlabel("width (px)")
    plt.ylabel("movement time (sec)")

    m, c = np.polyfit(x, y, 1)
    plt.plot(x, m*x + c, c="red")

    plt.show()

