---
title: "Import/Export"
description: "Flair Import/Export API entrypoints to automate workflows and develop your own tools."
sidebar:
  order: 5
---
<div class="api">

<!-- markdownlint-disable -->

# <kbd>module</kbd> `flair_import_export`
API module exposing functions related to the import and export of the Flair style. 

Flair stylizations are exported as `.style` files, which contains data stored as text-based python dictionaries. 

**Examples:**
 

Export *only* the Flair globals into a style file: 

```python
import flair_import_export
flair_import_export.export_stylization(export_path="PATH/TO/SAVE/ONTO.style", materials=False, vfx=False, proxies=False)
``` 

**Global Variables**
---------------
- **cjson**
- **maya_useNewAPI**

---

## <kbd>function</kbd> `import_stylization`

```python
import_stylization(
    import_data,
    selected=False,
    namespace_changes=None,
    maya_attrs=True,
    materials=True,
    vfx=True,
    proxies=True,
    auto_import=False,
    prefix='',
    quiet=False
)
```

Imports the stylization from a `.style` file into the scene. 

**Args:**
 
 - <b>`import_data`</b> (unicode, dict):  Path to import stylization from or dict of cached stylization 
 - <b>`selected`</b> (bool):  If import should only happen to selected objects (default: entire scene) 
 - <b>`namespace_changes`</b> (dict):  Dictionary with name changes (default: no changes) 
 - <b>`maya_attrs`</b> (bool):  If the maya attributes need to be imported (default: True) 
 - <b>`materials`</b> (bool):  If the materials need to be imported (default: True) 
 - <b>`vfx`</b> (bool):  If the vertexFX need to be imported (default: True) 
 - <b>`proxies`</b> (bool):  If proxies need to be imported (default: True) 
 - <b>`auto_import`</b> (bool):  If this function is called from auto-importing the style (default: False) 
 - <b>`prefix`</b> (unicode):  Prefix in case objects are in an additional hierarchy/group (default: no prefixes) 
 - <b>`quiet`</b> (bool):  If no success prompt should be display at the end (default: False) 

---

## <kbd>function</kbd> `export_stylization`

```python
export_stylization(
    export_path,
    selected=False,
    maya_attrs=True,
    materials=True,
    vfx=True,
    proxies=True,
    quiet=False
)
```

Exports the stylization of the scene into a `.style` file. 

**Args:**
 
 - <b>`export_path`</b> (unicode):  Path to save .style file onto 
 - <b>`selected`</b> (bool):  If export should only happen from selected objects (default: entire scene) 
 - <b>`maya_attrs`</b> (bool):  If the style needs to be exported (default: True) 
 - <b>`materials`</b> (bool):  If the materials need to be exported (default: True) 
 - <b>`vfx`</b> (bool):  If the vertex data needs to be exported e.g., vertexFX, baked data (default: True) 
 - <b>`proxies`</b> (bool):  If proxies need to be exported (default: True) 
 - <b>`quiet`</b> (bool):  If no success prompt should be display at the end (default: False) 

---

## <kbd>function</kbd> `get_maya_attrs`

```python
get_maya_attrs()
```

Get the attributes from the Flair globals node. 

Data is returned as a Python dictionary i.e., `{ "attributeName" : value, ... }`. 

**Returns:**
 
 - <b>`(dict)`</b>:  Style attributes and their values 

---

## <kbd>function</kbd> `set_maya_attrs`

```python
set_maya_attrs(maya_attrs)
```

Set the attributes in the Flair globals node. 

**Args:**
 
 - <b>`maya_attrs`</b> (dict):  dictionary with Flair global attributes and their values i.e., `{ "attributeName" : value, ... }` 

---

## <kbd>function</kbd> `get_material_attrs`

```python
get_material_attrs(shapes=None)
```

From the specified shapes/components, get their materials, material attributes/textures/type and their values. 

Additionally, shapes assigned to the materials are stored within the `meshes` key. 

Data is returned as a Python dictionary e.g.,: 

