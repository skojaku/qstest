Python codes for the (q, s)-test, a generalised significance test for individual communities in networks. 

Please cite

  Kojaku, S. and Masuda, N. "A generalised significance test for individual communities in networks". Preprint arXiv:???? (2017)
———————————————————————————————————————————————————————————————————————————
Directory ./ contains the codes for installing this package and README files.
  
  ./LICENSE describes the licence of this package 
  
  ./MANIFEST.in is for pip (pip is a package management system for Python) 
  
  ./README.md is the README file for the Github	

  ./README.rst is for pip

  ./README.txt is this README file

  ./setup.cfg is for pip
  
  ./setup.py is the python script to install this package


Directory qstest/ contains Python codes.
      
  qstest/__init__.py is the header file of this package.
  
  qstest/cmalgorithm_wrapper.py contains the codes of community detection algorithms

  qstest/qstest.py contains the codes of the (q, s)-test 

  qstest/quality_functions.py contains the codes of quality functions
  
  qstest/size_functions.py contains the codes of size functions
———————————————————————————————————————————————————————————————————————————
Installation

  You can install this package with pip, a package management system for the software written in Python.
  
  To install qstest, type

    pip install qstest

  If you failed to install, then type the following command: 
	
    sudo python setup.py install
———————————————————————————————————————————————————————————————————————————
Usage
 
  sg, pvals = qstest(network, communities, qfunc, sfunc, cdalgorithm, num_of_rand_net = 500, alpha = 0.05, num_of_thread = 2)
 
  Input 

    network - Networkx Graph class instance.
  
    communities - C-dimensional list of lists. communities[c] is a list containing the IDs of nodes belonging to community c.
  
    qfunc - Quality function of individual communities. Following quality functions are available:
  
      qmod - Contribution of a community to the modularity. 
  
      qint - Internal average degree. 
  
      qexp - Expansion.　
  　
      qcnd - Conductance.　
  
      You can pass your quality function of individual communities to qstest. See "How to pass my quality function to qstest".
  
    sfunc - Size function (i.e., size of individual communities). Following size functions are available:
  
      n - Number of nodes in a community.
   
      vol - Sum of degrees of nodes in a community.
      
      You can pass your size function to qstest. See "How to pass my size function to qstest".
     
    cdalgorithm` - Community detection algorithm. Following algorithms (implemented in Networkx) are available:
  
      louvain_algorithm - Louvain algorithm (http://perso.crans.org/aynaud/communities/index.html).
  
      label_propagation - Label propagation algorithm (https://networkx.github.io/documentation/stable/reference/algorithms/community.html).
  
      You can pass your community detection algorithm to qstest. See "How to pass my community detection algorithm to qstest".
   
    num_of_rand_net (optional)  - Number of randomised networks. (Default: 500)
  
    alpha (optional)  - Statistical significance level before the Šidák correction. (Default: 0.05)
  
    num_of_thread (optional) - Maximum number of threads running in a CPU. (Default: 4)
  
  Output

    sg - C-dimensional list. sg[c] indicates that community c is significant (i.e., sg[c] = True) or insignificant (i.e., sg[c] = False). 
  
    pvals - C-dimensional list. pvals[c] is the p-value for community c. 
  
  Example
  
    import networkx as nx
    import qstest as qs
    
    network = nx.karate_club_graph()
    communities = qs.louvain_algorithm(network)
    sg, pvals = qs.qstest(network, communities, qs.qmod, qs.vol, qs.louvain_algorithm)
———————————————————————————————————————————————————————————————————————————
How to pass my quality function to qstest

  Write a quality function of a community (a large quality value indicates a good community) as follows:

    q = my_qfunc(network, community)

    Input
  
      network - Networkx Graph class instance.
   
      community - List of nodes belonging to a community.
  
    Output
  
      q - Quality of the community.

  Then, pass the implemented my_qfunc to qstest:

    sg, pvals = qstest(network, communities, my_qfunc, sfunc, cdalgorithm)

  Example

    import networkx as nx
    import qstest as qs
    
    # Number of intra-community edges
    def my_qfunc(network, nodes):
            return network.subgraph(nodes).size()
    
    network = nx.karate_club_graph()
    communities = qs.louvain_algorithm(network)
    sg, pvals = qs.qstest(network, communities, my_qfunc, qs.vol, qs.louvain_algorithm)
———————————————————————————————————————————————————————————————————————————
How to pass my size function to qstest
 
  Write a size function of a community as follows:
  
    sz = my_sfunc(network, community)

    Input
      network - Networkx Graph class instance.
 
      community - List of the IDs of nodes belonging to a community.

    Output

      sz - Size of the community.

  Then, provide the implemented my_sfunc to qstest:

    sg, pvals = qstest(network, communities, qfunc, my_sfunc, cdalgorithm)

  Example

    import networkx as nx
    import qstest as qs
    
    # Square of the number of nodes in a community
    def my_sfunc(network, nodes):
            return len(nodes) * len(nodes)
    
    network = nx.karate_club_graph()
    communities = qs.louvain_algorithm(network)
    sg, pvals = qs.qstest(network, communities, qs.qmod, my_sfunc, qs.louvain_algorithm)
———————————————————————————————————————————————————————————————————————————
How to pass my community detection algorithm to qstest

  To pass your community detection algorithm to qstest, write the following wrapper function:
   
    communities = my_cdalgorithm(network)

    Input 

      network - Networkx Graph class instance. 
    
    Output

      communities - C-dimensional list of lists. communities[c] is a list containing the IDs of nodes belonging to community c.
    
  Then, provide the implemented my_cdalgorithm to qstest:

    sg, pvals = qstest(network, communities, qfunc, sfunc, my_cdalgorithm)
    
  If the community-detection algorithm requires parameters such as the number of communities, then pass the parameters through global variables, e.g., define a global variable C, then access to C from the cdalgorithm.
  
  Example

    import networkx as nx
    import qstest as qs
    from networkx.algorithms import community as nxcdalgorithm
    
    # Wrapper function of async_fluidc implemented in Networkx 2.0
    def my_cdalgorithm(network):
            communities = []
            subnets = nx.connected_component_subgraphs(network)
            for subnet in subnets:
                    coms_iter = nxcdalgorithm.asyn_fluidc(subnet, min([C, subnet.order()]), maxiter)
                    for nodes in iter(coms_iter):
                           communities.append(list(nodes))
            return communities
    
    # Pareameters of the community detection algorithm called from my_cdalgorithm
    C = 3
    maxiter = 10
    
    network = nx.karate_club_graph()
    communities = my_cdalgorithm(network)
    sg, pvals = qs.qstest(network, communities, qs.qmod, qs.vol, my_cdalgorithm)
———————————————————————————————————————————————————————————————————————————
Requirements

  Python 2.7 or later.

  SciPy 1.0 or later.

  Networkx 2.0 or later.
———————————————————————————————————————————————————————————————————————————
Last updated: 28 November 2017
