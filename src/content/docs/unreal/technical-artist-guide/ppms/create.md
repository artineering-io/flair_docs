---
title: Create a Flair PPM
sidebar:
  label: Create
  order: 1
---

Flair uses normal Unreal Engine materials for Post-Processing. This is intended as Flair for UE is meant to run in every platform that UE supports. While the UE materials are incredibly powerful, they do contain some caveats for pure post-processing purposes that will be explained below.

## Creating a Flair Post-Process Material

If you just wish to skip ahead and create a UE material preconfigured for post-processing purposes, you can create a Flair Post-Process Material asset from the _Content Browser._

Flair assets are created from the **Content Browser** via the dedicated **Flair** submenu:

1. Right-click in the Content Browser (or click the **+ Add** button)
2. Find the **Flair** category in the menu
3. Choose Flair Post-Process Material

   ![Creating a Flair Post-Process Material](/media/unreal/technical-artist-guide/ppms/create/create-menu.png)

This option duplicates a preconfigured material (`/Flair/Materials/PPM_FlairBase`) to use as a starting point when authoring new Post-Process Materials.

Within this material, you only need to configure the output User Scene Texture: `Post-Process Material → User Scene Texture` as needed.

### Manual Flair PPM configuration

If you wish to setup the material yourself instead of using the `Content Browser → Flair → Flair Post-Process Material` submenu, create a normal UE material and configure the following:

- **Material → Material Domain:** Post Process
- **Material → Advanced → Allow Negative Emissive Color:** True
- **Post-Process Material → Blendable Location:** Scene Color Before DoF
- **Post-Process Material → Is Blendable:** False
- **Post-Process Material → Output Alpha:** True
- **Post-Process Material → Disable Pre Exposure Scale:** True

Once a Flair PPM has been created and configured, it can simply be added to the Post-Process Materials array within a Flair Effect Layer.

<figure>
<img src="/media/unreal/technical-artist-guide/ppms/create/add-to-layer.png" alt="Adding a PPM onto a Flair Effect Layer" />
<figcaption>Adding a PPM onto a Flair Effect Layer</figcaption>
</figure>

Now that you've setup the PPM, let's dive into [Authoring Flair PPMs](/unreal/technical-artist-guide/ppms/authoring/).
