### Advanced Controls
To generate lines, we run an edge-detection algorithm on three different types of data: depth, normals and color. So, whenever there is a difference within neighboring pixels for each data type, an edge is extracted.

There is a specific limit to the difference in depth, normals, and color that needs to be exceeded to extract an edge. This limit, in technical terms, is called a threshold. Advanced controls give access to these thresholds to adjust the generated lines.

#### Depth Edge Threshold
Depth threshold at which a line from _depth_ differences is generated. 0.001 will generate an edge on minuscule depth differences, a higher value will generate an edge only after a certain depth difference has been achieved. 
The depth threshold is directly linked to the global [World Scale](/maya/getting-started/globals/#world-scale) attribute so that the same values can be used at different world scales.

:::note
If _Flow Edge Threshold_ and _Color Edge Threshold_ are set to 1.0, a high _Depth Edge Threshold_ will only show lines at silhouettes.
:::

#### Flow Edge Threshold
Flow threshold at which a line from _normal_ differences is generated. 0.001 will generate an edge on minuscule normal differences, whereas 1.0 will remove lines from normals altogether.

:::note
Normal maps change the normals and therefore also help generate edges at specific parts of objects.
:::

#### Color Edge Threshold
Color threshold at which a line from _color_ differences is generated. 0.001 will generate an edge on minuscule color differences, whereas 1.0 will remove lines from color altogether. 

:::note
Having low color edge thresholds will make the edge detection quite sensitive to noise or grunge in textures.
:::

#### Lighting Edge Blend
Amount of lighting within the color pass to generate edges from. At a _Lighting Edge Blend_ of 0.0, the color will only consist of the albedo. At a _Lighting Edge Blend_ of 1.0, lighting will be applied too the albedo, so edges can also be generated from cast shadows and shading.
