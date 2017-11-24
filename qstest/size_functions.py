import numpy as np

def calc_n(G, coms):
	lab = coms.values();
	C =max(lab) + 1;
	nc = [0.0] * C;
	for cid in lab:
		nc[cid]+=1.0
	return nc

def calc_vol(G, coms):
	deg = G.degree();
	C =max(coms.values()) + 1;
	volc = [0.0] * C;
	for nid, cid in coms.items():
		volc[cid]+=deg[nid]

	return volc
