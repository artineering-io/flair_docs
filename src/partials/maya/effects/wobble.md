### Geometry Wobble
Geometry wobble adds imperfections by deforming the geometry in 3D. Enabling this attribute will show the wobble controls in the globals node (see below) and the wobble widgets in the NoiseFX and VertexFX tools.

<figure class="aio-ui">
<img src="/media/maya/getting-started/globals/wobble-attrs.png" alt="Global wobble attributes in the Attribute Editor" />
<figcaption>The global wobble attributes in the Attribute Editor.</figcaption>
</figure>

In case you can't see the wobble effect, make sure Flair materials also have their wobble attribute enabled.

:::note
Once the wobble attribute has been enabled globally, material presets will default as wobbled.
:::

#### Wobble Frequency
Defines the regularity of the effect. A higher frequency will make the wobble more "irregular", whereas a lower frequency will make it more "regular". The frequency is directly linked to the global [World Scale](/maya/getting-started/globals/#world-scale).

#### Wobble Amplitude
Defines the amount of wobble. A higher amplitude will deform more than a lower amplitude. The amplitude is directly linked to the global [World Scale](/maya/getting-started/globals/#world-scale).

#### Wobble Phase
Defines the form of the wobble. Useful when you want a different wobble deformation or want to vary the wobble on a frame-by-frame basis.

:::note
As wobble is generated from noise in 3D, make sure to toggle the *deformed* attribute in materials if they are animated/deformed so that the wobble is baked in place.
:::

#### Wobble Blur
Defines the amount of wobble blur for each TAA sample, generating a soft edge by averaging different wobble positions. This was inspired by the "Painting with polygons" [paper](https://dl.acm.org/doi/10.1145/1597990.1598012) by Isaac Botkin. 

:::note
TAA needs to be enabled to show this effect.
:::
