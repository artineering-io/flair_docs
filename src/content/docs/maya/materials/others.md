---
title: "Other materials"
sidebar:
  order: 4
---
Flair features other bespoke materials used for certain styles that require different AOVs than the Flair shader material provides.

<figure class="float-right aio-ui">
<img src="/media/maya/materials/others/cutout-mat-ae.png" alt="Cutout material node" />
<figcaption>The default cutout material in the Attribute Editor.</figcaption>
</figure>

## Cutout material

The cutout material is required by the [**Cutout shader style**](/maya/styles/library/cutout) and generates the cutout stencil which needs to be set on all cutout objects. To assign this material on an object, select an object and load the "_\_cutout_" material preset (see [material presets](/maya/materials/presets)).

The cutout material controls how objects affect the cutout stencil and the paper color, and is divided in optional _Settings_ and _Attributes_.
   
### Settings
Closed by default, once opened, each _Setting_ allows you to customize what optional features the cutout material should have. Most of these settings are disabled by default, as to avoid unnecessary computations and clutter for artists. If needed, enabling settings will provide the necessary attributes to configure them.

#### VtxControl
Enables the control of stylization effects through the vertex colors. This attribute is automatically managed by _Flair_ and is activated as soon as you start using [_VertexFX_](/maya/art-direction/vertexfx/).

#### Colored
Overrides the color of the canvas with the color specified in the _Color Tint_ attribute, which is generated when this setting is checked.

#### Transparent
Only shows if the _Colored_ setting is checked, allows to create transparent colored cutouts. The setting creates relevant transparency attributes, [documented here](../flair-shader/#transparent).

#### Alpha
Allows the use of alpha masks to modify the cutout stencil. The setting creates relevant alpha attributes, [documented here](../flair-shader/#alpha-mask).

#### Displacement
Useful to add geometric detail, which can enhance the cutout silhouette. Displacement and its attributes are [documented here](../flair-shader/#displacement).

------------------------

### Attributes
The cutout material attributes modify the behaviour of the cutout material.

#### Cut
If checked, the material will make the object a cutout stencil. Otherwise, the object will not be cutout. This is enabled by default.

#### Cutout Mask
_Cutout Mask_ is an black and white uv-map that defines what parts of the object should be cut-out and which parts should not. This attribute toggles the use of the [_Cutout Mask File_](#cutout-mask-file).

#### Cutout Mask File
Specifies the file path to the _Cutout Mask_. In _Cutout Masks_, white is cut, whereas black is uncut. The path can be absolute or relative to the project root directory.

#### Color Tint
The color of the canvas is overridden with the custom color set by this attribute. This attribute is only available if the _Colored_ setting is enabled.

---

<figure class="float-right aio-ui">
<img src="/media/maya/materials/others/hatching-mat-ae.png" alt="Cutout material node" />
<figcaption>The default cutout material in the Attribute Editor.</figcaption>
</figure>

## Hatching Material

The hatching material is required by the [**Hatching shader style**](/maya/styles/library/hatching) and generates the required fractalized noise on all hatching/stippling objects. To assign this material on an object, select an object and load any "_\_hatching_" material preset (see [material presets](/maya/materials/presets)).

The hatching material shares most of the attributes of the normal Flair material, controlling whatever is behind the hatching lines. See the [Flair shader](/maya/materials/flair-shader) for a description on any undocumented attribute below.

:::note
Activate the `Deformed` setting attribute within Hatching materials to bake the hatching/stippling lines/points onto animated objects.
:::

### Density
Controls the overall density of the hatching lines.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/materials/others/density.mp4" style="width:300px" type="video/mp4" />
</video>
<figcaption>Varying density between 10 and 200</figcaption>
</figure>

### Dynamic Noise
If checked, enables the _fractalization_ that ensures a constant line density regardless of camera position and zoom. This may produces a slight "blending effect" when moving. Disable this attribute if the shot keeps the object at the same camera distance and zoom level.

<div class="d-flex">

<figure>
<video autoplay loop muted playsinline style="width:300px">
<source src="/media/maya/materials/others/fract_on.mp4" type="video/mp4" />
</video>
<figcaption>Dynamic noise enabled.</figcaption>
</figure>
<figure>
<video autoplay loop muted playsinline style="width:300px">
<source src="/media/maya/materials/others/fract_off.mp4" type="video/mp4" />
</video>
<figcaption>Dynamic noise disabled.</figcaption>
</figure>

</div>

------------------

## Stylization (proc.)
When the [_NoiseFX_](/tools/noisefx/) tool has been used on these custom material, the _Stylization (procedural)_ section will appear at the bottom of the _Attribute Editor_ within the material. This section contains all the procedural attributes that the _NoiseFX_ tool creates and modifies. Therefore, you can mostly ignore these attributes within the material, unless you want to key and animate them.

<figure class="aio-ui">
<img src="/media/maya/materials/others/noisefx-ae.png" alt="Stylization (procedural) attributes" />
<figcaption>Some procedural stylization attributes created through NoiseFX.</figcaption>
</figure>
