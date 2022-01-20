import numpy as np
from env.env import *
from utils.output import write_Q, write_report
from evaluator import performance_evaluator

Q = []  # Q表

'''
@brief 各矩阵的构建，包括元素矩阵、中止状态矩阵和位置矩阵
'''
def construct_mat(filename):
    global mat_ele,mat_end, sta_num
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
@brief 构建reward矩阵
@param s 用于构建reward的日志序列
@return R 构建好的reward矩阵
'''
def construct_R(s):
    R = np.zeros((sta_num, sta_num))
    R = np.matrix(R)
    last = -1
    for id, ele in enumerate(s):
        cur = mat_ele.index(ele)
        if last != -1:
            '''一般合法动作赋值为10'''
            R[last, cur] = 10
            if id == len(s)-1:
                '''达到终点的动作赋值为100'''
                R[last, cur] = 100
        last = cur
    return R


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

'''
@brief Q-learning过程，根据标准日志构造Q表
@param filename 标准日志存放位置
'''
def Q_Learning(filename):
    global Q
    '''初始化矩阵'''
    Q = np.zeros((sta_num, sta_num))
    Q = np.matrix(Q)
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            s = line.split()
            if not line:
                break
            R = construct_R(s)
            for id,ele in enumerate(s):
                if id == len(s)-1:
                    break
                '''初始状态为当前步对应节点'''
                state = mat_ele.index(ele)
                '''epsilon greedy选下一个状态'''
                [next_state, reward] = epsilon_greedy(state, R)
                '''根据reward是否为0决定是否需要更新Q表'''
                if reward != 0:
                    '''更新Q表'''
                    Q[state, next_state] = R[state, next_state] + γ *(Q[next_state]).max()  #更新





if __name__ == '__main__':
    '''根据标准日志序列构造各矩阵'''
    construct_mat(standard_file)
    '''根据标准日志序列进行Q-Learning，构造Q表'''
    Q_Learning(standard_file)
    '''将Q表写入中间文件'''
    write_Q(q_file, Q)
    '''进行性能分析'''
    performance_evaluator(inp_file, res_file, Q, mat_ele, mat_pos, mat_end)
    '''写分析报告'''
    write_report(point_score_list,env_score_list,order_score_list,tot_score_list, Q)


 