---
title: Effect Layer Parameters
sidebar:
  label: Parameters
  order: 3
---

The defined effect layer parameters are applied onto the following materials:

- PPM dynamic instances (MIDs) created from the layer's referenced PPMs
- Surface materials through the referenced MPCs

These parameters are applied following a three-tier cascade:

1. **Material compiled default** (implicit — if no override exists, the MID inherits it)
2. **Layer override** (unexposed: `Default Value`)
3. **Actor override** (exposed: value from the FlairStyle)

Parameters not defined within the effect layer are silently ignored so materials use their default value. Parameters defined within the layer but unexposed, apply the `Default Value` set within the layer parameter. Parameters that are defined within the layer and exposed, apply the value within the FlairStyle referencing the effect layer.

## Creating a Parameter

To create effect layer parameters, you can do this either automatically from the PPMs and MPCs referenced in the material with the `Fetch Parameters` button [documented in the breakdown](/unreal/technical-artist-guide/effect-layers/breakdown/#fetch-parameters) or manually by adding array elements.

We recommend doing this automatically and excluding parameters that you don't want fetched with the `_` prefix. However, if you need can also do this manually by simply adding an element.

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/parameters/add-parameter.png" alt="Adding a parameter array element" />
<figcaption>Adding a parameter array element.</figcaption>
</figure>

Once parameters have been added, you will see all the metadata that can be set with it i.e., `FFlairParameterInfo`. This metadata defines how the parameter will be used within Flair and how it will be presented to artists when exposed in the FlairStyle.

<figure>
<img src="/media/unreal/technical-artist-guide/effect-layers/parameters/empty-parameter.png" alt="An empty parameter element" />
<figcaption>An empty parameter element.</figcaption>
</figure>

When a parameter is orphaned, it means that no parameter with the given `Name` can be found within the referenced PPMs or MPCs. These parameters are highlighted in orange as they require action to be named correctly or deleted.

When collapsed, array elements present the Parameter names and their default value.

## Parameter Configuration

Each parameter in the `Parameters` array is a `FFlairParameterInfo` struct with unique properties.

### Exposed vs. Unexposed

One of the core principles of Flair Effect Layer parameters is if they are exposed or unexposed, as this changes how they are interpreted internally and what kind of configurations are available for the parameter.

- **Exposed**: Appears per-actor on the FlairStyle. Artists tweak it per level or per shot, and can **animate it in Sequencer**, where parameters appear in the same groups and UI order as the Details panel (see [Animating in Sequencer](/unreal/artist-guide/sequencer/)).
- **Unexposed**: Does _not_ appear in the FlairStyle. The `Default Value` acts as a layer-level override, applied to all FlairStyles referencing this layer. Useful for internal thresholds, fixed iteration counts, or any parameter that should be consistent across the production. Unexposed parameters are slightly cheaper than exposed ones (no per-actor lookup).

### Runtime properties

Runtime properties are included in cooked builds and can also affect how parameters are presented to artists within the FlairStyle details panel.

- **Name**: Name of the parameter matching the parameter name in the PPM or MPC (Convention: PascalCase).
- **Variant**: Optional suffix that disambiguates two layers driving the **same** material parameter `Name`. Leave it empty and the parameter keys on `Name` alone. Set it and the parameter keys on `Name` + `Variant`, so two layers that share a parameter name stay separate instead of being merged into one. Only applies to material (PPM) parameters, not MPC parameters.
- **Exposed:** Whether this parameter is exposed and controlled per-actor on the FlairStyle. When false, the default value is applied at the layer level (shared across all styles). Internal name: `bExposed`
- **Type:** Parameter type i.e., Scalar, Vector, Color, Texture, Enum, or Bool
- **Default Value:** Type-specific default value (overridden if exposed). Internal name: `DefaultValue`

**Enum-specific:**

- **Enum Asset**: User Defined Enum asset defining the available dropdown options. Internal name: `EnumAsset`
- **Default Enum Value**: Enum default value (overridden if exposed). Internal name: `DefaultEnumValue`

**Texture-specific:**

- **Seamless**: if true, it preprocesses textures and derives parameters for texture synthesis automatically. Internal name: `bSeamless`

**Bool-specific:**

- **Default Bool Value**: Read-only mirror of the static switch value in the material, shown as `True`/`False` with the parameter row tagged `[static]`. Static switches select a shader permutation, so Flair never writes them, set them on the material instance itself. Bool parameters never appear on the FlairStyle and cannot be keyed in Sequencer. Internal name: `DefaultBoolValue`

### Editor-only properties (visible when `bExposed = true`)

Editor-only properties _only_ affect how the parameters are presented to artists within the FlairStyle details panel.

- **Display Name**: Optional display name for the UI. Falls back to `Name` if empty.
- **Tooltip:** Tooltip shown when hovering the parameter in the FlairStyle Details panel
- **Group:** Group name for organizing parameters in the FlairStyle Details panel. Falls back to the Effect Layer Name.
- **UI Order**: Sort order within the Details panel (lower values appear first). Groups are sorted by the minimum UI Order of their parameters. Parameters within a group are sorted by UI Order.<br />Use gaps (e.g., 0, 10, 20) to allow future insertions without renumbering.
- **Source Name**: Name of the source PPM or MPC this parameter modifies

**Vector-specific:**

- **Vector Dimension**: Number of channels shown for Vector parameters (default: Vec2)
- **Vector Labels:** Custom labels for vector channels (comma-separated, e.g., "U,V" or "R,G,B"). Falls back to X,Y,Z,W

**Texture-specific:**

- **Texture Picker**: Content path filter for the texture picker. When non-empty, only textures under this path are shown (e.g., "/Flair/Textures/Canvases"). When empty, the picker is unrestricted.

**Scalar-specific**:

- **Min/Max**: hard clamp bounds. Set `MinValue > SoftMinValue` to remove the hard minimum (unbounded). Set `MaxValue < SoftMaxValue` to remove the hard maximum.
- **SoftMin/SoftMax**: slider drag range (users can type values beyond this range)

## Cross-Layer Parameter Deduplication

When multiple effect layers expose a parameter with the **same name** (`FName`, case-insensitive) **and the same Variant**, Flair treats them as one shared parameter:

- **Storage:** one value per name + variant in the FlairStyle's parameter maps
- **Defaults:** first-layer-wins. The first layer in the `EffectLayers` array determines the default values and UI metadata.
- **Grouping**: groups with the same name from different layers are merged.
- **Apply broadcast:** parameter changes within the FlairStyle propagates to all layers' MIDs and MPCs that share the same name + variant.

This lets you share parameters across layers without duplication, so Artists see a single parameter that controls all layers.

:::note[Need two layers to keep separate values for the same material parameter?]
Give them different **Variant** suffixes (e.g., `Edge` and `Line`) and they'll appear as two distinct parameters in the FlairStyle instead of being merged into one (e.g., `LightingBlendEdge` and `LightingBlendLine`). Layers that should stay linked simply leave **Variant** empty (or matching).
:::

## Authoring Tips

- Use **Groups** to organize parameters in the Details panel.
- **Orphaned** parameters (orange tint) no longer exist in any material or MPC. Either rename it or click `Fetch Parameters` to refresh, then remove remaining orphans.
- Prefix private material parameters with `_` to exclude them from being fetched automatically.
- The `SourceName` rows shows which PPMs/MPCs define each parameter, speeding up parameter chasing.

Now that you have learnt how to customize the FlairStyle parameters, let's control things further by defining the art-direction tools with [Control Definitions](/unreal/technical-artist-guide/effect-layers/control-definitions/).
