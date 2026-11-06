---
title: "Import/Export Nodes"
sidebar:
  order: 5
---
The _import_ and _export_ nodes are required whenever the Flair graph is used as a plugin. They serve to import whatever data is required and export the end result to the viewport. As such, the Flair graph won't work as a plugin if these two nodes are not used.

<figure class="aio-ui">
<img src="/media/maya/graph/import-export-node/import_export.png" alt="Import and Export nodes connected to each other" />
<figcaption>Import and Export nodes connected to each other.</figcaption>
</figure>

:::caution
Only one _Import_ and _Export_ node can be used per Flair graph.
:::

## Import Node

The import node allows to import render targets and uniforms (variables) from _Autodesk Maya_ onto the Flair Graph. Render targets are only available on-demand, so they can be chosen from the import node properties when selected (see below).

<figure class="aio-ui">
<img src="/media/maya/graph/import-export-node/import_params.png" alt="Import node parameters" />
<figcaption>Import node parameters when the node is selected.</figcaption>
</figure>

You can choose as many as necessary for the shader style, and you can request different render targets at any point. Just keep in mind that altering the order may break some connections from the import node.

### Available AOVs

| Target             | Contents |
|--------------------|----------|
| **Albedo**             | Albedo color with painterly shading |
| **Lighting**           | Diffuse lighting                    |
| **Speclight**          | Specular lighting |
| **Shadows**            | Cast shadow mask |
| **Light control**      | **R** - Light control, **G** - Toon regions, **B** - diffuse gradient $$\vec{n}\cdot\vec{L}$$  |
| **Normals and depth**  | **RG** - Normals in tangent space (flow), **B** - Linear depth, **A** - Z-Buffer |
| **Velocity and noise** | **RG** - Velocity in projection-space, **BA** - Fractalized noise |
| **World positions**    | **RGB** - World position in XYZ |
| **Canvas**             | **RG** - Canvas normals in tangent-space, **b** - Canvas heightmap |
| **Alternate canvas**   | **RG** - Alternate canvas normals in tangent-space, **b** - Alternate canvas heightmap |
| **Pigment control**    | **RGB** - Effect controls |
| **Canvas control**     | **RGB** - Effect controls |
| **Edge control**       | **RGB** - Effect controls |
| **Abstract control**   | **RGB** - Effect controls |

## Export Node

The export node allows to export the resulting image back to Autodesk Maya. The export node only accepts one input.
