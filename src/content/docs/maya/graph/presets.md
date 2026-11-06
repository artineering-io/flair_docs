---
title: "Node Presets"
sidebar:
  order: 7
---
Node _presets_ can facilitate the creation of one or multiple nodes with the click of a button.

<figure class="aio-ui">
<img src="/media/maya/graph/presets/presets_context.png" alt="The available presets when right-clicking on the graph interface" />
<figcaption>The available presets when right-clicking on the graph interface.</figcaption>
</figure>

## Loading a preset
To load a preset, simply select it from the right-click context menu (see above).

## Creating a preset
Creating a preset unfortunately requires a bit more work.

Selected nodes can be serialized to _json_ by simply copying them `Ctrl + c`. These can in turn be pasted `Ctrl + v` in other Flair graphs or even sent via email for someone else to paste it in their Flair graphs.

To make a preset, copy the nodes that make the preset and paste them in a text file under `Flair->presets->nodes` with the `.json` extension.

The preset will then be available the next time the Flair graph style is loaded in _Maya_ or when Flair in standalone is restarted. The preset in the context menu has the same name as the preset _json_ file.
