import numpy as np

'''检测时Q表阈值大小'''
threshold = 300
'''epsilon-greedy参数'''
eps = 0.8
'''学习率'''
γ = 0.8

'''各种文件路径'''
standard_file = './standard.txt'
q_file = './q.txt'
inp_file = './inp.txt'
res_file = './res.txt'
report_file = './report.txt'
visualize_path = './visualize/'


mat_ele = []   # 元素矩阵，存储所有状态
mat_pos = []        # 位置矩阵，是一个二维矩阵，表示每个位置对应的元素的可能情况
mat_end = []   # 终止状态矩阵
sta_num = 0         # 状态数

mat_ele_set = set([])   # 元素矩阵，存储所有状态
mat_end_set = set([])   # 终止状态矩阵

point_score_list = []   # 点性能异常分数
order_score_list = []   # 序列性能异常分数
env_score_list = []     # 组群性能异常分数
tot_score_list = []     # 总分数