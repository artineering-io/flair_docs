---
title: Flair for Unreal Breakdown - Artist's Perspective
sidebar:
  label: Breakdown
  order: 2
---

```mermaid
graph LR
    subgraph Preset["<b>Style Preset<b>"]
        direction TB
        PP["Style Parameters<br>Effect Layers"]
    end

    subgraph FS["<b>Flair Style Actor<b>"]
        direction TB
            direction LR
            Params["Style Parameters"]
            FX["Effect Layers"]
    end

    subgraph NFX["<b>NoiseFX<b>"]
        direction TB
        subgraph AD["Art-direction per material"]
                NDesc["Relative offsets<br>Procedural 3D noises"]
        end
    end

    Preset <-- "Load / Save" --> FS
    FS -- "Defines controls for" --> NFX
```

From an artist's perspective, Flair for Unreal Engine currently consists of only three elements.

- The **Style Presets** can **load/save** the details of a **Style Actor** including its style parameters and effect layers.
- The **Flair Style Actor** **containing the style parameters and effect layers** within the level that define the style.
- The **NoiseFX**, which are defined by the **Style Actor** and have the **controls to art-direct effects per material**.

The heart of Flair within Unreal Engine lies in the FlairStyle actor, so it's time to [create a Flair Style Actor](/unreal/artist-guide/create-style-actor/).
