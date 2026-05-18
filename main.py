from load_data import load_data
from sort import bubble_sort
import numpy as np
import matplotlib.pyplot as plt


def main():
    print("Hello from programmier-bung-2-aufgabe-1-dummy!")
    data = load_data("activity.csv")
    power_W = data["PowerOriginal"]
    sorted_power_W = bubble_sort(power_W)
    plt.title("Leistungskurve")
    time_axis_sec = np.arange(len(sorted_power_W))
    time_axis_min = time_axis_sec / 60
    plt.xlabel("Zeit t/min")
    plt.ylabel("Leistung W")
    plt.plot(time_axis_min, sorted_power_W[::-1])
    plt.savefig("leistungskurve.png")
    plt.show


if __name__ == "__main__":
    main()
