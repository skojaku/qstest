import numpy as np
import community as com
from networkx.algorithms import community 

def louvain_algorithm(G):
	# Find communities using the Louvain algorithm 
	coms = com.best_partition(G);
	
	nodes = G.nodes();
	C = max(coms.values())  + 1

	communities = [];
	for i in range(C):
		communities.append([])
	
	for nid in nodes:
		communities[ coms[nid] ].append( nid );
	
	return	communities

	
def label_propagation(G):
	coms_iter = community.asyn_lpa_communities(G)
	communities = []
	for nodes in iter(coms_iter):
		communities.append(list(nodes))
			
	return communities	
