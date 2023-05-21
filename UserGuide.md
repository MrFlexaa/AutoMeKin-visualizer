# WORKFLOW
To understand how the modules **RXReader** and **RXVisualizer** work, on wich this program is based, please visit https://github.com/dgarayr/amk_tools/blob/master/UserGuide.md?plain=1
## get_network.py

This script have the same funtion that **amk_gen_view.py** from **amk_tools**.
The idea of this script is to get the CRN (chemical reaction networkx) once we have the data.
The data that we will analyze is store in the RXNet.cg file (there are others RXNet files but this is the most important) in the directory FINAL_HL_MOL (or FINAL_LL_MOL, depending on the level of computation).

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
If we want to represent the global CRN we use this part of the code. Here no parsing has been developed because we want a general image.

we must use the command `$get_network.py finaldir global`


In the case of Glicolonitrile here exposed we would get this:






