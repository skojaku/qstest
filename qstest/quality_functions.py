import numpy as np
def calc_qmod(G, coms):
	
	deg = G.degree();
	nodes = G.nodes();
	labs = coms.values();

	C =max(labs) + 1;
	N = len(labs)
	qs = np.array( [0.0] * C, dtype=np.float);
	D =  np.array( [0.0] * C, dtype=np.float) ;
	
	for i in nodes:
		cid = coms[i];
		for j in G[i]:
			if( cid!= coms[j] ):
				continue;
			qs[ cid ] += 1.0;
		D[cid]+=deg[i];	

	M = sum(D)/2.0;
	qs = (qs - D * D/ (2.0*M)) / (2*M); 
	return qs.tolist()

def calc_qint(G, coms):

	nodes = G.nodes();
	labs = coms.values();
	C =max(labs) + 1;
	N = len(labs)
	qs = np.array( [0.0] * C, dtype=np.float);
	n =  np.array( [0.0] * C, dtype=np.float) ;
	for i in nodes:
		cid = coms[i];
		for j in G[i]:
			if( cid!= coms[j] ):
				continue;
			qs[ cid ] += 1.0;
		n[cid]+=1;	

	qs = qs / n; 
	return qs.tolist()

def calc_qext(G, coms):

	nodes = G.nodes();
	labs = coms.values();
	C =max(labs) + 1;
	N = len(labs)
	qs = np.array( [0.0] * C, dtype=np.float );
	n =  np.array( [0.0] * C, dtype=np.float ) ;
	for i in nodes:
		cid = coms[i];
		for j in G[i]:
			if( cid== coms[j] ):
				continue;
			qs[ cid ] +=  1.0;
		n[cid]+=1;	

	qs = -qs / n; 
	return qs.tolist()

def calc_qcnd(G, coms):
	deg = G.degree();
	nodes = G.nodes();
	labs = coms.values();
	C =max(labs) + 1;
	N = len(labs)
	qs = np.array( [0.0] * C, dtype=np.float );
	D =  np.array( [0.0] * C, dtype=np.float ) ;
	for i in nodes:
		cid = coms[i];
		for j in G[i]:
			if( cid== coms[j] ):
				continue;
			qs[ cid ] +=  1.0;
		D[cid]+=deg[i];	

	qs = -qs / D; 
	return qs.tolist()
