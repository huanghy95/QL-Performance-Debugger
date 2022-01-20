import numpy as np
print("===checkpoint1===")
import matplotlib.pyplot as plt
print("===checkpoint2===")

tot_score = []
point_score = []
order_score = []
env_score = []


lost1 = []
lost2 = []
lost3 = []

log_id = []
tot = 0
tot2 = 0
tot3 = 0


with open('./r1.txt', 'r') as f:
    line = f.readline()
    while line:
        tot = tot + 1
        tot_score.append(float(line))
        line = f.readline()

with open('./r2.txt', 'r') as f:
    line = f.readline()
    while line:
        # tot2 = tot2 + 1
        point_score.append(float(line))
        line = f.readline()

with open('./r3.txt', 'r') as f:
    line = f.readline()
    while line:
        # tot3 = tot3 + 1
        # if tot3 == tot:
        #     break
        order_score.append(float(line))
        line = f.readline()

with open('./r4.txt', 'r') as f:
    line = f.readline()
    while line:
        # tot3 = tot3 + 1
        # if tot3 == tot:
        #     break
        env_score.append(float(line))
        line = f.readline()
        

for i in range(tot):
    log_id.append(i)

# print(log_id)


#第一行第一列图形
#第一行第二列图形
plt.figure()
plt.plot(log_id, point_score, 'green', label="point_score")


plt.legend(loc = 0)
plt.xlabel('Log-ID')
plt.ylabel('Performance-Problem-Score')
# plt.xlim(0, episodes)
# plt.ylim(-100, 0)
plt.title("Performance-Debug-Evaluator")

plt.savefig('./visualize1.png')

plt.figure()
plt.plot(log_id, env_score, 'orange', label="env_score")

plt.legend(loc = 0)
plt.xlabel('Log-ID')
plt.ylabel('Performance-Problem-Score')
# plt.xlim(0, episodes)
# plt.ylim(-100, 0)
plt.title("Performance-Debug-Evaluator")

plt.savefig('./visualize2.png')


plt.figure()
plt.plot(log_id, order_score, 'blue', label="order_score")

plt.legend(loc = 0)
plt.xlabel('Log-ID')
plt.ylabel('Performance-Problem-Score')
# plt.xlim(0, episodes)
# plt.ylim(-100, 0)
plt.title("Performance-Debug-Evaluator")

plt.savefig('./visualize3.png')


plt.figure()
plt.plot(log_id, tot_score, 'r', label="tot_score")

plt.legend(loc = 0)
plt.xlabel('Log-ID')
plt.ylabel('Performance-Problem-Score')
# plt.xlim(0, episodes)
# plt.ylim(-100, 0)
plt.title("Performance-Debug-Evaluator")

plt.savefig('./visualize4.png')