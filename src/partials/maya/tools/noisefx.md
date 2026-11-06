The _NoiseFX_ tool simplifies the [procedural control of effects](#showcase) on selected Flair materials. The tool is opened by clicking on the `NFX` shelf icon and shares the same window with the [_VertexFX_](/maya/art-direction/vertexfx/) tool.

<figure class="float-right aio-ui aio-window">
<img src="/media/tools/noisefx/ui-noisefx.png" alt="NoiseFX tool window" />
<figcaption>NoiseFX of the watercolor style.</figcaption>
</figure>

Each Flair material (including proxies) supports NoiseFX, but the effects driven by NoiseFX depend on the loaded style. To apply NoiseFX, select an object with a Flair material and modify the desired slider.

From top to bottom, these are the different elements of the NoiseFX tool.

<figure class="float-left">
<img src="/media/tools/noisefx/viewPassive.png" alt="View NoiseFX"  style="max-height: 32px" />
</figure>

On the top-left, you will find an eye button which toggles the parameter view. This will allow you to view the control parameters that you are currently affecting through the _NoiseFX Widgets_.

<figure class="float-left">
<img src="/media/tools/noisefx/reset.png" alt="Reset button"  style="max-height: 32px" />
</figure>

On the top-right, you will find the reset button, which resets ALL NoiseFX of either, the selected objects, or ALL objects in the scene when no selection is active. A prompt will ask for confirmation, listing the objects that will have their NoiseFX removed.

Next to the reset button is the `Bake 3D` button. This button toggles the `Animated` setting in the assigned Flair materials, baking the current 3D position of objects. Baking is useful to attach the current NoiseFX patterns to an animated/deformed object. If the 3D position is not baked, NoiseFX will "float" in 3D space, instead of moving with animated objects.

## Noise widgets
Each style has different effects, therefore, the noise widgets (sections) will vary depending on the currently loaded style. Each widget handles a specific effect/behaviour within the style e.g., _Lighting_, _Pigment turbulence_, _Color bleeding_.

On the left side of each widget, you will always find a generalized term for the behaviour of each effect. Right next to it, there will be a sphere icon that gives a preview of what the effect will do.

### Toggle/reset
To the right of the preview icon, you will find two buttons.

<figure class="float-left">
<img src="/media/tools/noisefx/reset.png" alt="Reset NoiseFX"  style="max-height: 32px" />
</figure>

This button resets the NoiseFX values for that effect, allowing to start anew or completely remove its influence. This button is smaller than the reset _ALL_ NoiseFX button at the top-right of the window.

<figure class="float-left">
<img src="/media/tools/noisefx/io.png" alt="NoiseFX toggle"  style="max-height: 32px" />
</figure>

This button toggles the NoiseFX on/off to visualize the influence that the noise makes for the style.

### NoiseFX type
Directly underneath the preview icon, there is a combo box widget that gives the ability to change between different noise types.

* **None** - No NoiseFX is applied
* **Simple** - Default simplex noise
* **Cloud** - Fractalized noise resembling the cloud noise in Photoshop
* **Custom** - Custom noise, which can be written in glsl `flair/maya/shaders/material/include/noise.glsl` [`customNoise(vec4 v)`].

When multiple materials are selected and each one contains a different noise type, the combo box widget will be highlighted in red.

### Modifying noise
Modifying noise is simple, select the object with the material that you wish to modify and use one of the three relative sliders.

* **Scale** - Modifies the scale of the 3D/2D noise for the specified effect [noise frequency]. The scale will be relative to the [World Scale](/maya/getting-started/globals/#world-scale) global attribute.
* **Noise** - Modifies the contrast (how strong it is) of the noise for the specified effect. Keep in mind that noise is composed out of positive and negative values and the contrast amplifies the noise in both directions [noise amplitude].
* **Phase** - Modifies the phase of the noise to get different patterns at the same scale [noise phase].
* **Shift** - Shifts the noise towards positive or negative values, accordingly [noise shift].

## Showcase
Here we select the object that contains the material to which we want to add NoiseFX onto. Using the NoiseFX tool, we modify the _noise_, _scale_ and _offset_ of the density to create a natural-looking pigment turbulence effect.

<figure>
<video autoplay loop muted playsinline style="width:500px">
<source src="/media/tools/noisefx/showcase.mp4" type="video/mp4" />
</video>
<figcaption>Adding and modifying density NoiseFX</figcaption>
</figure>

## Internal workings

The NoiseFX tool simplifies the toggling and modifying of procedural attributes on Flair materials.  
These can be found within each material when opening the NoiseFX group in the Attribute editor.

<figure class="aio-ui">
<img src="/media/tools/noisefx/noiseFX_AE.png" alt="NoiseFX attributes" />
<figcaption>Using NoiseFX on the material of the selected object.</figcaption>
</figure>

## FAQ
<details>

<summary>Can I change the type of noise that NoiseFX uses?</summary>

Yes, you can write your own noise function for the _Custom_ noise type. However, you will need to modify the material glsl shader code to do so at `flair/maya/shaders/material/include/noise.glsl` [`customNoise(vec4 v)`].

</details>
