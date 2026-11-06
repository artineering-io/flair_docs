---
title: Breaking down the Flair Style Actor
sidebar:
  label: Flair Style Actor
  order: 4
---

The FlairStyle actor allows to control the entire style it represents. It is the main building block of Flair for Unreal Engine and the one in charge of compositing and rendering all the effects according to the set parameters. Make sure to [create a Flair Style Actor](/unreal/artist-guide/create-style-actor/) to follow along.

When selecting a FlairStyle actor either using the `PARAM` shelf button or normally through the viewport/outliner, the details panel will show two important sections under the _Flair_ category.

- Parameters
- Effect Layers

As an artist, you will mainly work with the _Parameters_. However, it is important to know that the parameters available have been exposed by the _Effect Layers_ within the style.

<figure>
<img src="/media/unreal/artist-guide/style-actor/flair-category.png" alt="The Flair category in the Details panel of a FlairStyle actor" />
<figcaption>The Details panel of a FlairStyle actor. Clicking on <code>Style</code> will open the <a href="/tools/style-presets/">style presets</a>.</figcaption>
</figure>

## Parameters

The parameters section is available in the FlairStyle actor _Details_ panel. It contains all **exposed parameters** for the style organized into groups (1).

Each parameter has:

- A **name** and **tooltip** upon hovering (2)
- A **slider or input** appropriate to its type (number, color, texture) (3)
- A **reset button** that appears when the value differs from the default (4)

![Parameters of a FlairStyle actor](/media/unreal/artist-guide/style-actor/parameters.png)

Feel free to change the parameters within your style to your liking!

FlairStyle Parameters are Blueprintable. You just need to reference them through their internal names, which can be read from the parameter tooltip.

:::tip
Slider parameters often support values beyond the initial slider range, so do not hesitate to try out values outside of their default range.
:::

:::tip
Same parameter in two layers? The topmost wins.
:::

Exposed parameters can also be **animated over time** in Unreal's Sequencer, which you can learn more at [Animating in Sequencer](/unreal/artist-guide/sequencer/).

### Parameter Types

| Type | Control | Description |
| --- | --- | --- |
| **Scalar** | Slider + number input | Single float value (e.g., blur intensity, edge width) |
| **Vector** | Multi-channel spinboxes | 2, 3, or 4 component values with custom labels |
| **Color** | Color picker swatch | RGBA color with live viewport preview |
| **Texture** | Asset picker | Texture reference (e.g., canvas texture) |
| **Enum** | Dropdown combobox | Selection from a `UUserDefinedEnum` asset. |

:::tip
Static switches aren't shown here. Style authors set them on the effect layer.
:::

## Effect Layers

Effect layers are the building blocks of your look. Each layer is a reusable **data asset** containing one or more post-process materials representing an effect and their parameters.

1. Select your FlairStyle actor
2. In the **Details panel**, find **Flair→Effect Layers**
3. Click **+** to add an element

   ![Adding an effect layer element](/media/unreal/artist-guide/style-actor/add-layer.png)

4. Pick an existing `FlairEffectLayer` asset from the dropdown
   1. If the layer needs other layers, Flair adds them above it automatically.
5. Use the **checkbox** to enable/disable individual layers

Layers are computed **top to bottom**, so the order matters. Drag to reorder.

Edit an effect layer and every style using it updates immediately.

:::tip
Multiple FlairStyle actors can reference the same effect layer, enabling reuse.
:::

For the most part, you won't need to touch the Effect Layers once they have been configured by the style authors. But you can learn more about them in the [Technical Artist Guide](/unreal/technical-artist-guide/).

Now that you know how to modify style parameters, how do we art-direct them? Let's introduce [NoiseFX](/tools/noisefx/).
