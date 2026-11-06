---
title: "refer to earlier example to instance material presets library"
description: "Flair Material presets API entrypoints to automate workflows and develop your own tools."
sidebar:
  label: "Material presets"
  order: 15
---
<div class="api">

<!-- markdownlint-disable -->

# <kbd>module</kbd> `flair_material_presets`
API module exposing functions related to material presets within Flair. The material presets are directly applied onto [*flairShader*](/maya/materials/flair-shader/) nodes assigned to objects, changing material settings and attributes. This module is directly used by the [Material Presets UI](/maya/materials/presets/). 

Presets are individually stored as `.json` files and contain attributes of objects and their values. 

**Examples:**
 

Instance the material presets library 

```python
import flair_material_presets

mat_preset_lib = flair_material_presets.MaterialPresetLibrary()
mat_preset_lib.find()  # not needed to manually find starting Flair 1.1.3+

print(mat_preset_lib)
``` 

Load material presets onto objects with the material presets library 

```python

# create object (if needed)
object = cmds.polySphere(r=1)

# create a new material and set "_painterly" preset with all options enabled
options = { "new": True, "textures": True, "noiseFX": True, "attributes": True }
mat_preset_lib.load("_painterly", options, object)

# load "green" preset, but only its noiseFX values
options = { "new": False, "textures": False, "noiseFX": True, "attributes": False }
mat_preset_lib.load("green", options, object)
``` 

**Global Variables**
---------------
- **SFX_MATERIAL**
- **FLAIR_MATERIAL**
- **MAYA_DEFAULT_MATERIALS**

---

## <kbd>function</kbd> `get_material_attrs`

```python
get_material_attrs(mat, all_attrs=True)
```

From the specified material, get the attributes/textures/type and their values. 

Data is returned as a Python dictionary e.g.,: 

```python
{'attributes': {'albedo': [(0.0, 0.0, 0.0)],
                'alphaMask': 0.0,
                 ... },
 'textures': {'albedo': {'attrs': {'alphaGain': 1.0,
                                   'alphaIsLuminance': False,
                                    ... },
                         'name': 'file1',
                          ... }
              'alphaMask':  0.0,
               ... },
 'type': 'flairShader'
}
``` 

**Args:**
 
 - <b>`mat`</b> (unicode):  Name of the material 
 - <b>`all_attrs`</b> (bool):  If all attributes are needed. Otherwise, only textures and Maya's ShaderFX settings 

**Returns:**
 
 - <b>`(dict)`</b>:  Material data containing all specified attributes and their values 

---

## <kbd>function</kbd> `set_material_attrs`

```python
set_material_attrs(mat, mat_data, options=None, silent=False)
```

Set material data onto material according to options. 

Options are: 
- *textures* - attributes with connected textures as their inputs 
- *noiseFX* - attributes that control NoiseFX within the material 
- *attributes* - all remaining attributes. 

**Args:**
 
 - <b>`mat`</b> (unicode):  Name of the material to set attributes onto 
 - <b>`mat_data`</b> (dict):  Dictionary of material data (Formatted as with `get_material_attrs()`) 
 - <b>`options`</b> (dict):  Dictionary of options to set (default: `{"textures": True, "noiseFX": True, "attributes": True }`) 
 - <b>`silent`</b> (bool):  If no warnings should be printed out when attribute is not found on material 

---

## <kbd>class</kbd> `MaterialPresetLibrary`
Preset library class to save and load material presets within Flair. 

This class inherits from the Python *dict* object, extending its functionality. 

**Example:**
 

Load library and print available presets 

```python
# load preset library
mat_preset_lib = flair_material_presets.MaterialPresetLibrary()

# print available presets
preset_names = mat_preset_lib.keys()
print(preset_names)
``` 

---

### <kbd>method</kbd> `MaterialPresetLibrary.delete`

```python
delete(name)
```

Deletes the preset from the library. 

**Args:**
 
 - <b>`name`</b> (unicode):  Name of the preset to delete 

---

### <kbd>method</kbd> `MaterialPresetLibrary.find`

```python
find()
```

Finds all available material presets and populates the library class.   Material presets are searched on disk in the following locations: 
- Specified presets folder in environment variable `FLAIR_PRESETS_PATH` (`FLAIR_PRESETS_PATH/materials`) 
- User presets folder (`AppDocuments/Flair/presets/materials`) 
- Installation presets folder 

---

### <kbd>method</kbd> `MaterialPresetLibrary.load`

```python
load(name, options, objects=None)
```

Load the material preset with the specified options onto objects/components. If no Flair material has been assigned to the specified objects, one will be created. 

Options are: 
- *new* - create a new material even if the same material type was assigned before 
- *textures* - set attributes with connected textures as their inputs 
- *noiseFX* - set attributes that control NoiseFX within the material 
- *attributes* - set all remaining attributes. 

Options are a requirement for this method and can be defined as follows: 

`options = {"new": False, "textures": True, "noiseFX": True, "attributes": True }` 

**Special presets will work the same way they do within the [Material Presets UI](/maya/materials/presets/#special-presets).** 

**Args:**
 
 - <b>`name`</b> (unicode):  name of material preset 
 - <b>`options`</b> (dict):  options to load the material with 
 - <b>`objects`</b> (unicode, list):  name of objects to load preset onto (default: selected objects/components) 

---

### <kbd>method</kbd> `MaterialPresetLibrary.rename_preset`

```python
rename_preset(name, new_name)
```

Rename an existing preset. 

**Args:**
 
 - <b>`name`</b> (unicode):  name of the preset to rename 
 - <b>`new_name`</b> (unicode):  new name of the preset 

---

### <kbd>method</kbd> `MaterialPresetLibrary.save`

```python
save(name, mat)
```

Save the material attributes into a preset under the specified name.   The preset is saved on disk in the first location that is writable among the following: 
- Specified presets folder in environment variable `FLAIR_PRESETS_PATH` (`FLAIR_PRESETS_PATH/materials`) 
- User presets folder (`AppDocuments/Flair/presets/materials`) 
- Installation presets folder 

**Args:**
 
 - <b>`name`</b> (unicode):  name of the material preset 
 - <b>`mat`</b> (list, unicode):  name of the material to create preset from 

</div>
