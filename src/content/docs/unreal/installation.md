---
title: Installation
description: Install Flair for Unreal Engine into your project.
sidebar:
  order: 1
---

## Prerequisites

| Operating system | Version | VRAM | RAM |
| --- | --- | --- | --- |
| Windows | 11 | 8 GB | 16 GB |
| Linux | Rocky 9+ (RHEL 9), Unreal Engine 5.8+ | 8 GB | 16 GB |
| macOS | (coming soon) | n/a | 24 GB |

## Installation

1. Download Flair for Unreal.
2. With your UE project closed, copy the **Flair** plugin folder into your project's `Plugins/` directory.
3. Install any [optional](#optional) plugins.
4. Open your UE project to load the plugin.
5. On first launch, Flair installs **PySide6**. This happens only once and may freeze the splash screen for a moment.

### Linux

On Linux, Flair supports **Unreal Engine 5.8 and newer**. Unreal Engine 5.7 has engine bugs on Linux that make the editor crash or freeze when you switch some Flair styles, and that make clicks unreliable; Unreal Engine 5.8 fixes them. On Windows, Flair supports Unreal Engine 5.7 and newer.

On a Wayland desktop (the default on Rocky 9, Fedora and most current distributions), start Unreal Engine through X11 so that Flair's windows work properly:

```bash
SDL_VIDEODRIVER=x11 QT_QPA_PLATFORM=xcb <UE folder>/Engine/Binaries/Linux/UnrealEditor <your project>.uproject
```

- **SDL_VIDEODRIVER=x11** runs the editor on X11. Without it, the editor can look less sharp on scaled displays, menus can open away from the mouse, and the viewport may not respond to WASD.
- **QT_QPA_PLATFORM=xcb** runs Flair's windows on X11 too. Without it, Flair's windows don't stay on top of the editor.
- On an X11 desktop session you can start the editor as usual.

To avoid typing this each time, add a shortcut to your `~/.bashrc`, for example:

```bash
alias ue='SDL_VIDEODRIVER=x11 QT_QPA_PLATFORM=xcb "<UE folder>/Engine/Binaries/Linux/UnrealEditor"'
```

Online and floating licenses need **libcurl**, which every desktop Linux distribution installs by default (package `libcurl` on Rocky and Fedora, `libcurl4` on Debian and Ubuntu). Behind a proxy, set the usual `https_proxy` environment variable before starting Unreal Engine.

### Optional

1. [NVIDIA DLSS](https://developer.nvidia.com/rtx/dlss#getstarted-2): improves the temporal coherence (flickering) of effects.
   1. Download the DLSS plugins.
   2. Extract and copy the following plugins into your project's `Plugins/` directory:
      1. DLSS
      2. DLSSMoviePipelineSupport
      3. StreamlineNGXCommon
2. [Odyssey](https://www.fab.com/listings/c2a71aa9-998c-4286-9d5b-df91d9cc4034?lang=en): a 2D toolset for Unreal Engine, to paint and draw on textures that complement Flair.
   1. [Odyssey | Installation and tablet configuration | Get ready on UE 5.7!](https://youtu.be/r01hSy7RD6s?si=wwSP54VNhakrQFhv)
