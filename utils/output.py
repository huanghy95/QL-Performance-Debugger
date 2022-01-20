import numpy as np
from env.env import *

'''
@brief 将Q表写入文件中
@param filename 写入文件名
@param Q Q表
'''
def write_Q(filename, Q):
    with open(filename, 'w') as f:
        f.write(str(Q))


'''
@brief 将生成的性能分析报告写入文件
@param point_score_list 点分数序列
@param env_score_list 群组分数序列
@param order_score_list 顺序分数序列
@param tot_score_list 总分数序列
'''
def write_report(point_score_list,env_score_list,order_score_list,tot_score_list, Q):
    point_score_list = sorted(enumerate(point_score_list),key = lambda point_score_list:point_score_list[1], reverse = True)
    env_score_list = sorted(enumerate(env_score_list),key = lambda env_score_list:env_score_list[1], reverse = True)
    order_score_list = sorted(enumerate(order_score_list),key = lambda order_score_list:order_score_list[1], reverse = True)
    tot_score_list = sorted(enumerate(tot_score_list),key = lambda tot_score_list:tot_score_list[1], reverse = True)

    with open(report_file, 'w') as f:
        f.write('========== Top 10 performance delay sequences ==========\n')
        for i in range(10):
            f.write('Sequence '+str(tot_score_list[i][0])+', Score: '+str(tot_score_list[i][1])+'\n')
        f.write('\n')

        f.write('========== Top 10 env performance delay sequences ==========\n')
        for i in range(10):
            f.write('Sequence '+str(env_score_list[i][0])+', Score: '+str(env_score_list[i][1])+'\n')
        f.write('\n')

        f.write('========== Top 10 point performance delay sequences ==========\n')
        for i in range(10):
            f.write('Sequence '+str(point_score_list[i][0])+', Score: '+str(point_score_list[i][1])+'\n')
        f.write('\n')

        f.write('========== Top 10 order performance delay sequences ==========\n')
        for i in range(10):
            f.write('Sequence '+str(order_score_list[i][0])+', Score: '+str(order_score_list[i][1])+'\n')