# -*- coding: utf-8 -*-
import numpy as np
import community as com
from networkx.algorithms import community as nxcom


# Wrapper function of the build-in Louvain algorithm of Networkx
# 
# Usage
#
#   communities = louvain(network)
#
# Input
#
#   network - Networkx Graph class instance.
#
# Output
#
#   communities - C-dimensional list of lists. communities[c] is a list containing the IDs of nodes belonging to community c. Node and communiy indices start from 0.
#
def louvain(network):
    coms = com.best_partition(network)

    nodes = network.nodes()
    C = max(coms.values()) + 1

    communities = []
    for i in range(C):
        communities.append([])

    for nid in nodes:
        communities[coms[nid]].append(nid)

    return communities


# Wrapper function of the built-in label propgation algorithm of Networkx
#
# Usage
#
#   communities = label_propagation(network)
#
# Input
#
#   network - Networkx Graph class instance.
#
# Output
#
#   communities - C-dimensional list of lists. communities[c] is a list containing the IDs of nodes belonging to community c. Node and communiy indices start from 0.
#
def label_propagation(network):
    coms_iter = nxcom.asyn_lpa_communities(network)
    communities = []
    for nodes in iter(coms_iter):
        communities.append(list(nodes))

    return communities
