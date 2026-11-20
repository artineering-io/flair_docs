---
title: Getting Started with Flair for Unreal
sidebar:
  label: Getting Started
  order: 1
---

:::caution
Make sure you have properly [installed Flair for Unreal Engine](/unreal/installation/).
:::

## First-Time Setup

When you first interact with Flair (e.g., editing a FlairStyle actor), you'll be asked to accept the **End User License Agreement (EULA)**. This is a one-time step and your acceptance is remembered across sessions.

## The Flair Shelf

The most commonly used Flair tools can be found in the Flair shelf, which can be opened by clicking on `Main Menu→Tools→Flair`.

<figure>
<img src="/media/unreal/artist-guide/getting-started/flair-shelf.png" alt="The Flair shelf, docked in the editor" />
<figcaption>We recommend docking the Flair shelf here (or anywhere else you might prefer)</figcaption>
</figure>

There are 5 buttons currently in the shelf

1. **`DOCS`** - Opens up the browser with this documentation
2. **`STYLE`** - Opens up the Style Presets window
3. **`PARAM`** - Selects the most relevant Flair Style actor to show it's parameters.<br />Prioritizes the currently selected style, then the unbound style with the most effect layers, then the closest to the viewport camera. If no FlairStyle exists in the level, one is auto-created.
4. **`MAT`** - Opens the material editor window with the materials assigned on the selected actor
5. **`NFX`** - Opens the NoiseFX window

:::tip
Double clicking on each button will "reset" the window it opens.
:::

:::note
More shelf buttons will appear as we develop new tools and features.
:::

## Add support for Render Passes

Effects and their art direction need custom render passes rendered from the materials in your level. Each **Master Material** needs a **Flair Slab** for that: a material function in front of the material's outputs that renders the right data for each Flair render pass.

### Insert Flair Slabs automatically

The first time you place a Flair Style in a project, Flair offers to insert the slabs for you. Click **Yes** and pick the folder with your master materials. Flair only asks once per project, and you can do it any time from the right-click menus:

- **Content Browser → right-click a folder → Flair → Insert Flair Slabs** for every master material in the folder and its subfolders, after you confirm.
- **Content Browser → right-click a master material → Flair → Insert Flair Slabs**
- **Viewport or Outliner → right-click actors → Flair → Insert Flair Slabs** for the master materials of the selected actors.

Flair picks the right slab for each material and wires it in. It skips materials that already have one, Flair's own materials, and materials that can't take one, such as post-process materials. The Output Log lists what was inserted and skipped.

Fab materials (under `/Fab/`) are skipped too: Fab content can't reference Flair, so the slab couldn't be saved. To stylize them, duplicate the Fab master into your project and point its material instances to the copy.

A progress dialog shows each material as it's processed. In each material, the slab takes the place of the node it feeds, and that node moves to the right to make room.

:::caution
The materials are left modified but unsaved, and the insertion can't be undone with Ctrl+Z. Save them once you're happy with the result.
:::

**Remove Flair Slabs**, in the same menus, takes them out again and restores your original connections. Slabs don't change the look without a Flair Style, but they cost some performance, so remove them if you stop using Flair in a project.

You might need to add the slab by hand if:

- The Output Log says _Front Material isn't driven directly by a Substrate Slab_, for example because it goes through a reroute or a blend.
- An actor's right-click menu has no **Flair** entry, because its materials aren't on a mesh or decal.

### Add a Flair Slab by hand

Open your Master Material and add the **Flair Slab** material function in front of the _Substrate Slab_. Not all inputs need to be connected, but **all outputs of the slab need to be connected** onto the material for Flair to work properly.

<figure>
<img src="/media/unreal/artist-guide/getting-started/flair-slab.png" alt="Flair Slab in front of the Substrate Slab" />
<figcaption>The Flair Slab will automatically know what to render depending on the current Flair render pass.</figcaption>
</figure>

There are nine different Flair slabs to choose from, separated by how Unreal Engine renders them.

