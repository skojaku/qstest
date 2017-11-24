import numpy as np
from scipy.stats import norm
import networkx as nx
import multiprocessing as mp


def qstest(G, coms, qfunc, sfunc, community_detection_algorithm, num_of_rand_net = 500, num_of_thread = 4, alpha_prime = 0.05):

	# compute quality, q, and size, s, for each community 	
	q = np.array( qfunc(G, coms), dtype=np.float );	
	s = np.array( sfunc(G, coms), dtype=np.float );	
	C =max(coms.values()) + 1;
	alpha = 1.0 - (1-alpha_prime)**(1.0/float(C));
	
	# draw quality and size of communities detected in randomised networks 
	q_tilde = [];
	s_tilde = [];
	if num_of_thread ==1: # single thread
		q_tilde, s_tilde = draw_qs_samples(G, coms, qfunc, sfunc, community_detection_algorithm, num_of_rand_net)
	else: # multithreads
		private_args = [(G, coms, qfunc, sfunc, community_detection_algorithm, num_of_rand_net/10) for i in range(num_of_thread)];
		pool = mp.Pool(num_of_thread)
	    	qs_tilde = pool.map(wrapper_draw_qs_samples, private_args)
		for i in range(num_of_thread):
			q_tilde+= qs_tilde[i][0]; 
			s_tilde+= qs_tilde[i][1];
 
	q_tilde = np.array(q_tilde, dtype=np.float);	
	s_tilde = np.array(s_tilde, dtype=np.float);	
	
	# estimate p-value using the gaussian kernel density estimatior
	q_ave = np.mean(q_tilde)
	s_ave = np.mean(s_tilde)
	q_std = np.std(q_tilde,ddof=1)
	s_std = np.std(s_tilde,ddof=1)
	gamma = np.corrcoef(q_tilde, s_tilde)[0, 1]
	h = float(len(q_tilde))**(-1.0/6.0);
	
	pvals = [1] * C;
	significant = [False] * C;
	for cid in range(C):
		w = np.exp( - ( (s[cid] - s_tilde) / (np.sqrt(2.0) * h * s_std) )**2 );
		
		cd = norm.cdf(  ( (q[cid] -q_tilde)/ (h * q_std) - gamma * (s[cid] - s_tilde) / (h * s_std) ) / np.sqrt( 1.0 - gamma * gamma) );	
			
		pvals[cid] = 1.0 - ( sum( w * cd ) / sum(w));
		significant[cid] = pvals[cid] <= alpha;

	return significant, pvals, alpha	
		
def draw_qs_samples(G, coms, qfunc, sfunc, community_detection_algorithm, num_of_rand_net):
	
	deg = [x[1] for x in G.degree()];
	q_rand = [];
	s_rand = [];
	for i in range(num_of_rand_net):
		Gr = nx.configuration_model( deg );
		coms_rand = community_detection_algorithm(Gr);	
		q_rand =  q_rand + qfunc(Gr, coms_rand);	
		s_rand =  s_rand + sfunc(Gr, coms_rand);

	return q_rand, s_rand

def wrapper_draw_qs_samples(args):
    return draw_qs_samples(*args)	
	
	
