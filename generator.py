import numpy as np

max_len = 10
cor_log_num = 1000
sta_num = 30

ck_log_num = 500
ck_sta_num = 40

eps = 0.95

standard = []
standard_num = 10
standard_sta = 10

for i in range(standard_num):
    l = int(np.random.randint(2, max_len-1, 1))
    ar = []
    for j in range(l):
        sta = np.random.randint(0, standard_sta-1, 1)
        ar.append(sta)
    standard.append(ar)

with open('standard.txt', 'w') as f:
    for i in range(cor_log_num):
        r = np.random.rand()
        if r < eps:
            choice = np.random.randint(0, standard_num-1, 1)[0]
            for ele in standard[choice]:
                f.write(str(int(ele))+' ')
            f.write('\n')
        else :
            l = int(np.random.randint(2, max_len-1, 1))
            for j in range(l):
                sta = np.random.randint(0, sta_num-1, 1)
                f.write(str(int(sta))+' ')
            f.write('\n')
        
with open('inp.txt', 'w') as f:
    for i in range(ck_log_num):
        r = np.random.rand()
        if r < eps:
            l = int(np.random.randint(2, max_len-1, 1))
            for j in range(l):
                sta = np.random.randint(0, standard_sta-1, 1)
                f.write(str(int(sta))+' ')
            f.write('\n')
        else :
            l = int(np.random.randint(2, max_len-1, 1))
            for j in range(l):
                sta = np.random.randint(0, ck_sta_num-1, 1)
                f.write(str(int(sta))+' ')
            f.write('\n')
        