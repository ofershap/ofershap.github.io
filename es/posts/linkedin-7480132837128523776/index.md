# Casi rompemos producción por una actualización en la que nadie de nuestro lado se fijó...

Casi rompemos producción por una actualización en la que nadie de nuestro lado se fijó...
Una de las librerías en las que nos apoyamos (Vercel AI SDK) sacó una versión con breaking changes y, cuando fuimos a implementar una solución que solo existía en la versión más avanzada, nos dimos cuenta de que teníamos un problema mucho más amplio que actualizar el código. Es algo que ocurre con todas las librerías y SDK, con modelos que de repente dejan de tener soporte, y además hay funciones nuevas en la era de la IA (en cuyo centro estamos) que salen con alta frecuencia y se nos escapan.

Así que, en lugar de solo actualizar una versión y arreglar hacia atrás, Ori Shavit, el desarrollador del equipo, aportó una salida genial: construyó una automatización que nos envía una vez por semana (los domingos) un mensaje en Slack con todo lo que cambió en las librerías y los modelos de los que depende el equipo. Qué hay de nuevo, qué dejó de tener soporte, qué se anunció y vale la pena tener en cuenta.

Así detectamos, por ejemplo, un modelo que dejará de tener soporte en diciembre y creamos una tarea para ocuparnos pronto, y así nos mantenemos al día de todas las funciones que salen y que pueden mejorar el proyecto.

Delegar en un agente el trabajo de seguir las actualizaciones es un gran ejemplo de cómo se puede aprovechar la IA en los equipos de desarrollo no solo para completar código, sino también para la sincronización y la actualización continua.

Original: https://ofershap.github.io/posts/an-agent-that-tracks-dependency-changes/
Source: https://www.linkedin.com/posts/ofershap_%D7%9B%D7%9E%D7%A2%D7%98-%D7%A9%D7%91%D7%A8%D7%A0%D7%95-%D7%90%D7%AA-%D7%94%D7%A4%D7%A8%D7%95%D7%93%D7%A7%D7%A9%D7%9F-%D7%91%D7%92%D7%9C%D7%9C-%D7%A2%D7%93%D7%9B%D7%95%D7%9F-%D7%A9%D7%90%D7%A3-%D7%90%D7%97%D7%93-activity-7480132837128523776-T0Kf
Published: 2026-07-07T08:37:22.519000+03:00
