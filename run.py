import os

JobConfigs=["HNL_ULID_2016a" , "HNL_ULID_2016b" , "HNL_ULID_2017" , "HNL_ULID_2018"]

#for JobConfig in JobConfigs:
#    os.system("python tnp_tamsa.py  config/HNL_v4.py "+ JobConfig)

JobConfigs=["HNLMVACONVLoose_18","HNLMVACONVMedium_18","HNLMVACONVTight_18"]

for JobConfig in JobConfigs:
    os.system("python tnp_tamsa.py  config/HNL_v1.py "+ JobConfig)
