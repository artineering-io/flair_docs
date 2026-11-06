#### Geometry Blur
Geometry blur deforms geometry in the shader for each TAA sample. When accumulating all these deformations, objects and all their effects will appear blurred out, as the repeating patterns overlap each other to abstract their original form. 

Enabling this attribute will show the Geometry Blur controls in the globals node (see below).

<figure class="aio-ui">
<img src="/media/maya/getting-started/globals/geo-blur-attrs.png" alt="Global wobble attributes in the Attribute Editor" />
<figcaption>The global geometry blur attributes in the Attribute Editor.</figcaption>
</figure>

:::note
TAA needs to be enabled to show this effect.
:::

##### Geo Blur Type
Geometry blur can be deformed according to different volumes represented by regular polyhedrons ([platonic solids](https://en.wikipedia.org/wiki/Platonic_solid)).
* **6-sided - hexahedron** - deforms each vertex along 8 offsets in a "cube" pattern
* **8-sided - octahedron** - deforms each vertex along 6 offsets in a "diamond" pattern
* **12-sided - dodecahedron** - deforms each vertex along 20 offsets
* **20-sided - icosahedron** - deforms each vertex along 12 offsets

:::note
If this sounds too confusing, just pick the one that you think looks best.
:::

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/geo-blur.mp4" type="video/mp4" />
</video>
<figcaption>Visualization of geo blur depth of field (icosahedron).</figcaption>
</figure>

##### Geo Blur Range
The depth range at which geometry should be deformed (blurred) in the scene. This attribute consists of four (4) values that define the different distances from the camera to deform. From left to right: Close, Close Mid, Far Mid, Far.

Between the _Close Mid_ and _Far Mid_ distances, no deformation will take place and objects will be sharp. Beyond these distances towards the _Close_ and _Far_ depths, the geometry will be deformed by the _Geo Blur Factor_, which is defined below.
 
:::note
The distances are relative to the _World Scale_ global. For example, if the world scale is of _100_, a _1000_ Maya unit distance will be _10_ (1000/100). If the world scale is 1, a _1000_ Maya unit distance will be _1000_.
:::

##### Geo Blur Factor
The factor to deform the geometry width, depending on the distance to the camera defined in the _Geo Width Range_. The first value is at _Close_ distance and the second value is at _Far_ distance. 

##### Geo Blur Radomize
Randomize the offsets so that the geometric patterns are even less recognizeable.

##### Geo Motion Blur
Deforms the geometry uniformly according to the past vertex motion data (motion vectors). Both, [VelocityPV](#velocity-pv) and [TAA](#taa) need to be enabled to visualize this effect.
