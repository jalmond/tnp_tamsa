import os

JobConfigs=["HLTEl12_2016a","HLTEl12_2016b","HLTEl12_2017","HLTEl12_2018", "HLTEl23_2016a","HLTEl23_2016b","HLTEl23_2017","HLTEl23_2018"]
JobConfigs=["HLTEl23_2016a"]#,"HLTEl23_2016b","HLTEl23_2017","HLTEl23_2018"]

for JobConfig in JobConfigs:
    os.system("python tnp_tamsa.py  config/HNL_v1.py "+ JobConfig)
