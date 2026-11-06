---
title: "Convert Materials"
sidebar:
  order: 5
---
Flair materials are needed to take advantage of all Flair features. For this purpose, we have developed different ways to automatically convert conventional Maya and Arnold materials into Flair materials.

The Flair material conversion will try to port over the shading values and textures as best it can. This includes albedo, transparency, normal maps, shading (diffuse) and specularity.

## Converting through presets

When converting only a specific material to a Flair material, it is best to take advantage of the `_inherit` material preset. Select the object or component with the material you wish to convert and load the `_inherit` preset. This will automatically convert the material to a Flair material and try to keep all assigned textures. Learn more about [material presets here](/maya/materials/presets/).

<figure class="aio-ui aio-window">
<img src="/media/maya/materials/convert/inherit-preset.png" alt="Inherit preset in material presets window" />
<figcaption>The _inherit preset in the Material presets tool.</figcaption>
</figure>

:::note
When converting a material, keep in mind that all objects that had the previous material assigned will also have the new Flair shader material. To have only the selected object or component change material, you need to toggle `Create new material` in the material presets window first.
:::

## Converting multiple objects in batch

When converting more than one material, it is best to use the material convertion buttons available in the [Flair toolbox](/maya/toolbox/).

<figure class="aio-ui aio-window">
<img src="/media/maya/materials/convert/convert.png" alt="Material convertion tools in the Flair toolbox" />
<figcaption>The material convertion options in the Flair Toolbox.</figcaption>
</figure>

These buttons will convert all selected objects to Flair materials or ShaderFX materials. If no object is selected, all materials in the scene will be converted. So, depending on your current selection when pressing the button, the following confirmation messages appear.

<div class="d-flex">

<figure class="aio-ui aio-window">
<img src="/media/maya/materials/convert/convert-selected.png" alt="Convert selected confirmation message" />
<figcaption>Confirm the convertion of current selection.</figcaption>
</figure>
<figure class="aio-ui aio-window">
<img src="/media/maya/materials/convert/convert-all.png" alt="Convert ALL confirmation message" />
<figcaption>Confirm the convertion of ALL materials.</figcaption>
</figure>

</div>

Once the confirmation dialog are accepted, the materials will be automatically converted.

To automate this process in a script, you can use the `convert_to_flair(objs=None)` function in the `maya/scripts/flair_materials.py` file.

```python
import flair_materials as fmat
fmat.convert_to_flair()
```
