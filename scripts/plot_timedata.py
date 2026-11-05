
import matplotlib.pyplot as plt

def parse_datum(dat):
    # Parse as a bool or as a float
    if dat in ["True", "False"]:
        return True if dat == "True" else False
    else:
        return float(dat)


if __name__ == "__main__":
    LEG_GAIN_NAMES = [
        "FL",
        "FR",
        "RL",
        "RR"
    ]

    with open("logs\\timedata.csv", "r") as log_file:
        # I'm not even going to bother with a proper CSV reader. I know what I'm doing
        start_step = 100
        end_step = 200
        lines = log_file.readlines()
        head = lines[0].strip().split(",")
        data = [[parse_datum(datum) for datum in line.split(",")] for line in lines[(start_step+1):(end_step+1)]]  # trim the head and tail to just get good data

        # Plot trajectories of data for each leg
        for idx in range(1,len(head)):
            # Find which leg this is
            leg_name = LEG_GAIN_NAMES[0]
            leg_idx = 0
            for j in range(len(LEG_GAIN_NAMES)):
                if LEG_GAIN_NAMES[j] in head[idx]:
                    leg_name = LEG_GAIN_NAMES[j]
                    leg_idx = j

            plt.subplot(2, 2, leg_idx+1)  # ((idx-1) % 4) + 1
            plt.plot([d[0] for d in data], [d[idx] for d in data], label=head[idx])
            plt.legend()
        plt.gcf().suptitle("Features over time")
        plt.gcf().supxlabel("Time (simulation steps)")
        plt.gcf().supylabel("Values")
        plt.show()

        # Plot gait diagrams over the same timespan
        # Actual foot contact force is index 1 + 2 * 4 and actual foot height is index 1 + 3 * 4
        plt.clf()
        for idx in range(4):
            # Construct lines for when the foot is in contact
            contact = [(d[0], idx) for d in data if d[1+2*4+idx] > 0]
            stance = [(d[0], idx) for d in data if d[1+idx] > 0]
            plt.plot([d[0] for d in contact], [d[1] for d in contact], 'o', label=head[1+2*4+idx])
            plt.plot([d[0] for d in stance], [d[1]+0.1 for d in stance], 'o', label=head[1+idx])
        plt.legend()
        plt.title("Gait diagram")
        plt.xlabel("Time (steps)")
        plt.ylabel("Leg index")
        plt.show()

        # Plot DOF target & pos trajectories
        dof_joint_names = ["hip", "thigh", "calf"]
        plt.clf()
        # Plot actual DOF positions
        for idx in range(17,17+12):
            # Find which leg and joint this is
            leg_name = LEG_GAIN_NAMES[0]
            leg_idx = 0
            joint_name = dof_joint_names[0]
            joint_idx = 0
            for l in range(len(LEG_GAIN_NAMES)):
                if LEG_GAIN_NAMES[l] in head[idx]:
                    leg_name = LEG_GAIN_NAMES[l]
                    leg_idx = l
            for j in range(len(dof_joint_names)):
                if dof_joint_names[j] in head[idx]:
                    joint_name = dof_joint_names[j]
                    joint_idx = j
            plt.subplot(4, 3, 1 + leg_idx * 3 + joint_idx)
            plt.plot([d[0] for d in data], [d[idx] for d in data], label=head[idx])
        # Plot target DOF positions
        for idx in range(17+12,17+12+12):
            # Find which leg and joint this is
            leg_name = LEG_GAIN_NAMES[0]
            leg_idx = 0
            joint_name = dof_joint_names[0]
            joint_idx = 0
            for l in range(len(LEG_GAIN_NAMES)):
                if LEG_GAIN_NAMES[l] in head[idx]:
                    leg_name = LEG_GAIN_NAMES[l]
                    leg_idx = l
            for j in range(len(dof_joint_names)):
                if dof_joint_names[j] in head[idx]:
                    joint_name = dof_joint_names[j]
                    joint_idx = j
            plt.subplot(4, 3, 1 + leg_idx * 3 + joint_idx)
            plt.plot([d[0] for d in data], [d[idx] for d in data], ':', label=head[idx])
            plt.legend()
        plt.gcf().suptitle("DOF Trajectories")
        plt.gcf().supxlabel("Time (steps)")
        plt.gcf().supylabel("Angle (radians)")
        plt.show()


