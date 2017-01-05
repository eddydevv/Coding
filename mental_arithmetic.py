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


def file_path(p, file_type):
    path = "./test_results/"
    if not os.path.exists(path):
        os.makedirs(path)

    file_name = p + str(datetime.datetime.now()) + file_type
    complete_name = os.path.join(path ,file_name)
    return complete_name


def plot_graph():
    for p in participants:
        plt.plot(info[p]['rand_nums'], info[p]['count'], 'ro')
        plt.xlim(0,18)
        plt.ylim(0,110)
        plt.savefig(file_path(p, ".png"))


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
        file(p)


def file(p):
    f = open(file_path(p, ".txt"), 'w')
    f.write("-" * 80 + "\n\n")
    f.write(" "* 30 + p + "\n")
    f.write("-" *80 + "\n")
    f.write("  Random Number          Count                          DateTime\n")
    f.write("-----------------      ---------      -----------------------------------------\n")
    for i in range(len(info[p]['count'])):
        f.write("\t" + info[p]['rand_nums'][i] + "\t\t" + info[p]['count'][i] + "\t\t" + info[p]['date_time'][i] + "\n")
    f.write("-" * 80 + "\n")
    f.write("\n")
    f.close()


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
    elif(options == '2'):
        plot_graph()
        show_info()
    elif(options == '3'):
        cp = enter_name()
