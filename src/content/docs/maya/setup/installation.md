---
title: "Installation"
sidebar:
  order: 1
---
Installing Flair is as simple as a drag-and-drop.  

<div class="d-flex flex-justify-around">

<figure class="video-embed">
<iframe src="https://www.youtube.com/embed/GiXa6NPbT4c" title="Installing and activating Flair for Maya" allowfullscreen loading="lazy"></iframe>
<figcaption>Installing and activating Flair for Maya</figcaption>
</figure>

<figure class="video-embed">
<iframe src="https://www.youtube.com/embed/ABOvM372LZw" title="Updating Flair for Maya!" allowfullscreen loading="lazy"></iframe>
<figcaption>Updating Flair for Maya!</figcaption>
</figure>

</div>

1. Make sure you have all [pre-requisites](/maya/setup/#pre-requisites)
2. Download and extract all the contents of the Flair *zip* file into any folder outside of Maya  
e.g., `Documents/Flair`, `Downloads/Flair`, a shared drive.
3. Open the folder where you extracted Flair into, this will become your installation folder
4. Drag-and-drop the `install_maya.mel` file onto the Maya viewport
5. Select for whom you want to install Flair for and click `Accept` ([see options](#installation-options))
    <figure class="aio-ui aio-window">
        <img src="/media/maya/setup/installation/installation.png" alt="Flair installation prompt" />
        <figcaption>Flair installation prompt that appears after the viewport drag-and-drop.</figcaption>
    </figure>
6. Upon successful installation, a restart prompt will appear
    <figure class="aio-ui aio-window">
        <img src="/media/maya/success.png" alt="Dialog stating that the changes were successful" />
        <figcaption>Flair has been successfully installed.</figcaption>
    </figure>
7. Restart Maya
8. After restarting, the Flair shelf should appear in Maya
9. Click on the `glob` or `test` shelf button to verify the installation and prompt the Flair activation
9. [Activate Flair](/maya/setup/activation) if needed.

:::caution
If the drag-and-drop of the `install_maya.mel` file fails, make sure that its directory only contains valid [ASCII characters](https://en.wikipedia.org/wiki/ASCII), or Maya won't be able to read the _MEL_ file.
:::

### Installation options

#### Only for me
*Recommended for individuals* for simple installations without admin rights.

The installer will only insert the Flair paths into your `Maya.env` file for the Maya version in use.

All flair-related files are kept within the Flair installation folder, except for the license file, which is placed in:
* Windows: `Documents/maya`
* macOS: `~/Library/Preferences/Autodesk/maya/`
* Linux: `~/maya`

:::note
The "Only for me" option allows keeping different versions of Flair on different versions of Maya. However, everyone using Flair will need read/write permissions to the Flair installation folder.
:::

#### For all users
*Recommended for studios or institutions* where multiple artists use Flair from the same workstation/server.

This method allows installing Flair automatically in all supported Maya versions, even in environments with strict read-only policies e.g., **Rez**.

The Flair installation "For all users" requires admin/sudo privileges to place files in:

**License and modules**
* Windows: `%CommonProgramFiles%/Autodesk Shared/Modules/maya`
* macOS: `/Users/Shared/Autodesk/modules/maya/`
* Linux: `/usr/autodesk/modules/maya`

**Canvas caches**
* Windows: `%ProgramData%/Flair`
* macOS: `/Users/Shared/Flair`
* Linux: `opt/Flair`

After installation and activation, artists will find their **presets and preferences** in:
* Windows: `Documents/AppDocuments/Flair`
* macOS: `~/Library/Preferences/Autodesk/AppDocuments/Flair`
* Linux: `~/AppDocuments/Flair`

:::caution
If you need to customize where the _program data_ (caches) and _app documents_ (presets/preferences) are stored, you can follow the instructons within `flair/maya/scripts/coop/_custom_dirs_example.json`.
:::

#### Only for me (but read-only)
There is a third hidden option where you can make an _"Only for me"_ installation read-only by setting the environment variable `FLAIR_READ_ONLY=1`. This will force Flair to behave as if it was installed _"For all users"_.

For this installation to work properly, make sure the directories to save canvas caches, presets and preferences have read/write access for artists using Flair, as these will default to the _"For all users"_ directories (which can be customized within the `_custom_dirs_example.json` file). 

Keep in mind that the license will remain within the local Maya folder, so it won't be available for other users.

---

## FAQ
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
