---
title: Flair for Unreal Engine - Artist Guide
description: The artist guide to using Flair's stylized rendering framework in Unreal Engine.
sidebar:
  label: Overview
  order: 0
---

The artist guide to using Flair's stylized rendering framework in Unreal Engine.

:::note[For Technical Artists]
If you're authoring effect layers, writing post-process materials, or defining control definitions, see the [Technical Artist Guide](/unreal/technical-artist-guide/).
:::

## What is Flair for Unreal Engine?

Flair is a post-processing framework for Unreal Engine that lets you create **stylized rendering effects** — watercolor, sketch, and more — directly inside the editor. It works as a layer-based system on top of UE's post-process pipeline, giving artists control over the look of their scenes without writing shaders (though you still can if needed :).

**Key features:**

- Layer-based style composition
- Art-direction in real-time
  - Style presets
  - Style parameters
  - Per-material control with NoiseFX
  - Animate style parameters over time in Sequencer
- Canvas texture support for paper/surface effects
- No shader authoring required for day-to-day use

Flair for Unreal Engine is in active development to match and surpass Flair for Maya with it's modular effect layer framework. However, that doesn't mean that you cannot use Flair for Unreal Engine already in your projects. The modular architecture has been established so new updates will either be aesthetic, bring new-styles, new tools, better UX or optimizations under the hood.

## Learning Journey

1. [Getting Started with Flair for Unreal](/unreal/artist-guide/getting-started/)
2. [Flair for Unreal Breakdown - Artist's Perspective](/unreal/artist-guide/breakdown/)

### Flair Style

For setting up the style and its effects

3. [Create a Flair Style Actor](/unreal/artist-guide/create-style-actor/)
4. [Using Presets to save/load styles](/tools/style-presets/)
5. [Breaking down the Flair Style Actor](/unreal/artist-guide/style-actor/)

### Art-direction Tools

For fine-grained control of effects.

6. [NoiseFX](/tools/noisefx/)
7. [Animating in Sequencer](/unreal/artist-guide/sequencer/)

---

8. [Tips and Best Practices](/unreal/artist-guide/tips/)

Now that you've reached the end of the Flair for Unreal Engine - Artist's Guide, it's time to go deeper into the Flair framework to author your own effects and create your own Flair styles: [Flair for Unreal Engine - Technical Artist Guide](/unreal/technical-artist-guide/).
