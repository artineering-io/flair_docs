---
title: "Viewport Renderer"
sidebar:
  order: 1
---
The _Viewport Renderer_ (`RENDR` icon in the [_Flair shelf_](/maya/getting-started/flair-shelf/))  is a simple tool to render individual images and playblasts, divided into two sections: _Frame Capture_ (save image) and _Quick Playblast_ (save video).

<figure class="aio-ui aio-window">
<img src="/media/maya/rendering/viewport/rendr.png" alt="Viewport Renderer" />
<figcaption>The Viewport Renderer captures frames and creates playblast.</figcaption>
</figure>

## Frame capture
The upper section of the _Viewport Renderer_ contains all options to capture a frame (image).

On the left side, you can define a custom resolution to render at. If left unchecked, the viewport resolution will be taken when rendering.

On the right side, you can find the settings to render with.
* **Quality** - Defines the quality of the viewport rendering, either standard or with _TAA_.
* **Alpha** - Defines how the alpha (transparency) is handled in the rendered frames. The options are _None_ (no alpha), _Linear_ (linear alpha) and _Premult._ (premultiplied alpha).
* **Format** - Defines the image file format to save the image as i.e., _.png, .jpg, .exr, .tif, .iff_.

:::note
Captured _.exr_ images will have the color space baked-in, as to facilitate its quick use for single images. Use the Flair Renderer if you do not want this behavior.
:::

The `Render` button will open a saving dialog to capture/render the frame in the directory you specify.

## Quick Playblast
The lower section of the _Viewport Renderer_ contains all options to create a quick playblast (video).

On the left side, you can define where to get the playblast resolution from. _From Viewport_ will get the viewport resolution to playblast with. _From Render Settings_ will get the [_Render Settings_](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=GUID-59DFB8B7-776B-4243-B404-A3D602FF8CFD) resolution to playblast with.  

On the right side, you can find the settings to playblast with.
* **R. scale** - Defines the render scale of the original vertical and horizotal resolutions to render with.  
The options range from 50% to 200%. Refer to the Globals [documentation](/maya/getting-started/globals/#render-scale) to learn about the impact this has on performance and memory footprint.  
* **Format** - Defines the video file format to save the playblast as i.e., _.avi, .mov (qt)_. The video file format will depend on what codecs your computer currently supports.

:::note
To use _TAA_, you'll have to render an image sequence with the [_Flair Renderer_](/maya/rendering/sequence/) and create the video yourself.
:::

The `Playblast` button will playblast the video in the directory you specify.
