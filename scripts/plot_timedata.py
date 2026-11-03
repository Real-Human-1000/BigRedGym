
import matplotlib.pyplot as plt

def parse_datum(dat):
    # Parse as a bool or as a float
    if dat in ["True", "False"]:
        return True if dat == "True" else False
    else:
        return float(dat)


if __name__ == "__main__":
    with open("logs\\timedata.csv", "r") as log_file:
        # I'm not even going to bother with a proper CSV reader. I know what I'm doing
        start_step = 300
        end_step = 400
        lines = log_file.readlines()
        head = lines[0].strip().split(",")
        data = [[parse_datum(datum) for datum in line.split(",")] for line in lines[(start_step+1):(end_step+1)]]  # trim the head and tail to just get good data
        for idx in range(1,len(head)):
            plt.subplot(2, 2, ((idx-1) % 4) + 1)
            plt.plot([d[0] for d in data], [d[idx] for d in data], label=head[idx])
            plt.legend()
        plt.gcf().suptitle("Features over time")
        plt.gcf().supxlabel("Time (simulation steps)")
        plt.gcf().supylabel("Values")
        plt.show()

