import random

def Greedy(JobList, ProcessorsTime):
    for i in range(len(JobList)):
        ProcessorsTime[findMin(ProcessorsTime)[1]] += JobList[i]
    return ProcessorsTime
def AntColony(JobList, ProcessorsTime, NOA, FT):
    for i in range(len(JobList)):
        ProcessorsTime[findMin(ProcessorsTime)[1]] += JobList[i]
    best_PT = ProcessorsTime
    ProcessorsTime = [0] * len(ProcessorsTime)
    for k in range(10):
        #FIRST ANT
        road = [False] * len(JobList)
        for i in range(len(JobList)):
            tmp = findMin(ProcessorsTime)[1]
            road[i] = tmp
            ProcessorsTime[tmp] += JobList[i]
        best = findMax(ProcessorsTime)[0]
        fermon = road
        fermon_count = FT-1
        ProcessorsTime = [0] * len(ProcessorsTime)

        #REST OF ANTS
        while(fermon_count>0):
            for ants in range(NOA):
                road = [False] * len(JobList)
                for i in range(len(JobList)):
                    lotto = random.randint(1, FT)
                    if lotto <= fermon_count:
                        destiny = fermon[i]
                    else:
                        destiny = random.randint(0,len(ProcessorsTime)-2)
                        if destiny >= fermon[i]:
                            destiny +=1
                    road[i] = destiny
                    ProcessorsTime[destiny] += JobList[i]
                if best > findMax(ProcessorsTime)[0]:
                    best = findMax(ProcessorsTime)[0]
                    fermon = road
                    best_PT = ProcessorsTime
                    fermon_count = FT-1
                ProcessorsTime = [0]*len(ProcessorsTime)
            fermon_count -= 1
    return best_PT
def findMin(tab):
    minimum_index = 0
    minimum = tab[0]
    for i in range(len(tab)):
        if(minimum > tab[i]):
            minimum = tab[i]
            minimum_index = i
    return minimum, minimum_index
def findMax(tab):
    max_index = 0
    maxi = tab[0]
    for i in range(len(tab)):
        if(maxi < tab[i]):
            maxi = tab[i]
            max_index = i
    return maxi, max_index
def rand_list(index, max_t):
    tab = []
    for i in range(index):
        rand = random.randint(1,max_t)
        tab.append(rand)
    return tab
def GetData(filename):
    try:
        with open(filename,'r') as f:
            data = f.readlines()
            for line in range(len(data)):
                data[line] = int(data[line].replace('\n', ''))
            Processors = data[0]
            Jobs = data[1]
            del data[0]
            del data[0]
    except IOError:
        with open(filename, 'w') as f:
            Processors = random.randint(25,50)
            Jobs = random.randint(50,200)
            Max_Time = 1000
            data = rand_list(Jobs, Max_Time)
            f.write(str(Processors) + "\n")
            f.write(str(Jobs) + "\n")
            for i in data:
                f.write(str(i) + "\n")
    return Processors, Jobs, data


random.seed(12)
NumOfAnts = 1000
Ferment_Time = 20
filepaths = ["m10n200.txt","m25.txt","m50.txt","m50n200.txt","m50n1000.txt"]
filepaths2 = ["Inst 1.txt","Inst 2.txt","Inst 3.txt","Inst 4.txt","Inst 5.txt","Inst 6.txt","Inst 7.txt","Inst 8.txt",
              "Inst 9.txt","Inst 10.txt","Inst 11.txt","Inst 12.txt","Inst 13.txt","Inst 14.txt","Inst 15.txt"]

for filepath in filepaths:
    data = GetData(filepath)
    JobTimes = data[2]
    Processors = data[0]
    #JobTimes = [3,1,2,2,1,3,2]
    #Processors = 3

    print("\n",filepath)
    ProcTimes = Greedy(JobTimes,[0]*Processors)
    #print("\nLista na wejściu: ",JobTimes)
    print("ALGORYTM ZACHLANNY")
    #print("Lista czasów procesów P0-Px: ", ProcTimes)
    print("Maksymalny czas (czas, procesor): ",findMax(ProcTimes))

    ProcTimes = AntColony(JobTimes,[0]*Processors, NumOfAnts, Ferment_Time)
    print("\nANT-COLONY")
    #print("Lista czasów procesów P0-Px: ", ProcTimes)
    print("Maksymalny czas (czas, procesor): ",findMax(ProcTimes))