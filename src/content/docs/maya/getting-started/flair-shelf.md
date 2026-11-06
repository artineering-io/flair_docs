---
title: "Flair Shelf"
sidebar:
  order: 1
---
<figure class="">
<img src="/media/maya/getting-started/flair-shelf/flair-shelf.png" alt="Flair shelf" />
<figcaption>The Flair shelf with its three segments: Art-direction, Lighting/Inspection and Rendering.</figcaption>
</figure>

The _Flair shelf_ contains all tools required to work with Flair, separated into three segments:
1. [Art-direction](#art-direction)
2. [Lighting/Inspection](#lightinginspection)
3. [Rendering](#rendering)

While most users will find themselves working with the first segment, it's important to understand what the remaining two segments are for. 

:::note
Don't like working with shelves? The last shelf tool will popup the shelf into its own window.
:::
## Art-direction
The art-direction tools can be found in the left side of the shelf, ordered from highest to lowest level of control.
1. **FLAIR** - opens the browser with the [Flair documentation](/).  
`Double click` shows the "What's New" splash window.
1. **STYLE** - opens the _Style Presets_ to load/save styles and their parameters [[docs](/tools/style-presets/)].
1. **GLOB** - selects the global node to change style attributes [[docs](/maya/getting-started/globals/)].
1. **PRES** - opens the _Material Presets_ to load/save predefined Flair materials and their parameters [[docs](/maya/materials/presets)].  
1. **MAT** - selects the materials of currently selected objects or components.  
`Double click` shows the material tab within the _Attribute Editor_,  without changing the current selection. If the material was already shown, it will refresh the UI fixing any potential issues.  
`Right click -> Only show material in AE` will have the same functionality as double clicking on the `mat` shelf icon.  
`Right click -> Select objects assigned to selected material` will select all objects that share the selected material.
1. **BULK** - opens the _Bulk Attribute_ tool. An attribute editor that lets you modify multiple Flair materials at once (in bulk) [[docs](/maya/art-direction/bulkattr)].
1. **NFX** - opens the _NoiseFX_ tool that lets you control effects procedurally on Flair materials [[docs](/tools/noisefx/)].
1. **VFX** - opens the _VertexFX_ window that lets you paint each effect directly onto your 3D models [[docs](/maya/art-direction/vertexfx)].

## Lighting/Inspection
The lighting and inspecting tools allow to easily create the supported lights within Flair and to troubleshoot if things are not looking quite right.
1. **Supported lights** - shelf icons for the four different supported lights: ambient, directional, point (no shadow maps) and spot light.
1. **PASS** - opens the _Inspector_, which lets you toggle on/off each style pass and troubleshoot the inner workings of the style itself.
1. **TEST** - creates our favourite sphere with default lighting.

## Rendering
1. **TBOX** - opens the _Flair Toolbox_, containing useful functions to work with Flair in production [[docs](/maya/toolbox/)].
1. **FLOAT** - opens a floating viewport with a 1280 x 720 resolution, or a resolution defined in the `FLAIR_FV_CUSTOM_RES` environment variable e.g., `FLAIR_FV_CUSTOM_RES=1280x720`.  
`Right click -> Float viewport 1024 x 540` opens a floating viewport with a 1024 x 540 resolution.  
`Right click -> Float viewport 1080 x 1080` opens a floating viewport with a 1080 x 1080 square resolution.  
`Right click -> Float viewport 1920 x 1080` opens a floating viewport with a 1920 x 1080 resolution (Full HD).  
`Right click -> Float viewport 2048 x 1152` opens a floating viewport with a 2048 x 1152 resolution (2K).  
`Right click -> Custom float viewport` opens a floating viewport with a custom resolution set through a small dialog.
1. **RENDR** - opens the _Viewport Renderer_, which quickly allows to save screenshots or playblasts [[docs](/maya/rendering/viewport/)].
1. **SEQ** - opens the _Flair Renderer_, which allows to render sequences and all different AOVs for production [[docs](/maya/rendering/sequence/)].
1. **IM/EX** - opens the _Import/Export_ tool to import or export _.style_ files [[docs](/maya/styles/import-export)]  
`Right click -> Custom auto-import` function found in: `flair_import_export.auto_import_style()`.  
`Right click -> Custom import` function found in: `flair_import_export.custom_import()`.  
Custom import functions can be overriden depending on the project's pipeline.
1. **SUPP.** - opens the browser straight to [support at the Artineering page](https://artineering.io/support).

## Popup shelf
Opens a popup shelf so that you can always access the Flair tools while using other shelves.
<figure class="aio-ui aio-window">
<img src="/media/maya/getting-started/flair-shelf/flair-popup-shelf.png" alt="Flair popup shelf" />
<figcaption>The popup shelf with all Flair tools.</figcaption>
</figure>
