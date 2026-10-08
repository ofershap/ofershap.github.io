# Aquí tienes un resumen (TL;DR) en hebreo: el equipo de Lovable publicó un post técnico en su blog sobre cómo trasladaron toda su plataforma para que funcione usando... ¡Lovable! Reconstruyeron todo el proyecto para que funcione sobre su propia infraestructura.

Aquí tienes un resumen (TL;DR) en hebreo: el equipo de Lovable publicó un post técnico en su blog sobre cómo trasladaron toda su plataforma para que funcione usando... ¡Lovable! Reconstruyeron todo el proyecto para que funcione sobre su propia infraestructura. 

El post es largo y está en inglés, pero aquí va su resumen:

La empresa Lovable trasladó su sitio principal de Next.js a TanStack Start y ahora lo aloja exactamente como cualquier sitio creado con ellos.

La razón principal: Dogfooding, usar ellos mismos la infraestructura que venden y descubrir los problemas antes que los usuarios.
* La migración llevó medio año aproximadamente. En ese tiempo el código pasó de 350 mil a más de 850 mil líneas.
* En lugar de un cambio brusco, ejecutaron Next.js y TanStack en paralelo y fueron moviendo grupos de routes gradualmente.
* Hicieron que aproximadamente el 97% del código fuera compartido e independiente del framework. Una pequeña capa de adapters lo adaptaba a cada framework.
* Un solo desarrollador llevó a cabo casi toda la migración con ayuda de un grupo de AI agents que escribieron PRs, comprobaron la compatibilidad e identificaron código nuevo que no se podía migrar.
* Cada grupo de routes pasó por un rollout gradual: interno, 1% de los usuarios y luego hasta el 100%.
* Hubo un incidente grave en el que la tasa de errores saltó a cerca del 50% por exceder el límite de memoria de Cloudflare Workers. 
La lección: medir memoria y rendimiento desde el principio y no ignorar ni siquiera un 0,1% de errores.
* Usar TanStack Start les dio un entorno de desarrollo local significativamente más rápido y ligero:
unos 10 segundos y 1,5GB de RAM.
Frente a unos 70 segundos y 8GB en Next.js.

Afirman que los AI agents tienen más éxito con TanStack porque el conocimiento sobre él es pequeño pero coherente. Next.js tiene muchas versiones y enfoques contradictorios.

La desventaja: en una app grande TanStack requiere muchos ajustes de bundling personalizados. Ellos tienen 17 plugins personalizados.

El resultado:
* La mediana de TTFB mejoró un 49%.
* El build de producción bajó de más de 12 minutos a 6-9 minutos.

La mayor ventaja: ahora los empleados no técnicos pueden editar lovable.dev usando la propia Lovable.
(En lugar de que los desarrolladores se ocupen de cada funcionalidad y cada pequeño cambio, test A/B o cambio de diseño).

El punto central: la migración gradual, el código compartido, el rollout controlado y los AI agents permitieron a un solo desarrollador llevar a cabo una migración enorme que antes probablemente habría requerido varios equipos.

Así que si construyo en Lovable un sistema para construir sitios web, entonces construyo usando un sistema para construir sitios web que se asienta sobre un sistema para construir sitios web, un sistema para construir sitios web... y si ustedes construyen sobre el sistema que construyo yo, entonces... bueno, ya lo entienden


El artículo original: https://lnkd.in/dtfsqhKx

Original: https://ofershap.github.io/posts/linkedin-7500903183968477184/
Source: https://www.linkedin.com/posts/ofershap_how-we-migrated-lovabledev-away-from-nextjs-activity-7500903183968477184-nJJP
Published: 2026-09-02T16:11:19.100000+03:00
