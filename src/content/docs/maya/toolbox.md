---
title: "Flair Toolbox"
sidebar:
  order: 7
---
The _Flair toolbox_ is a handy collection of style-specific and miscellaneous  tools opened by clicking on the `TBOX` [shelf icon](/maya/getting-started/flair-shelf/).

<figure class="aio-ui aio-window">
<img src="/media/maya/toolbox/tbox.png" alt="Flair Toolbox window" />
<figcaption>The Flair Toolbox containing useful style-specific and miscellaneous tools.</figcaption>
</figure>

## Warp Settings
Clicking on the Warp Settings button opens the _Warp Settings_ window, giving additional warp effect options.

<figure class="aio-ui aio-window">
<img src="/media/maya/warp-settings.png" alt="Warp settings window" />
<figcaption>The available Warp Settings.</figcaption>
</figure>

### Toggle instance on selected
This button will toggle the inflated instance which generates the warp effect on/off, thereby also enabling and disabling the effect. This is especially useful for transparent objects that should not drive the warped effect.

### Bake effect position on selected
This button will automatically check the _Animated_ attribute in materials assigned to the selected objects. Doing this will keep the warped effect in-place under animation.

## Unsubdivide Previews
_Unsubdivide Previews_ can be useful in a various situations where you need to work with unsubdivided meshes.
* When advecting (attaching) the canvas to the underlaying motion to correctly advect the canvas to the underlaying motion.
* For performance and stability issues on computers running with integrated graphics

To use it, simply select the objects from which you'd like to unsubdivide and click on the `Unsubdivide Previews` button.

:::note
If nothing is selected, the tool will try to unsubdivide **ALL** meshes/shapes in the scene.
:::

## Re-link textures
_Re-link textures_ opens up a file-dialog to select a folder in which to locate textures that are missing. When opening scenes that were stylized by someone else or from another computer, the texture paths within Flair materials might not be the same anymore. This button automatically re-links all existing textures from a specific directory with the click of a button.

:::note
The new image paths will be relative to the Maya project or absolute if outside of the Maya project's folder.
:::

## VRAM Info
Prints out details of the current Video Ram (VRAM) usage in Maya's _Script Editor_.

## Reset Viewport
Resets the viewport in case you are encountering glitching issues.

## Sanitize Flair

<span class="new-label">New in Flair 1.2</span>
Unloads the plugin and tries to remove all traces of Flair from the open scene. This is not undoable so a confirmation dialog will appear before it happens.

## Convert Materials
These buttons can quickly and automatically convert Maya materials to Flair or ShaderFX materials, inheriting attributes and textures. This is especially useful for quickly loading existing Maya scenes and seeing how they render in Flair. 

You can learn how this works in the [Convert Materials docs](/maya/materials/convert/#converting-multiple-objects-in-batch).
