# -*- coding: utf-8 -*-
import numpy as np
import community as com
from networkx.algorithms import community as nxcom


# Wrapper function of the Louvain algorithm implemented in Networkx
# 
#
# Usage:
#
#   communities = louvain_algorithm(network)
#
#
# Input:
#
#   network - Networkx Graph class instance.
#
#
# Output:
#
#   communities - List of lists. communities[c] is the list containing the IDs of nodes belonging to community c. 
#
#
def louvain_algorithm(network):
    coms = com.best_partition(network)

    nodes = network.nodes()
    C = max(coms.values()) + 1

    communities = []
    for i in range(C):
        communities.append([])

    for nid in nodes:
        communities[coms[nid]].append(nid)

    return communities


# Wrapper function of the label propgation algorithm implemented in Networkx
#
#
# Usage:
#
#   communities = label_propagation_algorithm(network)
#
#
# Input:
#
#   network - Networkx Graph class instance.
#
#
# Output:
#
#   communities - List of lists. communities[c] is the list containing the IDs of nodes belonging to community c. 
#
#
def label_propagation_algorithm(network):
    coms_iter = nxcom.asyn_lpa_communities(network)
    communities = []
    for nodes in iter(coms_iter):
        communities.append(list(nodes))

    return communities
