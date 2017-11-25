#import numpy as np
import networkx as nx
from networkx.algorithms.community import LFR_benchmark_graph
#import community
#from networkx.algorithms import community 
import qstest as qs

# Output reuslts
 
# Generate a network using the LFR model
G = LFR_benchmark_graph(300, 3, 3, 0.1, average_degree=10, min_community=50, seed=1)

# Find communities using the Louvain algorithm
print 0 in G[1]
#coms = qs.louvain_algorithm(G)
coms = qs.label_propagation(G)
#print qs.calc_qcnd(G, coms[3])
#coms = community.best_partition(G);

## Compute the statistical significance of the detected communities
significant, pvals = qs.qstest(G, coms, qs.qmod, qs.n, qs.label_propagation, num_of_thread=1, num_of_rand_net = 10);
#significant, pvals, alpha = qs.qstest(G, coms, qs.calc_qmod, qs.calc_vol, qs.label_propagation, num_of_thread=2, num_of_rand_net = 10);
#significant, pvals, alpha = qs.qstest(G, coms, qs.calc_qmod, qs.calc_vol, qs.louvain_algorithm, num_of_thread=2, num_of_rand_net = 10);


print('# Test results')
for i in range(len(significant)):
	if significant[i]:
		print('community {:d}: significant (pval={:4f})'.format(i, pvals[i]))
	else:
		print('community {:d}: insignificant (pval={:4f})'.format(i, pvals[i]))


