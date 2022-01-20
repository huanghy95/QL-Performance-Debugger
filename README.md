# QL-Performance-Debugger
SYSU RL HW: a performance debugger based on Q-Learning

### Architecture
```shell
.
├── env
│   ├── env.py  # 环境变量
│   └── __pycache__
│       └── env.cpython-38.pyc
├── evaluator.py # 性能分析脚本
├── generator.py # 源数据生成脚本
├── inp.txt
├── main.py # entry
├── __pycache__
│   └── evaluator.cpython-38.pyc
├── q.txt
├── README.md
├── report.txt
├── res.txt
├── standard.txt
├── utils
│   ├── output.py   # 与文件交互
│   ├── __pycache__
│   │   ├── output.cpython-38.pyc
│   │   └── utils.cpython-38.pyc
│   └── utils.py
└── visualize
    └── visualize.py # 可视化脚本
```

### Running and testing
#### Using integration script
直接运行集成脚本`hacker.sh`
```shell
bash hacker.sh
```

#### Normal method
(Optional) 生成测试数据
```shell
python3 generator.py
```
运行主函数
```shell
python3 main.py
```

(Optional) 可视化
```shell
cd visualize && python3 visualize.py
```
