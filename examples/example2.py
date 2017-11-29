import networkx as nx
import qstest as qs

# Number of intra-community edges
def my_qfunc(network, nodes):
        return network.subgraph(nodes).size()

network = nx.karate_club_graph()
communities = qs.louvain(network)
sg, p_values = qs.qstest(network, communities, my_qfunc, qs.vol, qs.louvain)
