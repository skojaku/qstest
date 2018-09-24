Python codes for the (q, s)-test, a significance test for individual communities in networks. 

Please cite

  Kojaku, S. and Masuda, N. "A generalised significance test for individual communities in networks". Sci. Rep. 8, 7351 (2018)
———————————————————————————————————————————————————————————————————————————
Contents
  
  LICENSE - License of qstest
  
  README.md - README file for Github	

  README.txt - This README file

  setup.py - Script for installing qstest
 
  requirements.txt - List of libraries installed by setup.py 

  test.py - Test code for Travis CI

  .gitignore - Configuration file for GitHub
  
  .travis.yml - Configuration file for Travis CI
  
  qstest/ - Python codes for the (q, s)-test:
      
    qstest/__init__.py - Header file
  
    qstest/cdalgorithm_wrapper.py - Codes for community-detection algorithms

    qstest/qstest.py contains - Codes for the (q, s)-test 

    qstest/quality_functions.py - Codes for calculating quality functions of a community 
  
    qstest/size_functions.py - Codes for calculating the size of a community
  
  examples/ - example codes:
    
    examples/example1.py - Usage of qstest with a built-in quality function, community-size function and community detection algorithm

    examples/example2.py - Usage of qstest with a user-defined quality function

    examples/example3.py - Usage of qstest with a user-defined community-size function 

    examples/example4.py - Usage of qstest with a user-defined community-detection algorithm
———————————————————————————————————————————————————————————————————————————
Installation

  You can install qstest with pip, a package management system for Python.
  
  To install, run 

    pip install qstest

  If this does not work, try 
	
    python setup.py install
———————————————————————————————————————————————————————————————————————————
Usage
 
  sg, p_values = qstest(network, communities, qfunc, sfunc, cdalgorithm, num_of_rand_net = 500, alpha = 0.05, num_of_thread = 4)
 
  Input 

    network - Networkx Graph class instance
  
    communities - C-dimensional list of lists. communities[c] is a list containing the IDs of nodes belonging to community c. Node and community indices start from 0.
  
    qfunc - Quality of a community. The following quality functions are available:
  
      qmod - Contribution of a community to the modularity 
  
      qint - Internal average degree 
  
      qexp - Expansion　
  　
      qcnd - Conductance　
  
      To pass your quality function to qstest, see "How to pass your quality function to qstest" below.
  
    sfunc - Community-size function (i.e., size of a community). The following community-size functions are available:
  
      n - Number of nodes in a community
   
      vol - Sum of the degrees of nodes in a community
      
      To pass your community-size function to qstest, see "How to pass your community-size function to qstest" below.
     
    cdalgorithm - Community-detection algorithm. The following algorithms are available:
  
      louvain - Louvain algorithm (http://perso.crans.org/aynaud/communities/index.html)
  
      label_propagation - Label propagation algorithm (https://networkx.github.io/documentation/stable/reference/algorithms/community.html)
  
      To pass your community-detection algorithm to qstest, see "How to pass your community-detection algorithm to qstest" below.
   
    num_of_rand_net (optional) - Number of randomised networks (Default: 500)
  
    alpha (optional) - Statistical significance level before the Šidák correction (Default: 0.05)
  
    num_of_thread (optional) - Maximum number of CPU threads (Default: 4)
  
  Output

    sg - Results of the significance test (C-dimensional list). sg[c] = True or False indicates that community c is significant or insignificant, respectively. 
  
    p_values - P-values for the communities (C-dimensional list). p_values[c] is the p-value for community c. 
  
  Example (examples/example1.py)
  
    import networkx as nx
    import qstest as qs
    
    network = nx.karate_club_graph()
    communities = qs.louvain(network)
    sg, p_values = qs.qstest(network, communities, qs.qmod, qs.vol, qs.louvain)
———————————————————————————————————————————————————————————————————————————
How to pass your quality function to qstest

  Write a quality function of a community as follows:

    q = my_qfunc(network, community)

    Input
  
      network - Networkx Graph class instance
   
      community - List of nodes belonging to a community
  
    Output
  
      q - Quality of the community

  Then, pass my_qfunc to qstest:

    sg, p_values = qstest(network, communities, my_qfunc, sfunc, cdalgorithm)

  Example (examples/example2.py)

    import networkx as nx
    import qstest as qs
    
    # Number of intra-community edges
    def my_qfunc(network, nodes):
            return network.subgraph(nodes).size()
    
    network = nx.karate_club_graph()
    communities = qs.louvain(network)
    sg, p_values = qs.qstest(network, communities, my_qfunc, qs.vol, qs.louvain)
———————————————————————————————————————————————————————————————————————————
How to pass your community-size function to qstest
    
  Write a community-size function of a community as follows:
  
    s = my_sfunc(network, community)

    Input

      network - Networkx Graph class instance
 
      community - List of the IDs of nodes belonging to a community

    Output

      s - Size of the community

  Then, pass my_sfunc to qstest:

    sg, p_values = qstest(network, communities, qfunc, my_sfunc, cdalgorithm)

  Example (examples/example3.py)

    import networkx as nx
    import qstest as qs
    
    # Square of the number of nodes in a community
    def my_sfunc(network, nodes):
            return len(nodes) * len(nodes)
    
    network = nx.karate_club_graph()
    communities = qs.louvain(network)
    sg, p_values = qs.qstest(network, communities, qs.qmod, my_sfunc, qs.louvain)
———————————————————————————————————————————————————————————————————————————
How to pass your community-detection algorithm to qstest

  To pass your community-detection algorithm to qstest, write a wrapper function of the following form:
   
    communities = my_cdalgorithm(network)

    Input 

      network - Networkx Graph class instance
    
    Output

      communities - C-dimensional list of lists. communities[c] is a list containing the IDs of nodes belonging to community c.
    
  Then, pass my_cdalgorithm to qstest:

    sg, p_values = qstest(network, communities, qfunc, sfunc, my_cdalgorithm)
    
  If the community-detection algorithm requires parameters such as the number of communities, then pass the parameters as global variables, e.g., define a global variable X, then use X within the cdalgorithm.
  
  Example (examples/example4.py)

    import networkx as nx
    import qstest as qs
    from networkx.algorithms import community as nxcdalgorithm
    
    # Wrapper function for async_fluidc implemented in Networkx 2.0
    def my_cdalgorithm(network):
            communities = []
            subnets = nx.connected_component_subgraphs(network)
            for subnet in subnets:
                    coms_iter = nxcdalgorithm.asyn_fluidc(subnet, min([C, subnet.order()]), maxiter)
                    for nodes in iter(coms_iter):
                           communities.append(list(nodes))
            return communities
    
    # Pareameters of async_fluidc
    C = 3
    maxiter = 10
    
    network = nx.karate_club_graph()
    communities = my_cdalgorithm(network)
    sg, p_values = qs.qstest(network, communities, qs.qmod, qs.vol, my_cdalgorithm)
———————————————————————————————————————————————————————————————————————————
Requirements

  Python 2.7, 3.4 or later

  SciPy 1.0 or later

  Networkx 2.0 or later

  python-louvain 0.9
———————————————————————————————————————————————————————————————————————————
Last updated: 29 November 2017
