import numpy as np

def qmod(G, nodes):
	deg = G.degree(nodes);
	q = 0;
	D = 0;	
	for i in nodes:
		for j in nodes:
			if(G.has_edge(i, j)==False):
				continue
			q += 1.0;
		D+=deg[i];	

	M = G.size()/2; 
	q = (q - D * D/ (2.0*M)) / (2*M); 
	return q


def qint(G, nodes):
	deg = G.degree(nodes);
	q = 0;
	n = 0;	
	for i in nodes:
		for j in nodes:
			if(G.has_edge(i, j)==False):
				continue
			q += 1.0;
		n+=1;	

	q = q/n 
	return q

def qext(G, nodes):
	deg = G.degree(nodes);
	q = 0;
	n = 0;
	D = 0;	
	for i in nodes:
		for j in nodes:
			if(G.has_edge(i, j)==False):
				continue
			q += 1.0;
		n+=1;
		D+=deg[i];	

	
	q = -(D-q)/n 
	return q

def qcnd(G, nodes):
	deg = G.degree(nodes);
	q = 0;
	n = 0;
	D = 0;	
	for i in nodes:
		for j in nodes:
			if(G.has_edge(i, j)==False):
				continue
			q += 1.0;
		n+=1;
		D+=deg[i];	

	
	q = -(D-q)/D 
	return q
