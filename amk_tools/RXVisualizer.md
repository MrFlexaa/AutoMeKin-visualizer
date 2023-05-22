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
  We can move the energy label with the same idea as mentioned above. 
  ```python
  def Elabel_shift(data,target_label, label_shift):
      if target_label in data['lab']:
          loc = [ndx for ndx,lab in enumerate(data["lab"]) if lab == target_label][0]
          data['y'][loc]+=label_shift
  ```

  `Elabel_shift(cds_lab_elab.data, "PRX", y)   #Move "PRX" y distance`
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
