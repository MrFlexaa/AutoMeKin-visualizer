Here Im going to explain the changes presented in the new version of RXVisualizer

- I have added this new parameters at the **profile_bokeh_plot** definition. This generate the Bokeh figure for energy profiles, create the graph generated from **RXReader** module. 
    ```python

    bfig.yaxis.axis_label_text_font = "Latex"

    bfig.y_range=bkm.Range1d(-19,169)
    bfig.yaxis.ticker=bkm.FixedTicker(ticks=[0,20,40,60,80,100,120,140,160])
    bfig.yaxis.major_label_overrides={0:'0', 20:'20', 40:'40', 60:'60', 80:'80', 100 :'100',120:'120' ,140:'140', 160:'160'}
    bfig.yaxis.major_label_text_font='latex'   #LATEX font style

    bfig.xgrid.grid_line_color = None
    bfig.ygrid.grid_line_color = None
    bfig.margin=(40,40,40,40)
    bfig.outline_line_color='white'

    bfig.x_range.flipped = True

    ```
    - LaTeX font style has been applied to the graph
    - y-axis ticker and limits customizables
    - Grid lines and margin removes
    - Possibility to invert the x-axis of the graphs.
    
    I would like to comment that the following line of code in the **profile_bokeh_plot** generate the list of ColumnDataSources, here is stored all the data of the paths.
    
    `cds_paths = profile_datasourcer(G,profile_list)`
    
    Here you can change the node data, for example,if you want to shift the x-axis in any path in order to make it fit into the graph. It has been useful to me when I had     two paths in the same graph and I wanted to move on node to the right in order to fit better with other ones.
    
    `cds_paths[y].data['x'][0]=new_value  #access to the x-axis data of this node from path y`
  
  
- In the same definition, **profile_bokeh_plot**, just before the energy_label are set up; we can change this data. We can also access to this information and change it. 
  We can move the energy label with the same idea as mentioned above (also **label_shift** is shown below).
  ```python
  def Elabel_shift(data,target_label, label_shift):
      if target_label in data['lab']:
          loc = [ndx for ndx,lab in enumerate(data["lab"]) if lab == target_label][0]
          data['y'][loc]+=label_shift
  ```

  `Elabel_shift(cds_lab_elab.data, "PRX", y)   #Move "PRX" y distance`
    
- At the end of RXVisualizer have been added some new functions established (made by Diego Garay-Ruiz) to be used in conjunction with the module **SVG.py**, in order to     make easier the generation and analysis of this graphs. 

  Here will be introduced some of these functions used in the **SVG** definition:

    - `rescale_profiles(prof,rescale_factor=1)` Get larger or smaller profiles for the image.
    - `arxvizz.label_shift(prof,"TS110",5) #move TSX y distance` Shift a specific label in a profile.
    - `show_energy(prof)` Display energies for a profile
    - We can also modify the colors of the paths that form the graph. Use a `color_palette` with a color or a set of colors (one for each path)
    ```python 
    #color_palette=['#956cb4','#6acc64','#ee854a','#4878d0'] 
    color_palette=['#797979']
    ```
    `recolor_profile(prof,color_palette)` 
    - `reset_profiles(prof)` Make all profiles visible, important to use after change some data of the graph, like using some parsing definitions.
    - Some functions such as `read_and_path`, `select_by_mol` and `hide_by_mol` were created to analyse the paths of the graph and parsing them, but this idea has been          integrated in the **paths** definitions beacuse we can get the desired paths directly.
    
    
<br />
<br />

I would like to mention that two style_information has been added at the beggining of RXVisalizer because the second one must be use specifically with the **SVG.py**
The size must be given in "pt" format, If we don't do it this way we have the following error from bokeh module:

`ERROR: WARNING:bokeh.io.export:The webdriver raised a TimeoutException while waiting for a 'bokeh:idle' event to signify that the layout has rendered. Something may have gone wrong`

The first time you see this error It may seem like a big problem, but it can be solved with that small detail. 



   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
