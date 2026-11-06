---
title: Seamless Textures
sidebar:
  order: 7
---

Texture parameters within a Flair Effect Layer have the ability to become seamless through stochastic sampling over gaussianized versions thereof. This is used to create seamless canvases within Flair, but can be extrapolated to other uses, as well.

## Setup

To setup support for seamless textures, both the Flair Effect Layer and the PPMs reading them need to be configured accordingly.

### On the Flair Effect Layer

Fetch or create a texture parameter and enable `Seamless`.

![A seamless texture parameter](/media/unreal/technical-artist-guide/effect-layers/seamless-textures/seamless-parameter.png)

This will preprocess the texture to create a gaussianized version thereof and its look-up-table (LUT). These new textures are stored under `/Flair/Cache/Canvases` as follows:

- `<SourceName>_Processed` — gaussianized version
- `<SourceName>_InvLUT` — inverse LUT

To avoid confusion from artists, you can set the `Texture Picker Path` to show only the original textures and not the processed ones. This keeps the cache's hidden.

### On the Post-Process Materials

The material needs to read from the new textures instead of the original ones too. Please refer to `Flair_Canvas_Synthesis` to generate the seamless gaussianized version of the texture and `Flair_Canvas_Restore` to restore the seamless texture to its original un-gaussianized values.

Both of these materials can be found under `/Flair/Materials/Canvas`.

In `Flair_Canvas_Synthesis` you will notice an unconnected Canvas Texture node, this node is only meant to fetch the parameter within the Flair Effect Layer. For the actual synthesis, we read from `_CanvasTexture_Processed` instead (note the `_` prefix that declares it "private").

In `Flair_Canvas_Restore` we read from the synthetized UST and from the `_CanvasTexture_InvLUT` to restore the histogram of the original canvas texture.

We are entering PPM authoring territory now, and while this guide is not meant to teach how to use the UE material editor, it is meant to facilitate working with Flair, so let's [create a Flair PPM](/unreal/technical-artist-guide/ppms/create/).
