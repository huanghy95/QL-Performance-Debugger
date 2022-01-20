import numpy as np
import os
from env.env import *

'''
@brief 对待检测日志序列进行性能评估
@param input 待检测日志存放位置
@param output 评估结果输出位置
@param Q Q表
'''
def performance_evaluator(input, output, Q, mat_ele, mat_pos, mat_end):
    if os.path.exists(visualize_path+'r1.txt'):  # 如果文件存在
        os.remove(visualize_path+'r1.txt')
    if os.path.exists(visualize_path+'r2.txt'):  # 如果文件存在
        os.remove(visualize_path+'r2.txt')
    if os.path.exists(visualize_path+'r3.txt'):  # 如果文件存在
        os.remove(visualize_path+'r3.txt')
    if os.path.exists(visualize_path+'r4.txt'):  # 如果文件存在
        os.remove(visualize_path+'r4.txt')
    cnt = 0
    with open(input, 'r') as f:
        with open(output, 'w') as fo:
            while True:
                '''初始化各分值'''
                point_score = 0.0
                order_score = 0.0
                env_score = 0.0
                line = f.readline()
                cnt += 1
                s = line.split()
                if not line:
                    break
                last = -1

                for id,ele in enumerate(s):
                    '''遍历到终节点'''
                    if id == len(s)-1:
                        if ele not in mat_end:
                            '''终止节点非法，群组score增加'''
                            env_score += 8
                        break

                    if id >= len(mat_pos) or ele not in mat_pos[id]:
                        '''节点位置非法，群组score增加'''
                        env_score += 4
                    
                    '''节点正常'''
                    if ele in mat_ele:
                        if last != -1:
                            '''确认日志序列中动作Q值'''
                            qs = Q[mat_ele.index(last), mat_ele.index(ele)]
                            '''根据Q表中的值和threshold计算顺序score'''
                            order_score = (order_score + threshold - qs) if qs < threshold else order_score
                        last = ele
                    else:
                        '''节点异常，点性能分数增加'''
                        point_score += 10
                        last = -1
                
                '''转储各分数'''
                order_score /= threshold
                point_score_list.append(point_score)
                env_score_list.append(env_score)
                order_score_list.append(order_score)
                tot_score_list.append(point_score+env_score+order_score)
                
                '''将结果写入result文件'''
                fo.write('Log Sequence '+str(cnt)+': [point_score: '+str(point_score)+', order_score: '+str(order_score)+', env_score: '+str(env_score)+']\n')
                with open(visualize_path+'r1.txt', 'a') as f1:
                    f1.write(str(point_score+env_score+order_score)+'\n')
                with open(visualize_path+'r2.txt', 'a') as f1:
                    f1.write(str(point_score)+'\n')
                with open(visualize_path+'r3.txt', 'a') as f1:
                    f1.write(str(order_score)+'\n')
                with open(visualize_path+'r4.txt', 'a') as f1:
                    f1.write(str(env_score)+'\n')