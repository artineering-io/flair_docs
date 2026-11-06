---
title: Create a Flair Style Actor
sidebar:
  order: 3
---

## Placing a FlairStyle Actor

1. Open the **Place Actors** panel
2. Search for **Flair Style**
3. Drag it into your level

A `FlairStyle` is a post-process volume designed for stylized rendering. By default, it is **bounded**, so its effects only apply when the camera is inside the volume. To apply the Flair style to the entire scene, enable **Infinite Extent (Unbound)** in the volume's settings.

A FlairStyle volume contains all the exposed parameters of a style, as well as the effect layers that compose it. All non-relevant post-process volume options are hidden so that you can concentrate on the style.

![The Details panel of a FlairStyle actor](/media/unreal/artist-guide/create-style-actor/details.png)

:::tip
If you do not have any FlairStyle actor in your level and click on the `PARAM` shelf icon, an _unbounded_ FlairStyle actor is automatically created, which works the same way as with Flair for Maya.
:::

Before diving into the Flair Style, let's learn how to quickly set them up [using Style Presets](/tools/style-presets/).

## Bounded vs. Unbound Volumes

| Mode | Behavior |
| --- | --- |
| **Unbound** | Affects the entire scene. Simplest setup recommended for most use cases. |
| **Bounded** | Affects only the area inside the volume. Supports **blend radius** for smooth transitions. |

When using bounded volumes:

- Render passes activate when the camera enters the volume (or its blend radius). Blend Radius fades the style in.
- Overlapping styles stack. Each renders its own layers, so a layer in two styles runs twice.
- `BlendWeight` is the master switch. At `0`, the style is off.

:::tip
Shared layers in overlapping volumes apply twice. Keep them in one style.
:::
