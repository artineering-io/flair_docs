### Fray

The Fray attributes allow to control globally how the frayed distortion should behave.

#### Frayed Type
The frayed type dictates where the frayed distortion should happen.

* Everything - applied everywhere
* Geometry - applied around depth differences
* Edges - applied around any recognized edge (color, normals, depth)

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/fray/frayed-type.mp4" type="video/mp4" />
</video>
<figcaption>Cycling through Everything, Geometry and Edges</figcaption>
</figure>

#### Frayed

<a class="pill-link" href="#art-directable-attributes">Art-directable</a>

The amount of frayed distortion. 

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/fray/frayed.mp4" type="video/mp4" />
</video>
<figcaption>Different frayed values</figcaption>
</figure>

#### Frayed Max Distortion
Defines the maximum amount that the frayed distortion can grow iteratively, even with art-direction.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/fray/frayed-max-distortion.mp4" type="video/mp4" />
</video>
<figcaption>Different max-frayed values, clamping the frayed distortion.</figcaption>
</figure>

:::note
Longer frayed edges are much more prone to flicker than shorter ones.
:::

#### Frayed Depth Range
The depth range at which frayed distortions are reduced or increased by the _Frayed Depth Factor_. This attribute consists of four (4) values that define the different distances from the camera to modify the amount of frayed distortions. From left to right: Close, Close Mid, Far Mid, Far.

Between the _Close Mid_ and _Far Mid_ distances, the global _Frayed_ value that has been set will apply. Beyond these distances towards the _Close_ and _Far_ depths, the global _Frayed_ value will be multiplied by the _Frayed Depth Factor_, which is defined below.

:::note
The distances are relative to the _World Scale_ global. For example, if the world scale is of _100_, a _1000_ Maya unit distance will be _10_ (1000/100). If the world scale is 1, a _1000_ Maya unit distance will be _1000_.
:::

#### Frayed Depth Factor
The factor to multiply the frayed distortions with, depending on the distance to the camera defined in the _Frayed Depth Range_. The first value is at _Close_ distance and the second value is at _Far_ distance. 

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/fray/frayed-depth-range.mp4" type="video/mp4" />
</video>
<figcaption>Frayed distortion changes according to the Frayed Depth Range and Frayed Depth Factor.</figcaption>
</figure>

:::note
You can set both of these values to 1.0 if you do not wish to modify the _Frayed_ distortions along the depth.
:::

#### Frayed Feathering
Fades the frayed distortion towards the tips of the distortion.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/fray/frayed-feathering.mp4" type="video/mp4" />
</video>
<figcaption>Frayed feathering between 0 and 1.</figcaption>
</figure>

#### Frayed Frequency
Defines the base frequency of the feature noise controlling the frayed distortion. A higher frequency will make the frayed distortion finer, whereas a lower frequency make the frayed distortion coarser.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/fray/frayed-frequency.mp4" type="video/mp4" />
</video>
<figcaption>Frayed frequency between 0 and 100.</figcaption>
</figure>

:::note
A high frequency can cause flickering as the feature noise enters sub-pixel dimensions.
:::

#### Frayed Phase
Shifts the base feature noise value around, creating new distortions at different values.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/fray/frayed-phase.mp4" type="video/mp4" />
</video>
<figcaption>Frayed phase between 0 and 1.</figcaption>
</figure>

#### Frayed Grain
Accumulates the color along the feature noise, generating frayed grain.

<figure>
<video autoplay loop muted playsinline>
<source src="/media/maya/styles/library/fray/frayed-grain.mp4" type="video/mp4" />
</video>
<figcaption>Frayed grain between 0 and 2.</figcaption>
</figure>
