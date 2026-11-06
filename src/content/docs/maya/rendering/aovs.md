---
title: "Flair AOVs"
sidebar:
  order: 4
---
Flair uses a lot of AOVs internally to generate the different effects for each style. Most of these can also be rendered out using the [Flair Renderer](/maya/rendering/sequence/) or the [Standalone Renderer](/maya/rendering/standalone/).

What each one of these AOVs contains is documented below.

## General AOVs

### Cryptomatte
The `cryptomatte` AOV contains ID masks for different type of data.
* **Object** - A unique ID for each object
* **Material** - A unique ID for each material
* **Asset** - A unique ID for each asset (grouped objects)

:::caution
Currently only two ranks are supported per cryptomatte.
:::

### Albedo
The `albedo` AOV contains the raw color of objects. Keep in mind that painterly material attributes will render to the albedo, as well e.g., cangiante, custom light color.

### Lighting
The `lighting` AOV contains the current lighting.

### Specular
The `specular` AOV contains the current specular lighting.

### Shadows
The `shadows` AOV contains a shadow matte of cast shadows and their colors.
* **RGB** - Color of the cast shadow
* **A** - Opacity of the cast shadow

### Control Light
The `controlLight" AOV contains different types of data to control lighting in each channel.
* **R** - Final Color mask: materials with the `Final Color` attribute enabled will render this channel to 1.0
* **G** - Toon Matte: - `Toon Shaded` materials embed the three regions i.e., light, mid and shade in this channel. The values can be converted to an RGB matte if needed using the Nuke blinkscript available in the Flair downloads of commercial and Picasso/DaVinci licenses.
* **B** - Diffuse Gradient: renders out the entire diffuse gradient $$\vec{n}\cdot\vec{L}$$ (with positive and negative values)

### Normals and Depth
The `normalsDepth` AOV contains the tangent-space normals (flow) and depth in different channels.
* **R** - Tangent-space Normal in U direction
* **G** - Tangent-space Normal in V direction
* **B** - Depth in linear Maya units
* **A** - Z-buffer

:::note
Tangent-space normal is equivalent to a view-space normal without its Z direction. You can reconstruct the view-space normals as these were previously normalized.
:::

### Velocity and Noise
The `velocityNoise` AOV contains the velocity in projection-space and the material's `Feature Noise`.
* **R** - Velocity in U direction
* **G** - Velocity in V direction
* **BA** - Feature Noise (fractalized)

### World Position
The `worldPosition` AOV contains the position of each pixel in the virtual world.
* **R** - X position
* **G** - Y position
* **B** - Z position

### Abstract Control
The `abstractCtrlTarget` AOV contains the painted parameters to control different abstraction effects. 

### Pigment Control
The `pigmentCtrlTarget` AOV contains the painted parameters to control different color effects. 

### Edge Control
The `edgeCtrlTarget` AOV contains the painted parameters to control different edge effects.

### Canvas Control
The `canvasCtrlTarget` AOV contains the painted parameters to control different canvas/distortion effects.

### Canvas
The `canvasTarget` AOV contains the data from the Main Canvas.
* **R** - Normal in U direction
* **G** - Normal in V direction
* **B** - Heightmap

### Alternate Canvas
The `altCanvasTarget` AOV contains the data from the Alternate Canvas.
* **R** - Normal in U direction
* **G** - Normal in V direction
* **B** - Heightmap

### Ambient Occlusion
The `ambientOcclusion` AOV contains the ambient occlusion.

### Bloom
The `bloomTarget` AOV contains the bloom contribution.

### Output
The `outputTarget` is the AOV that you currently see in the viewport.

---

## Watercolor-specific AOVs

### Edges
The `edgeTarget` AOV contains the different edges being recognized.
* **R** - Lightness edge
* **G** - Chromacity edge
* **B** - Depth edge

### Edge Dilation
The `edgeDilTarget` AOV contains the dilated edges used for edge darkening.
* **R** - Dilated lightness edge
* **G** - Dilated chromacity edge
* **B** - Dilated depth edge

### Bleeding
The `bleedingTarget` AOV contains the bled pixels before they are applied to the style.

---

## Line-specific AOVs

### Toon Lines
The `toonLines` AOV contains only the toon lines.

### Sketch Lines
The `sketchLines` AOV contains only the sketch lines.

### Line AOVs
The `lineAOVs` contain the original positions of where the toon and sketch lines where extracted.
* **R** - U position of toon line
* **G** - V position of toon line
* **B** - packed _LocUV_ position of first sketch line
* **A** - packed _LocUV_ position of second sketch line

:::note
Nuke blinkscript to use this AOV and extract sketch lines from other renderers is available in the Flair downloads of commercial and Picasso/DaVinci licenses.
:::

---

## Fray-specific AOVs

### Edges
The `edgeTarget` AOV contains the dilated edges used for edge darkening and controlling where to apply the frayed effect.
* **R** - Dilated lightness edge
* **G** - Dilated chromacity edge
* **B** - Dilated depth edge

### Noise Iteration
The `noiseIterTarget` AOV contains the frayed noise and their offset.
* **RG** - Frayed `Feature Noise`
* **BA** - Offset of frayed pixel from its last position

### Control and Depth
The `ctrlsDepthTarget` AOV  contains the frayed control and depth.
* **RGB** - Frayed controls
* **A** - Frayed linear depth in Maya units

---

## Warp-specific AOVs

### Inflated Noise
The `inflatedNoiseTarget` AOV contains the inflated fractalized noise to warp the end result. 

:::note
Nuke blinkscript to warp passes from other renderers are available in the Flair downloads of commercial and Picasso/DaVinci licenses.
:::

### Edges
The `edgeTarget` AOV contains the different edges being recognized.
* **R** - Lightness edge
* **G** - Chromacity edge
* **B** - Depth edge

### Edge Dilation
The `edgeDilTarget` AOV contains the dilated edges used for edge darkening.
* **R** - Dilated lightness edge
* **G** - Dilated chromacity edge
* **B** - Dilated depth edge

---

## Cutout-specific AOVs

### Edges
The `edgeTarget` AOV contains the cutout edge being recognized.
