---
title: Animating in Sequencer
sidebar:
  order: 5
---

You can animate a Flair Style's parameters over time with Unreal's Sequencer so your look can evolve across a shot.

## Add a Flair parameter track

1. Add your **Flair Style** actor to a Level Sequence in one of two ways
   - Click and drag the desired Flair Style actor from the outliner to the sequencer panel.
   - Click `+ Add` in Sequencer, go to `Add Actor Track` and select the desired Flair Style actor.

     ![Adding an actor track for a Flair Style](/media/unreal/artist-guide/sequencer/add-actor-track.png)

2. On the style's binding, click **+ Track** and choose **Flair Parameters**.

   ![The Flair Parameters track](/media/unreal/artist-guide/sequencer/flair-parameters-track.png)

3. Pick the parameter you want to animate. Parameters are organized into the same **groups and order** you see in the Details panel, so they're easy to find.
4. A track is added with a starting key at the current playhead position.

:::tip
Track channels use the same friendly parameter names you see in the Details panel. Hover over a channel to see its internal name, and for numeric (scalar) parameters, its expected value range.
:::

## Key your animation

- Scrub to a time, then change the parameter's value to add a key
- As you move the playhead, the Style updates **live** in the viewport so you can see the result while you work.
- You can spread multiple parameters across rows on the same track.

## Values restore automatically

- When you close the sequence
- When the section is defined as When Finished → Restore State

This happens so you won't accidentally leave your Style actor stuck on an animated value.

## What you can (and can't) key

- **Keyable:** exposed scalar, vector, color, and enum parameters.
- **Not keyable:** unexposed parameters or parameters linked to an effect's _iteration count_. Animating those would force expensive rebuilds every frame, so they're intentionally kept off the timeline.

:::tip
If a parameter you expect isn't in the picker, it's most likely not exposed, or it's linked to an iteration count.
:::
