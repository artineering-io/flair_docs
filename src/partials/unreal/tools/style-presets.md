Style presets are predefined FlairStyle configurations that you can load or save at any time.

If you have more than one FlairStyle actors in the level, the tool will work similarly to selecting the FlairStyle actor from the `PARAM` shelf icon. It will prioritize the currently selected style actor, then the unbound style actor with the most effect layers and finally the the closest style actor to the viewport camera. When loading a style preset, if no FlairStyle actor exists in the level, one is automatically created.

<figure class="video-embed">
<iframe src="https://www.youtube.com/embed/SKA45fPAtug" title="Style presets in Flair for Unreal Engine" allowfullscreen loading="lazy"></iframe>
<figcaption>The Style presets work similarly to how they work within Flair for Maya.</figcaption>
</figure>

### Opening the Preset Browser

Click the `STYLE` button in the Flair shelf or in the Flair section of the FlairStyle details panel.

<figure>
<img src="/media/tools/style-presets/style-button.png" alt="The STYLE button in the Flair shelf" />
<figcaption>The <code>STYLE</code> button opens the style presets</figcaption>
</figure>

It is the same UI that you find in Flair for Maya, though the Loading options do differ.

![The style presets window](/media/tools/style-presets/window.png)

### Loading a Preset

1. Browse or filter the preset list
2. Choose your **load options**:
   - **Load engine:** load internal engine parameters (prepended with `_`)
   - **Load parameters:** load scalar, vector, and color parameters
   - **Load textures:** load texture parameters
   - **Load layers:** replace all effect layers
3. Select your desired preset
4. Click on **Load** or **Double click on the preset**

### Saving a Preset

1. Set up your desired look
2. Within the Preset Browser, type a name in the **Save** field
3. **Press enter** or **click on save**

This will save all effect layers, style parameters and render a thumbnail so that you can load them at a later point.

### Preset Locations

Presets are stored in up to three locations (highest priority first):

| Location | Path | Purpose |
| --- | --- | --- |
| **Custom** | `$FLAIR_PRESETS_PATH/styles/` | Optional. Set the `FLAIR_PRESETS_PATH` environment variable to add a custom preset directory (e.g., a studio-wide shared network folder). Highest priority when set. |
| **Project** | `{ProjectDir}/Flair/Presets/styles/` | Team presets, checked into version control |
| **Plugin** | `{PluginDir}/Presets/styles/` | Built-in presets shipped with Flair (read-only) |

If two presets share the same filename, the higher-priority location wins.

### Modifying Presets

When you save a new preset with the same name of an existing preset, the existing preset will be overridden by the new one.

When you right click on a preset, a context menu appears allowing to:

- Edit preset - Opens the default text editor to edit the preset `.json` content.
- Rename preset - Opens a rename dialog to rename the preset.
- Open folder - Opens the folder containing the preset

![The preset context menu](/media/tools/style-presets/context-menu.png)

At the bottom-right of the preset window you will find two additional buttons:

- Refresh - Refreshes the presets, reflecting any new changes
- Delete - Deletes the selected preset after confirming it on the warning dialog

![The Refresh and Delete buttons](/media/tools/style-presets/buttons.png)

Now that we know how to quickly load styles, it's time to start [Breaking down the Flair Style Actor](/unreal/artist-guide/style-actor/).
