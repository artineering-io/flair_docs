---
title: "Expressions"
sidebar:
  order: 9
---
You can set expressions on shader parameters to procedurally set their values. Expressions are available for the following types of parameters:

* Bool, Integer and Float types
* Vectors of integer and float types

The expression text field is toggled using the "magic wand" icon (<i class="fas fa-magic"></i>) to the right of supported parameters. Once clicked, a green expression text field will appear, where the expression can be entered.

<figure class="aio-ui">
<img src="/media/maya/graph/expressions/expressions.png" alt="Shader parameters with a global variable in the expression" />
<figcaption>Shader parameters with a global variable in the expression.</figcaption>
</figure>

Expressions are implemented using [SeExpr](http://wdas.github.io/SeExpr/doxygen/), which enable flexible artistic control, when required. The language comes with some [built-in functions](http://wdas.github.io/SeExpr/doxygen/userdoc.html) and, in addition, you can use the global values defined in the [Globals panel](/maya/graph/overview/#3-globals) (see above).
