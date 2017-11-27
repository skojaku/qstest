# -*- coding: utf-8 -*-
import numpy as np


# Number of nodes in a community 
#
# Usage
#
#   s = n(network, community)
#
# Input
#
#   network - Networkx Graph class instance.
#
#   community - List of the IDs of nodes in a community.
#
# Output
#
#   s - Number of nodes in a community. 
#
def n(network, community):
	s = len(community)
	return s 


# Sum of degrees of nodes in a community   
#
# Usage
#
#   s = vol(network, community)
#
# Input
#
#   network - Networkx Graph class instance.
#
#   community - List of the IDs of nodes in a community.
#
# Output
#
#   s - Sum of degrees of nodes in a community.
#
def vol(network, community):
	s = sum( [ x[1] for x in network.degree(community)] )
	return s
