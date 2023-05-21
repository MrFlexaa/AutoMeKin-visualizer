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
   
   I have added the formulas used in the study of Glicolonitrile. You can change it directly from the code at line 77. 
   Again,  a new direcory will be created to store the network with the name of the corresponding formula
  
 ```python
 formulass=['CH+CH2NO', 'CH2+CHNO','CHN+CH2O','CHO+CH2N','CN+CH3O','H2N+C2HO','H2O+CH2N','HO+C2H2N']
 ```
   
 
 
 







