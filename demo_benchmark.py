# Generated with SMOP  0.41
from libsmop import *
# .\demo_benchmark.m

    clc
    clear
    close_('all')
    seqs=cellarray(['ADL-Rundle-1','ADL-Rundle-3','AVG-TownCentre','ETH-Crossing','ETH-Jelmoli','ETH-Linthescher','KITTI-16','KITTI-19','PETS09-S2L2','TUD-Crossing','Venice-1'])
# .\demo_benchmark.m:3
    
    
    for s in arange(1,length(seqs)).reshape(-1):
        single_tracker(seqs[s])
    