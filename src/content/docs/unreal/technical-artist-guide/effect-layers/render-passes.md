---
title: Custom Render Passes
sidebar:
  label: Render Passes
  order: 5
---

Custom Render passes provide additional scene data beyond the default UE render. They are implemented as **Blueprint subclasses** of `FlairRenderPass` (a custom `ASceneCapture2D`).

- Render passes are defined as **Blueprint subclasses** of `FlairRenderPass`
- They are **auto-spawned** by the FlairStyle when referenced by an effect layer
- For bounded volumes, passes **activate/deactivate** automatically based on camera position
- Spawned passes appear in the **Scene Outliner** for inspection (camera frustum is hidden)

In summary, render passes are Blueprint assets that are automatically managed by the FlairStyle actor when referenced.

## Referencing a Render Pass within a Flair Effect Layer

To reference a render pass, open the Flair Effect Layer that requires it and, go to the Render Passes array and add an element to it.

![Adding a render pass element to an effect layer](/media/unreal/technical-artist-guide/effect-layers/render-passes/add-element.png)

Once you add an element, select your control or custom render pass.

![Selecting a render pass](/media/unreal/technical-artist-guide/effect-layers/render-passes/select-pass.png)

Once referenced, the FlairStyle actor will manage the render passes:

- **Auto-spawned** when the effect layer is enabled → no manual placement needed
  - Spawned passes are **transient** and not saved with the level
  - Spawned passes are **attached** to the FlairStyle actor, listed in the Outliner for inspection
- **Merged by Render Pass index** → one capture is spawned per index, whether that is the same pass referenced by two layers or two variants of the same pass
- **Activated/deactivated** automatically on bounded FlairStyles with zero overhead
- **Activated/deactivated** when the FlairStyle actor is hidden.

## CustomPass1 and CustomPass2

We have prepared two custom passes that you can use at any point, without having to create your own Render Pass from scratch. These have already been setup and can be referenced directly in the Flair Effect Layer.

To specify what they render, just modify the _Flair_CustomRenderPass_ material functions available in `/Flair/Materials/_Functions`

![The Flair_CustomRenderPass material functions](/media/unreal/technical-artist-guide/effect-layers/render-passes/custom-pass-functions.png)

These functions render to User Scene Textures called _Flair_CustomPass1_ and _Flair_CustomPass2_ respectively. These can in turn be read directly by your own PPMs.

## Creating a Render Pass from Scratch

If you do not want to use the ready-made custom render passes, you can create your own.

1. Create a **Blueprint subclass** of `FlairRenderPass`
2. Configure the FlairRenderPass Blueprint with:
   - **Flair → Render Pass:** the index of the render pass. Materials branch on `ViewProperty: Post Process Volume User Flags` within the material to render different data per pass. Index 1 is reserved, indices 2 to 5 are taken by the control passes (Pigment, Distortion, Edge and Abstraction), and variants share the index of the pass they vary. The custom render passes use index 6 and 7. You can either reuse these or use higher indexes i.e., 8, 9… up to 15. Indices must stay below 16.
   - **Pass Info → UST Base Color / UST Normal / UST Scene Color:** which User Scene Texture each output writes to. Only fill in the ones that will be read and leave the rest empty.
   - Scene Capture → `Primitive Render Mode` or `Use ShowOnly List` depending on your needs
3. Reference the Blueprint class in the effect layer's **Render Passes** array as [explained before](#referencing-a-render-pass-within-a-flair-effect-layer).

While the render pass asset has been setup, we need to configure the surface materials to render data onto the User Scene Texture too. This can be done by modifying the main `Flair_RenderPasses` material function found in `/Flair/Materials/_Functions`.

When opened, locate the _Flair_Switch_ node and add an input element. The index number must correlate with your FlairRenderPass Blueprint's Render Pass index for things to work.

:::tip
When a pass writes a **UST Base Color**, materials see its index plus 16 (e.g. 19 instead of 3). `Flair_RenderPasses` removes the extra 16 with an _Fmod_ before the _Flair_Switch_, so you connect your pass at its normal index. If you read `Post Process Volume User Flags` in your own materials, add the same _Fmod_ by 16.
:::

