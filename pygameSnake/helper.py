import matplotlib.pyplot as plt
from IPython import display

plt.ion()


# def plot_score(scores, mean_scores):
#     display.clear_output(wait=True)
#     display.display(plt.gcf())
#     plt.clf()
#     plt.title('Training...')
#     plt.xlabel('Number of Games')
#     plt.ylabel('Score')
#     plt.plot(scores)
#     plt.plot(mean_scores)
#     plt.ylim(ymin=0)
#     plt.text(len(scores)-1, scores[-1], str(scores[-1]))
#     plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
#     plt.show(block=False)
#     plt.pause(.1)
#
#
# def save_score_graph():
#     plt.savefig("result_graph.png")


def plot_interaction_graph(random, instruction, mean):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Interval(5s)')
    plt.ylabel('Times of Interaction')
    plt.plot(instruction)
    plt.plot(random)
    plt.plot(mean)
    plt.ylim(ymin=0)
    plt.text(len(instruction) - 1, instruction[-1], "Instr:"+str(instruction[-1]))
    plt.text(len(random)-1, random[-1], "Rand:"+str(random[-1]))
    plt.text(len(mean)-1, mean[-1], "Mean:"+str(mean[-1]))
    plt.show(block=False)
    plt.pause(.1)


def save_interaction_graph():
    plt.savefig("interactive_graph.png")

