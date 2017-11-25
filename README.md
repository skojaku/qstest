# qstest
Python codes for the (q,s)--test, a generalised significance test for individual communities in networks. 

Please cite  
Kojaku, S. and Masuda, N. "A generalised significance test for individual communities in networks". Preprint arXiv:???? (2017).

# Installation
  To install, type
    
    pip install qstest
  
## USAGE
 
    s, pvals = qs.qstest(network, communities, qfunc, sfunc, cdalgorithm)
 
#### Input -  
* `network` - Networkx Graph class instance.
* `communities` - C-dimensional list. communities[c] is a list containing the ids of the nodes in community c.
* `qfunc` - Quality function of individual communities. Following quality functions are available:
    * qs.qmod - Modularity-based quality function of individual communities, 
    * qs.qint - Internal average degree, 
    * qs.qexp - Expansion,　　
    * qs.qcnd - Conductance.　

  To use your quality function of individual communities, see [Quality functions](#quality-functions).

 * `sfunc`  - Size function of individual communities. Following quality functions are available:
    * qs.n - Number of nodes in a community, 
    * qs.vol - Sum of degrees of nodes in a community.
    
    To use your measure of the size of a community, see [Size functions](#size-functions).
   
 * `cdalgorithm` - Algorithm for finding communities. Following algorithms are available:
    * louvain_algorithm - [Louvain algorithm](http://perso.crans.org/aynaud/communities/index.html) 
    * label_propagation - [Label propagation algorithm](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.asyn_lpa.asyn_lpa_communities.html#networkx.algorithms.community.asyn_lpa.asyn_lpa_communities)

    To use other algorithms, see [Community detection algorithms](#community_detection_algorithms) 
 
 * `num_of_rand_net` (optional)  - Number of randomised networks. (Default: 500)
 * `alpha` (optional)  - Statistical significance level before the Šidák correction. (Default: 0.05)
 * `num_of_thread` (optional) - Number of threads allowed. (Default: 4)
  
#### Output -   
 * `s` - C-dimensional list. s[c] = True if community c is significant, and s[c] = False if it is insignificant. 
 * `pvals` - C-dimensional list. pvals[c] is the p-value for community c. 

#### Example
```python
import networkx as nx
from networkx.algorithms.community import LFR_benchmark_graph
import qstest as qs

network = LFR_benchmark_graph(300, 3, 3, 0.1, average_degree=10, min_community = 50, seed = 1)
communities = qs.louvain_algorithm(network)
s, pvals = qs.qstest(network, communities, qs.qmod, qs.vol, qs.louvain_algorithm, num_of_thread = 1)
```

## Quality functions
The (q,s)--test can accept your quality function of individual communities. To this end, implement the quality function as follows.

    q = qfunc( network, community )
    
#### Input -
 * `network` - Networkx Graph class instance. 
 * `community` - List of nodes belonging to a community

#### Output -
  * `q` - Quality of the community
  
Note that there is no restriction on the name of the quality function.

#### Example
```python
def qmod(network, nodes):
        deg = network.degree(nodes);
        q = 0;
        D = 0;
        for i in nodes:
                for j in nodes:
                        if( network.has_edge(i, j) == False ):
                                continue
                        q += 1.0;
                D += deg[i];
        M = network.size() / 2;
        q = (q - D * D / (2.0*M)) / (2*M);
        return q
```

## Size functions
The (q,s)--test can accept various measure of the size of a community. The size function should be implemented as follows.

    s = sfunc( network, community )
    
#### Input -
 * `network` - Networkx Graph class instance. 
 * `community` - List of nodes belonging to a community

#### Output - 
  * `s` - Size of the community
  
Note that there is no restriction on the name of the size function.

#### Example
```python
def n(G, nodes):
        return len(nodes)
```

### Community detection algorithms
The (q,s)-test is not associated with a specific algorithm for finding communities in networks. In many cases, different community-detection algorithms take different inputs and outputs. To absorb the differences, the community-detection algorithm should be wrapped as follow.

    communities = cmalgorithm( network )
    
#### Input -
 * `network` - Networkx Graph class instance. 

#### Output - 
 * `community` - List of nodes belonging to a community
  
Note that there is no restriction on the name of cmalgorithm. If the community-detection algorithm requires parameters such as the number of communities, then pass the parameters through global variables: define, for example, a global variable C, then access to C from the cmdalgorithm.

#### Example:

```python
import community as lva
from networkx.algorithms import community as lpa

def louvain_algorithm(network):
        coms = lva.best_partition(network);
        communities = [];
        for i in range(max(coms.values()) + 1):
                communities.append([])
        
        for nid in G.nodes():
                communities[ coms[nid] ].append( nid );
        
        return  communities

        
def label_propagation(network):
        coms_iter = lpa.asyn_lpa_communities(network)
        communities = []
        for nodes in iter(coms_iter):
                communities.append(list(nodes))
                        
        return communities      
```

## REQUIREMENT: 
* Python 2.7 or later
* Networkx 2.0 or later
--- 
Last updated: 17 October 2017


