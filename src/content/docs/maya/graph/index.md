---
title: "Flair Graph"
sidebar:
  label: Overview
  order: 0
---
<figure>
<img src="/media/maya/graph/header.jpg" alt="Flair graph example" />
</figure>

The Flair Graph allows artists to use, modify or create their own shader styles using a node-based framework.

## Using a Flair Graph

To use a Flair shader graph, load a "Graph" style within Flair either by loading a graph [style preset](/tools/style-presets/) (`(default)` or any style prepended with `g_`) or by manually changing the style to `Graph` in the [Globals](/maya/getting-started/globals) node's _Style_ attribute. This loads a graph shader style to use within Maya with all its defined global attributes and art-direction controls.

If you want to change the graph that is currently running, either load another preset or, if no preset for that graph is available, manually load the graph through the Globals node. To do so, select the Globals node and under `Style`, press on the `...` button to the right of the currently loaded graph style (see below). This will open a file selection dialog, that allows to select `*.flaira` files--which are saved graph styles.

<figure class="aio-ui">
<img src="/media/maya/graph/ae.png" alt="Flair graph button on the globals node" />
<figcaption>Currently loaded graph and "Show Flair Graph" button in the Attribute Editor.</figcaption>
</figure>

A graph shader style will behave exactly the same way as an in-built C++ style available in Flair. You can art-direct any scene and work the same way as with other shader styles. However, the Flair graph allows to completely customize the style at any point, if needed.

## Modify or create a Flair Graph

To modify or create a Flair graph shader style, you will have to open the Flair graph interface. This is done from within the Globals node, when a Flair graph style is loaded. Select the Globals node and under `Style`, press the `Show Flair Graph` button (see above). This will open the Flair graph interface in a separate window. 

The Flair graph interface allows you to completely customize the shader style and save it as a `*.flaira` file.
It is a simple but functional user interface to configure the shader style with nodes. We have broken it down in the [Interface Overview](./overview), so make sure to start there.

<figure class="aio-ui">
<img src="/media/maya/graph/main_interface.png" alt="Flair Graph Interface" />
<figcaption>The default Flair Graph interface.</figcaption>
</figure>

## Limitations

At the moment, only one instance of Maya can be open when using a Flair graph shader style.

Graph styles won't work with batch rendering yet. If you are planning to render a long project, please use a C++ shader style, instead.

Depending on the complexity of the Flair Graph, the performance of the shader style can be considerably slower compared to a C++ equivalent in Flair.

:::note
We are working on reducing/removing these three limitations. If you are interested in helping expedite this development, [get in touch](https://artineering.io/contact) with us.
:::
