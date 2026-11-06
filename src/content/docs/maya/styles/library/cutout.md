---
title: "Cutout shader style"
sidebar:
  label: "Cutout"
  order: 3
---
<figure>
<img src="/media/maya/styles/library/cutout/header.jpg" alt="Cutout header image" />
</figure>

[Back to Cutout Features](https://artineering.io/styles/cutout
)

## Style breakdown

The cutout shader style emulates traditional paper cutout animation in 3D,
without using scissors and hundreds of paper sheets. No more trees or fingers are harmed when animating.

There are three fundamental elements within the cutout shader style which need to be controlled:
* Papers
* Cutout stencils
* External lighting

### Papers
The top and bottom layers of paper (canvases) are controlled respectively by the _Main canvas_ and _Alternate canvas_ attribute groups. There are over ten distinct _canvas textures_ (heightmaps) to choose from and you can even add your own. These can be customized in _color_, _scale_, _rotation_, _roughness_, _shading_, and _tiles_. See the [_canvas_ documentation](/maya/getting-started/globals/#canvas) for a description of these attributes.

### Cutout Stencils
The cutout stencils are created through the **[cutout material](/maya/materials/others/#cutout-material)**, which can easily be created and assigned using the [material presets](/maya/materials/presets/). Each cutout material automatically creates a stencil of the object it is assigned too. The cutout stencil can further be controlled and art-directed using [VertexFX](/maya/art-direction/vertexfx/) and [NoiseFX](/tools/noisefx/).

<div class="d-flex">

<figure>
<video autoplay loop muted playsinline style="height:150px;">
<source src="/media/maya/styles/library/cutout/noiseFX.mp4" type="video/mp4" />
</video>
<figcaption>Cutout controlled through NoiseFX.</figcaption>
</figure>
<figure>
<video autoplay loop muted playsinline style="height:150px;">
<source src="/media/maya/styles/library/cutout/paintFX.mp4" type="video/mp4" />
</video>
<figcaption>Cutout controlled through PaintFX.</figcaption>
</figure>

</div>

### External Lighting
External lighting affects the cast shadow (drop shadow) and bevel of the cutout, together with the overall shading of the paper sheets (canvases).

Lighting is controlled globally through the canvas light defined by the [Canvas Light Tilt](/maya/getting-started/globals/#canvas-light-tilt) and [Canvas Light Dir](/maya/getting-started/globals/#canvas-light-dir) attributes.

Only the two sheets of paper need to be lit within the cutout shader style. There will not be any shading control within the cutout material assigned to objects in the scene.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/cutout/lighting.mp4" type="video/mp4" />
</video>
<figcaption>Lighting affecting the Cutout stylization.</figcaption>
</figure>

---

## Tutorials

<div class="d-flex flex-justify-around">

<figure class="video-embed">
<iframe src="https://www.youtube.com/embed/gltNchMmyA0" title="Cutout 101 - How to use the cutout style in Flair/MNPRX" allowfullscreen loading="lazy"></iframe>
<figcaption>Cutout 101 - How to use the cutout style in Flair/MNPRX</figcaption>
</figure>

<figure class="video-embed">
<iframe src="https://www.youtube.com/embed/zrbPOeOdF0E" title="Cutout 102 - How to stylize an animation with the 3D Cutout style" allowfullscreen loading="lazy"></iframe>
<figcaption>Cutout 102 - How to stylize an animation with the 3D Cutout style</figcaption>
</figure>

</div>

---

## Attributes

In this section, we only document global attributes specific to the warp shader style. To learn more about other global attributes, please see the [globals node documentation](/maya/getting-started/globals).

<figure class="aio-ui">
<img src="/media/maya/styles/library/cutout/style-attrs.png" alt="Style attributes" />
<figcaption>Style attributes in the globals node</figcaption>
</figure>

:::note
The cutout style also requires a custom cutout material. The cutout material is documented [here](/maya/materials/others/#cutout-material).
:::

### Invert
Invert the cutout effect. This attribute is useful for emulating simple, two-layered paper cut animation, instead.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/cutout/invert.mp4" type="video/mp4" />
</video>
<figcaption>Inverting the cutout effect.</figcaption>
</figure>

### Distance
Distance between the two canvases (papers). A longer distance will increase the offset of the cast shadow.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/cutout/distance.mp4" type="video/mp4" />
</video>
<figcaption>Varying paper distance between 0 and 6</figcaption>
</figure>

### Drop Shadow
Intensity of the cast shadow.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/cutout/drop-shadow.mp4" type="video/mp4" />
</video>
<figcaption>Drop shadow between 0 and 6</figcaption>
</figure>

### Drop Shadow Radius
Radius of the drop shadow in pixels. This modifies the shadow casted by the top canvas (paper) on the bottom canvas.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/cutout/drop-shadow-radius.mp4" type="video/mp4" />
</video>
<figcaption>Drop shadow radius between 1 and 20</figcaption>
</figure>

### Outer Bevel Shadow
Intensity of the outer bevel shadow (paper curving away from the light).

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/cutout/outer-bevel-shadow.mp4" type="video/mp4" />
</video>
<figcaption>Outer bevel shadow between 0.0 and 1.2</figcaption>
</figure>

### Outer Bevel Highlight
Intensity of the outer bevel highlight (paper curving towards the light).

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/cutout/outer-bevel-highlight.mp4" type="video/mp4" />
</video>
<figcaption>Outer bevel highlights between 0.0 and 2.0</figcaption>
</figure>

### Outer Bevel Radius
Radius of the outer bevel in pixels. The outer bevel simulates the paper curving near cut edges.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/cutout/outer-bevel-radius.mp4" type="video/mp4" />
</video>
<figcaption>Outer bevel radius between 1 and 25</figcaption>
</figure>

### Cut Highlight
Intensity of the cut edge near the bevel shadow (cut edge facing the light). A value of zero means that the cut edge is invisible.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/cutout/cut-highlight.mp4" type="video/mp4" />
</video>
<figcaption>Cut highlight between 0 and 1.0</figcaption>
</figure>

### Cut Opp. Highlight
Intensity of the cut paper edge near the bevel highlight (cut edge turning away from the light). A value of zero means that the cut edge is invisible.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/cutout/cut-opp-highlight.mp4" type="video/mp4" />
</video>
<figcaption>Cut opposite highlight between 0 and 1.0</figcaption>
</figure>

### Gradient Shade
Intensity of the gradient shading effect. The gradient shading is a lighting gradient overlaid on the image and oriented towards the direction of the light.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/cutout/gradient-shade.mp4" type="video/mp4" />
</video>
<figcaption>Gradient shading between 0 and 1.0. The gradient follows the direction of the Canvas Light attribute.</figcaption>
</figure>

---

## Art-directable Attributes
Attributes labeled as art-directable can be controlled further with [NoiseFX](/tools/noisefx/), [VertexFX](/maya/art-direction/vertexfx/) and [proxy materials](/maya/materials/proxy-material/).
