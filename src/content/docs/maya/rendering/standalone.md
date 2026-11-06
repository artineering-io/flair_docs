---
title: "Standalone Renderer"
sidebar:
  order: 3
---
Standalone rendering can be done without opening the Maya user interface by running Maya from the command line in batch mode.

An example of this setup can be found in the scripts folder of Flair `flair/maya/scripts/flair_batch.py`.

## Prerequisites
1. The shell is using the GPU 
    * Windows - This can be set in Windows 11 under `System -> Display -> Graphics`
2. A Flair license is installed in the computer/server

## Usage

The usage of standalone rendering in Flair will depend a lot on what is being set in the `flair_batch.py` file. We have tried to document it thoroughly and make it as flexible as possible for different integrations.

In a nutshell, the `flair_batch.py` file will run on the scene you open through Maya batch with either the arguments you initialize the Flair `Renderer` class with, or whatever has been saved in the opened scene.

``` python
# initialize the renderer
# check flair_render.py for full list of options
renderer = fr.Renderer(name = "<Scene>.<Camera>.<####>",  # tag options: <Scene>, <Camera>, <Target>, <RenderLayer>, <####> (empty: grab _sequenceName global)
                       directory = "",  # a specific directory to render onto, (empty: grab _sequenceDir global or "project/images")
                       sequence = True,  # if a sequence or an individual frame
                       frame_range = [],  # entire playback range of scene if left empty
                       frame_step = 1,  # render only every X frames
                       targets = ["albedo", "outputTarget"],  # AOVs to render
                       targets_to_distort = ["outputTarget"],  # AOVs to distort (TAA, canvas disitortion, etc)
                       force_distortion_blending = [],  # AOVs to force distortion blending onto
                       cryptomatte = True,  # if cryptomattes should be rendered
                       taa = True,  # if TAA should be enabled
                       resolution = [1920, 1080],
                       render_scale = 1.0,  # options: "1.0", "1.5", "2.0"
                       alpha = "Premult.",  # options: "None", "Linear", "Premult."
                       img_format = ".exr",  # options: ".png", ".jpg", ".exr", ".tiff", ".iff"
                       cameras = ["|shotcam"],  # all renderable cameras of the scene if left empty
                       each_light = False,  # if each light should be rendered separately
                       )
```

After initialization, the `flair_batch.py` will then render with everything that has been specified when opened together with the desired Maya scene file in batch, as follows.

### Windows:    
#### Powershell
``` shell
cd "C:/Program Files/Autodesk/Maya2024/bin"
./mayabatch -file "path/to/maya/file" -command 'python(""import flair_batch"")' -noAutoloadPlugins
```

#### Command Prompt
``` shell
cd "C:/Program Files/Autodesk/Maya2024/bin"
mayabatch -file "path/to/maya/file" -command "python(\"import flair_batch\")" -noAutoloadPlugins
```

### Linux
``` shell
cd "/opt/maya2024/bin"
maya -batch "path/to/maya/file" -command "python(\"import flair_batch\") -noAutoloadPlugins
```
