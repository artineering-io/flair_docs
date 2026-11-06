---
title: Iterative Effect Layers
sidebar:
  label: Iterative Layers
  order: 6
---

Iterative effect layers allow to dynamically loop Post-Process Materials as needed to render effects. However, they need to be setup accordingly for them to work as intended.

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/iterative/iterative-layer.png" alt="An iterative effect layer" />
<figcaption>A new iterative effect that has been defined.</figcaption>
</figure>

By setting a Flair Effect Layer as an `Iterative Effect`, new options will appear and post-process materials gain additional properties for ping-pong rendering.

## Iteration Parameter Name

The first option allows to specify an iteration parameter name. This parameter can be used within the PPMs to pass the iteration index along to the MIDs. The index starts at `0`.

## Iterative Context

Once a Flair Effect Layer has been defined as iterative, the `Iterative Context` option appears under each PPM. When enabled, the PPM participates in the iteration and new options appear underneath.

![Iterative context options of a PPM](/media/unreal/technical-artist-guide/effect-layers/iterative/iterative-context.png)

### Iterative Material Properties

- **Iterative Context:** Whether this material participates or knows about current iterations
- **Final Pass:** marks a material as the final pass of an iterative sequence. The final pass still contains the iterative context (i.e., iteration count for normalization), but the context is reset afterwards.
- **Iterations:** number of iterations (ping-pong passes) to perform. A value of `0` skips the material while still advancing the iteration state.
- **Iterations Parameter Link:** links the iteration count of the material to a scalar parameter to dynamically change the amount of iterations without touching the layer's PPMs. If that parameter uses a **Variant**, enter its full variant name (`Name` + `Variant`, e.g. `IterationsEdge`) and not the base name. A parameter used as an iteration link is intentionally **excluded from Sequencer keying** as animating it would force a full rebuild whenever the count changes. Therefore it won't appear in the parameter track picker (see [Animating in Sequencer](/unreal/artist-guide/sequencer/)).

:::note
A _Final Pass_ is always required to read from the correct iteration output and reset the iteration context for future iterative PPMs.
:::

If a material has iterations, the PPM icon will change accordingly to reflect that.

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/ppm-iterative-icon.png" alt="Iterative PPM icon" width="128" />
<figcaption>An iterative PPM material</figcaption>
</figure>

It might be redundant, but keep the iterations as low as possible so that you maximize performance.

## Material Setup

Materials supporting an iterative context require additional setup.

Iteration is performed via ping pong rendering on User Scene Textures (USTs). This means that when one pass renders to UST-A, the next pass renders to UST-B as PPMs can't read and write to the same UST. The next pass would naturally render again to UST-A, then to UST-B, UST-A, UST-B and so forth.

Therefore, materials within an iterative context need two material instances in the **same folder** as the base material with their corresponding suffix:

- `IterativeMaterialName_A` → reads from UST_B, writes to UST_A
- `IterativeMaterialName_B` → reads from UST_A, writes to UST_B

Only the material without suffix needs to be referenced, as Flair will automatically alternate between A and B on each iteration to read and write from the correct UST.

The same must be done for Materials assigned as a final pass so that they read from A or B based on which UST contains the latest data, then reset the iteration index to 0 ending the iterative sequence.

For reference, take a look how Flair_Line_Dilation is setup within `/Flair/Materials/Lines`.

The last undocumented bit of the Flair Effect Layer are the support for [Seamless Textures](/unreal/technical-artist-guide/effect-layers/seamless-textures/), so let's get to it to have everything covered.
