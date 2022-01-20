import numpy as np
from env.env import *

'''
@brief 各矩阵的构建，包括元素矩阵、中止状态矩阵和位置矩阵
'''
def construct_mat(filename):
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            s = line.split()
            if not line:
                break
            for id, ele in enumerate(s):
                '''维护位置矩阵'''
                if len(mat_pos) < id+1:
                    mat_pos.insert(id, [])
                mat_pos[id].append(ele)
                '''维护元素矩阵'''
                mat_ele_set.add(ele)
                '''维护终止状态矩阵'''
                if (id == len(s)-1):
                    mat_end_set.add(ele)

    '''将set转回为list'''
    mat_ele = list(mat_ele_set)
    mat_end = list(mat_end_set)
    sta_num = len(mat_ele)


'''
@brief 根据 epsilon-greedy 选择动作
@param state 输入状态
@param R reward矩阵
@return [next_state, reward] 根据action达到的下一个状态，以及这个action带来的reward
'''
def epsilon_greedy(state, R):
    r = np.random.rand()
    if r < eps: # 贪心选
        reward = (R[state]).max()
        next_state = np.argwhere(R[state] == reward)[0][1]
    else :  # 随机选
        next_state = np.random.randint(0, sta_num-1, 1)
        reward = R[state, next_state]
    return [next_state, reward]