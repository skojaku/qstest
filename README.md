# qstest
Python codes for the (q,s)--test, a generalised significance test for individual communities in networks. 

Please cite:

    Kojaku, S. and Masuda, N. "A generalised significance test for individual communities in networks". Preprint arXiv:???? (2017).

# Installation
  To install, type

```bash 
    pip install qstest
```

## USAGE
 
 ```python
    s, pvals = qs.qstest(network, communities, qfunc, sfunc, cdalgorithm)
 ```
 
#### Input -  
* `network` - Networkx Graph class instance.
* `communities` - C-dimensional list. communities[c] is a list containing the ids of the nodes in community c.
* `qfunc` - Quality function of individual communities. Following quality functions are available:
    * qs.qmod - Modularity-based quality function of individual communities, 
    * qs.qint - Internal average degree, 
    * qs.qexp - Expansion,　　
    * qs.qcnd - Conductance.　

  You can use your quality function of individual communities. See ["How to provide my quality function to qstest"](#how-to-provide-my-quality-function-to-qstest).

 * `sfunc`  - Size function of individual communities. Following quality functions are available:
    * qs.n - Number of nodes in a community, 
    * qs.vol - Sum of degrees of nodes in a community.
    
    You can use your measure of the size of a community. See ["How to provide my measure of community size to qstest"](#how-to-provide-my-measure-of-community-size-to-qstest).
   
 * `cdalgorithm` - Algorithm for finding communities. Following algorithms are available:
    * qs.louvain_algorithm - [Louvain algorithm](http://perso.crans.org/aynaud/communities/index.html),
    * qs.label_propagation - [Label propagation algorithm](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.asyn_lpa.asyn_lpa_communities.html#networkx.algorithms.community.asyn_lpa.asyn_lpa_communities).

    You can use your algorithm for finding communities. See See ["How to provide my community-detection algorithm to qstest"](#how-to-provide-my-measure-of-community-size-to-qstest).
 
 * `num_of_rand_net` (optional)  - Number of randomised networks. (Default: 500)
 * `alpha` (optional)  - Statistical significance level before the Šidák correction. (Default: 0.05)
 * `num_of_thread` (optional) - Number of threads allowed. (Default: 2)
  
#### Output -   
 * `s` - C-dimensional list. s[c] = True if community c is significant, and s[c] = False if it is insignificant. 
 * `pvals` - C-dimensional list. pvals[c] is the p-value for community c. 

#### Example
```python
import networkx as nx
import qstest as qs

network = nx.karate_club_graph()
communities = qs.louvain_algorithm(network)
s, pvals = qs.qstest(network, communities, qs.qmod, qs.vol, qs.louvain_algorithm)
```

## How to provide my quality function to **qstest**
You can use your quality function for the significance test. We assume that a large value of the quality function indicates a good community. To this end, write a function (by any name) for computing the quality of a community as follows.

 ```python
    q = my_qfunc( network, community )
```

#### Input -
 * `network` - Networkx Graph class instance. 
 * `community` - List of nodes belonging to a community.

#### Output -
  * `q` - Quality of the community.

Then, provide the implemented **my_qfunc** to **qstest**:
```python
s, pvals = qs.qstest(network, communities, my_qfunc, sfunc, cdalgorithm)
```

#### Example
```python
import networkx as nx
import qstest as qs

 # Number of intra-community edges
def my_qfunc(network, nodes):
        return network.subgraph(nodes).size();

network = nx.karate_club_graph()
communities = qs.louvain_algorithm(network)
s, pvals = qs.qstest(network, communities, my_qfunc, qs.vol, qs.louvain_algorithm)
```

## How to provide my measure of community size to **qstest**
You can use your measure of community size for the significance test. To this end, write a function (by any name) for computing the size of a community as follows.

```python
    sz = my_sfunc( network, community )
```

#### Input -
 * `network` - Networkx Graph class instance. 
 * `community` - List of nodes belonging to a community

#### Output - 
  * `sz` - Size of the community

Then, provide the implemented **my_sfunc** to **qstest**:
```python
s, pvals = qs.qstest(network, communities, qfunc, my_sfunc, cdalgorithm)
```  

#### Example
```python
import networkx as nx
import qstest as qs

 # Number of intra-community edges
def my_sfunc(network, nodes):
        return network.subgraph(nodes).size();

network = nx.karate_club_graph()
communities = qs.louvain_algorithm(network)
s, pvals = qs.qstest(network, communities, qs.qmod, my_sfunc, qs.louvain_algorithm)
```

## How to provide my community-detection algorithm to **qstest**
You can use the algorithm that you used to find communities in networks. To this end, write the following wrapper function (by any name).
 
 ```python
    communities = my_cdalgorithm( network )
 ```
    
#### Input -
 * `network` - Networkx Graph class instance. 

#### Output - 
 * `community` - List of nodes belonging to a community

Then, provide the implemented **my_cdalgorithm** to **qstest**:
```python
s, pvals = qs.qstest(network, communities, qfunc, sfunc, my_cdalgorithm)
```  

If the community-detection algorithm requires parameters such as the number of communities, then pass the parameters through global variables: define, for example, a global variable C, then access to C from the cdalgorithm.
  
#### Example:
```python
import networkx as nx
import qstest as qs
from networkx.algorithms import community as nxcdalgorithm

# Pareameters of the community-detection algorithm (async_fluidc) called from my_cdalgorithm
C = 3
maxiter = 10

# Wrapper function for an algorithm, async_fluidc, implemented in Networkx 2.0
def my_cdalgorithm(network):
        communities = []
        subnets = nx.connected_component_subgraphs(network)
        for subnet in subnets:
                coms_iter = nxcdalgorithm.asyn_fluidc(subnet, min([C, subnet.order()]), maxiter)
                for nodes in iter(coms_iter):
                       communities.append(list(nodes))
        return communities

network = nx.karate_club_graph()
communities = my_cdalgorithm(network)
s, pvals = qs.qstest(network, communities, qs.qmod, qs.vol, my_cdalgorithm)
```

## REQUIREMENT: 
* Python 2.7 or later
* Networkx 2.0 or later
--- 
Last updated: 17 October 2017


