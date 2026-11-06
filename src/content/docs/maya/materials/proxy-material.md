---
title: "Proxy material"
sidebar:
  order: 3
---
Proxy materials are invisible materials that only render effect control maps within Flair, thereby not rendering any color but only modifying effects on the final image, instead.

Any mesh assigned to a proxy material becomes an art-direction tool to stylize elements in the scene. This makes them extremely versatile as they can change effects at all levels of control. For example, they can affect the entire image by being placed in front of the camera as a proxy card, or affect only a specific part of the scene in 3D space by being placed in front of it. The tutorial below showcases this versatility.

<figure class="video-embed">
<iframe src="https://www.youtube.com/embed/A_gdVg4K7Uc" title="Video" allowfullscreen loading="lazy"></iframe>
</figure>

Any flairShader material can become a proxy material by toggling the [proxy setting](/maya/materials/flair-shader/#proxy), but proxies can also easily be created or assigned from the [material presets tool](/maya/materials/presets/#special-presets) using the _proxy_ preset.

As flairShader materials, proxies are divided into optional _Proxy Settings_ and _Proxy_ attributes. The proxy attributes are always present no matter what settings are enabled, so let's introduce them first.

<figure class="aio-ui">
<img src="/media/maya/materials/proxy-AE.png" alt="Flair proxy material node" />
<figcaption>The proxy attributes in the Attribute Editor.</figcaption>
</figure>

---

## Proxy
Proxies show few parameters by default, as effect control is achieved mostly through the [_VertexFX_](/maya/art-direction/vertexfx) and [_NoiseFX_](/tools/noisefx/) tools being applied onto the material.

### Color Tint
_Color Tint_ darkens pixels with a specified color. This attribute is especially useful for materials like tinted windows.

<div>

<figure>
<video autoplay loop muted playsinline style="height:150px">
<source src="/media/maya/materials/proxy-material/color-tint.mp4" type="video/mp4" />
</video>
<figcaption>Color Tint with a light red color.</figcaption>
</figure>

</div>

### Feathering
_Feathering_ softens the hard edges of the proxy materials. This effect works as a fresnel, so it shows best when the material is applied to round objects.

<div>

<figure>
<video autoplay loop muted playsinline style="height:150px">
<source src="/media/maya/materials/proxy-material/feathering.mp4" type="video/mp4" />
</video>
<figcaption>Feathering the Color Tint (0...3.0).</figcaption>
</figure>

</div>

:::note
When proxies clip with other objects, a hard edge might be visible due to the compenetration of meshes.  Use the [Wobble Blur](/maya/materials/proxy-material/#wobble-blur) effect to achieve a smoother transition and feathering when compenetration becomes an issue.
:::

### Cookie Mask
_Cookie Mask_ specifies an image containing a mask of the proxy. It is especially useful if you place a proxy plane (card) in front of the camera to create effect vignettes.

<figure>
<video autoplay loop muted playsinline style="width:150px">
<source src="/media/maya/materials/proxy-material/cookie-mask.mp4" type="video/mp4" />
</video>
<figcaption>Cookie mask applied on a proxy material.</figcaption>
</figure>

### Invert Cookie
_Invert Cookie_ inverts the applied _Cookie Mask_ values.

<figure>
<video autoplay loop muted playsinline style="width:150px">
<source src="/media/maya/materials/proxy-material/cookie-invert.mp4" type="video/mp4" />
</video>
<figcaption>Cookie mask inverted on a proxy material.</figcaption>
</figure>

---

## Proxy Settings

The first section provides the **Proxy Settings** that allow to customize what optional features the proxy material should have.

### Animated
The _Animated_ setting bakes the current position of vertices so that effects that rely on the 3D positions can stay in place when proxies are deformed/animated. If this setting is not enabled, features like _NoiseFX_ or _Wobble_ would float around in 3D space and not move with the proxies.

---

### Proxy
The _Proxy_ setting enables the proxy material behavior. When disabled, the proxy material will become a normal [flairShader material](/maya/materials/flair-shader/).

---

### VertexFX
The _VertexFX_ setting toggles the control of effects through vertex colors. The attribute is automatically enabled by Flair and is toggled as soon as you start painting with the [_VertexFX_](/maya/art-direction/vertexfx/) tool.

---

### NoiseFX
The _NoiseFX_ setting toggles the use of NoiseFX in the material and enables the NoiseFX section at the bottom of the Attribute Editor. _NoiseFX_ is generally toggled automatically when the [NoiseFX](/tools/noisefx/) tool is used and allows you to key and animate NoiseFX attributes when needed.

<figure class="aio-ui">
<img src="/media/maya/materials/noisefx.png" alt="NoiseFX attributes" />
<figcaption>The beginning of the NoiseFX attributes</figcaption>
</figure>

---

### Offsets

<span class="new-label">New in Flair 1.2</span>
The _Offsets_ setting toggles the available offsets and the respective section within the Attribute Editor. The effects of these attributes will only be visible on effects and styles that work with thresholds and depth i.e., lines.

For example, with the right thresholding offsets, you can have only outlines (silhouette) appear behind a proxy plane, thereby changing how lines draw at a certain depth.

<figure class="aio-ui">
<img src="/media/maya/materials/offsets.png" alt="Offset attributes" />
<figcaption>The available Offset attributes</figcaption>
</figure>

#### Depth Threshold Offset
_Depth Threshold Offset_ modifies the global depth threshold on everything inside or behind the proxy material

#### Flow Threshold Offset
_Flow Threshold Offset_ modifies the global flow (normals) threshold on everything inside or behind the proxy material

#### Color Threshold Offset
_Color Threshold Offset_ modifies the global color threshold on everything inside or behind the proxy material

#### Depth Bias
_Depth Bias_ offsets the depth of the proxy material to help fix potential depth-based artifacts with overlapping geometries.

---

### Wobble

<span class="new-label">New in Flair 1.2</span>
The _Wobble_ setting activates the use of wobble offsets within the proxy and toggles its attributes in the _Attribute Editor_. These material attributes offset the global wobble values set in the [globals node](/maya/getting-started/globals/#geometry-wobble), so make sure to enable and set the wobble effect globally first.

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

It is difficult to clearly visualize the wobble on a proxy, so the examples below feature the normal flairShader material. However, the exact same deformation and diffusion applies to proxy materials, as well.

#### Wobble Frequency
Offsets the regularity of the wobble. A higher frequency will make the wobble more "irregular", whereas a lower frequency will make it more "regular". The frequency is directly linked to the global [World Scale](/maya/getting-started/globals/#world-scale).

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/wobble-frequency.mp4" type="video/mp4" />
</video>
<figcaption>Wobble Frequency (0...5) - Visualized in a normal flairShader material.</figcaption>
</figure>

#### Wobble Amplitude
Defines the amount of wobble. A higher amplitude will deform more than a lower amplitude. The amplitude is directly linked to the global [World Scale](/maya/getting-started/globals/#world-scale).

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/wobble-amplitude.mp4" type="video/mp4" />
</video>
<figcaption>Wobble Amplitude (0...2.5) - Visualized in a normal flairShader material.</figcaption>
</figure>

#### Wobble Phase
Defines the form of the wobble. Useful when you want a different wobble deformation or want to vary the wobble on a frame-by-frame basis.

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/wobble-phase.mp4" type="video/mp4" />
</video>
<figcaption>Wobble Phase (0...3) - Visualized in a normal flairShader material.</figcaption>
</figure>

:::note
As wobble is generated from noise in 3D, make sure to toggle the *deformed* attribute in materials if they are animated/deformed so that the wobble is baked in place.
:::

#### Wobble Blur
Defines the amount of wobble blur for TAA samples, generating a soft edge by averaging different wobble positions as layers.

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/wobble-jitter.mp4" type="video/mp4" />
</video>
<figcaption>Wobble Blur (0...1) - Visualized in a normal flairShader material.</figcaption>
</figure>

#### Wobble Blur Layers
Defines the amount of wobble blur layers i.e., the amount of wobbled positions to use during the wobble blur.

<figure>
<video autoplay loop muted playsinline style="width:152px">
<source src="/media/maya/materials/wobble-layers.mp4" type="video/mp4" />
</video>
<figcaption>Wobble Blur Layers (32...1) - Visualized in a normal flairShader material.</figcaption>
</figure>

:::note
With a low layer amount, you can use Wobble Blur to achieve a layered watercolor look!
:::

#### Wobble Motion
Defines the amount of motion offset of the wobble, generating streaks of motion under animation. For this attribute to show its effect, make sure that velocity is enabled in the _Globals_ node and in the material.

<figure>
<video autoplay loop muted playsinline style="height:152px">
<source src="/media/maya/wobble-motion.mp4" type="video/mp4" />
</video>
<figcaption>Wobble motion at 0.5 and 2.5 - Visualized in a normal flairShader material.</figcaption>
</figure>

---

### Culling
The _Culling_ setting defines which faces should be culled within the proxy.

* **None** - No culling, all objects with the material are rendered as double sided.
* **Front** - The front-facing faces are going to be culled, only rendering the back faces.
* **Back** - The back-facing faces are going to be culled, only rendering front-faces. This can help performance on objects with many polygons.
