# Un concepto genial que conviene conocer: Google publicó como código abierto cómo trabajan en Stitch (su herramienta de diseño). Su idea: separar la capa de UI de la capa de lógica de tal manera que un agente pueda usarla fácilmente y con menos fallos.

Traducción automática del post original, sin revisión de un traductor humano. Las afirmaciones históricas pueden haber cambiado.

Un concepto genial que conviene conocer: Google publicó como código abierto cómo trabajan en Stitch (su herramienta de diseño). Su idea: separar la capa de UI de la capa de lógica de tal manera que un agente pueda usarla fácilmente y con menos fallos. 

¿Cómo lo hicieron? 
Quien recuerde la época de Microsoft .NET sabrá que tenían una idea parecida de separar las capas con un archivo xml que representa la ui, y en Android sigue funcionando así; ahora, para agentes, usan Markdown para representar los elementos visuales (archivos md) y básicamente construyen una capa de UI basada en texto que la describe.

Cuando la capa de interfaz visual está lista (las descripciones, el "storybook" que la muestra), lo único que le queda al agente es unir las piezas en una sola lógica, colocar los elementos en los lugares correctos de la pantalla y conectarles la business logic.

Quien se dedica a construir sistemas web sabe que uno de los desafíos es lograr que la interfaz se vea y funcione bien y no sea chapucera (sloppy), y que a la IA le cuesta muchísimo, por no hablar de depurarla (debug), así que la solución que proponen y publican para nosotros puede ser un trampolín para interfaces de calidad que se construyen con más facilidad y con menos fallos y alucinaciones mediante IA

Si te interesa profundizar y ver el repo, este es el enlace:

Original: https://ofershap.github.io/posts/how-google-stitch-describes-ui-for-ai-agents/
Source: https://www.linkedin.com/posts/ofershap_stitchs-designmd-format-is-now-open-source-activity-7457656988970258432-X-jV
Published: 2026-05-06T08:06:22.737000+03:00
