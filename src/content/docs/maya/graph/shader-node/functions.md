---
title: "Intrinsic Functions"
sidebar:
  order: 4
---
All intrinsic GLSL functions for fragment shaders are supported by Flair shaders. We have documented some of the most used ones here, but for an exhaustive list, please refer to the [OpenGL reference card, Page 9](https://www.khronos.org/files/opengl45-quick-reference-card.pdf).

In addition to the intrinsic GLSL functions, we have implemented custom functions and included them in this documentation. If you wish for us to implement other functions and offer them out-of-the box, please let us know.

<div class="aio-uniform-list" markdown=1>

## acos
Returns the arccosine of an `angle` in radians.

```glsl
float acos(float angle)  
vec2 acos(vec2 angle)  
vec3 acos(vec3 angle)  
vec4 acos(vec4 angle)
```

## asin
Returns the arcsine of an `angle` in radians.

```glsl
float asin(float angle)  
vec2 asin(vec2 angle)  
vec3 asin(vec3 angle)  
vec4 asin(vec4 angle)
```

## atan
Returns the arctangent of an `angle` in radians.

```glsl
float atan(float angle)  
vec2 atan(vec2 angle)  
vec3 atan(vec3 angle)  
vec4 atan(vec4 angle)
```

## cos
Returns the cosine of an `angle` in radians.

```glsl
float cos(float angle)  
vec2 cos(vec2 angle)  
vec3 cos(vec3 angle)  
vec4 cos(vec4 angle)
```

## degrees
Converts `radians` to degrees.

```glsl
float degrees(float radians)  
vec2 degrees(vec2 radians)  
vec3 degrees(vec3 radians)  
vec4 degrees(vec4 radians)
```

## exp
Calculates the constant *e* raised to the power of `x`.

```glsl
float exp(float x)  
vec2 exp(vec2 x)  
vec3 exp(vec3 x)  
vec4 exp(vec4 x)
```

## exp2
Calculates 2 raised to the power of `x`.

```glsl
float exp2(float x)  
vec2 exp2(vec2 x)  
vec3 exp2(vec3 x)  
vec4 exp2(vec4 x)
```

## getViewportScalingFactor
Returns the viewport scaling factor for resolution independent effects proportional to the render width (1024 = 1.0).

```glsl
float getViewportScalingFactor()
```

## lab2rgb
Converts an Lab `color` to RGB color space

```glsl
vec3 lab2rgb(vec3 color)
```

## lab2xyz
Converts an Lab `color` to XYZ color space

```glsl
vec3 lab2xyz(vec3 color)
```

## lerp
Interpolates between `value1` and `value2` according to `t`. The interpolated value can go beyond `value1` and `value2` if `t` is not between 0...1.
Note: `mix()` equivalent from HLSL.

```glsl
float lerp(float value1, float value2, float t)
vec2 lerp(vec2 value1, vec2 value2, float t)
vec3 lerp(vec3 value1, vec3 value2, float t)
vec4 lerp(vec4 value1, vec4 value2, float t)
```

## log
Calculates the power to which the constant *e* has been raised to produce `x`.

```glsl
float log(float x)  
vec2 log(vec2 x)  
vec3 log(vec3 x)  
vec4 log(vec4 x)
```

## log2
Calculates the power to which 2 has been raised to produce `x`.

```glsl
float log2(float x)  
```

## log10
Calculates the power to which 10 has been raised to produce `x`.

```glsl
float log10(float x)  
```

## luminance
Calculates the luminance (grayscale) of an image.

```glsl
float luminance(vec3 color)
```

## mix
Interpolates between `value1` and `value2` according to `t`. The interpolated value can go beyond `value1` and `value2` if `t` is not between 0...1.

```glsl
float mix(float value1, float value2, float t)
vec2 mix(vec2 value1, vec2 value2, float t)
vec3 mix(vec3 value1, vec3 value2, float t)
vec4 mix(vec4 value1, vec4 value2, float t)
```

## pow
Calculates `x` raised to the power of `y`.

```glsl
float pow(float x, float y)  
vec2 pow(vec2 x, vec2 y)  
vec3 pow(vec3 x, vec3 y)  
vec4 pow(vec4 x, vec4 y)
```

## radians
Converts `degrees` to radians

```glsl
float radians(float degrees)  
vec2 radians(vec2 degrees)  
vec3 radians(vec3 degrees)  
vec4 radians(vec4 degrees)
```

## remap
Remaps `value` between `newMin` and `newMax` based on its previous `oldMin` and `oldMax` values.

```glsl
float remap(float value, float oldMin, float oldMax, float newMin, float newMax)
```

## rgb2hsv
Converts an RGB`color` to HSV color space

```glsl
vec3 rgb2hsv(vec3 color)
```

## rgb2lab
Converts an RGB `color` to Lab color space

```glsl
vec3 rgb2lab(vec3 color)
```

## rgb2xyz
Converts an RGB `color` to XYZ color space

```glsl
vec3 rgb2xyz(vec3 color)
```

## saturate
Clamps the value between 0...1

```glsl
float saturate(float value)
vec2 saturate(vec2 value)
vec3 saturate(vec3 value)
vec4 saturate(vec4 value)
```

## sin
Returns the sine of an `angle` in radians

```glsl
float sin(float angle)  
vec2 sin(vec2 angle)  
vec3 sin(vec3 angle)  
vec4 sin(vec4 angle)
```

## tan
Returns the tangent of an `angle` in radians

```glsl
float tan(float angle)  
vec2 tan(vec2 angle)  
vec3 tan(vec3 angle)  
vec4 tan(vec4 angle)
```

## texelFetch
Fetches the texel of a `texture` at a specific integer texture `coordinate` at mipmap `lod` (usually 0)

```glsl
vec4 texelFetch(sampler2D texture, ivec2 coordiante, int lod)
```

## texture
Samples the texel of a `texture` at a specific `uv` coordinate

```glsl
vec4 texture(sampler2D texture, vec2 uv)
```

## textureSize
Returns the texture size of an input texture in a `sampler2D` at mipmap `lod` (usually `0`)

```glsl
ivec2 textureSize(sampler2D sampler, int lod)
```

## unpremultiply
Unpremultiplies an `image`

```glsl
vec4 unpremultiply(vec4 image)
```

## xyz2lab
Converts an XYZ `color` to Lab color space

```glsl
vec3 xyz2lab(vec3 color)
```

## xyz2rgb
Converts an XYZ `color` to RGB color space

```glsl
vec3 xyz2rgb(vec3 color)
```

</div>
