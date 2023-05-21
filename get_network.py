#script to get the network

from amk_tools.RXVisualizer import *
from amk_tools import RXReader as arx
from amk_tools import RXVisualizer as arxviz
import networkx as nx
import sys
import os

# from amk_tools 
def generate_network(finaldir,source, formula):
    rxnfile = "RXNet.cg"
    # Adding barrierless channels
    data = arx.RX_parser(finaldir,rxnfile)
    data_barrless = arx.RX_parser(finaldir=finaldir,rxnfile="RXNet.barrless")

    joined_data = [data[ii]+data_barrless[ii] for ii in range(len(data))]
    data = joined_data #adding barrless
    # Building G

    G = arx.RX_builder(finaldir,data)
    target = arx.formula_locator(G,formula)
    limits = arx.node_synonym_search(G,[[source],target])
    path_list = arx.add_paths(G,limits[0],limits[1])
    G = arx.graph_path_selector(G,path_list)
    
    # Generate visualization (& handle model addition)
    layout = arxviz.generate_visualization(G,finaldir,title="Network"+formula,outfile=dir_network+"\\network_"+formula+".html",
                                        Nvibrations=-1,with_profiles=True,
                                        layout_function=nx.kamada_kawai_layout) #nx.kamada_kawai_layout) nx.spring_layout()


finaldir = str(sys.argv[1]) #dir where is rxnfile
rxnfile = "RXNet.cg" #file where is the data
# Adding barrierless channels
data = arx.RX_parser(finaldir,rxnfile)
data_barrless = arx.RX_parser(finaldir=finaldir,rxnfile="RXNet.barrless")
joined_data = [data[ii]+data_barrless[ii] for ii in range(len(data))]
data = joined_data #esto sirve para meterle los barrless
# Building G
G = arx.RX_builder(finaldir,data)

source = str(sys.argv[2]) 
if sys.argv[2]=="global":
    # paht_list contains all channels
    path_list = arx.add_paths(G)
    newdir_net="network_paths" #create new dir in order to store the results there
    dir_network=os.path.join(finaldir,newdir_net)
    isExist=os.path.exists(dir_network)
    if not isExist:
        os.makedirs(dir_network)    
    # Generate visualization (& handle model addition)
    layout = arxviz.generate_visualization(G,finaldir,title="Network visualization",outfile=dir_network+"\\network_"+sys.argv[2]+".html",
                                        Nvibrations=-1,with_profiles=True,
                                        layout_function=nx.kamada_kawai_layout)  #nx.kamada_kawai_layout) nx.spring_layout()
else:
    source = str(sys.argv[2]) #molecule that start the CRN
    formula = str(sys.argv[3]) #molecules that will finish the paths from the source
    
    #create paths networkx for all the formulas in the arrays
    if (sys.argv[3])=='all':
        newdir_net="network_all_paths"
        dir_network=os.path.join(finaldir,newdir_net)
        isExist=os.path.exists(dir_network)
        if not isExist:
            os.makedirs(dir_network)
        formulass=['CH+CH2NO', 'CH2+CHNO','CHN+CH2O','CHO+CH2N','CN+CH3O','H2N+C2HO','H2O+CH2N','HO+C2H2N']
        for formulas in formulass:
            generate_network(finaldir, source, formulas)
  
    target = arx.formula_locator(G,formula)
    limits = arx.node_synonym_search(G,[[source],target])
    path_list = arx.add_paths(G,limits[0],limits[1])
    # Printing all paths found
    newdir_net="network_paths"
    dir_network=os.path.join(finaldir,newdir_net)
    isExist=os.path.exists(dir_network)
    if not isExist:
        os.makedirs(dir_network)
    # Reduce the graph, keeping only the nodes involved in paths
    G = arx.graph_path_selector(G,path_list)
    
    # Generate visualization (& handle model addition)
    layout = arxviz.generate_visualization(G,finaldir,title="Network visualization",outfile=dir_network+"\\network_"+formula+".html",
                                        Nvibrations=-1,with_profiles=True,
                                        layout_function=nx.kamada_kawai_layout) #nx.kamada_kawai_layout) nx.spring_layout()
#the networkx will be stored in the folder HL, in a subfolder called network_path








    
    
