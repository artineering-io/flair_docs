---
title: "FAQ"
sidebar:
  order: 12
---
## Use of Flair
<details>

<summary>Can I use Flair for my student production?</summary>

Yes, of course! As a student, you can either use the Free version or support us on Patreon for 5€ per month to get a community license and render at any resolution. Additionally, you can also ask your university to purchase Flair Indie for Education so that you can use it.

</details>

<details>

<summary>Are there floating licenses available?</summary>

Yes, floating licenses are available when purchasing multiple Flair _STUDIO_ or _INDIE for Education_ licenses [directly through us](https://artineering.io/contact). More details on floating licenses can be found [here](/maya/setup/activation/#floating-licenses).

</details>

<details>

<summary>Are there offline licenses available?</summary>

Yes, floating licenses work entirely offline and can be used by studios whose workstations don't have internet access due to security reasons.

</details>

## Installation
<details>

<summary>I can't install 'only for me'</summary>

If the user-based installation won't work no matter what, you can manually enter the required environment variable in the _Maya.env_ file.

1. Open the _Maya.env_ file usually found in `Documents/maya/202X/Maya.env` with a text editor (make sure its the _Maya.env_ file of the version of Maya you want to install in)
1. Enter this environment variable: `MAYA_MODULE_PATH=#YOURFLAIRMAYAPATH#` (replace _#YOURFLAIRMAYAPATH#_ with the path where `Flair/maya` is located)
1. Restart Maya.

</details>

<details>

<summary>I can't install 'for ALL users'</summary>

The installation for all users requires administrator rights in the computer where you are installing Flair in. This is because we need to put the _module_ file within _Program Files_.
To do this manually, follow the steps below:

1. Duplicate the _flair.mod_ file within the `Flair/maya` folder and open the duplicate with a text editor.
1. Change all `./` with the path to the Flair folder (with forward slashes) and save.
1. (Windows) Copy the edited _flair.mod_ and paste it in `Program Files/Common Files/Autodesk Shared/Modules/Maya/202X` (paste it in the Maya version that you want to install Flair in).
1. Restart Maya.

</details>

<details>

<summary>Flair doesn't load on macOS</summary>

macOS is particularly strict when an app has not been “vetted” through the App Store. You will need to allow `flairEngine.bundle` and `libomp.dylib` to run in your system.

<div class="d-flex">

<figure class="aio-ui-mac">
<img src="/media/maya/macos_warning_flair.png" alt="macOS warning prompt about flairEngine.bundle" />
<figcaption>flairEngine.bundle is the Flair plugin.</figcaption>
</figure>
<figure class="aio-ui-mac">
<img src="/media/maya/macos_warning_libomp.png" alt="macOS warning prompt about libomp.dylib" />
<figcaption>libomp.dylib is a Flair dependency.</figcaption>
</figure>

</div>

When these prompts appear, just click on `Done` to dismiss them. Then go to `Apple menu -> System Settings...->Privacy and Security`. At the bottom, you will find the blocked applications with the option to `Allow Anyway`. Do so for both the `flairEngine.bundle` and `libomp.dylib`.

<div class="d-flex">

<figure class="aio-ui-mac">
<img src="/media/maya/macos_allow.png" alt="Privacy and Security section of System Settings with the Allow Anyway button" />
<figcaption>Click on Allow Anyway to allow the Flair plugin to run on your system.</figcaption>
</figure>

</div>

Once you do so, the prompts will appear again, but this time with an option to `Open Anyway`.

<div class="d-flex">

<figure class="aio-ui-mac">
<img src="/media/maya/macos_warning_flair_allow.png" alt="macOS warning prompt about flairEngine.bundle with the Allow option" />
<figcaption>Click on Open Anyway to run the Flair plugin.</figcaption>
</figure>
<figure class="aio-ui-mac">
<img src="/media/maya/macos_warning_libomp_allow.png" alt="macOS warning prompt about libomp.dylib with the Allow option" />
<figcaption>Click on Open Anyway to run the Flair plugin.</figcaption>
</figure>

</div>

Click on `Open Anyway` to allow Flair to run on your Mac.

If you can't see the _flairShader_ material render, restart Maya one last time so that Flair can run normally with all permissions set.

</details>

## Activation
<details>

<summary>Whitelist URL and port on firewall for the Flair license to be validated</summary>

If you can't validate Flair on your workstation because your access to the internet is restricted by a firewall, add a whitelist rule for our licensing server: _api.keygen.sh_ on port 443.

</details>

<details>

<summary>I have not received my activation key</summary>

The email is most likely in your spam folder. Please double-check the spam folder of the email you entered or your _Patreon_ email (for _Community_ licenses).

If the license still has not arrived within an hour [contact us](https://artineering.io/contact) to help you get started.

</details>

<details>

<summary>Flair freezes on Linux during activation</summary>

If Maya freezes after claiming a license, it could be that the required QtWebEngine dependencies are not found. The easiest workaround is to add an environment variable to auto-accept the Flair EULA with `FLAIR_ACCEPT_EULA=1`.  
Yes, Linux can be a pain sometimes as every Linux distribution is different.

</details>

<details>

<summary>The viewport is all black and I get the Error compiling GLSL code on Windows.</summary>

This can happen when the viewport is forced to use DirectX (e.g., with an environment variable) instead of OpenGL. 

During installation, we try to automatically set the Viewport 2.0 rendering engine to OpenGL, but this can fail depending on your setup.  Check your Maya setup for anything that might force the viewport to use DirectX and remove it. Then, manually set the rendering engine to OpenGL (`Preferences->Display->Viewport 2.0->Rendering Engine->OpenGL Core Profile`). Maya will prompt to restart the application and Flair will be able to run after restarting.

</details>

## Viewport
<details>

<summary>How do I toggle lighting on the viewport?</summary>

You can toggle lighting on the viewport by going into the viewport menu at the top and selecting `Lighting -> Use All Lights`, or by toggling the _Use all lights_ icon.
<figure class="aio-ui">
<img src="/media/maya/faq/toggle_lighting.png" alt="Toggling shadows on the viewport" />
</figure>

Additionally, the shortcut **`7`** will enable lighting, whereas the shortcut **`5`** will revert to default lighting.

</details>

<details>

<summary>How do I toggle cast shadows on the viewport?</summary>

You can toggle cast shadows on the viewport by going into the viewport menu at the top and selecting `Lighting -> Shadows`, or by toggling the _Shadows_ icon.

<figure class="aio-ui">
<img src="/media/maya/faq/toggle_shadows.png" alt="Toggling shadows on the viewport" />
</figure>

</details>

## NoiseFX
<details>

<summary>Can I change the type of noise that NoiseFX uses?</summary>

Yes, you can write your own noise function for the _Custom_ noise type. However, you will need to modify the material glsl shader code to do so at `flair/maya/shaders/material/include/noise.glsl` [`customNoise(vec4 v)`].

</details>

## VertexFX
<details>

<summary>The scene size becomes too big after using VertexFX</summary>

This happens because Maya is not optimized to save a lot of data on vertices. Thankfully, in the [globals node](/maya/getting-started/globals/#separate-stylization), you can define to _separate the stylization_ of the scene and save it in a different file. The option `Yes, save and replace` will make your Maya scene lighter again.

</details>

<details>

<summary>Painting VertexFX is super slow</summary>

Painting vertices on objects with many polygons can be quite slow in Maya, depending on how many vertices the object has. So, make sure you are not working in 'subdivided preview' mode ('3' on your keyboard) during painting or try separating meshes to reduce the amount of vertices that Maya needs to iterate over while painting.

</details>

<details>

<summary>Can I apply VertexFX on Nurbs or changing topology?</summary>

This is unfortunately not possible as nurbs don't have vertices to save the painted effects onto.

</details>

<details>

<summary>Can I paint VertexFX on meshes with changing topology?</summary>

It is possible but not recommended. If you change the topology, the vertex count will also change so you may encounter unpredictable behaviors and even Maya crashes.

</details>
