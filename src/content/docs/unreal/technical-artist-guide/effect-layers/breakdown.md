---
title: Breaking down the Flair Effect Layer
sidebar:
  label: Breakdown
  order: 2
---

Flair Effect Layers are quite powerful as they contain much more than just a collection of Post-Process Materials (PPMs), they contain everything to make and control an effect. Make sure to [create a Flair Effect Layer](/unreal/technical-artist-guide/effect-layers/create/) to follow along.

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/breakdown/empty-layer.png" alt="An empty Flair Effect Layer" />
<figcaption>An empty Flair Effect Layer with all its properties.</figcaption>
</figure>

When opening a Flair Effect Layer asset, the details panel will show up with all relevant effect data.

## Effect Name

The "nice" or "ui" descriptive name of the effect layer

## Iterative Effect

If the effect layer should show the iterative options. Iterative effect layers contain PPMs that iterate over themselves (ping-pong rendering), allowing to compute PPMs in a loop. This is an advanced concept documented in [Iterative Effect Layers](/unreal/technical-artist-guide/effect-layers/iterative/).

## Prerequisites

Everything that must be computed _before_ this effect layer runs is grouped here — the render passes it needs, and any other effect layers it depends on.

### Render Passes

References the Blueprint subclasses of `FlairRenderPass` that should be rendered to produce or control the effect. You can define your own [Custom Render Passes](/unreal/technical-artist-guide/effect-layers/render-passes/) to be rendered with Flair

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/breakdown/render-passes.png" alt="Render pass prerequisites of an effect layer" />
<figcaption>This effect layer needs the Flair_EdgeCtrlPass to art-direct the edge.</figcaption>
</figure>

### Effect Layers

References other effect layers that must be computed before this one. Use this when an effect only makes sense once another has already run e.g., a layer that reads data an earlier layer produces.

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/breakdown/prerequisites.png" alt="Effect layer prerequisites" />
<figcaption>This effect layer needs the Flair_Beauty effect layer to run as a prerequisite</figcaption>
</figure>

When you add this layer to a FlairStyle, Flair automatically inserts any listed prerequisite layers that aren't already above it. This works transitively: if a prerequisite has its own prerequisites, those get inserted too, all the way down.

A few things to keep in mind:

- **Only inserts, never reorders.** Flair adds missing prerequisites directly above the layer you just added; it never moves or removes layers you've already placed, so you stay in control of the final stack order.
- **Position matters.** A prerequisite already sitting _above_ the added layer counts as satisfied. If it only exists _below_ (or not at all), a fresh copy is inserted above as a later layer may need its own copy computed first.
- **Cycles are handled safely.** If two layers depend on each other (directly or through a chain), Flair skips the looping insertion and shows a warning in the viewport naming the layer involved.
- **Editor-only convenience.** Prerequisites resolve as you build styles in the editor. At runtime (PIE, packaged games) the already-resolved layer stack is used as-is.

## Post-Process Materials (PPMs)

References the PPMs that are used to generate the effect. You can add as many as needed, but pay close attention to the order of operations.

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/breakdown/ppms.png" alt="Post-process materials of an effect layer" />
<figcaption>All the PPMs for the line dilation effect layer. The arrows around the <code>Flair_Line_Dilation</code> effect layer represent an iterative material.</figcaption>
</figure>

PPMs are represented with different icons depending on what type of PPM materials they are.

<div class="d-flex">
<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/breakdown/ppm-icon.png" alt="PPM icon" width="128" />
<figcaption>A normal PPM material</figcaption>
</figure>
<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/ppm-iterative-icon.png" alt="Iterative PPM icon" width="128" />
<figcaption>An iterative PPM material</figcaption>
</figure>
</div>

## Material Parameter Collections (MPCs)

References the MPCs that are needed for the effect. The MPCs' scalar and vector parameters are name-matched and pushed to surface materials during parameter updates. This links the FlairStyle parameter system to surface materials e.g., 3D noise frequency/phase for NoiseFX.

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/breakdown/mpcs.png" alt="Material parameter collections of an effect layer" />
<figcaption>The <code>Flair_Line_Sketch</code> effect uses the <code>Flair_Feature_Noise</code> MPC to control the dynamic fractalized noise within surface materials that is needed to offset the sketch lines.</figcaption>
</figure>

## Fetch Parameters

The `Fetch Parameters` button auto-discovers all available parameters within referenced PPMs and MPCs so that they can be defined and exposed within the FlairStyle.

![The Fetch Parameters button](/media/unreal/technical-artist-guide/effect-layers/breakdown/fetch-parameters.png)

This button does a lot and comes quite in handy to avoid defining each effect parameter individually.

1. Scans all materials for scalar, vector, texture, and static switch parameters
2. Scans all MPCs for scalar and vector parameters
3. Adds new parameters as **unexposed** with defaults pulled from the source
4. **Skips** the iteration parameter and private parameters (parameter names starting with `_`)
5. **Auto-detects Enum type** when a scalar parameter has an enum control type set on the material
6. **Auto-detects Color type** for vector parameters with color/tint/hue-related names
7. Updates `SourceName` on all parameters (visible as tooltip on hover in the collapsed row)
8. Refreshes orphan status on all parameters

## Parameters

The list of managed parameters within this layer with defaults, types, metadata and exposure settings. We cover all options in [Effect Layer Parameters](/unreal/technical-artist-guide/effect-layers/parameters/).

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/breakdown/parameters.png" alt="Parameters of an effect layer" />
<figcaption>The parameters managed by the <code>Flair_Line_Dilation</code> effect layer.</figcaption>
</figure>

## Control Definitions

The list of definitions within this layer with its control name, target, channel and metadata to populate art-direction tools such as NoiseFX. We cover all options in [Control Definitions](/unreal/technical-artist-guide/effect-layers/control-definitions/).

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/breakdown/control-definitions.png" alt="Control definitions of an effect layer" />
<figcaption>The control definitions from the <code>Flair_Line_Dilation</code> effect layer.</figcaption>
</figure>

All these properties can be defined within an effect layer to generate and fully control an effect. With this foundation, let's dive deeper into the most used property [Effect Layer Parameters](/unreal/technical-artist-guide/effect-layers/parameters/).
