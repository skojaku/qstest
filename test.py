import numpy as np
import networkx as nx
from networkx.algorithms.community import LFR_benchmark_graph
import qstest as qs
import sys
sys.path.append("../python-louvain-master")
import community 
 
# generate a network with communities using the LFR model
G = LFR_benchmark_graph(100, 2, 2, 0.1, average_degree=5, min_community=20, seed=10)

#first compute the best partition
coms = community.best_partition(G);

significant, pvals = qs.qstest(G, coms, qs.calc_qmod, qs.calc_vol, community.best_partition, num_of_thread=2, num_of_rand_net = 10);

#print significant
#print pvals

