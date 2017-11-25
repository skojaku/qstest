import networkx as nx
import qstest as qs
from networkx.algorithms import community as nxcdalgorithm 

# Pareameters of the community-detection algorithm (async_fluidc) called from my_cdalgorithm
C = 3 
maxiter = 10

def my_cdalgorithm(network):
        communities = [] 
	subnets = nx.connected_component_subgraphs(network)
	
	for subnet in subnets:
        	coms_iter = nxcdalgorithm.asyn_fluidc(subnet, min([C, subnet.order()]), maxiter) 
        	for nodes in iter(coms_iter): 
         	       communities.append(list(nodes)) 
                         
        return communities 

network = nx.karate_club_graph()
communities = my_cdalgorithm(network)
s, pvals = qs.qstest(network, communities, qs.qmod, qs.vol, my_cdalgorithm)
