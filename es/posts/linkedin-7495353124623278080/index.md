# ¿Cómo se aseguran de que su archivo .env esté siempre actualizado y de que todo el equipo esté sincronizado con él?

Traducción automática del post original, sin revisión de un traductor humano. Las afirmaciones históricas pueden haber cambiado.

¿Cómo se aseguran de que su archivo .env esté siempre actualizado y de que todo el equipo esté sincronizado con él?
Nuestra solución fue redefinir "qué es un archivo env": no es un archivo que alguien guarda y actualiza a mano, sino un build artifact que se genera solo cada vez que se ejecuta la aplicación.

Durante mucho tiempo nuestra solución para gestionar el env era mala y manual: un mensaje en Slack. 
(Si te sientes identificado, levanta la mano...)
Si alguien añade una nueva variable de entorno, sube el código y tres días después otra persona hace pull, ejecuta y obtiene un fallo por una variable de la que nunca había oído hablar. Y entonces llega el mensaje de siempre o el deambular entre mensajes de Slack. Incluso si se pasa por algún gestor de secretos como bitwarden, se sigue perdiendo tiempo valioso por la falta de sincronización...

En nuestro producto, que ya tiene decenas de servicios (front y back), el problema se vuelve mucho mayor porque cada proyecto tiene su propio env.

Así que nuestra solución fue pasar a la nube: cada servicio tiene hoy un secreto en el Secret Manager de Google que guarda todas las variables de desarrollo local como un objeto JSON. Basta con actualizar un valor en un solo lugar y todo el equipo lo recibe, con historial (y de paso también la posibilidad de volver atrás fácilmente).

Y desde el lado del desarrollador (DevEx), la sincronización dejó de ser un comando que alguien tiene que recordar y pasó a ser una acción automática: escribimos un pequeño executor para Nx y lo definimos como dependencia de cada dev target nuestro, de modo que incluso antes de que la aplicación arranque, Nx ya ha descargado los secretos actualizados y escrito un env nuevo. 

¿Y qué se hace si se quiere hacer un override en local?
También eso lo resolvimos con elegancia: todo lo que se pone en env.local se fusiona por encima de lo que llegó de la nube. Los valores compartidos siguen siendo compartidos, tu equipo sigue siendo tuyo.

Hay un pequeño precio que pagar: cada cierto tiempo hay que refrescar nuestra conexión con GCP (el refresco ocurre automáticamente, pero aun así hay que aprobar la conexión a través del navegador) y las actualizaciones de secretos requieren trabajar con la horrenda interfaz de secretos de Google (para la que también cosí una solución en forma de extensión de navegador que la ordena), pero desde que lo hicimos, "en mi máquina funciona" dejó de ser un problema de variables de entorno.

Si todavía luchan por sincronizar archivos env en el equipo, les recomiendo encarecidamente adoptar esta forma de trabajo: ahorra mucho dolor de cabeza y tiempo valioso de desarrolladores, y enfoca en lo que de verdad importa

Original: https://ofershap.github.io/posts/linkedin-7495353124623278080/
Source: https://www.linkedin.com/posts/ofershap_%D7%90%D7%99%D7%9A-%D7%90%D7%AA%D7%9D-%D7%93%D7%95%D7%90%D7%92%D7%99%D7%9D-%D7%A9%D7%94%D7%A7%D7%95%D7%91%D7%A5-env-%D7%A9%D7%9C%D7%9B%D7%9D-%D7%99%D7%94%D7%99%D7%94-%D7%AA%D7%9E%D7%99%D7%93-activity-7495353124623278080-oV7i
Published: 2026-08-18T08:37:21.837000+03:00
