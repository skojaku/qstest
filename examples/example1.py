import networkx as nx
import qstest as qs

network = nx.karate_club_graph()
communities = qs.louvain(network)
sg, p_values = qs.qstest(network, communities, qs.qmod, qs.vol, qs.louvain)
