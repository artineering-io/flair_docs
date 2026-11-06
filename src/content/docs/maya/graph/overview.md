---
title: "Interface Overview"
sidebar:
  order: 1
---
The Flair graph interface comprises 5 distinct panels (sections), each responsible for defining and controlling the shader style. 

This page contains an overview on how to interact with Flair and where to dive deeper when necessary. All panels can be toggled anytime through the `View` button in the Flair Graph menu.

<figure class="aio-ui">
<img src="/media/maya/graph/overview/all_panels.png" alt="Flair Graph Interface showing all panels" />
<figcaption>The Flair Graph interface with the most used panels open.</figcaption>
</figure>

### 1. Node Graph
The node graph is the central node interface defining the shader pipeline.
In this panel, you can create nodes, select them to modify their properties and connect them to each other to build an image-processing shader pipeline. You can consider it the "document" where the shader pipeline is "written" with nodes.

Further documentation on how to interact and what can be done with the node graph can be found [here](/maya/graph/node-graph).

### 2. Parameters
The parameters panel is context sensitive, showing the parameters of selected nodes in the graph. If no node is selected, it will be blank. In Maya, this would be the equivalent of the _Attribute Editor_. When a node is selected, the Parameters panel will show the available parameters.

<figure class="aio-ui">
<img src="/media/maya/graph/overview/parameters.png" alt="The parameters of a shader node" />
<figcaption>The parameters of a shader node that contains a motion blur shader.</figcaption>
</figure>

1. Type of node, in this case a `shader` node.
2. Name of the node, which can be defined/set here.
3. Input parameter name, automatically prepended by an `i:` for "input".
4. Exact value of the parameter. In this example, we have a float parameter, but this will look different depending on the type of parameter.
5. An optional interface to interact and set the parameter without inputing exact values.
6. Parameters that support expressions, will show a "magic wand" icon (<i class="fas fa-magic"></i>) to the right of them. Once toggled (clicked), the widgets to set values will be replaced by a green text field to enter an expression (see 7).
7. Text field to enter expressions. Learn more about expressions [here](/maya/graph/expressions)

More details about node parameters are available in the documentation for each node type.

### 3. Globals
The globals panel defines the global attributes that will be available in the Maya _Attribute Editor_. The same globals can also be used in [expressions](/maya/graph/expressions) within shader node parameters. Supported global values can be:

- integers (`int`)
- floats (`float`)
- vectors (`vec2`, `vec3`, or `vec4`)
- or options (`enum`).

:::note
Globals are _declared_ in the Flair graph using the _Globals_ panel `Menu→View→Globals` and are _defined_ (set) in the host application (i.e., Maya).
:::

<figure class="aio-ui">
<img src="/media/maya/graph/overview/globals.png" alt="The globals of the Flair document" />
<figcaption>The globals of the Flair document.</figcaption>
</figure>

1. `+` button opens the "Add a Global" dialog (shown below), which helps add global attributes.
2. Current properties of the global will change depending on the type of global attribute.
3. Edit the global attribute, this button will open the "Add a Global" dialog again for editing.
4. Delete the global attribute.

Once the `+` button is clicked, the "Add a Global" window appears to add or customize existing globals.

<figure class="aio-ui aio-window">
<img src="/media/maya/graph/overview/add_a_global.png" alt="The Add a Global dialog" />
<figcaption>The "Add a Global" dialog shown after pressing the "+" button.</figcaption>
</figure>

1. New Global attribute name (some names are reserved by Flair, including names starting with "_").
2. Type of Global attribute to create
3. Properties of the Global attribute, this will change depending on the type of Global being created. For `enum` globals, the first field you indicate will be set as the default field.
4. `Ok` will create the global.

When a global is added, it can be used by its name in parameter expressions and will be automatically appear in the _Attribute Editor_ within _Autodesk Maya_. The global can be set and keyed in Maya for each frame and is automatically udated in the Flair graph.

<figure class="aio-ui">
<img src="/media/maya/graph/overview/global_ae.png" alt="A global in the Attribute Editor of Maya" />
<figcaption>The newly created global in the Attribute Editor of the "custom" Flair graph style.</figcaption>
</figure>

### 4. Control definitions
The control definition panel dynamically defines the _noiseFX_ and _vertexFX_ controls available to control the shader style in Maya.

<figure class="aio-ui">
<img src="/media/maya/graph/overview/control_definitions.png" alt="The control definitions of the Flair document" />
<figcaption>The control definitions of the Flair document.</figcaption>
</figure>

1. `+` button adds a new definition group to define a new control. A definition group is comprised of two sections, the left section contains the control properties, whereas the right sections defines the naming of control options. The tooltips shown when hovering over elements explain their use, which is also documented below.
2. Name of the control written vertically on the left side of the _vertexFX and _noiseFX_ widgets.
3. Description of the control appearing on top of the control.
4. Control target (image) that the control will modify. Flair currently supports only 4 targets.
5. Channel that the control will modify in the target (image). Some targets support the modification of more than one channel for the same control.
6. If "Only Positive" values are to be modified. Default are positive and negative values.
7. VertexFX options to _increase_ or _decrease_ the control parameter.
8. NoiseFX option to increase the noise fluctuation of the control parameter e.g., *density* effect noise can be called *turbulence*.
9. Delete the control definition group.

Each control definition group will automatically modify the _NoiseFX_ and _VertexFX_ interface within Maya.

<figure class="aio-ui">
<div class="d-flex bottom">

<img src="/media/maya/graph/overview/control_vertexfx.png" alt="The newly defined control in the VertexFX tool" />
<img src="/media/maya/graph/overview/control_noisefx.png" alt="The newly defined control in the NoiseFX tool" />

</div>
<figcaption>The newly created control within the NoiseFX and VertexFX tools based on the control definition.</figcaption>
</figure>

#### Customizing the icons in VertexFX and NoiseFX control widgets

To customize the icons that appear on the _VertexFX_ and _NoiseFX_ tool in Maya, you need to place icons with the exact same name as in the control definition (1) in the `Flair/maya`, under `icons/nFx` or `icons/pFx`.

### 5. Settings
The settings panel defines the graph settings, which are globals that only affect the current Flair graph document.

<figure class="aio-ui">
<img src="/media/maya/graph/overview/settings.png" alt="The Settings of the Flair document" />
<figcaption>The settings of the Flair document.</figcaption>
</figure>

:::note
When using the Flair graph as a plugin, this panel can be mostly ignored as the values are automatically gathered from the host application.
:::

#### Project Directory

Allows to set a directory, which other file paths can be relative from. This is useful for sharing Flair graphs with others.

#### World Scale

Defines a global world scale for converting between different 3D measurement units.
