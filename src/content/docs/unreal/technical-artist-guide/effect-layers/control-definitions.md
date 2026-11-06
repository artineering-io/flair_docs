---
title: Control Definitions
sidebar:
  order: 4
---

Control definitions configure the art direction controls available to [NoiseFX](/tools/noisefx/) and future tools. They are authored on Flair Effect Layers and gathered by the Flair Style to populate the Python art-direction tools.

## Creating a Control Definition

Control Definitions are created manually within a Flair Effect Layer by adding array elements.

![Adding a control definition array element](/media/unreal/technical-artist-guide/effect-layers/control-definitions/add-control-definition.png)

Once a Control Definition has been added, it's properties appear to customize the control.

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/control-definitions/empty-control-definition.png" alt="An empty control definition" />
<figcaption>An empty control definition</figcaption>
</figure>

When collapsed, array elements present their Effect name, Target and Channel they affect.

## Properties

Each element in the `Control Definitions` array represents a `FFlairControlDefinition` with multiple properties defining the control for an effect.

- **Effect:** Effect control label within a style used as the display name in art-direction tools and as the deduplication key across layers
- **Description:** Description shown in art-direction tools (may also be used as a tooltip)
- **Target:** Control target this control will affect e.g., Pigment, Distortion, Edge, Abstract
- **Channel:** R, G, or B within the control target (alpha is reserved for blending)
- **Only Positive:** Whether only positive values are allowed (vs. bidirectional).
- **Increase/Decrease Labels**: Labels to use when increasing or decreasing the effect
- **Noise Label:** Label used for the noise option (e.g., "Turbulence")
- **UI Order:** Sort order in art-direction tools (lower values appear first). Use gaps (e.g., 0, 10, 20) to allow future insertions without renumbering.

## Control Schema

In total, there are currently 4 control targets, each with 3 control channels = **12 max control slots** per style. These control targets have been semantically named to allow some degree of cross-stylization when adhered to the following schema:

| Target | R | G | B |
| --- | --- | --- | --- |
| **Pigment Control** | Pigmentation | Application | Density |
| **Distortion Control** | Distortion | Orientation | Shape |
| **Edge Control** | Edge | Width | Transition |
| **Abstraction Control** | Abstraction | Detail | Blending |

This schema is used by NoiseFX parameters on surface materials to assign an intention to otherwise abstract controls i.e., `{Param}{Attr}NFX`:

- `{Param}`: control parameter name (e.g., `pigmentation`)
- `{Attr}`: NoiseFX attribute: `Scale`, `Intensity`, `Phase`, `Shift`, `Type`
- `NFX`: literal suffix

Example: `PigmentationScaleNFX`, `ApplicationIntensityNFX`, `DensityTypeNFX`

The `{Param}NFX` static switch enables/disables the noise for that control on the material.

## Cross-Layer Deduplication

When multiple layers define a control with the same `Effect` (case-sensitive `FString` comparison), the first layer in the stack wins. The FlairStyle gathers from all enabled layers, deduplicates, and returns the list sorted by `UIOrder`.

The control definitions are directly affecting control targets, which are rendered by [Custom Render Passes](/unreal/technical-artist-guide/effect-layers/render-passes/).
