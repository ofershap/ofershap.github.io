# Todos hablan de background agents; yo construí un foreground agent.

Traducción automática del post original, sin revisión de un traductor humano. Las afirmaciones históricas pueden haber cambiado.

Todos hablan de background agents; yo construí un foreground agent.
Cursor, ChatGPT y otros ofrecen la opción de ejecutar un "agente de código" que corre de forma autónoma entre bastidores. Esto tiene varios problemas: uno es que no se ve lo que realmente se está haciendo, el segundo es que requiere aprobaciones de Privacy, y el tercero es que tiene costes adicionales.

Como ya trabajo habitualmente con Cursor y necesitaba ejecutar una tarea compleja, encontré una solución que me ahorraba tener que sentarme a aprobar cada paso del proceso de Cursor,
y no fue nada complicado.

Abrí las Developer Tools de Cursor desde el menú Help, le pedí a ChatGPT un pequeño script en JS y lo pegué en la consola. 

El script: cada vez que aparecían mensajes pidiéndome aprobar algo ("accept", "run", "25 tools limit"), hacía clic en ellos por mí.

El método: copié el HTML que representaba el área del botón y pedí en el prompt que escribiera un script que cada 15 segundos comprobara si aparece y, si es así, haga clic. También me gusta explicar para qué es: "para poder pegarlo en las Devtools de Cursor". Siempre ayuda dar contexto a la IA. 

El resultado: gané continuidad de trabajo, casi idéntica a un Background agent, pero bajo mi control.

Así que en lugar de usar un Agent que está "en segundo plano", construí uno que está simplemente frente a mí: hace clic en mi nombre y me permite fluir de verdad.

Es divertido reingenierizar los límites de la propia interfaz, y asombroso ver que funcionó sin problemas: unos minutos después volví al ordenador y descubrí que mi tarea se había completado con éxito y por completo.

Una última nota pequeña pero importante: esto es genial para proyectos pequeños y para desarrollo al estilo vibe-coding (sin necesidad de vigilar la calidad del código resultante), pero puede ser destructivo para cambios en proyectos existentes. 
Además, puede descontrolarse muy rápido y gasta tokens.
Por eso, si imitan el método, úsenlo con juicio y cuidado, y aunque corra solo, vigilen todo lo que hace.

Original: https://ofershap.github.io/posts/linkedin-7355484666633641984/
Source: https://www.linkedin.com/posts/ofershap_%D7%9B%D7%95%D7%9C%D7%9D-%D7%9E%D7%93%D7%91%D7%A8%D7%99%D7%9D-%D7%A2%D7%9C-background-agents-%D7%90%D7%A0%D7%99-%D7%91%D7%A0%D7%99%D7%AA%D7%99-activity-7355484666633641984-KicT
Published: 2025-07-28T09:30:02.822000+03:00
