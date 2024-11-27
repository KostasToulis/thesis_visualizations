import matplotlib.pyplot as plt
import numpy as np

best_trajectory = np.loadtxt('bestTrajectory.txt')
search_trajectory = np.loadtxt('searchTrajectory.txt')
best_costs = np.loadtxt('bestCosts.txt')


# def plot_search_trajectories(best_trajectory, search_trajectory):
    # # Create a figure and two subplots vertically aligned
    # fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    #
    # # Create the line charts
    # ax1.plot(best_trajectory[:, 0], best_trajectory[:, 1], label='Best Trajectory', color='red')
    # ax2.plot(search_trajectory[:, 0], search_trajectory[:, 1], label='Search Trajectory', color='red')
    #
    # # Add labels and title to the first subplot
    # ax1.set_ylabel('Value')
    # ax1.set_title('Best Trajectory')
    # ax1.legend()
    #
    # # Add labels and title to the second subplot
    # ax2.set_xlabel('Row Number')
    # ax2.set_ylabel('Value')
    # ax2.set_title('Search Trajectory')
    # ax2.legend()
    #
    # # Show the plot
    # plt.show()


def plot_search_trajectory(search_trajectory):
    fig, ax = plt.subplots()
    ax.plot(search_trajectory[:, 0], search_trajectory[:, 1], label='Search Trajectory', color='gray')
    ax.set_xlabel("LS Iteration", fontsize=28)
    ax.set_ylabel("Solution Cost", fontsize=28)

    # ax.set_xticklabels([0, 1000, 2000, 3000, 4000], fontsize=24)
    # ax.set_yticklabels([500, 530, 560, 590, 620], fontsize=24)
    ax.xaxis.tick_top()
    ax.yaxis.tick_right()

    # plt.ylim([490, 630])
    # plt.xlim([-200,5000])
    plt.show()

def plot_costs(best_costs):

    fig, ax = plt.subplots()
    x = [i+1 for i in range(len(best_costs))]

    ax.bar(x, best_costs, color='gray')
    ax.set_xticklabels(x, fontsize=24)
    ax.set_yticklabels([480, 490, 500, 510, 520, 530], fontsize=24)
    ax.yaxis.tick_right()
    ax.set_ylabel('Solution Cost', fontsize=26)
    ax.set_xlabel('LNS iteration', fontsize=26)
    # ax.set_title('Solution Cost Evolution per LNS Iteration', fontsize=24)


    plt.ylim([480, 530])
    plt.show()


plot_search_trajectory(search_trajectory)
# plot_costs(best_costs)