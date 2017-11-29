import networkx as nx
import qstest as qs

network = nx.karate_club_graph()
communities = qs.louvain(network)
sg, pvals = qs.qstest(network, communities, qs.qmod, qs.vol, qs.louvain)
