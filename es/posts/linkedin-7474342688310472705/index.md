# Como líder de un equipo de desarrollo, una de las cosas más útiles que hago últimamente es analizar con IA los Pull Requests de mi equipo.

Como líder de un equipo de desarrollo, una de las cosas más útiles que hago últimamente es analizar con IA los Pull Requests de mi equipo. 

Le pido a Cursor o a Claude Code (conectados a nuestro repo mediante la GitHub CLI) que analicen los PR (es decir, ejecuta realmente gh pr list con comandos de búsqueda) y me devuelvan conclusiones como: 
Rendimiento: analizar el último sprint (o trimestre), quién tocó más el código en cierta área, dónde hay cuellos de botella, quién hace más reviews, quién genera más bugs, etc.
O análisis de fallos: localizar el smoking gun que causó un incidente en producción o un aumento de errores que identificamos en nuestras herramientas de observabilidad. 

Esta capacidad da una imagen clara de lo que hizo cada uno, dónde aportó y dónde se atascó, y me convierte en un gestor mucho más preciso y basado en datos. 

Sigo sosteniéndolo: estamos en una era de transición de ser Data driven a ser AI Driven. Si el análisis de datos y la extracción de conclusiones exigían una inversión de horas o días, estaban reservados a los analistas y servían sobre todo a la gente de producto, hoy cualquier persona, sea cual sea su rol, puede analizar casi sin esfuerzo los datos cercanos a sus necesidades y obtener conclusiones digeridas e inteligentes que le sirven y le afinan.

El último caso que tuve me llevó a escribir esta publicación. En tiempo real vi un fallo en producción, le pedí al modelo que localizara el fallo en los logs de GCP y luego revisara todos los PR de las últimas dos semanas y señalara exactamente qué cambio causó el problema. Una especie de smoking gun que sin IA habría tomado horas encontrar e implicado al menos a un desarrollador, si no a más, en esta investigación.

Cuando hoy se puede simplemente hacer una pregunta en lenguaje natural y recibir una respuesta en segundos, de repente los líderes de equipo tienen una herramienta de gestión que no existía antes. Este cambio de mentalidad (mindset) de tener a mano una herramienta de análisis e investigación y no solo una herramienta de "autocompletado de código" es un valor enorme que nos permite ser supergestores.

Original: https://ofershap.github.io/posts/using-ai-to-analyze-my-teams-pull-requests/
Source: https://www.linkedin.com/posts/ofershap_%D7%91%D7%AA%D7%95%D7%A8-%D7%A8%D7%90%D7%A9-%D7%A6%D7%95%D7%95%D7%AA-%D7%A4%D7%99%D7%AA%D7%95%D7%97-%D7%90%D7%97%D7%93-%D7%94%D7%93%D7%91%D7%A8%D7%99%D7%9D-%D7%94%D7%99%D7%95%D7%AA%D7%A8-%D7%A9%D7%99%D7%9E%D7%95%D7%A9%D7%99%D7%99%D7%9D-activity-7474342688310472705-v1mV
Published: 2026-06-21T09:09:23.465000+03:00
