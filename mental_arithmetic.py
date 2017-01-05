import random
import os.path, os
import datetime
import time
import matplotlib.pyplot as plt

cp = ""
options = '1'
participants = []
info = {}

def generate_rand():
    rand_num = random.randint(1,17)
    arr = []
    print()
    print("-" * 50)
    print("The random number is", rand_num)
    i = 100
    while(i >= 0):
      arr.append(i)
      i -= rand_num

    for i in range(len(arr)):
        if(i%5 == 0):
            print()

        print("%d" % arr[i], end="\t")
    print("\n")
    print("-" * 50)
    return rand_num


def record_count(r, p):
    count, rand_nums, date_time = [], [], []
    input("Press Enter to start timer...")
    start_time = time.time()
    input("Press Enter to stop timer...")
    end_time = time.time()
    record = end_time - start_time
    print("-" * 50)
    info[p]['count'].append(str(round(float(record), 4)))
    info[p]['rand_nums'].append(str(r))
    info[p]['date_time'].append(str(datetime.datetime.now()))
    print(info)
    file(p)


def file_path(p, file_type, doc_type):
    path = "./test_results/"
    timed_path = "./test_results/timestamped/"
    if not os.path.exists(timed_path):
        os.makedirs(timed_path)

    if doc_type == 'summary':
        file_name  = p + file_type
    elif doc_type == 'timestamped':
        file_name = p + str(datetime.datetime.now()) + file_type
        path = timed_path

    complete_name = os.path.join(path ,file_name)
    return complete_name


def plot_graph():
    for p in participants:
        plt.plot(info[p]['rand_nums'], info[p]['count'], 'ro')
        plt.xlim(0,18)
        plt.ylim(0,float(max(info[p]['count']))+1)
        plt.savefig(file_path(p, ".png", "timestamped"))

        with open(file_path(p, ".txt", "summary")) as f:
            lines = f.readlines()

        x, y = [], []
        for line in lines[6:]:
            line = line.split()
            x.append(int(line[0]))
            y.append(float(line[1]))

        plt.xlim(0,18)
        plt.ylim(0,120)
        plt.plot(x,y,'ro')
        print(x,y)
        plt.savefig(file_path(p, ".png", "summary"))
        plt.close()


def show_info():
    for p in participants:
        print("")
        print("-" * 50)
        print("Information for", p)
        print("")
        print("  Random Number        Count")
        print("-----------------    ---------")
        for i in range(len(info[p]['count'])):
            print("\t" + info[p]['rand_nums'][i] + "\t\t" + info[p]['count'][i])
        print("-" * 50)


def file(p):
    tpath = file_path(p, ".txt", "timestamped")
    spath = file_path(p, ".txt", "summary")
    timestamped_file = {'path': tpath, 'file': open(tpath, 'w')}
    summary_file = {'path': spath, 'file': open(spath, 'a')}
    for f in [timestamped_file, summary_file]:
        if(os.path.getsize(f['path']) == 0):
            f['file'].write("-" * 80 + "\n\n")
            f['file'].write(" "* 30 + p + "\n")
            f['file'].write("-" *80 + "\n")
            f['file'].write("  Random Number          Count                          DateTime\n")
            f['file'].write("-----------------      ---------      -----------------------------------------\n")
            for i in range(len(info[p]['count'])):
                f['file'].write("\t" + info[p]['rand_nums'][i] + "\t\t" + info[p]['count'][i] + "\t\t" + info[p]['date_time'][i] + "\n")
        else:
            f['file'].write("\t" + info[p]['rand_nums'][-1] + "\t\t" + info[p]['count'][-1] + "\t\t" + info[p]['date_time'][-1] + "\n")

        if(f['file'] == timestamped_file):
            f['file'].write("-" * 80 + "\n")
            f['file'].write("\n")
        f['file'].close()


def enter_name():
    p = input("Enter name of participant: ")
    print("")
    if p not in participants:
        participants.append(p)
        info[p] = { 'rand_nums': [], 'count': [], 'date_time': []}

    return p


cp = enter_name()
while(options != '0'):
    print("Enter one of the options below")
    print("1: Start Test, 2: Show Info, 3: Change Participant, 0:Exit")
    options = input()
    if(options == '1'):
        r = generate_rand()
        record_count(r, cp)
        plot_graph()
    elif(options == '2'):
        show_info()
    elif(options == '3'):
        cp = enter_name()
