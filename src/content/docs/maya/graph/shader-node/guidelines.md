---
title: "Coding Guidelines"
sidebar:
  order: 5
---
These are internal coding guidelines that we adhere to at Artineering and are present in the shaders provided by Flair. You may use whatever guideline you prefer!

## Inputs/Outputs
Inputs and outputs are written in Pascal Case e.g., **ThisWordIsInPascalCase**
Note that while similar to Camel Case, the first letter **is** capitalized.

If only one output is made within the shader, you may name this `Output`, otherwise, use a descriptive name for the output that you are creating. Do **not** name them `Output1`, `Output2`, etc.

## Variables
Variables in GLSL are written in Camel Case e.g., **thisWordIsInCamelCase**
