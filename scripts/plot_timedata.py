import matplotlib.pyplot as plt

if __name__ == "__main__":
    with open("logs\\timedata.csv", "r") as log_file:
        # I'm not even going to bother with a proper CSV reader. I know what I'm doing
        lines = log_file.readlines()
        data = [[float(datum) for datum in line.split(",")] for line in lines[1:-2]]  # trim the head and tail to just get good data
        plt.plot([d[0] for d in data], [d[1] for d in data], label="Base height")
        plt.plot([d[0] for d in data], [d[2] for d in data], label="Commanded height")
        plt.legend()
        plt.title("Base Height & Command Over Time")
        plt.xlabel("Time (simulation steps)")
        plt.ylabel("Height (meters)")
        plt.show()

