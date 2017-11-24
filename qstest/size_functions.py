import numpy as np
import networkx as nx

def n(G, nodes):
	return len(nodes)

def vol(G, nodes):
	return sum( [ x[1] for x in G.degree(nodes)] );
