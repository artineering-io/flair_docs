---
title: Create a Flair Effect Layer
sidebar:
  label: Create
  order: 1
---

Flair Effect Layers are the building blocks of a Flair style, and are derived from a `UDataAsset`. As such, they are reusable assets that only contain data defining the effect layer, which get's interpreted by all FlairStyle actors referencing it.

Flair offers a growing library of effect layers, which can be found in `/Flair/Effects`. You can create your effect layers wherever they are needed in your project structure.

The Flair Effect Layer is created directly from the **Content Browser** via the dedicated **Flair** submenu:

1. Right-click in the Content Browser (or click the **+ Add** button)
2. Find the **Flair** category in the menu
3. Choose Flair Effect Layer

   ![The Flair submenu of the Content Browser](/media/unreal/technical-artist-guide/effect-layers/create/create-menu.png)

This creates a new `UFlairEffectLayer` data asset within the folder, containing everything required by a post-processing effect to work.

Once saved, the Flair Effect Layer can be added to any FlairStyle.

<figure>
<img src="/media/unreal/technical-artist-guide/add-layer.png" alt="Adding an effect layer to an empty Flair Style" />
<figcaption>Adding an effect layer to an empty Flair Style.</figcaption>
</figure>

To configure the newly created data asset, let's begin [Breaking down the Flair Effect Layer](/unreal/technical-artist-guide/effect-layers/breakdown/).
