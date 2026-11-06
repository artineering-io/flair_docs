### Clean Lines
Clean lines can be customized in terms of intensity and color. Coloring of lines happens in the following order: [Density](#line-density), [Coloration](#line-coloration), [Light Response](#line-light-response).

#### Line Intensity
Opacity of the generated lines. A lower intensity will make the toon lines more transparent.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/lines/line-intensity.mp4" type="video/mp4" />
</video>
<figcaption>Line intensity between 0 and 1.</figcaption>
</figure>

:::note
As lines are generated at the middle of an edge, blending the intensity will reveal the edge underneath.
:::

#### Line Density
The density of the line, whereas a value of 1 equals the object's color. A higher density accumulates color making the line more saturated and darker. A lower density makes the line brighter.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/lines/line-density.mp4" type="video/mp4" />
</video>
<figcaption>Line density between 0 and 3.</figcaption>
</figure>

:::note
To see the full effect, the [Line Coloration](#line-coloration) and [Line Light Response](#line-light-response) should be set to 0.
:::

#### Line Color
Global color for the lines. The amount of line coloration can be adjusted with the _Line Coloration_ attribute below.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/lines/line-color.mp4" type="video/mp4" />
</video>
<figcaption>Changing toon line colors.</figcaption>
</figure>

#### Line Coloration

<a class="pill-link" href="#art-directable-attributes">Art-directable</a>

The amount of _Line Color_ that should be applied. A negative art-directed coloration will bring the line color back to the object's original color.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/lines/line-coloration.mp4" type="video/mp4" />
</video>
<figcaption>Line coloration between 0 and 1 at a line density of 1.</figcaption>
</figure>

#### Outline and Inline Light Response

<span class="new-label">New in Flair 1.2</span>
The influence lighting will have over the color of the outline (silhouette) or inline.

<div class="d-flex">

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/lines/line-light-response.mp4" type="video/mp4" />
</video>
<figcaption>Outline and Inline light response (-1...1).</figcaption>
</figure>
<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/lines/outline-light-response.mp4" type="video/mp4" />
</video>
<figcaption>Outline light response (-1...1).</figcaption>
</figure>

</div>

In this example, we set the flairShader `Diffuse Factor` to `1.0`, but toggle the [`Final Color`](/maya/materials/flair-shader/#final-color) setting so that lighting does not affect the material. That way, only the line responds to light. In cases where there is _z-fighting_ when coloring lines, make use of the `Offsets` setting within flairShader materials and modify the [`Depth Bias`](/maya/materials/flair-shader/#depth-bias) as needed.

:::note
You can use the Outline Light Response to make 2D rim lights!
:::