<div class="d-flex">
<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/render-passes/flair-switch.png" alt="The Flair_Switch node within Flair_RenderPasses" />
<figcaption>The Flair_Switch node within Flair_RenderPasses</figcaption>
</figure>
<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/render-passes/flair-switch-add.png" alt="Adding a new pass to the Flair_Switch node" />
<figcaption>Adding a new pass to the Flair_Switch node</figcaption>
</figure>
</div>

The new input will appear on the Flair Switch and you can proceed to connect whatever needs to be rendered in your new Render Pass.

:::caution
We'd still recommend using the `Flair_CustomPass` material functions instead as the Flair_RenderPasses function might change with future updates.
:::

Every input of the _Flair_Switch_ is computed in every view, including the main render: material Switch and If nodes calculate all their inputs and only pick one at the end. If your pass needs expensive work, put it in a _Custom_ node that returns early outside your pass:

```hlsl
// Only compute this in render pass 8
[branch] if ((View.PostVolumeUserFlags % 16) != 8) {
    return 0.0;
}
// expensive work here
```

While additional render passes are quite fast to render, if performance is of outmost importance, feel free to butcher the `Flair_Switch` to have as little render passes as needed. However, be aware that you might have to rewire/recreate your changes to the `FlairRenderPasses` material function after a Flair update.

## Adding Post-Process Materials to a Render Pass

A render pass can also carry its own post-process materials. Any material listed in the render pass Blueprint's **Post Process Materials** array is automatically inserted at the **front** of the FlairStyle's post-process stack, before every effect layer material.

This is useful for _composite_ or _decode_ passes: a material that reads the data your pass rendered into its User Scene Texture and resolves it before the effect layers consume it.

To use it:

1. Open your `FlairRenderPass` Blueprint and go to **Class Defaults**.
2. Find **Flair → Post Process Materials** and add your composite/decode material(s).
3. Reference the pass in an effect layer's Render Passes array as usual.

:::caution
Set these in the Blueprint's **Class Defaults**, not on a pass instance you drag into a level for debugging. Flair reads the materials from the class defaults, so per-instance values are ignored by design.
:::

Like the passes themselves, these materials are **deduplicated by material asset**, so the same material listed by two different passes is only added once. They follow the render pass declaration order.

## Pass Variants

A render pass can write up to three User Scene Textures, but most effect layers only read one of them. If a texture is written and never read, Unreal shows a yellow _Unused Output_ warning and turns the post-process debug overlay on.

To avoid this, create a **variant** of your pass that only writes the textures that are needed.

1. Right-click your render pass Blueprint → **Duplicate**, so the variant starts with the same **Render Pass** index and settings
2. In **Class Defaults**, clear the **Pass Info** UST names that are not needed
3. Remove any **Post Process Materials** that read the textures you cleared
4. Leave the **Render Pass** index untouched and change nothing else
5. Reference the variant in the effect layers that only need those outputs

Passes sharing a Render Pass index are merged into a single capture that writes whichever textures the referenced variants ask for. Referencing only the lean variant renders one texture, referencing both renders both, always from one capture.

:::caution
Variants sharing an index can only differ in their UST names and Post Process Materials. If you need different Scene Capture settings, such as a ShowOnly list or a different `Primitive Render Mode`, use a different Render Pass index instead.
:::

If two variants of the same index write different texture names to the same slot, the first one is used and a warning names both passes.

### Checking your work

Set `r.PostProcessing.UserSceneTextureDebug 1` in the console to always show the overlay, and set it back to `2` once you are done.

- Yellow **Unused Output**: a texture is written but nothing reads it. Clear its name from the variant.
- Red **Missing Input**: a texture is read but nothing writes it. Either reference a variant that writes it, or you cleared a name but kept the material that reads it.

Now that you know how to create your own render passes, let's learn how to do [Iterative Effect Layers](/unreal/technical-artist-guide/effect-layers/iterative/)!