```python
{'flairMat': {'attributes': {'albedo': [(0.0, 0.0, 0.0)],
                             'alphaMask': 0.0,
                             ... },
               'meshes': ['|pSphere1'],
               'textures': {'albedo': {'attrs': {'alphaGain': 1.0,
                                                 'alphaIsLuminance': False,
                                                 ... },
                                       'name': 'file1',
                                       ... }
                            'alphaMask':  0.0,
                            ... },
               'type': 'flairShader' },
 ... }
``` 

**Args:**
 
 - <b>`shapes`</b> (list, unicode):  Shapes to extract material data from (default: selected shapes/components) 

**Returns:**
 
 - <b>`(dict)`</b>:  All material data from shapes/components 

---

## <kbd>function</kbd> `set_materials`

```python
set_materials(objects=None, materials=None)
```

Set material data onto objects. 

**Args:**
 
 - <b>`objects`</b> (list):  List of objects to assign to (default, all shapes/components defined within the `meshes` key) 
 - <b>`materials`</b> (dict):  Dictionary of material data (Formatted as with `get_material_attrs()`) 

---

## <kbd>function</kbd> `get_proxies`

```python
get_proxies(materials)
```

Get proxies from material data. 

**Args:**
 
 - <b>`materials`</b> (dict):  Dictionary of material data 

**Returns:**
 
 - <b>`(list)`</b>:  List of proxy meshes 

---

## <kbd>function</kbd> `set_proxies`

```python
set_proxies(materials, style_path)
```

Set proxies in the scene, if available. 

Proxy meshes are exported with the suffix `_proxies.fbx` alongside the `.style` file. So, if this file is found alongside the style_path, the geometry will be imported and proxy materials assigned to it. 

**Args:**
 
 - <b>`materials`</b> (dict):  Dictionary with material data 
 - <b>`style_path`</b> (unicode):  Path of the `.style` file 

---

## <kbd>function</kbd> `get_vertex_data`

```python
get_vertex_data(shapes, data_type='VertexFX')
```

From the specified shapes, get their vertex data i.e., VertexFX or baked positions. 

Data is returned as a Python dictionary e.g.,: 

```python
{'|pSphere1': {'controlSetA': {0: [0.0, 0.0, 0.0025098039768636227, 0.0],
                               1: [0.0, 0.0, 0.0025098039768636227, 0.0],
                               ... },
                ... },
... }
``` 

**Args:**
 
 - <b>`shapes`</b> (unicode, list):  Shapes to get vertex control values from 
 - <b>`data_type`</b> (unicode):  Type of data i.e., "VertexFX", "baked" (default: "VertexFX) 

**Returns:**
 
 - <b>`(dict)`</b>:  Vertex data for all specified shapes 

---

## <kbd>function</kbd> `set_vertex_data`

```python
set_vertex_data(objects, vertex_data, data_type='VertexFX')
```

Set vertex data onto shapes, be it VertexFX or baked positions. 

**Args:**
 
 - <b>`objects`</b> (unicode, list):  Objects to set vertex data onto 
 - <b>`vertex_data`</b> (dict):  Dictionary containing the vertex data (Formatted as with `get_vertex_data()`) 
 - <b>`data_type`</b> (unicode):  Type of data i.e., "VertexFX", "baked" (default: "VertexFX) 

---

## <kbd>function</kbd> `custom_import`

```python
custom_import()
```

Custom import function that can be customized within the *_custom_import_export.py* module to have any kind of predefined options, namespace changes and even prefixes applied. Refer to `_custom_import_export_example.py` for an example on how this can be customized. 

Usually run when right-clicking on the `im/ex` shelf button and selecting `Custom import`. 

---

## <kbd>function</kbd> `auto_import_style`

```python
auto_import_style()
```

Custom auto-import function that can be customized within the *_custom_import_export.py* module to automatically browse the style of assets in the scene and apply them with predetermined values. Refer to `_custom_import_export_example.py` for an example on how this can be customized. 

Usually run when right-clicking on the `im/ex` shelf button and selecting `Custom auto-import`. 

</div>
