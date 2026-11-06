---
title: Flair for Unreal Breakdown - Technical Artist's Perspective
sidebar:
  label: Breakdown
  order: 1
---

```mermaid
graph TB
subgraph PRE["<b>Style Preset</b><br><i>.json</i>"]
    direction TB
    PD["Style Parameters<br>Effect Layers"]
end

subgraph FS["<b>Flair Style Actor</b>"]
    direction LR
    SP["<b>Style Parameters</b>"]
    subgraph EL["<b>Effect Layers</b>"]
        direction LR
        RP["Render Passes"]
        PPM["Post-Process Materials"]
        MPC["Material Parameter Collections"]
        CD["Control Definitions"]
        subgraph P["Parameters"]
            direction TB
            EX["Exposed"]
            UX["Unexposed"]
        end
    end
end

subgraph AT["<b>Art-direction Tools</b>"]
    direction TB
    subgraph NFX["<b>NoiseFX</b>"]
            NDesc["Relative offsets<br>Procedural 3D noises"]
    end
end

subgraph O["<b>Output</b>"]
    direction TB
    IMG["Scene Textures<br>User Scene Textures (UST)"]
end

    PRE <-- "Load / Save" --> FS
    CD --> AT
    EX -- "Exposes" --> SP
    UX --> PPM
    SP --> PPM
    UX --> MPC
    SP --> MPC
    RP --> PPM
    AT -.-> RP
    MPC --> PPM
    MPC --> RP
    PPM --> O

style PRE fill:#f2fcfe,stroke:#333,stroke-width:1px
style EL fill:#ffefba,stroke:#333,stroke-width:1px
style P fill:#fffde4,stroke:#333,stroke-width:1px
style PPM fill:#fffde4,stroke:#333,stroke-width:1px
style MPC fill:#fffde4,stroke:#333,stroke-width:1px
style CD fill:#fffde4,stroke:#333,stroke-width:1px
style RP fill:#fffde4,stroke:#333,stroke-width:1px
style NFX fill:#f2fcfe,stroke:#333,stroke-width:1px
style SP fill:#f2fcfe,stroke:#333,stroke-width:1px
style O fill:#fef2fc,stroke:#333,stroke-width:1px
```

From a technical artist's perspective, Flair for Unreal Engine consists of four elements.

- The **Style Presets** containing **parameter values and effect layer references** of a Flair style. Presets are saved in plain-text _.json_ files, making them revision-friendly and platform agnostic.
- The **Flair Style Actor** containing **parameters and effect layers** defining the style within a level. Effect layers are the building blocks of a style and the most important concept within Flair.
- The **Art-direction Tools**, defined from each effect layer's control definitions, in charge of modifying the render passes controlling the style.
- The **Output**, which can be to custom User Scene Textures (UST) or overriding Scene Textures.

Hopefully by the end of this guide, you'll have a clear understanding on how everything works and can confidently expand upon and even create your own Flair styles.

The heart of Flair within Unreal Engine lies in the FlairStyle actor and how it's effect layers entirely define the style, so it's time to [Mix-and-Match Flair Effect Layers](/unreal/technical-artist-guide/mix-and-match/).
