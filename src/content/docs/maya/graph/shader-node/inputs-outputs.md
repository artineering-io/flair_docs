---
title: "Inputs and Outputs"
sidebar:
  order: 2
---
Inputs and outputs need to be specified in both, the _interface_ and the _GLSL_ code for Flair shaders to work correctly. Flair shaders are mainly written in plain _GLSL_, but the interface is defined within the comment block `\* interface */` in a simpler language called _TOML_.

*TOML* is a minimal markup language (similar to YAML) that makes defining inputs and outputs for the shader easier for artists. 

:::note
Names in the interface **must correlate** to names in the shader code for values to bind correctly.
:::

---

## Outputs

There can be multiple _Outputs_ in a Flair shader and they need to be defined through the _interface_ (TOML) and declared in the *GLSL* code as follows:

<div class="d-flex aio-code">

<div markdown=1>

### One output

```yaml
# TOML
# defines one "Output" for the node 
outputs = ["Output"]  
```

```glsl
// GLSL
// declares one output: "Output" 
out vec4 Output;

```
<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/one_output.png" alt="A shader node with one output" />
<figcaption>A shader node with one output.</figcaption>
</figure>

</div>

<div markdown=1>

### Multiple outputs

```yaml
# TOML
# defines three outputs for the node
outputs = ["Color", "Normals", "Edges"] 
```

```glsl
// GLSL
// declares three outputs
out vec4 Color;
out vec4 Normals;
out vec4 Edges;
```

<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/multiple_outputs.png" alt="A shader node with multiple outputs" />
<figcaption>A shader node with multiple outputs.</figcaption>
</figure>

</div>

</div>

---

## Inputs

There can be multiple _Inputs_ in a Flair shader of different types, which also need to be _defined_ in the interface and _declared_ in the GLSL code as follows:

### Texture Inputs

<div class="d-flex aio-code">

<div markdown=1>

### One input texture
```yaml
# TOML
# define a texture input
[[textures]]  
name = "Texture"

```

```glsl
// GLSL
// declare an input texture
uniform sampler2D Texture;

```
<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/one_input.png" alt="An integer parameter" />
<figcaption>A shader node with one input.</figcaption>
</figure>

</div>

<div markdown=1>

### Multiple input textures
```yaml
# TOML
# define two texture inputs
[[textures]]  
name = "Texture1"

[[textures]]  
name = "Texture2"
```

```glsl
// GLSL
// declare two input textures
uniform sampler2D Texture1;
uniform sampler2D Texture2;
```
<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/multiple_inputs.png" alt="An integer parameter" />
<figcaption>A shader node with multiple inputs.</figcaption>
</figure>

</div>

</div>

### Integer numbers

```yaml
# TOML
[[uniforms]]
name = "Integer"
type = "int"      # define an integer input (parameter)
```

```glsl
// GLSL
uniform int Integer;  // declare an integer number
```
<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/param_integer.png" alt="An integer parameter" />
<figcaption>An integer parameter.</figcaption>
</figure>

### Integer vectors

```yaml
# TOML
[[uniforms]]
name = "IntVector2"  # define an integer vector input (parameter)
type = "ivec2"       # or "ivec3", "ivec4" depending on how many channels are needed 
```

```glsl
// GLSL
uniform ivec2 IntVector2;  // declare an integer vector (ivec3 or ivec4 respectively)
```

<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/param_ivec2.png" alt="An integer vec2 parameter" />
<figcaption>An integer vec2 parameter.</figcaption>
</figure>

### Floating-point numbers

```yaml
# TOML
[[uniforms]]
name = "Float"
type = "float"  # define a float input (parameter)
```

```glsl
// GLSL
uniform int Float;  // declare a float number
```

<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/param_float.png" alt="A float parameter" />
<figcaption>A float parameter.</figcaption>
</figure>

### Floating-point vectors

```yaml
# TOML
[[uniforms]]
name = "FloatVector2"  # define a float vector (parameter)
type = "vec2"          # or "vec3", "vec4" depending on how many channels are needed
```

```glsl
// GLSL
uniform vec2 FloatVector2;  // declare a float vector (vec3 or vec4 respectively)
```

