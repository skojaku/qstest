# qstest
Python codes for the (q,s)--test 

Please cite  
Kojaku, S. and Masuda, N. "A generalised significance test for individual communities in networks". Preprint arXiv:???? (2017).


## Files
Directory qstest/ contains python codes.  
  * qstest/__init__.py is for initialing this package
  * qstest/qstest.py is the main codes of the (q,s)-test 
  * qstest/quality_functions.py contains the codes of the quality functions of individual communities
  * qstest/size_functions.py contains the codes of the size of individual communities.


## Installation
  To install using pip, type
    
    pip install qstest
    
  To install from source files, type
        
    python setup.py install 
       	
  Then, you can import the qstest module to your script by:
    
    import qstest as qs
  
## USAGE:
 
    s, pvals = qs.qstest(network, communities, qfunc, sfunc, cdalgorithm)
 
### Input  
* **network** - Networkx Graph class instance.
* **communities** - C-dimensional list. communities[c] is a list containing the ids of the nodes in community c.
* **qfunc** - Quality function of individual communities.　Following quality functions are available:
    * qs.qmod - Modularity-based quality function of individual communities, 
    * qs.qint - Internal average degree, 
    * qs.qexp - Expansion,　　
    * qs.qcnd - Conductance.　

  To use your quality function, see [Quality functions](#Quality_functions).

 * **sfunc**  - Size function of individual communities. Following quality functions are available:
    * qs.n - Number of nodes in a community, 
    * qs.vol - Sum of degrees of nodes in a community.
    
    To use your quality function, see [Size functions](#Size_functions).
   
 * **cdalgorithm** - Algorithm for finding communities. Following algorithms are available
    * louvain_algorithm - [Louvain algorithm](http://perso.crans.org/aynaud/communities/index.html) 
    * label_propagation - [Label propagation algorithm](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.asyn_lpa.asyn_lpa_communities.html#networkx.algorithms.community.asyn_lpa.asyn_lpa_communities)
  
 * **(optional) num_of_rand_net** - Number of randomised networks. (Default: 500)
 * **(optional) alpha** - Statistical significance level before the Šidák correction. (Default: 0.05)
 * **(optional) num_of_thread** - Number of threads allowed. (Default: 4)
  
### Output  
 * s - C-dimensional list. s[c] = True if community c is significant. Otherwise s[c] = False. 
 * pvals - C-dimensional list. pvals[c] is the p-value for community c.

## Quality functions
  The (q,s)--test can accept various quality functions of individual communities.
  You can use your quality function of individual communities, or use four ''off-the-shelf'' quality functions, 
  qs.qmod, qs.qint, qs.qext and qs.cnd.
  
  The quality function, say qfunc, should be implemented as follows.
    
    q = qfunc( network, community )
    
  ### Input
 * network - Networkx Graph class instance. 
 * community - List of nodes belonging to a community

  ### Output  
  * q - Quality of the community
  
There is no restriction on the name of the quality function.
We implement four quality functions, qs.qmod, qs.qint, qs.qext and qs.cnd.
  We implement four types of quality functions as follows
  * qs.qmod 
  * qs.qint
  * qs.qexp
  * qs.qcnd
  The qstest module contains four types of quality functions as follows.
  
    calc_qint(network, nodes)

## Size functions

## Community detection algorithms

### REQUIREMENT: 
      
  MATLAB 2012 or later.

---
Last updated: 17 October 2017


