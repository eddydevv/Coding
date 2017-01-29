import glob
import os.path, os
import matplotlib.pyplot as plt
import math

participants = []
info = {}

def max_y(info):
    x = []
    for k,v in info.items():
        x.extend(v['counts'])

    return math.ceil(max(x))


def read_files():
    for file_name in glob.glob('./test_results/*.txt'):
        with open(file_name, 'r') as f:
            lines = f.readlines()

        x, y = [], []
        for line in lines[6:]:
            line = line.split()
            x.append(int(line[0]))
            y.append(float(line[1]))

        basename = os.path.basename(file_name).strip('.txt')
        info[basename] = {}
        info[basename]['rand_nums'] = x
        info[basename]['counts'] = y

    return info


class Participant:
    def __init__(self, code_name, p_info):
        self.code_name = code_name
        self.data = p_info

    def __str__(self):
        return str(self.code_name) + ": " + str(self.data)


class Graph:
    def __init__(self, participant):
        self.participant = participant
        self.x = []
        self.y = []

    def coordinates(self, rand_nums, counts):
        self.x = rand_nums
        self.y = counts

    def plot_graph(self, limx, limy):
        plt.xlim(0,limx)
        plt.ylim(0,limy)
        plt.plot(self.x,self.y,'ro')
        graph_dir = "./graphs/"
        if not os.path.exists(graph_dir):
            os.makedirs(graph_dir)

        graph_path = os.path.join(graph_dir, self.participant + '.png')
        plt.savefig(graph_path)
        plt.close()



participants = read_files()
max_count = max_y(participants)
for k,v in participants.items():
    p = Participant(k, v)
    g = Graph(p.code_name)
    g.coordinates(p.data['rand_nums'], p.data['counts'])
    y = math.ceil(max(p.data['counts']))
    g.plot_graph(18, max_count + 1)