- **Opaque** - For opaque master materials without blending (Opaque, Masked)
- **Translucent** - For translucent master materials (TranslucentGreyTransmittance, Additive, etc), and for opaque ones that use **Opacity** with a lit shading model other than Default Lit, such as Single Layer Water.
- **Decals** - For decal materials (see [Decal materials](#decal-materials) below)

<figure>
<img src="/media/unreal/artist-guide/getting-started/slab-options.png" alt="Flair Slab options in the Material Editor" />
<figcaption>Flair Slab options in the Material Editor.</figcaption>
</figure>

The **`Flair Slab Opaque`** and **`Flair Slab Translucent`** are the nodes to use with _Substrate Materials_.

If you are still using the Legacy material system, use the respective `(Legacy)` variants.

<figure>
<img src="/media/unreal/artist-guide/getting-started/slab-translucent-legacy.png" alt="Translucent Flair slab on a legacy material" />
<figcaption>Connecting a translucent Flair slab onto a legacy material.<br />Note that some inputs are input, but all outputs are still connected.</figcaption>
</figure>

<figure>
<img src="/media/unreal/artist-guide/getting-started/slab-opaque-legacy.png" alt="Opaque Flair slab on a legacy material" />
<figcaption>Connecting an opaque Flair slab onto a legacy material using the MaterialAttributes pin.</figcaption>
</figure>

:::tip
Please refer to `MM_Flair`, `MM_Flair_Card`, `MM_Flair_Translucent` and their respective _Legacy_ variants to see how the Flair Slab material functions are connected.
:::

### Translucent materials

For Flair to stylize translucent materials, they need to render before depth of field:

- **Material → Translucency Pass:** _**Before DOF**_

If you leave it on the default _After DOF_, translucent objects draw on top of the Flair effects, for example over the canvas.

If your translucent material uses refraction (e.g. glass), also add these lines to your project's `Config/DefaultEngine.ini`, under `[/Script/Engine.RendererSettings]`:

```ini
r.Translucency.StandardSeparated=1
r.Mobile.Distortion.BeforeTranslucency=1
```

The first line fixes refraction on desktop, the second on mobile. Without them, you might see:

- A smaller, darker core inside the glass that changes with the glass color.
- The glass tint looking distorted along with the background behind it.

:::tip
The desktop setting has no effect when MSAA is enabled.
:::

### Decal materials

Decals use the **`Flair Slab Decals`** node, or **`Flair Slab Decals (Legacy)`** for the Legacy material system. The quickest start is `MM_Flair_Decal` or `MM_Flair_Decal_Legacy` in `/Flair/Materials/MasterMaterials`. To set up your own decal material:

- **Material → Material Domain:** _**Deferred Decal**_
- **Material → Blend Mode:** _**TranslucentGray**_

With Substrate, connect the slab's outputs to a _Substrate Slab_, then to **Substrate Convert To Decal**. Connect your opacity to the slab's **Coverage** input and to the **Coverage** of _Substrate Convert To Decal_. With the Legacy material system, connect the slab's outputs to the material and your opacity to both the slab's **Opacity** input and the material's **Opacity**.

The slab's **Normal** pin is optional. Only connect it if your decal has a normal map.

What to expect from decals:

- Decals affect Flair effects in **Unreal Engine 5.8** and later. In 5.7 they only show in the final image.
- Decals can only **increase** art direction. Pushing an effect up under a decal works; pushing it down has no effect.
- Under a decal, effect settings that come from the material, such as edge thresholds, use the decal's values instead of the surface's.

If a thick line appears where a decal ends on a character, the decal box is projecting onto the character's body:

- **Rendering → Receives Decals:** _**off**_ on the character, or
- **Decal → Decal Size:** reduce _X_ (the projection depth) so the box stays below the body.

:::tip
The `NFX` tool works on decals too: select the Decal Actor to art-direct its material.
:::

With Flair for Unreal Engine now set up and ready, it's time to learn the [Flair for Unreal Breakdown](/unreal/artist-guide/breakdown/).
