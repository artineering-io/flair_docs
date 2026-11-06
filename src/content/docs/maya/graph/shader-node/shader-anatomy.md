---
title: "Shader Anatomy"
sidebar:
  order: 1
---
While the shaders in the Flair graph are mostly writen in GLSL, one can also define the interface that will be shown in Flair. Therefore, shaders in Flair are divided in two parts, the **interface** and the **shader** code. 

The **shader code** of a Flair shader is written in plain ***GLSL*** code, whereas the **interface** is written in ***TOML*** and defined within a special `/* interface */` comment block.

## Example shader code

Here is an example on how a Flair shader looks like with a detailed explanation below:

<div class="d-flex" markdown=1>

```glsl
/* interface
outputs = ["Output"]

[[uniforms]]  # table (dict) within "uniforms"
name = "Color"
type = "vec3"
widget = "color"
*/

uniform vec3 Color;
out vec4 Output;

void main() {
	Output = vec4(Color, 1.0);
}
```
```text
⬅️ Interface begins with: /* interface
← Shader has one output  

← We declare one uniform in the interface
← Uniform is named `Color`
← Uniform is a `vec3` type 
← Uniform will have a `color` widget
Interface comment block ends with: */

⬅️ GLSL code begins after here
← Declare one vec3 uniform
← Declare one vec4 output

← Main function that outputs the input color when run.
```

</div>

__From these shaders, Flair will:__

1. Identify outputs/inputs
2. Modify the node interface based on the defined _interface_
3. Bind the data to the GLSL program
4. Run the GLSL program when requested

:::note
Many examples of different Flair shaders can be found under *Flair/shaders*.
:::
