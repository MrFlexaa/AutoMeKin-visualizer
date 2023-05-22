# WORKFLOW
To understand how the modules **RXReader** and **RXVisualizer** work, on wich this program is based, please visit https://github.com/dgarayr/amk_tools/blob/master/UserGuide.md?plain=1
## get_network.py

This script have the same funtion that **amk_gen_view.py** from **amk_tools**.
The idea of this script is to get the CRN (chemical reaction networkx) once we have the data.
The data that we will analyze is stored in the RXNet.cg file (there are others RXNet files but this is the most important) in the directory FINAL_HL_MOL (or FINAL_LL_MOL, depending on the level of computation).

```python
finaldir="FINAL_HL_MOL"
rxnfile = "RXNet.cg" 
```
The first step is to create the graph G, getting the data from RXnet.cg and adding the barrierless paths from RXNet.barrless.

```python
data = arx.RX_parser(finaldir,rxnfile)
data_barrless = arx.RX_parser(finaldir=finaldir,rxnfile="RXNet.barrless")
joined_data = [data[ii]+data_barrless[ii] for ii in range(len(data))]
data = joined_data #esto sirve para meterle los barrless
# Building G
G = arx.RX_builder(finaldir,data)
```
* If we want to represent the global CRN we use the part of the code where no parsing has been developed yet, in order to get a general image.
we must use the command: 

  `$get_network.py FINAL_HL_GL global`
  
  I have used this finaldir name beacuse the molecule studied is **GL** (Glicolonitrile), you can use the name you want in the calculus.

* If we want to parse by the source and the final formula of the path use this command:

  `$get_network.py FINAL_HL_GL MIN1 CN+CH3O `
  
  A new direcory will be created to store the network with the name of the corresponding formula
  
* To facilitate te data analysis process you can add the list of all the final formulas that you want to study. To use this strategy use the command:
    
   `$get_network.py FINAL_HL_GL all`
   
   I have added the formulas used in the study of Glicolonitrile. You can change it directly from the code at line 67. 
   Again,  a new direcory will be created to store the network with the name of the corresponding formula
  
 ```python
 formulass=['CH+CH2NO', 'CH2+CHNO','CHN+CH2O','CHO+CH2N','CN+CH3O','H2N+C2HO','H2O+CH2N','HO+C2H2N']
 ```
 
 
 
 
 
## SVG.py

This script is used to get the CRN images of the profile energy in SVG format. This image can also be visualized in the interactivate network generated with **get_network.py**, but this image can only be downloaded in PNG format. That's why we use this sript, in order to export it as SVG.

The first step is to get the step involved in a CRN with the **paths** definition:


```python
def paths(source,formula, PR):
    finaldir = str("GL_H+/FINAL_HL_GL")
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
```
Here we create the graph based on the RXNet.cg data, in which barrierless paths are also included. Then the CRN is parsed by source, formula (target) and even PR (product).
The **paths** function returns the list of paths that makes up the CRN. All this paths are included in the previous analysis, they are shown in the interactivate networkx generated above; but this script gives us the list of this paths containing all the steps. Once we have these paths the subsequent analysis is easier.

This code must me modified directly in order to make easier te workflow.  To call the function we use:
```python
source = str('MIN29')
formula = str('CH2N+CH2O')
PR=str('PR156')  #parse prod 

limits,path_list=paths(source, formula, PR)
print(path_list)
```
the results is

`[['MIN1', 'TS45', 'MIN7', 'TSb_21', 'PR44']]`
In this case only one path has been found with this parameters. 
Once we select the path which will be studied, we can use the **SVG** definition to represent it.



ERROR: WARNING:bokeh.io.export:The webdriver raised a TimeoutException while waiting for a 'bokeh:idle' event to signify that the layout has rendered. Something may have gone wrong.

ocurre al poner un style_information slo se puede utilizar el parametro pt no se puede vh para los tamaños































































