Atmospheric effects are useful to add atmospheric depth to bigger scenes by changing the color within a specific range.

#### Atmosphere Tint
Defines a custom atmospheric perspective color, making things at distance tint towards the specified color.

#### Atmosphere Range
Defines the range at which the atmospheric tint will start and end. Set these values high to _not_ have the atmosphere range affecting your scene.

If you wish to exclude an object from the atmosphere tint affect (e.g., a background plane), [enable the _Final Color_ attribute](/maya/materials/flair-shader/#final-color) in the Flair shader material assigned to that object.

:::note
The range is set for Maya units multiplied by the _World Scale_, consider this when setting up this attribute.
:::
