# "¿Qué eres real? ¡De eso hablamos hace exactamente 10 años!"

Traducción automática del post original, sin revisión de un traductor humano. Las afirmaciones históricas pueden haber cambiado.

"¿Qué eres real? ¡De eso hablamos hace exactamente 10 años!"

De repente, en mitad de una conversación con un amigo del pasado mientras nos sumergíamos en una charla sobre la memoria de la IA, o más exactamente por qué "olvida" cosas a mitad de una conversación. El amigo del pasado describió cómo funciona la context window, y yo oí "gestión de memoria RAM". Lo que entra en la ventana de contexto está disponible de inmediato para el modelo. Lo que no entra, para él no existe. Exactamente como la memoria de trabajo en un software normal.

Amigos, todo se repite. No hay nada nuevo bajo el sol y también está pasando ahora con la revolución de la IA.

La ventana de contexto es memoria a todos los efectos: lo que entra en ella está disponible de inmediato para el modelo, y lo que no entra, para él no existe. Exactamente como la memoria de trabajo en un software normal. RAG es exactamente como cargar desde un disco duro y los desafíos que eso conlleva. Resumir una conversación es compresión con pérdida. El Prompt caching es una caché clásica. Una sliding window es un ring buffer. Todos estos conceptos existen desde hace décadas, solo que con nombres nuevos.

Y esto no ocurre solo a nivel de infraestructura. Cada vez que llega una tecnología nueva, volvemos a mantener las mismas conversaciones. Cuando llegó Angular hubo discusiones sobre gestión de estado, separación de responsabilidades y arquitectura de componentes. Exactamente las mismas discusiones que existían años antes en otros contextos. Ahora con la IA es igual: qué guardar, qué tirar, qué indexar, qué recuperar. Preguntas que los ingenieros de software llevan generaciones resolviendo.

Y aquí hay también una herramienta de pensamiento que conviene no perderse. Si entiendes que la ventana de contexto se comporta como memoria de trabajo, puedes predecir de antemano qué funciones llegarán después, porque ya conoces los problemas y las soluciones del mundo clásico del software. Ser un desarrollador senior tiene sus ventajas 🙂 

Lo que cambia aún menos, pero nos engaña mucho, son las prácticas básicas de la ingeniería de software: precisamente porque la IA acelera el desarrollo, hoy son más importantes que nunca. 

Los datos de 2025 y 2026 son claros: el código generado con IA contiene más bugs, el tiempo de review de un PR aumenta significativamente y los problemas de legibilidad aparecen a mayor ritmo. El informe DORA lo mostró mejor que nadie: la IA es un amplificador. Los equipos con procesos sólidos se vuelven más fuertes. Los equipos con procesos débiles se vuelven más débiles.

Escribir código listo para producción con IA es el mismo desafío que sin IA. 
Hacen falta PR pequeños y legibles. Hacen falta principios SOLID para optimizar el contexto del agente que accede al código. Hay que pensar en la escala en producción cuando se llega a miles o millones de clientes, algo para lo que da la sensación de que los modelos aún no tienen suficiente contexto. Hay que planificar y compartir con el equipo para obtener varios puntos de vista, cada persona y su área de especialización, para asegurarnos de cubrir todo lo que realmente no se puede meter en el contexto del agente. 

En resumen, todas las prácticas de trabajo que constituyen la base del buen desarrollo de software no han cambiado. 
Así que la ilusión de no escribir código es cierta solo para la parte de escribir realmente el código. El mantenimiento del código requiere y obliga a una sincronización entre la máquina y el humano, con la aspiración de reducir esta interfaz costosa y lenta mediante capas de Trust elevadas.

La tecnología sí cambia y se renueva, pero los bugs permanecen. A trabajar

Original: https://ofershap.github.io/posts/ai-changes-the-tools-not-the-engineering-problems/
Source: https://www.linkedin.com/posts/ofershap_%D7%9E%D7%94-%D7%90%D7%AA%D7%94-%D7%90%D7%9E%D7%99%D7%AA%D7%99-%D7%A2%D7%9C-%D7%96%D7%94-%D7%93%D7%99%D7%91%D7%A8%D7%A0%D7%95-%D7%9C%D7%A4%D7%A0%D7%99-10-%D7%A9%D7%A0%D7%99%D7%9D-activity-7477950706319208448-Pxzd
Published: 2026-07-01T08:06:21.992000+03:00
