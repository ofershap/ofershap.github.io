# ¡Increíble! Un tipo llamado Matt Shumer publicó un vídeo de un juego de disparos que parece Call of Duty, construido por completo con un solo prompt con Claude Opus 5, sin ningún asset externo.

Traducción automática del post original, sin revisión de un traductor humano. Las afirmaciones históricas pueden haber cambiado.

¡Increíble! Un tipo llamado Matt Shumer publicó un vídeo de un juego de disparos que parece Call of Duty, construido por completo con un solo prompt con Claude Opus 5, sin ningún asset externo.

El vídeo recibió casi cuatro millones de visualizaciones(!) y mucha gente estaba segura de que era falso. Nadie saca un juego así con un solo prompt. Así que Shumer hizo lo más evidente y publicó todo el prompt y todo su código. 

Su prompt es realmente interesante porque es lo contrario de lo que todos aprendimos a hacer: en lugar de definir exactamente qué es bueno y detallar criterios, escribió de la forma más general posible: "Construye un juego de disparos de nivel Call of Duty, que sea utterly perfect, cada detalle con calidad AAA, desde las texturas hasta la física."

La calidad no viene de esa frase (finjan sorpresa). Viene *de la estructura* que da a sus agentes que ejecutan la tarea: 

- El agente principal divide el juego en partes pequeñas: el arma, las manos, la iluminación, el movimiento, el comportamiento de los enemigos, y a cada parte le asigna un agente constructor y un agente revisor distintos. 
- El agente revisor recibe un contexto limpio, sin todas las explicaciones del constructor sobre por qué hizo lo que hizo, y compara el resultado con imágenes reales de juego de Call of Duty en una prueba ciega. Solo aprueba si lo que salió es realmente mejor.

Shumer lo llamó Gauntlet Loop. La diferencia con la Reflection normal, en la que simplemente le pides al modelo que se revise y se mejore, es la separación. 

Un agente constructor tiende a ser indulgente con su propio trabajo, porque recuerda por qué tomó cada decisión y le resulta fácil justificar un resultado mediocre. Un agente nuevo con un contexto limpio y un listón externo simplemente no mantiene ese supuesto.

Desde que publicó el prompt, en un día la gente construyó con él juegos espaciales, carreras de karts y más juegos de disparos de una calidad descomunal. Shumer dice que lo usa en casi todos los proyectos en los que trabaja, y no solo para juegos. 

¿Quieres leer y ver más? Aquí:

Su tuit: https://lnkd.in/dEdgEjFN 

Su artículo: https://lnkd.in/dMikfdfe

Original: https://ofershap.github.io/posts/how-the-gauntlet-loop-built-a-game-from-one-prompt/
Source: https://www.linkedin.com/posts/ofershap_%D7%9C%D7%90-%D7%A0%D7%AA%D7%A4%D7%A1-%D7%91%D7%97%D7%95%D7%A8-%D7%91%D7%A9%D7%9D-%D7%9E%D7%90%D7%98-%D7%A9%D7%95%D7%9E%D7%A8-%D7%A4%D7%A8%D7%A1%D7%9D-%D7%95%D7%99%D7%93%D7%90%D7%95-%D7%A9%D7%9C-activity-7489553411802198016-kmG2
Published: 2026-08-02T08:31:22.547000+03:00
