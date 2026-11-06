---
title: "Bulk Attribute"
sidebar:
  order: 1
---
The bulk attribute tool (`BULK` icon in the [Flair shelf](/maya/getting-started/flair-shelf/)) allows to easily change settings and attributes of multiple Flair materials at the same time. Its functionality resembles the _Attribute Editor_, but it allows to modify all selected objects at once and provides other convenient functions.

<figure class="aio-ui aio-window">
<img src="/media/maya/art-direction/bulkattr/bulk-attr.png" alt="Bulk attribute tool" />
<figcaption>The bulk attribute tool shows all the settings and attributes from materials of selected objects.</figcaption>
</figure>

The settings and attributes that appear on the _Bulk Attribute_ tool depend on what objects or materials you have selected in the scene.

By default, the tool will automatically refresh when the selection changes to show the attributes/settings from selected materials or materials assigned to the current selection. You can disable this behaviour by unchecking the `Auto-refresh` option within the tool and refreshing manually through the `Refresh` button.

The material will be automatically gathered from any object you currently have selected. You can disable this behaviour by unchecking `Auto-materials` at the bottom right of the UI. If disabled, you will need to select the materials yourself for the attributes/settings to appear in the _Bulk Attribute_ tool.

## Convenience functions

When attributes have textures assigned to them, the attribute will present different convenience buttons to directly interact with it. The file path will be shown in a text edit, the `...` button will allow to directly browse for a new texture and the green reload button will quickly grab recent texture changes.

<figure class="aio-ui aio-window">
<img src="/media/maya/art-direction/bulkattr/bulk-texture-attr.png" alt="Bulk attribute tool" />
<figcaption>Texture attributes showing different convenience buttons.</figcaption>
</figure>

Scrolling over spin or combo boxes will modify their values. Allowing to see the changes without necessarilly click and dragging attributes around. So, to scroll the window, make sure to scroll on the left or right side to avoid changing attributes inadvertently.
