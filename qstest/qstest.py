# -*- coding: utf-8 -*-
import numpy as np
from scipy.stats import norm
import networkx as nx
import multiprocessing as mp


# The (q, s)-test
#
#
# Usage:
#
#   sg, pval = qstest(network, communities, qfunc, sfunc, cdalgorithm, num_of_rand_net, num_of_thread, alpha)
#
#
# Input:
#
#   network - Networkx Graph class instance.
#
#   communities - List of lists. communities[c] is the list containing the IDs of nodes belonging to community c.
#
#   qfunc - Quality function of individual communities. 
#
#   sfunc - Size function that computes the size of individual communities.
#
#   cdalgorithm - Community detection algorithm. 
#
#   num_of_rand_net (optional) - Number of randomised networks. (Default: 500).
#
#   alpha (optional) - Statistical significance level before the Šidák correction. (Default: 0.05).
#
#   num_of_thread (optional) - Maximum number of threads running in a CPU. (Default: 4).
#
#
# Output:
#
#   q - Quality of the community.
#
#
def qstest(network, communities, qfunc, sfunc, cdalgorithm, num_of_rand_net = 500, num_of_thread = 4, alpha = 0.05):

	q = np.array( [ qfunc(network, x) for x in communities], dtype=np.float )	
	s = np.array( [ sfunc(network, x) for x in communities], dtype=np.float )
	C =len(communities)
	alpha_corrected = 1.0 - (1-alpha)**(1.0/float(C))
	
	q_tilde = []
	s_tilde = []
	if num_of_thread ==1: # single thread
		q_tilde, s_tilde = draw_qs_samples(network, communities, qfunc, sfunc, cdalgorithm, num_of_rand_net)
	else: # multithreads
		private_args = [(network, communities, qfunc, sfunc, cdalgorithm, int(num_of_rand_net/num_of_thread)+1) for i in range(num_of_thread)]
		pool = mp.Pool(num_of_thread)
		qs_tilde = pool.map(wrapper_draw_qs_samples, private_args)
		for i in range(num_of_thread):
			q_tilde+= qs_tilde[i][0] 
			s_tilde+= qs_tilde[i][1]
 
	q_tilde = np.array(q_tilde, dtype=np.float)	
	s_tilde = np.array(s_tilde, dtype=np.float)	
	
	q_ave = np.mean(q_tilde)
	s_ave = np.mean(s_tilde)
	q_std = np.std(q_tilde,ddof=1)
	s_std = np.std(s_tilde,ddof=1)
	gamma = np.corrcoef(q_tilde, s_tilde)[0, 1]
	h = float(len(q_tilde))**(-1.0/6.0)
	pvals = [1] * C
	significant = [False] * C
	for cid in range(C):
		if s_std<=1e-30:
			continue	
		if q_std<=1e-30:
			continue	
		w = np.exp( - ( (s[cid] - s_tilde) / (np.sqrt(2.0) * h * s_std) )**2 )
		cd = norm.cdf(  ( (q[cid] -q_tilde)/ (h * q_std) - gamma * (s[cid] - s_tilde) / (h * s_std) ) / np.sqrt( 1.0 - gamma * gamma) )	
		denom = sum(w)	
		if denom<=1e-30:
			continue	
		pvals[cid] = 1.0 - ( sum( w * cd ) / denom)
		significant[cid] = pvals[cid] <= alpha_corrected

	return significant, pvals	


# Private function for qstest		
def draw_qs_samples(network, communities, qfunc, sfunc, cdalgorithm, num_of_rand_net):
	deg = [x[1] for x in network.degree()]
	q_rand = []
	s_rand = []
	for i in range(num_of_rand_net):
		networkr = nx.configuration_model( deg )
		communities_rand = cdalgorithm(networkr)
		q_rand =  q_rand + [qfunc(networkr, x) for x in communities_rand]	
		s_rand =  s_rand + [sfunc(networkr, x) for x in communities_rand]

	return q_rand, s_rand


# Private function for qstest		
def wrapper_draw_qs_samples(args):
    return draw_qs_samples(*args)	
			
