import networkx as nx
import qstest as qs
from networkx.algorithms import community as nxcdalgorithm

# Wrapper function for async_fluidc implemented in Networkx 2.0
def my_cdalgorithm(network):
        communities = []
        subnets = nx.connected_component_subgraphs(network)
        for subnet in subnets:
                coms_iter = nxcdalgorithm.asyn_fluidc(subnet, min([C, subnet.order()]), maxiter)
                for nodes in iter(coms_iter):
                       communities.append(list(nodes))
        return communities

# Pareameters of async_fluidc
C = 3
maxiter = 10

network = nx.karate_club_graph()
communities = my_cdalgorithm(network)
sg, p_values = qs.qstest(network, communities, qs.qmod, qs.vol, my_cdalgorithm)