<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/param_vec2.png" alt="A vec2 parameter" />
<figcaption>A floating-point vec2 parameter.</figcaption>
</figure>

### Matrices

```glsl
// GLSL
uniform mat2 Matrix2x2;  // declare a 2x2 matrix
uniform mat3 Matrix3x3;  // declare a 3x3 matrix
uniform mat4 Matrix4x4;  // declare a 4x4 matrix
```

:::note
Since matrices can't be defined yet from the parameter's panel, they can only be declared.
:::

---

## Interface definition

The interface for inputs can be further defined to enhance the functionality of uniforms and create more intuitive user interfaces.

### Sampler uniforms

`uniform sampler2D` inputs can have sampler state information attached, for example:

```yaml
# TOML
[[textures]]
name = "Color"
addressU = "mirror"
addressV = "mirror"
addressW = "mirror"
minFilter = "linear"
magFilter = "linear"
```

The following values are recognized:

- **addressU**, **addressV**, **addressW**: texture addressing mode for the U/V/W coordinate.
    - "**repeat"** - see GL_REPEAT
    - "**mirror"** - see GL_MIRRORED_REPEAT
    - "**clamp"** - see GL_CLAMP_TO_EDGE
    - "**border"** - see GL_CLAMP_TO_BORDER

<figure>
<img src="https://learnopengl.com/img/getting-started/texture_wrapping.png" alt="Different texture address modes" />
<figcaption>Different texture addressing modes. Image credit: learnopengl.com.</figcaption>
</figure>

- **minFilter**, **magFilter**: texture minification and magnification filters
    - "**nearest" -** nearest-neighbor interpolation, see GL_NEAREST
    - "**linear" -** linear interpolation, see GL_LINEAR

<figure>
<img src="https://learnopengl.com/img/getting-started/texture_filtering.png" alt="Different texture filtering filtering modes" />
<figcaption>Different texture filtering modes. Image credit: learnopengl.com.</figcaption>
</figure>

:::note
**By default, if no metadata is specified, sampler2D's are set to *REPEAT* and *NEAREST***
:::

### Numeric uniforms

`int` and `float` parameters can have optional attributes that further define their interface:

```glsl
# TOML
[[uniforms]]
name = "Float"
type = "float"
min = 0.0
max = 5.0
step = 0.2

[[uniforms]]
name = "Integer"
type = "int"
min = 0
max = 100
step = 20
```

- **min**: minimum value of the parameter. If nothing is specified, then the parameter has no minimum value.
- **max**: maximum value of the parameter. If nothing is specified, then the parameter has no maximum value.
- **step:** the step size when increasing or decreasing the parameter. If nothing is specified, it will be inferred from the min and max values, or the parameter type (*float* 0.1, *int* 1)

<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/param_integer_step.png" alt="Integer parameter with optional min, max and step size" />
<figcaption>Integer parameter with optional min, max and step size.</figcaption>
</figure>

For `int` parameters, one can create check boxes and combo boxes through the widget attribute.

```yaml
# TOML
[[uniforms]]
name = "Check"
type = "int"
widget = "checkbox"
```

<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/param_integer_check.png" alt="Integer parameter with check box interface" />
<figcaption>Integer parameter with a check box interface.</figcaption>
</figure>

```yaml
# TOML
[[uniforms]]
name = "Combobox"
type = "int"
widget = "combobox"
toggle = ["Option 0", "Option 1", "Option 2"]
```

<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/param_integer_combobox.png" alt="Integer parameter with combo box interface" />
<figcaption>Integer parameter with a combo box interface.</figcaption>
</figure>

For `vec3` and `vec4` parameters can also represent colors, the color widget is defined as follows:

```yaml
# TOML
[[uniforms]]
name = "Color"
type = "vec3"
widget = "color"
```

<figure class="aio-ui">
<img src="/media/maya/graph/shader-node/inputs-outputs/param_vec3_color.png" alt="Floating-point vector parameter with color interface" />
<figcaption>Floating-point vector parameter with color interface.</figcaption>
</figure>
