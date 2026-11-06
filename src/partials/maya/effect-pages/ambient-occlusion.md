Ambient Occlusion (AO) darkens the image in areas that are hard to reach for the ambient light due to the local shape of the geometry (e.g. concavities, crevices, holes). Note that this effect depends only on the geometry (and the viewpoint, to a lesser extent), and not on the lights present in the scene.

<figure class="video-embed">
<iframe src="https://www.youtube.com/embed/FZfnh0KFKPg" title="Video" allowfullscreen loading="lazy"></iframe>
</figure>

:::note
Flair currently uses a screen-space implementation of ambient occlusion based on the _Ground-Truth Ambient Occlusion_ algorithm (GTAO).
:::

#### AO Blend Mode
Defines how the computed ambient occlusion is applied on the final image.
* **None**: AO is not applied.
* **Multiply**: the AO is multiplied over the image.
* **Color Burn**: same as above, except that the AO is blended over the image using the _Color Burn_ blending mode.
* **Style-specific**: AO is applied by the current style, so the effect depends on the style implementation. (default)
	* With styles other than the *Graph* styles, the AO modulates the *pigment density*, resulting in darker colors in occluded areas.

#### AO Radius
The radius used by the ambient occlusion filter: larger radius results in larger darkened areas.

#### AO Strength
The strength of ambient occlusion: higher values make the ambient occlusion darker.
