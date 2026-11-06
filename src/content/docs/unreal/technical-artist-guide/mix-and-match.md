---
title: Mix-and-Match Flair Effect Layers
sidebar:
  label: Mix-and-Match
  order: 2
---

Within a FlairStyle actor you have the Parameters and the Effect Layers thereof (see [Create a Flair Style Actor](/unreal/artist-guide/create-style-actor/) and [Breaking down the Flair Style Actor](/unreal/artist-guide/style-actor/) from the artist's guide).

The effect layers define the FlairStyle actor and compose the style, so they are the building blocks of any Flair style. In its simplest form, each effect layer contains post-process materials that produce an effect. Many effects together render a style.

To begin your style authoring journey, make sure to load the `_base` preset and start adding layers onto it.

1. Select your FlairStyle actor
2. In the **Details panel**, find **Flair→Effect Layers**
3. Click **+** to add an element

   ![Adding an effect layer to a FlairStyle actor](/media/unreal/technical-artist-guide/add-layer.png)

4. Pick an existing `FlairEffectLayer` asset from the dropdown, for example:
   1. Flair_Beauty
   2. Flair_Line_Detection
   3. Flair_Line_Dilation

By adding these three effect layers, Flair has spawned two custom scene textures `Flair_Ctrl_Edge` and `Flair_Offset_Threshold` and all the post-process materials defined by these layers, as it can be seen in the _User Scene Texture Debug_ display.

![The User Scene Texture Debug display](/media/unreal/technical-artist-guide/mix-and-match/ust-debug.png)

:::tip
You can toggle the User Scene Texture Debug display with the following CVAR: `r.PostProcessing.UserSceneTextureDebug`. The default is to show the trace when there are errors or unused inputs.
:::

In this particular example, we have cached the beauty, computed the line detection and line dilation, but we are still not drawing the line. Let's add the last effect layer: `Flair_Line_Drawing`.

Now you should see _lines_ in the viewport and the _User Scene Texture Debug_ display should have disappeared. New parameters have also appeared to control the effects. And just like that, by adding these four layers, you can add lines, line parameters and controls to any Flair style!

:::tip
You could have added `Flair_Line_Drawing` directly and Flair would have inserted all other effect layers automagically, as they have been defined as prerequisites.
:::

We could of course combine all effect layer operations into one. However, keeping them separate makes it possible to reuse them within the same style or use `Flair_Line_Dilation` with your own Line detection algorithm.

Feel free to add other effect layers like `Flair_AO`, `Flair_Canvas` + `Flair_Canvas_Shading`, etc.

Keep in mind that the order of effect layers matters as effects are computed from top to bottom. You can reorder each layer by dragging them on the left side, and the right arrow can help to _Insert_, _Delete_, or _Duplicate_ an Effect Layer.

![Reordering effect layers](/media/unreal/technical-artist-guide/mix-and-match/reorder.png)

You just created your own lines style! You can use all of the existing Flair effect layers to compose a style, but you can go beyond when you [create a Flair Effect Layer](/unreal/technical-artist-guide/effect-layers/create/) yourself.
