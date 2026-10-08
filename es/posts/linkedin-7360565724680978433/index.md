# Guía avanzada de Cursor - context window is the new game we play

Guía avanzada de Cursor - context window is the new game we play

Para que funcione como debe, me creé un conjunto de reglas (cursor rules) que se cargan automáticamente al inicio de cada conversación. Las redacté con un tono de artes marciales (martial arts), tanto para que fueran cortas y ahorraran tokens (porque se suman a todas las conversaciones: modo always apply) como para dejar claro que son supuestos de base, no peticiones.

Las reglas le dicen, entre otras cosas:
- No estar de acuerdo conmigo automáticamente
- Revisar el código antes de cada respuesta
- No cambiar código que no sea necesario
Y algunas más (según las necesidades del proyecto)

Eso sí, noté que cuando la conversación de trabajo se alarga y la context window se llena, las reglas se olvidan. Simplemente deja de comportarse según ellas, aunque estén escritas al inicio de la conversación. La única forma de devolverlas a escena es recordárselo: "read the rules".

Es asombroso ver el efecto de las reglas: de repente deja de hacer suposiciones, de alucinar, reduce los errores y empieza a actuar según los patrones existentes. Sobre todo cuando le pido que primero estudie el código o el contexto antes de responder.

Para afinar el trabajo, también puse en mis Cursor rules explicaciones de lo que *no* hay que hacer:
- No añadir comentarios en el código si no los pido (de acuerdo con el coding standard del equipo)
- No ejecutar npm run, porque usamos hot reload
- No escribir documentación por iniciativa propia (probablemente hay un system prompt que lo empuja a hacerlo)

Y también le di instrucciones sobre cómo *sí* hacer las cosas, a partir de intentos fallidos del pasado en los que tras varias iteraciones descubrimos juntos cómo hacerlo, y luego lo fijé en una frase dentro del archivo:
- Cómo llamar a GitHub y extraer comentarios de un PR
- Cómo usar CURL cuando no hay MCP para una herramienta determinada
- Cómo escribimos los tests en el proyecto

Se puede ver el nuevo mundo de la programación (el basado en LLM) a través de 3 capas:
- La capa de modelos (qué modelo usas)
- La capa de agentes (qué herramienta de desarrollo usas)
- La capa de reglas (qué ajustes haces para tu necesidad personal)

La tercera capa es la que convierte a Cursor de un desarrollador "aprendiz" que hace sobre todo suposiciones fundamentadas (porque no tiene suficiente contexto) en un desarrollador más atento


Les invito a compartir sus propios consejos sobre qué les funcionó y qué no con Cursor 🤓

Original: https://ofershap.github.io/posts/managing-cursor-through-rules-and-context-windows/
Source: https://www.linkedin.com/posts/ofershap_%D7%9E%D7%93%D7%A8%D7%99%D7%9A-cursor-%D7%9C%D7%9E%D7%AA%D7%A7%D7%93%D7%9E%D7%99%D7%9D-context-window-is-activity-7360565724680978433-4Ew5
Published: 2025-08-11T10:00:21.462000+03:00
