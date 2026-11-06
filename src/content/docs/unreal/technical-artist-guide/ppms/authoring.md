---
title: Authoring Flair PPMs
sidebar:
  label: Authoring
  order: 2
---

Since we are working within Unreal Engine, there are certain behaviors that we need to consider to avoid headaches and head/pixel scratching while troubleshooting.

## PPM outputs

By default, PPMs render into the scene texture, but you can specify your own User Scene Texture (UST) by setting it within the details panel of the material:

- **Post-Process Material → User Scene Texture:** _YourUserSceneTextureName_

You can also specify a lower resolution by specifying **Post-Process Material → User Texture Divisor** and **Post-Process Material → Resolution Relative to Input**. A value of `2` would be half the resolution of the given _Input_.

### Output format

A properly configured Flair PPM will allow to render onto 4 channels (RGBA). However, the alpha channel is clamped between 0…1 by UE (even in PPMs).

- RGB [-inf...inf]
- A [0...1]

It is important to note that User Scene Textures (USTs) defaults to 16bit, which can limit the precision of data that you store in them. You can force 32-bit precision by setting the CVAR `r.SceneColorFormat 5`, but that is meant for testing only as per official UE docs.

## Is Blendable

Post-process materials are blendable by default in UE, which means two post-process volumes using the same material **merge into one pass** instead of running it twice. That is never what you want in Flair.

- **Post-Process Material → Is Blendable:** _false_

`PPM_FlairBase` already has it disabled, so materials created through the Flair PP material factory are fine. Check it on anything created another way.

If you leave it on, an effect layer used by two overlapping styles silently stops working:

- The layer contributes nothing as you enter a bound volume that also uses it
- Its values look overwritten by the other style's
- Disabling the layer in one style makes the other work again

Materials that output to a User Scene Texture are not affected, so usually only one layer in a style misbehaves — which makes it look like a Flair bug rather than a material setting.

:::caution
If an effect layer's PPMs silently fail to apply when two styles overlap, check **Is Blendable** first.
:::

## Naming Conventions

- Use **PascalCase** for all parameter names (e.g., `BleedIntensity`, `EdgeWidth`, `CanvasColor`).
- Prefix private parameters with `_` to exclude them from Flair parameter management e.g., `_InternalThreshold`.
- If two materials need different values for the same concept, use distinct names (e.g., `EdgeBlurIntensity` vs `FillBlurIntensity`). Unless you do want the same value for them.
- Iterative PPM instances use `_A` and `_B` suffixes, placed in the same folder as the base material. See [Iterative Effect Layers](/unreal/technical-artist-guide/effect-layers/iterative/) to learn more.

## Tips and Tricks

### Node-based vs custom node

Whenever possible, Epic Games recommends to use the node-graph as to keep compatibility with all platforms and future versions of the engine. Additionally, this lets their node-graph optimize all possible shader permutations. However, not all operations can be achieved through nodes and require the use of custom-nodes:

- **loops:** when iterating over neighboring pixels
- **matrices:** when doing matrix operations
- **precision:** when precision matters (noise), the material node-graph optimizations can sometimes cause precision artifacts that can be avoided using custom nodes.

### _ScreenPosition_ (ViewportUV) instead of _TextureCoordinate_

When wiring UVs into scene texture nodes like `SceneDepth`, `CustomDepth`, `SceneColor`, `WorldNormal`, etc., always use the `ScreenPosition` node set to **ViewportUV** instead of `TextureCoordinate`.

- `TextureCoordinate` outputs raw mesh UVs mapped `[0, 1]` across the **entire render target buffer**. It has no awareness of the active viewport region.
- `ScreenPosition` → **ViewportUV** outputs UVs remapped to the **actual rendered viewport rect**, accounting for `View.ViewRectMin` and `View.ViewSizeAndInvSize`.
- When the camera constrains the aspect ratio (e.g., `bConstrainAspectRatio = true` on a CineCamera), the viewport is a sub-region of the full buffer. `TextureCoordinate` will sample incorrect positions (offset into the black bar area), while `ScreenPosition` (ViewportUV) will correctly map to the active region.
- The same issue applies to split-screen, editor viewports, and VR eyes — any scenario where the viewport doesn't fill the entire render target.

:::caution
`TextureCoordinate` only works by coincidence when the viewport fills the entire render target. Always prefer `ScreenPosition` (ViewportUV) in post-process materials.
:::

### _ScreenResolution_ (Visible Resolution)

The actual resolution that you see might be different than the internal GBuffers that UE uses, hence it is important to work with the right values.

_ScreenResolution_ is the node that provides the Visible Resolution plug that even respects "Constrain Aspect Ratio" within cameras. In UE HLSL equivalent: `View.ViewSizeAndInvSize.xy`

### Visualize User Scene Textures (USTs)

You can use the `Flair_Inspector` effect layer and its material to troubleshoot USTs.

However, Unreal Engine also offers the handy but undocumented `vis` command to do so directly.

```txt
vis UST.YourUST  // Where "YourUST" is the name of your User Scene Texture.
```

By default, the vis command runs as PiP (Picture in Picture), other methods include

- `uv0` - anchored top-left
- `uv1` - full texture stretched across the screen
- `uv2` - 1:1 with no scaling centered on screen

You can also isolate channels by using the respective channel names `r`, `g`, `b`, `a` and even use multipliers `*8` or `/2`. By default the visualizer also runs `frac()` on values so they wrap anything above 1.0. To `saturate()` instead, you can append `sat` to the command.

A proper command would then be

```txt
vis UST.Flair_ThresholdOffset uv2 sat
```

To disable the visualization, just type `vis 0`.

To learn more, the only official documentation about the command is available through `vis help`.

### Best practices for working with custom nodes

- Always use `SceneTextureFetch` instead of `SceneTextureLookup` to get a pixel value to automatically support mobile platforms.

  ```hlsl
  float4 SceneTextureFetch(int SceneTextureIndex, float2 PixelOffset)
  ```
