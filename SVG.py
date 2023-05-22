from amk_tools import RXReader as arx
from amk_tools.RXVisualizer import *
from amk_tools import RXVisualizer as arxvizz
from amk_tools import SVG_Generation_AMKTools as arxSVG
from bokeh.io import export_svg 
import networkx as nx
import os



# Parsing files in directory finaldir
# RXNet file is rxnfile 
def SVG(x):
    finaldir = str("FINAL_HL_GL")  #change the directory  
    rxnfile = "RXNet.cg"
    
    #parameters of the figure
    size_height=900
    size_width=900 

    newdir_net=str("SVG_GRAPHS") #new dir created
    newdir_net_2=str(x[0])
    dir_network=os.path.join(finaldir,newdir_net)
    isExist=os.path.exists(dir_network)
    if not isExist:
        os.makedirs(dir_network)
        
    dir_network_2=os.path.join(dir_network,newdir_net_2)
    isExist=os.path.exists(dir_network_2)
    if not isExist:
        os.makedirs(dir_network_2)
    
    #Create the graph G
    # Reduce the graph, keeping only the nodes involved in paths
    data = arx.RX_parser(finaldir,rxnfile)
    data_barrless = arx.RX_parser(finaldir=finaldir,rxnfile="RXNet.barrless")
    joined_data = [data[ii]+data_barrless[ii] for ii in range(len(data))]
    data = joined_data 
    # Building and parsing G
    G = arx.RX_builder(finaldir,data)
    path_list=x
    G = arx.graph_path_selector(G,path_list)
    layout = arxvizz.generate_visualization(G,finaldir,title="Network visualization",outfile=dir_network_2+"\\network_.html",
                                                Nvibrations=-1,with_profiles=True,
                                                  layout_function=nx.kamada_kawai_layout) #nx.kamada_kawai_layout) nx.spring_layout()

    #we just have a G created but we are going to modify its path
    #G,paths = read_and_path(finaldir,rxnfile,barrierless,source,target,ethr=150)
    prof = arxvizz.profile_bokeh_plot(G,paths,width=size_width,height=size_height,out_backend="svg") #900, 900  
    # Call functions to modify the profiles, as if we were in the GUI

    # Styling for the resulting graph: RXVisualizer and change parameters
    #color_palette=['#956cb4','#6acc64','#ee854a','#4878d0'] #list of colour, one for each path
    color_palette=['#797979'] #grey
    
    arxvizz.rescale_profiles(prof,rescale_factor=1)
    #label shift definition, move the label up or down for better results useful if you have several paths
    #arxvizz.label_shift(prof,"TS110",5) #move TSX y distance
    arxvizz.show_energy(prof)
    
    arxvizz.recolor_profile(prof,color_palette)
    
    	# Generation of images, isolating the products in the list
    #paths of those products
    
    #global,parsing MIN-->TARGET and PROD

    export_svg(prof,filename=dir_network_2+"\\"+str(x[0])+".svg",width=size_width,height=size_height) #900,900
    arxSVG.reset_profiles(prof)
        


#get paths given the formula, source and target (PR)
def paths(source,formula, PR):
    finaldir = str("FINAL_HL_GL") #change dir if necessary
    rxnfile = "RXNet.cg"
    
    #FINAL_HL_GL RXNet.cg MIN1 HO+C2H2N PR25
    # Adding barrierless channels
    data = arx.RX_parser(finaldir,rxnfile)
    data_barrless = arx.RX_parser(finaldir=finaldir,rxnfile="RXNet.barrless")
        
    joined_data = [data[ii]+data_barrless[ii] for ii in range(len(data))]
    data = joined_data #esto sirve para meterle los barrless
    # Building and parsing G
    G = arx.RX_builder(finaldir,data)
    target = arx.formula_locator(G,formula)
    limits = arx.node_synonym_search(G,[[source],target])
    #parsing the paths
    path_list = arx.add_paths(G,[source],[PR],skip_int_frags=True)
    return limits, path_list
    #this path_list just give you the path of this parsed networkx
    
    

#parameters of the networkx
#get the paths_list of this network, in order to use it in SVG def
source = str('MIN1')
formula = str('CN+CH3O')
PR=str('PR44')  #parse prod 

limits,path_list=paths(source, formula, PR)
print(path_list)


#use the path given before
paths=[['MIN1', 'TS45', 'MIN7', 'TSb_21', 'PR44']]
SVG(paths)
