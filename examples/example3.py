import networkx as nx
import qstest as qs

# Square of the number of nodes in a community
def my_sfunc(network, nodes):
        return len(nodes) * len(nodes)

network = nx.karate_club_graph()
communities = qs.louvain(network)
sg, pvals = qs.qstest(network, communities, qs.qmod, my_sfunc, qs.louvain)
