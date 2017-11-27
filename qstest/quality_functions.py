# -*- coding: utf-8 -*-
import numpy as np


# Modularity-based quality function of individual communities
#
#
# Usage:
#
#   q = qmod(network, community)
#
#
# Input:
#
#   network - Networkx Graph class instance.
#
#   community - List of the IDs of nodes in a community.
#
#
# Output:
#
#   q - Quality of the community.
#
#
def qmod(network, community):
    deg = network.degree(community)
    q = 0
    D = 0
    for i in community:
        for j in community:
            if network.has_edge(i, j) == False:
                continue
            q += 1.0
        D += deg[i]

    M = network.size() / 2
    q = (q - D * D / (2.0 * M)) / (2 * M)
    return q


# Internal average degree 
#
#
# Usage:
#
#   q = qint(network, community)
#
#
# Input:
#
#   network - Networkx Graph class instance.
#
#   community - List of the IDs of nodes in a community.
#
#
# Output:
#   q - Quality of the community
#
#
def qint(network, community):
    deg = network.degree(community)
    q = 0
    n = 0
    for i in community:
        for j in community:
            if network.has_edge(i, j) == False:
                continue
            q += 1.0
        n += 1

    q = q / n
    return q


# Expansion 
#
#
# Usage:
#   q = qexp(network, community)
#
#
# Input:
#
#   network - Networkx Graph class instance.
#
#   community - List of the IDs of nodes in a community.
#
#
# Output:
#
#   q - Quality of the community.
#
#
def qext(network, community):
    deg = network.degree(community)
    q = 0
    n = 0
    D = 0
    for i in community:
        for j in community:
            if network.has_edge(i, j) == False:
                continue
            q += 1.0
        n += 1
        D += deg[i]

    q = -(D - q) / n
    return q


# Conductance 
#
#
# Usage:
#
#   q = qcnd(network, community)
#
#
# Input:
#
#   network - Networkx Graph class instance.
#
#   community - List of the IDs of nodes in a community.
#
#
# Output:
#
#   q - Quality of the community.
#
#
def qcnd(network, community):
    deg = network.degree(community)
    q = 0
    n = 0
    D = 0
    for i in community:
        for j in community:
            if network.has_edge(i, j) == False:
                continue
            q += 1.0
        n += 1
        D += deg[i]

    q = -(D - q) / D
    return q
