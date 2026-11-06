---
title: "Flair shader"
sidebar:
  order: 2
---
The _Flair Shader_ material was developed to meet most painterly shading requirements, support art-direction and render the necessary AOVs (Arbitrary Object Values i.e., normals, motion vectors...) in real-time. Built from scratch using the Maya API, it was conceived for artists, offering features only when needed.

:::note
A _Flair Shader_ material has two types of 'attributes': [**Settings**](.#settings) and normal [**Attributes**](.#painterly-shading).
:::

<figure class="aio-ui">
<img src="/media/maya/materials/flair-shader/node-AE.png" alt="Flair Shader material node attributes" />
<figcaption>The default Flair Shader material in the Attribute Editor.</figcaption>
</figure>

The first section of a Flair Shader material within the attribute editor, provides the [**Settings**](.#settings) that allow to enable/disable what features the material should have. Therefore, we document the default material [**Attributes**](.#painterly-shading) first.

## Painterly Shading
Painterly shading attributes focus on bringing colors into the foreground of shading control and work differently than most attributes found in PBR materials. This doesn't mean that they can't be combined with normal [_Shading_](#shading) parameters, but they require 3D artists to go back to thinking in terms of colors and light. The first group of attributes control the color in the lit parts of objects, whereas the second group of attributes (from [_Diffuse Factor_](#diffuse-factor) onwards) control the color in the shade of objects.

:::note
Painterly shading attributes are baked onto albedo AOVs and can't be separated for compositing purposes.
:::

### Cangiante
_Cangiante_ illumination changes the hue of the lit area towards a brighter and saturated related color. This attributes can also be used to enhance the color of any applied [_Albedo_](#albedo).
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/cangiante.mp4" type="video/mp4" />
</video>
<figcaption>Cangiante illumination (0...2.0)</figcaption>
</figure>

### Cangiante Wrap
_Cangiante Wrap_ defines the area of effect for the [_Cangiante_](#cangiante) illumination attribute.
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/cangiante-wrap.mp4" type="video/mp4" />
</video>
<figcaption>Cangiante Wrap (0...1.0)</figcaption>
</figure>

### Custom Light
_Custom Light_ changes the color of the lit area towards the [_Custom Light Color_](#custom-light-color).
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/light.mp4" type="video/mp4" />
</video>
<figcaption>Custom Light (0...1.0)</figcaption>
</figure>

### Custom Light Wrap
_Custom Light Wrap_ defines the area of effect for the [_Custom Light_](#custom-light) attribute.
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/light-wrap.mp4" type="video/mp4" />
</video>
<figcaption>Custom Light Wrap (0...1.0)</figcaption>
</figure>

### Custom Light Color
_Custom Light Color_ defines a custom color used by the [_Custom Light_](#custom-light) and [_Highlight_](#highlight) attributes.
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/light-color.mp4" type="video/mp4" />
</video>
<figcaption>Different custom light colors</figcaption>
</figure>

### Diffuse Factor
_Diffuse Factor_ defines the amount of diffuse shading within the material. `0` will be flat shading (entirely lit), `1` will be completely diffuse.
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/diffuse-factor.mp4" type="video/mp4" />
</video>
<figcaption>Diffuse Factor (0...1.0)</figcaption>
</figure>

:::note
For scenes that require strong contrasts in shading (e.g., at night), keep the _Diffuse Factor_ close to `1`.
:::

### Custom Shade
_Custom Shade_ changes the color of the shade area towards the [_Custom Shade Color_](#custom-shade-color).
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/shade.mp4" type="video/mp4" />
</video>
<figcaption>Custom Shade (0...1.0)</figcaption>
</figure>

### Custom Shade Wrap
_Custom Shade Wrap_ defines the area of effect for the _Custom Shade_ attribute. It behaves like the [_Custom Light Wrap_](#custom-light-wrap), but for the shade of an object.
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/shade-wrap.mp4" type="video/mp4" />
</video>
<figcaption>Custom Shade Wrap (0...1.0)</figcaption>
</figure>

### Custom Shade Color
_Custom Shade Color_ defines a custom color used by the [_Custom Shade_](#custom-shade) and [_Shadow Color Offset_](#shadow-color-offset) attributes.
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/shade-color.mp4" type="video/mp4" />
</video>
<figcaption>Different custom shade colors showcased with the Shadow Color Offset enabled</figcaption>
</figure>

### Shadow Color Offset
_Shadow Color Offset_ offsets the shadow color of a light to the [_Custom Shade Color_](#custom-shade-color).
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/shadow-color-offset.mp4" type="video/mp4" />
</video>
<figcaption>Shadow Color Offset on/off</figcaption>
</figure>

-----------------

## Shading
Shading attributes focus on common attributes found in materials, including various uses of texture mapping for different shading effects.

### Shading
_Shading_ defines the amount of shading within the material. `0` will be flat shading (entirely unlit), `1` will be shaded. It's the opposite of [_Diffuse Factor_](#diffuse-factor) and won't affect lighting from [_Light Maps_](#lightmap).
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/shading.mp4" type="video/mp4" />
</video>
<figcaption>Shading (0...1.0)</figcaption>
</figure>

### Color Tint
_Color Tint_ defines a custom tint color. It is especially useful when mixing an additional color to the albedo color or textures. The color tint will multiply with the albedo to tint it accordingly. So, leave the color tint white if you only want the color of the albedo texture.
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/color-tint.mp4" type="video/mp4" />
</video>
<figcaption>Different tint colors showcased with a Diffuse Factor of 0.6</figcaption>
</figure>

### Albedo
_Albedo_ contains the raw colors of the object, without any lighting information. Use a plain color or click on the checkerboard icon to select a texture.

<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/albedo-tint.mp4" type="video/mp4" />
</video>
<figcaption>Albedo Texture with different tint colors and a Diffuse Factor of 0.85</figcaption>
</figure>

Albedo textures with an alpha channel will only show transparency if the [Transparent](#transparent) setting is activated. Any albedo transparency will be overriden if you specify a custom _transparency map_ or _alpha mask_.

### Normal Map
_Normal Map_ is a texture which contains normal inclination deviations of the surface in the red and green channels, adding geometric detail without using polygons. Click on the checkerboard icon to select a texture.

### Bump Depth
Defines the intensity of the normal inclinations in the [_Normal Map_](#normal-map).
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/normal-map.mp4" type="video/mp4" />
</video>
<figcaption>Normal Map with Bump Depth (0...3.0)</figcaption>
</figure>

------------------
------------------

## Settings

Additional material attributes for optional features can be created on-demand by enabling different settings.

Setting attributes are found in the first section of the _Attribute Editor_. Most settings are disabled by default, as to avoid unnecessary computations and clutter for artists. When needed, enabling settings will show the necessary attributes in the Attribute Editor, any copied tabs thereof, and in the Property Editor of the Hypershade window.

---

### Toon Shaded

The _Toon Shaded_ setting activates toon/cell shading. Toon shading within Flair separates the reflectance of light into three regions i.e., shade, mid and light region. Each region can be controlled through the toon shading attributes in the Attribute Editor.

<figure class="aio-ui">
<img src="/media/maya/materials/flair-shader/toon-AE.png" alt="Toon Shading attributes in the Attribute Editor" />
<figcaption>The Toon Shading section in the Attribute Editor.</figcaption>
</figure>

#### Toon Shade Color
The _Toon Shade Color_ defines the color of the shade toon region.
<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/toon-shade-color.mp4" type="video/mp4" />
</video>
<figcaption>Different toon shade colors</figcaption>
</figure>

#### Toon Shade Wrap
The _Toon Shade Wrap_ defines the area of effect for the toon shade region.
<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/toon-shade-wrap.mp4" type="video/mp4" />
</video>
<figcaption>Toon shade wrap (0...1)</figcaption>
</figure>

#### Toon Shade Blur
The _Toon Shade Blur_ defines the softness between the shade and mid toon regions.
<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/toon-shade-blur.mp4" type="video/mp4" />
</video>
<figcaption>Toon shade blur (0...1)</figcaption>
</figure>

:::note
Toon region blur can also be controlled locally with VertexFX and NoiseFX, by enabling the _Toon Toolset_: `Fair Toolbox -> Toon Settings -> Toon Toolset`.
:::

#### Toon Mid Color
The _Toon Mid Color_ defines the color of the mid toon region.
<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/toon-mid-color.mp4" type="video/mp4" />
</video>
<figcaption>Different toon mid colors</figcaption>
</figure>

#### Toon Mid Wrap
The _Toon Mid Wrap_ defines the area of effect for the toon mid region.
<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/toon-mid-wrap.mp4" type="video/mp4" />
</video>
<figcaption>Toon mid wrap (0.6...0...1)</figcaption>
</figure>

:::note
You can use the _Toon Mid Wrap_ attribute to reduce toon shading to only two regions instead of three.
:::

#### Toon Mid Blur
The _Toon Mid Blur_ defines the softness between the mid and light toon regions.
<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/toon-mid-blur.mp4" type="video/mp4" />
</video>
<figcaption>Toon mid blur (0...1)</figcaption>
</figure>

#### Toon Light Color
The _Toon Light Color_ defines the color of the light toon region.
<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/toon-light-color.mp4" type="video/mp4" />
</video>
<figcaption>Different toon light colors</figcaption>
</figure>

#### Toon Smooth Lighting
The _Toon Smooth Lighting_ smoothly interpolates toon lighting of various light sources
<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/toon-smooth-lighting.mp4" type="video/mp4" />
</video>
<figcaption>Toon smooth lighting (0.005...1)</figcaption>
</figure>

---

### Animated
The _Animated_ setting bakes the current position of vertices so that effects that rely on the 3D positions can stay in place when objects are deformed/animated. If this setting is not enabled, features like _NoiseFX_ or _FeatureNoise_ would float around in 3D space and not move with the objects.

<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/not-deformed.mp4" type="video/mp4" />
</video>
<figcaption>NoiseFX without the Animated setting.</figcaption>
</figure>

<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/deformed.mp4" type="video/mp4" />
</video>
<figcaption>NoiseFX with the Animated setting.</figcaption>
</figure>

---

### Proxy

<span class="new-label">New in Flair 1.2</span>
The _Proxy_ setting changes the behavior of the flairShader material to become a proxy. When toggled, the objects assigned to the material become invisible and most of the available attributes in the Attribute Editor change. This is the normal behavior, as proxy materials do not render color, but effect controls. This means that any 3D mesh can become an art-direction tool!

As this is a behavioral change and a powerful art-direction tool, you can read more about it in the dedicated [proxy material page](/maya/materials/proxy-material).

<figure class="aio-ui">
<img src="/media/maya/materials/proxy-AE.png" alt="Flair proxy material node" />
<figcaption>The proxy attributes in the Attribute Editor.</figcaption>
</figure>

---

### Lighting
This group contains all settings affecting lighting within the material.

#### Light Linking
The _Light Linking_ setting toggles the ability to link lights within the material. This will allow `Windows->Relationship Editors->Light Linking` to work within the viewport. Keep in mind that allowing this on all materials can impact performance depending on how many lights you have in the scene.

#### Light Map
The _Light Map_ setting activates the use of light maps within the material and toggles light map attributes in the Attribute Editor. 
<figure class="aio-ui">
<img src="/media/maya/materials/flair-shader/light-map-AE.png" alt="Light Map attributes" />
<figcaption>The Light Map section in the Attribute Editor.</figcaption>
</figure>

##### Light Map File
_Light maps_ are grayscale texture maps that add light to the material (white is light). These can be baked from offline renderers, painted with VertexFX or assigned procedurally through NoiseFX. Click on the checkerboard icon to select a texture.

##### Shade in Light Map
If this attribute is enabled, _Light Maps_ will add both light and shade to the object. White `1.0` will add light, neutral grey `0.5` won't add anything, black `0` will add shade to the object.

<div class="d-flex">

<figure>
<img src="/media/maya/materials/flair-shader/light-map-map.png" alt="Light map used in video"  style="height: 152px" />
<figcaption>Light Map supporting Shade in Light Map.</figcaption>
</figure>
<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/light-map.mp4" type="video/mp4" />
</video>
<figcaption>Light Map applied.</figcaption>
</figure>

</div>

---

#### Specularity
The _Specularity_ setting activates the use of [specular reflectance models](#specular-model) within the material and toggles the attributes in the Specularity section.

<figure class="aio-ui">
<img src="/media/maya/materials/flair-shader/blinn-AE.png" alt="Blinn specularity attributes" />
<figcaption>Blinn specularity attributes.</figcaption>
</figure>

##### Specular Model
The _specularModel_ setting defines the shading algorithm used by the _Flair Shader_ material for specularity (shininess). A shading algorithm dictates how light is reflected along the surface of the object.

<figure>
<div class="d-flex">

<img src="/media/maya/materials/flair-shader/blinn.png" alt="Blinn" style="height:152px" />
<img src="/media/maya/materials/flair-shader/anisotropic.png" alt="Anisotropic" style="height:152px" />

</div>
<figcaption>Available specular reflectance models: Blinn and Anisotropic.</figcaption>
</figure>

Depending on the specular model, different attributes will appear in the _Specularity_ section.
<figure class="aio-ui">
<img src="/media/maya/materials/flair-shader/anisotropic-AE.png" alt="Anisotropic specularity attributes" />
<figcaption>Anisotropic specularity attributes.</figcaption>
</figure>

##### Roll Offs
_Specular Roll Off_, _Horizontal Roll Off_ and _Vertical Roll Off_ define the size of the specular highlight.

<div class="d-flex">

<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/roll-off.mp4" type="video/mp4" />
</video>
<figcaption style="width:17em">Blinn: Roll Off (0...1.0).</figcaption>
</figure>
<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/h-roll-off.mp4" type="video/mp4" />
</video>
<figcaption style="width:17em">Anisotropic: Horizontal Roll Off (0...0.5).</figcaption>
</figure>
<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/v-roll-off.mp4" type="video/mp4" />
</video>
<figcaption style="width:17em">Anisotropic: Vertical Roll Off (0...0.5).</figcaption>
</figure>

</div>

##### Specular Diffusion
_Specular Deffusion_ defines how diffuse or sharp a specular highlight is.

<figure>
<div class="d-flex">

<video autoplay loop muted playsinline style="height:152px;">
<source src="/media/maya/materials/flair-shader/blinn-diffusion.mp4" type="video/mp4" />
</video>
<video autoplay loop muted playsinline style="height:152px;">
<source src="/media/maya/materials/flair-shader/anisotropic-diffusion.mp4" type="video/mp4" />
</video>

</div>
<figcaption>Specular Diffusion (0...1.0).</figcaption>
</figure>

##### Specular Transparency
_Specular Transparency_ defines the transparency of the specular highlight.

<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/materials/flair-shader/specular-transparency.mp4" type="video/mp4" />
</video>
<figcaption>Specular Transparency (0...1.0).</figcaption>
</figure>

##### Specular Map
_Specular Maps_ are greyscale texture maps which mask the specularity within the material. Otherwise, the specularity will be even throughout the material.Click on the checkerboard icon to select a texture.

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/materials/flair-shader/specular-map.mp4" type="video/mp4" />
</video>
<figcaption>(1) without specularity; (2) with specularity; (3) with specularity and a Specular Map.</figcaption>
</figure>

:::note
**The specularity within the specular map is encoded within the intensity (white values) of the texture. White is specular, grey is semi-specular, black is diffuse.**
:::

---

#### Rim light
The _Rim Light_ settings activates the use of 3D rim lighting effect around the silhouette of objects on areas facing the light or opposite to it.

<figure class="aio-ui">
<img src="/media/maya/materials/flair-shader/rim-light-AE.png" alt="Rim light attributes in the Attribute Editor" />
<figcaption>Rim light attributes.</figcaption>
</figure>

##### Rim Light Intensity
_Rim Light_ controls the intensity of the rim light. Positive values adds the rim light, whereas negative values subtracts it.

<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/rim-light.mp4" type="video/mp4" />
</video>
<figcaption>Rim Light (-1,5...1,5).</figcaption>
</figure>

##### Rim Light Wrap
_Rim Light Wrap_ defines the area of effect of the rim light in either the lit or shaded areas of the object.

<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/rim-wrap.mp4" type="video/mp4" />
</video>
<figcaption>Rim Light Wrap (-1...1).</figcaption>
</figure>

##### Rim Light Color
Controls the color of the rim light. The color is additively blended on top of the underlaying shading.

<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/rim-color.mp4" type="video/mp4" />
</video>
<figcaption>Varying the hue of the rim light color.</figcaption>
</figure>

---

#### Highlight
The _Highlight_ setting activates the use of highlights to generate a sharp highlight with the [_Custom-Light Color_](#custom-light-color).
<figure class="aio-ui">
<img src="/media/maya/materials/flair-shader/highlight-AE.png" alt="Highlight attributes" />
<figcaption>The highlight attributes.</figcaption>
</figure>

##### Highlight Roll Off
_Highlight Roll Off_ defines the size of the highlight in the lit area of objects.

<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/highlight-roll-off.mp4" type="video/mp4" />
</video>
<figcaption>Highlight Roll Off with an orange Light Color (0...1.0)</figcaption>
</figure>

##### Highlight Diffusion
_Highlight Diffusion_ defines how diffuse (blurred) the highlight should be.

<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/highlight-diffusion.mp4" type="video/mp4" />
</video>
<figcaption>Highlight Diffusion (0...1.0)</figcaption>
</figure>

##### Highlight Transparency
_Highlight Transparency_ defines the transparency of the highlight.

<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/highlight-transparency.mp4" type="video/mp4" />
</video>
<figcaption>Highlight Transparency (0...1.0).</figcaption>
</figure>

---

#### Final Color
The _Final Color_ setting makes the albedo its final color. Objects assigned to a final color material are not affected by lighting or the _Atmosphere Color_ attribute that is set in the globals node. This allows you to use just the color, disregarding what is happening around them.

---
### Features
This group aggregates various features affecting the type of data that the material renders.

#### Transparent
The _Transparent_ setting activates the use of transparency and alpha masks in the material and toggles the attributes in the Attribute Editor.
<figure class="aio-ui">
<img src="/media/maya/materials/flair-shader/transparent-AE.png" alt="Transparency and alpha masking attributes" />
<figcaption>Transparency and alpha masking section in the Attribute Editor.</figcaption>
</figure>

##### Transparency Map
_Transparency Map_ is a greyscale texture which embeds the semi-transparency of the material. Click on the checkerboard icon to select a texture.

<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/transparency-map.mp4" type="video/mp4" />
</video>
<figcaption>Transparency Map, featuring semi-transparency.</figcaption>
</figure>

:::note
As with [_Alpha Masks_](#alpha-mask): white is opaque, grey values are semi-transparent, black is transparent. The darker the value of the _Transparency Map_, the more transparent the material will be.
:::

##### Transparency
_Transparency_ defines the overall semi-transparency of the material.
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/transparency.mp4" type="video/mp4" />
</video>
<figcaption>Transparency (0...1.0)</figcaption>
</figure>

##### Blend FX
_Blend FX_ defines if the control masks of effects (NoiseFX, VertexFX) should blend with transparency or not.

##### Blend AOVs
_Blend AOVs_ defines if AOVs (depth and normals) should blend with transparency or not. This attribute also shows the _AOV Blend_ attribute, which helps to blend AOVs further so that effects can look better on semi-transparent objects.

###### AOV Blend
_AOV Blend_, which only appears appears once _Blend AOVs_ is enabled, defines how much the AOVs should blend. A value of 0 will make the AOVs (depth and normals) of the material dissapear, while a value of 1 will blend AOVs as much as the color.

##### Alpha Mask
_Alpha Mask_ is a black and white image which embeds the alpha of the material. Alpha masks are binary and can only distinguish between opaque or fully transparent (white is opaque, black is transparent). Click on the checkerboard icon to select a texture.

:::note
Use the alpha masks if you want cast shadows to respect the transparency.
:::

##### Alpha Mask Cutoff
The grayscale value at which the [_Alpha Mask_](#alpha-mask) is transparent. Defines the threshold/boundary of the alpha mask in case there are grey values.
<figure>
<video autoplay loop muted playsinline style="width:200px">
<source src="/media/maya/materials/flair-shader/alpha-mask.mp4" type="video/mp4" />
</video>
<figcaption>Alpha Mask with Alpha Mask Cutoff (0.1...0.9).</figcaption>
</figure>

---

#### VertexFX
The _VertexFX_ setting toggles the control of effects through vertex colors. The attribute is automatically enabled by Flair and is toggled as soon as you start painting with the [_VertexFX_](/maya/art-direction/vertexfx/) tool.

---

#### Velocity
The _Velocity_ setting activates the calculation and rendering of motion vectors by the material. However, velocity will only be calculated if the [_VelocityPV_ global](/maya/getting-started/globals/#velocity-pv) is enabled. 

:::note
Velocity is enabled by default, but it can be deactivated per material if motion vectors are not required.
:::

---

#### Feature Noise
The _Feature Noise_ setting toggles the fractalized dynamic 3D noise that is used for certain sheder effects such as hatching, fray and sketch lines. Because it is dynamic, the feature noise will always be of the same pixel size, no matter how close or far the camera is from objects. When enabled, a new section within the Attribute Editor appears with attributes to customize the feature noise per material.

<figure class="aio-ui">
<img src="/media/maya/materials/flair-shader/feature_noise_offsets.png" alt="Feature noise offsets attributes" />
<figcaption>The base Feature Noise Offset attributes</figcaption>
</figure>

##### Noise Frequency
Offsets the Feature Noise frequency within the material.

##### Noise Phase
Offsets the Feature Noise phase within the material.

<figure>
<video autoplay loop muted playsinline style="width:450px">
<source src="/media/maya/materials/flair-shader/feature_noise_offsets.mp4" type="video/mp4" />
</video>
<figcaption>Left: Noise Frequency Offset - Right: Noise Phase Offset</figcaption>
</figure>

##### Noise Steps
Adds control over the noise _smoothsteps_ to change the appearance of feature noise by toggling two additional attributes underneath: `Noise Smoothstep Low` and `Noise Smoothstep High`.

<figure class="aio-ui">
<img src="/media/maya/materials/flair-shader/feature_noise_offsets_steps.png" alt="Feature noise offsets steps" />
<figcaption>Additional control over the feature noise appearance.</figcaption>
</figure>

:::note
To visualize the appearance of the feature noise in the viewport, use the _Pass Inspector_ (`PASS` in the _Flair_ shelf) and change the `Active Target` to _featureNoiseTarget_.
:::

---

#### NoiseFX
The _NoiseFX_ setting toggles the use of NoiseFX in the material and enables the NoiseFX section at the bottom of the Attribute Editor. _NoiseFX_ is generally toggled automatically when the [NoiseFX](/tools/noisefx/) tool is used and allows you to key and animate NoiseFX attributes when needed.

<figure class="aio-ui">
<img src="/media/maya/materials/noisefx.png" alt="NoiseFX attributes" />
<figcaption>The beginning of the NoiseFX attributes</figcaption>
</figure>

---

#### Offsets
The _Offsets_ setting toggles the available offsets per material and the respective section within the Attribute Editor. The effects of these attributes will only be visible on effects and styles that work with thresholds and depth i.e., lines (toon and sketch).

<figure class="aio-ui">
<img src="/media/maya/materials/offsets.png" alt="Offset attributes" />
<figcaption>The available Offset attributes</figcaption>
</figure>

##### Depth Threshold Offset
_Depth Threshold Offset_ modifies the global depth threshold for this material

##### Flow Threshold Offset
_Flow Threshold Offset_ modifies the global flow (normals) threshold for this material

##### Color Threshold Offset
_Color Threshold Offset_ modifies the global color threshold for this material

##### Depth Bias
_Depth Bias_ offsets the depth of objects assigned to the material to help fix potential depth-based artifacts with overlapping geometries.

---

### Geometry
This group contains all attributes changing the geometry of the material.

#### Displacement
The _Displacement_ setting activates the use of displacement within the material and toggles the attributes in the _Attribute Editor_.

<figure class="aio-ui">
<img src="/media/maya/materials/flair-shader/displacement-AE.png" alt="Displacement section" />
<figcaption>The Displacement section in the Attribute Editor.</figcaption>
</figure>

##### Displacement Map
_Displacement Map_ is a greyscale texture which embeds the displacement in the form of a heightmap. Click on the checkerboard icon to select a texture.

##### Displacement Multiplier
_Displacement Multiplier_ defines the amount of displacement to use. The higher the value, the more displacement there will be.

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/materials/flair-shader/displacement-multiplier.mp4" type="video/mp4" />
</video>
<figcaption>Displacement Multiplier (0...0.5).</figcaption>
</figure>

##### Displacement Offset
_Displacement Offset_ offsets the displacement inward, so that displacement can be inside and outside of the object.

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/materials/flair-shader/displacement-offset.mp4" type="video/mp4" />
</video>
<figcaption>Displacement Offset (0...1.0).</figcaption>
</figure>

##### Tessellation Factor
_Tessellation Factor_ defines the amount of subdivision within each polygon. The higher the factor, the more polygons are subdivided, giving more points to displace. There is no magic number, so you will need to find out how much tessellation is enough for your displacement purposes depending on the topology of each model.  

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/materials/flair-shader/tessellation-factor.mp4" type="video/mp4" />
</video>
<figcaption>Displacement with different Tesselation Factors (1.0...10.0).</figcaption>
</figure>

---

#### Wobble
The _Wobble_ setting activates the use of wobble offsets within the material and toggles its attributes in the _Attribute Editor_. These material attributes offset the global wobble values set in the [globals node](/maya/getting-started/globals/#geometry-wobble), so make sure to enable and set the wobble effect globally first.

Different types of wobble noise can be specified for different results

* **None** - No wobble is applied
* **Simple** - Default simplex wobble noise
* **Cloud** - More detailed fractalized wobble noise resembling the "cloud" noise in Photoshop (better appreciated at a higher polygon count).
* **Custom** - Custom noise, which can be written in glsl `flair/maya/shaders/material/include/noise.glsl` [`customNoise3(vec4 v)`].

<figure class="aio-ui">
<img src="/media/maya/materials/wobble-ae.png" alt="Wobble offsets section" />
<figcaption>The Wobble Offsets section in the Attribute Editor.</figcaption>
</figure>

:::note
Once the wobble attribute has been enabled globally, material presets will default as wobbled (Simple).
:::

##### Wobble Frequency
Offsets the regularity of the wobble. A higher frequency will make the wobble more "irregular", whereas a lower frequency will make it more "regular". The frequency is directly linked to the global [World Scale](/maya/getting-started/globals/#world-scale).

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/wobble-frequency.mp4" type="video/mp4" />
</video>
<figcaption>Wobble Frequency (0...5).</figcaption>
</figure>

##### Wobble Amplitude
Defines the amount of wobble. A higher amplitude will deform more than a lower amplitude. The amplitude is directly linked to the global [World Scale](/maya/getting-started/globals/#world-scale).

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/wobble-amplitude.mp4" type="video/mp4" />
</video>
<figcaption>Wobble Amplitude (0...2.5).</figcaption>
</figure>

##### Wobble Phase
Defines the form of the wobble. Useful when you want a different wobble deformation or want to vary the wobble on a frame-by-frame basis.

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/wobble-phase.mp4" type="video/mp4" />
</video>
<figcaption>Wobble Phase (0...3).</figcaption>
</figure>

:::note
As wobble is generated from noise in 3D, make sure to toggle the *deformed* attribute in materials if they are animated/deformed so that the wobble is baked in place.
:::

##### Wobble Blur
Defines the amount of wobble blur for TAA samples, generating a soft edge by averaging different wobble positions as layers.

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/wobble-jitter.mp4" type="video/mp4" />
</video>
<figcaption>Wobble Blur (0...1).</figcaption>
</figure>

##### Wobble Blur Layers
Defines the amount of wobble blur layers i.e., the amount of wobbled positions to use during the wobble blur.

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/materials/wobble-layers.mp4" type="video/mp4" />
</video>
<figcaption>Wobble Blur Layers (32...1).</figcaption>
</figure>

:::note
With a low layer amount, you can use Wobble Blur to achieve a layered watercolor look!
:::

##### Wobble Motion
Defines the amount of motion offset of the wobble, generating streaks of motion under animation. For this attribute to show its effect, make sure that velocity is enabled in the _Globals_ node and in the material.

<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/wobble-motion.mp4" type="video/mp4" />
</video>
<figcaption>Wobble motion at 0.5 and 2.5.</figcaption>
</figure>

---

#### Flip Back Faces
The _Flip Back Faces_ setting flips the normals of faces that are pointing away from the camera view. This is useful to obtain better results from single polygon objects like tree leaves.

---

#### Culling
The _Culling_ setting defines which faces should be culled within the material.

* **None** - No culling, all objects with the material are rendered as double sided.
* **Front** - The front-facing faces are going to be culled, only rendering the back faces.
* **Back** - The back-facing faces are going to be culled, only rendering front-faces. This can help performance on objects with many polygons.

------------------
------------------

## Advanced

### Modifying the shader source code
You may edit the source code of the material should you need to. The GLSL source files can be found in the Flair directory under `/maya/shader/material`. Please reach out on [Discord](https://discord.gg/6FJZCscQUM) to guide you further and learn what was missing for you. Maybe we can also help implement things for you.
