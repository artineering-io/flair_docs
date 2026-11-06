---
title: "Shader Conversion"
sidebar:
  order: 6
---
## HLSL to GLSL
Converting HLSL shaders to Flair GLSL shaders is quite straightforward. Here is the main syntax that needs to be changed.

1. Replace `Texture2D` with `sampler2D`
2. Replace fragment function with `void main() {`
3. Replace matrices
    1. Replace `float2x2` with `mat2`
    2. Replace `float3x3` with `mat3`
    3. Replace `float4x4` with `mat4`
    4. Change order of elements. HLSL is row mayor, whereas GLSL is column major
4. replace `float2` with `vec2`
5. replace `float3` with `vec3`
6. replace `float4` with `vec4`
7. Change Load to texelFetch
    - replace `Load` with `texelFetch`
    - replace `int3 loc = int3(i.pos.xy` with `ivec2 loc = ivec2(gl_FragCoord.xy`
8. Replace Sample with texture
    - replace `Sample` with `texture`
    - replace `i.uv` with `f_texcoord`
9. Replace `return` with `Output =`
