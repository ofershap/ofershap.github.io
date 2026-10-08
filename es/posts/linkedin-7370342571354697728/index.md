# ¡Empieza a hablar en LLM! 🈯

¡Empieza a hablar en LLM! 🈯 
Hasta ahora, la ingeniería de prompts intentaba arreglárselas con un lenguaje que no se construyó para ello. Microsoft ha lanzado ahora una nueva estructura de lenguaje económica, eficiente y organizada.

Hasta hoy no existía una forma realmente eficiente de escribir prompts para IA (para los ingenieros que desarrollan sistemas que trabajan contra la API)
Markdown servía para organizar textos, pero sin una verdadera jerarquía lógica. 
JSON intentaba describir la estructura, pero el formato está cargado de caracteres innecesarios y es difícil de leer y escribir a mano. 

En ambos es difícil producir prompts complejos, dinámicos y mantenibles. Cada pequeño cambio se convierte en una tarea engorrosa, y cada duplicación de un prompt crea duplicados y lógica dispersa.

A medida que los modelos se vuelven más potentes, la exigencia sobre ellos es más precisa, y crece la necesidad de un lenguaje nuevo que entienda los prompts no como texto, sino como código modular.

Aquí entra Microsoft, con un lenguaje nuevo:
 POML – Prompt Orchestration Markup Language.

POML es un lenguaje de marcado "abierto" que aporta orden, jerarquía y escalabilidad a la ingeniería de prompts. En lugar de mantener código textual "suelto", por fin se puede trabajar con etiquetas, plantillas, variables y estilos.

Volvemos un poco atrás en el tiempo, a la era de XML (¿lo recuerdas? antes de la era de JSON)

¿Cómo funciona en la práctica?

- Se usan elementos como `<role>`, `<task>`, `<example>` para definir partes lógicas del prompt.
- Se extrae información externa con `<document>`, `<table>`, `<image>` sin codificarla a mano.
- Se separa el formato de la lógica con `<stylesheet>`, de forma similar a CSS.
- Se definen variables, condiciones y bucles con un motor de `<let>`, `if`, `for`, para crear plantillas dinámicas.
- Por supuesto, ya hay soporte en VS Code (con una extensión dedicada que incluye autocompletado, vista previa y diagnósticos).

El resultado: gestión consistente de prompts, menos duplicación, alta flexibilidad para las actualizaciones y, sobre todo, ahorro de tokens innecesarios y mejora rápida del rendimiento.

Cuando el propio formato se vuelve inteligente y hay una verdadera optimización de toda la cadena de valor del LLM, el resultado es un ahorro de recursos y costes.

¡Merece la pena probarlo!

¿Cómo empezar? Desde aquí: https://lnkd.in/dQnXbH3t

Original: https://ofershap.github.io/posts/poml-treats-prompts-as-modular-code/
Source: https://www.linkedin.com/posts/ofershap_%D7%AA%D7%AA%D7%97%D7%99%D7%9C%D7%95-%D7%9C%D7%93%D7%91%D7%A8-llm%D7%99%D7%AA-%D7%A2%D7%93-%D7%A2%D7%9B%D7%A9%D7%99%D7%95-%D7%94%D7%A0%D7%93%D7%A1%D7%AA-%D7%A4%D7%A8%D7%95%D7%9E%D7%A4%D7%98%D7%99%D7%9D-activity-7370342571354697728-XUvc
Published: 2025-09-07T09:30:03.354000+03:00
