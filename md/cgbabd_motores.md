# Los motores de lectura

17 de octubre de 2026

Un motor, aquí, es un modelo que recibe textos y devuelve un resultado. Algunos traducen o revisan frases. Otros convierten cada fragmento en una lista de números, llamada vector, que permite buscar pasajes parecidos. Esa segunda operación se llama embedding: no escribe una traducción ni decide por sí sola qué significa una obra.


Los motores de la Destilería: qué se usó, qué está disponible y qué falta probar. Para cada uno: nombre exacto, proveedor, para qué sirve, gratis o pago, límites conocidos y estado. Las fichas de configuración práctica se actualizan con mediciones del 13 de octubre de 2026. Las cuotas citadas conservan la fecha de verificación de su fuente.

Regla de la casa: gratis primero; gasto de centavos solo con autorización expresa.

Regla de acceso: los motores de Google (Gemma, Gemini y los embeddings de Google) se llaman siempre por la API directa de Google con la key gratis de AI Studio, nunca por OpenRouter. Para motores que no son de Google, OpenRouter sí es vía válida: su capa gratis (50 llamadas al día, 20 por minuto) se usa sin restricción; el saldo pago no se gasta.

## Embeddings: en la bóveda

### nemotron-3-embed-1b
- Proveedor: NVIDIA, vía OpenRouter (capa gratis).
- Sirve para: embeddings.
- Gratis. Hasta 256 textos por llamada, 2,048 dimensiones, contexto 33K; el free tier de OpenRouter da 50 llamadas/día y 20/minuto.
- Estado: usado. Macbeth y Arena en la bóveda. Campeón del garaje: ganó las 5 medidas contra todos.

### gemini-embedding-001
- Proveedor: Google, Gemini Developer API (la key de AI Studio).
- Sirve para: embeddings.
- Gratis. 1,000 textos por día por modelo (el panel cuenta textos, no llamadas); reset a las 03:00; 3,072 dimensiones.
- Estado: usado. Macbeth y Lear en la bóveda. Encontró solo los picos de sueño (II.2, V.1).

### gemini-embedding-2
- Proveedor: Google, Gemini Developer API.
- Sirve para: embeddings.
- Gratis, misma cuota diaria por modelo que 001; 3,072 dimensiones.
- Estado: usado. Lear y Arena completos en la bóveda (Arena el 13 de octubre, Lear el 16 de octubre). Las corridas se planifican para que un corpus quepa en días enteros de cuota.

### pplx-embed-v1-0.6b
- Proveedor: Perplexity.
- Sirve para: embeddings.
- Pago, centavos: Macbeth entero costó ~$0.00009.
- Estado: usado. Macbeth en la bóveda. Escolta: segundo en 4 de 5 medidas.

### voyage-4, voyage-4-lite, voyage-4-large
- Proveedor: Voyage AI.
- Sirve para: embeddings.
- Gratis con saldo inicial: la documentación vigente (docs.voyageai.com/docs/pricing, verificada el 17 de octubre de 2026) regala los primeros 200 millones de tokens por cuenta para voyage-4-large, voyage-4 y voyage-4-lite; el panel de la cuenta mostraba 2M el 4 de octubre, así que conviene confirmar el saldo en el panel antes de una corrida grande. Cuenta sin tarjeta: 3 RPM, 10K TPM. Con tarjeta el límite sube a 2,000 RPM, pero vincularla exige un pago mínimo de $5.
- Estado: usados. Los tres en la bóveda de Macbeth; voyage-4-large ganó las dos medidas de vecinos y el 17 de octubre vectorizó completo el King (On Writing, 4,253 frases, 99,199 tokens según el uso informado por la API, en 14 llamadas dentro del límite sin tarjeta).

### qwen3-embedding-8b
- Proveedor: Alibaba, vía OpenRouter.
- Sirve para: embeddings.
- Pago, centavos (~$0.0002 Macbeth); 4,096 dimensiones.
- Estado: usado. Macbeth en la bóveda. Enterrado por su regla: perdió 3-2 contra Perplexity.

### text-embedding-3-small
- Proveedor: OpenAI.
- Sirve para: embeddings.
- Pago, centavos (~$0.00045 Macbeth).
- Estado: usado. Macbeth en la bóveda.

### lfm-2.5-embedding-350m
- Proveedor: Liquid, vía OpenRouter (capa gratis).
- Sirve para: embeddings.
- Gratis. 128 textos por llamada, 1,024 dimensiones, contexto de solo 512 tokens; ojo: el free tier puede retener los inputs.
- Estado: usado. Macbeth y Arena en la bóveda (se conserva como motor más, sin medallas).

### Cohere Embed (embed-v4.0)
- Proveedor: Cohere, API propia.
- Sirve para: embeddings.
- Trial key gratis, sin tarjeta: Embed 2,000 inputs/minuto, tope general 1,000 llamadas/mes por key, máximo 96 textos por llamada. embed-v4.0: 1,536 dimensiones por defecto (también 256/512/1024), contexto 128K, texto e imágenes. Los embedding_types int8 y uint8 corren con trial key.
- Modelos más nuevos: embed-v5.0-pro y embed-v5.0-fast (2,048 dimensiones por defecto); la documentación no dice si están habilitados para keys trial.
- Bonus traducción: Aya Expanse (chat, 23 idiomas) corre con la misma trial key dentro del tope mensual.
- Estado: usado. Arena completo en la bóveda (1,853/1,853, verificado el 13 de octubre), dentro del tope trial mensual.

## Generación y traducción: en uso

### gemma-4-26b-a4b-it
- Proveedor: Google, Gemini Developer API directa, capa gratuita.
- Uso: traducción teatral por IDs.
- Configuración: `streamGenerateContent?alt=sse`; lectura SSE por evento completo; `temperature: 0.2`, `maxOutputTokens: 8192`, `thinkingConfig.thinkingLevel: minimal`; ritmo normal de 120 segundos desde el inicio; tras HTTP 500 rápido, 30 segundos desde el cierre; tras duración mayor de 90 segundos o corte por plazo, 30 segundos desde el cierre; plazo global de 110 segundos; conservación de objetos JSON completos y válidos por ID.
- Tamaño completo medido: 50 frases. Paquetes completos en 62,26; 65,34; 73,70 y 74,68 segundos. En repesca: 50 frases recuperadas en 60,72 segundos y 50 en 64,28 segundos.
- Tamaño operativo: 50 frases. Prueba de 100: 10 llamadas, 64 frases recuperadas en una respuesta parcial y 9 respuestas HTTP 500; resultado de paquetes completos: 0/10. Medición inicial: corte de 85 segundos; siguientes llamadas: plazo de 110 segundos.
- Estado: cobertura de Macbeth completa, 1.479 traducciones guardadas. Segunda repesca: 236 frases recuperadas; paquetes de 50 completos en 76,19; 61,94; 61,53 y 74,96 segundos, y cierre de 36 en 56,65 segundos. Validación de IDs y recuperación de delimitadores JSON con el texto original de salida preservado. La revisión literaria es una etapa aparte.

### gemma-4-31b-it
- Proveedor: Google, Gemini Developer API directa, capa gratuita.
- Uso: traducción teatral por IDs.
- Configuración: `streamGenerateContent?alt=sse`; lectura SSE por evento completo; `temperature: 0.2`, `maxOutputTokens: 16384`, `thinkingConfig.thinkingLevel: minimal`; paquetes de hasta 50 IDs; plazo global de 100 segundos; intervalo de 90 segundos; conservación de objetos completos por ID.
- Medición de hoy: paquetes completos de 50 frases en 71,22 y 71,42 segundos. Salidas parciales útiles: 13 en 63,65 segundos, 29 en 93,38 segundos y 31 al corte de 100 segundos.
- Estado: 234 traducciones guardadas de Lear en la medición comunicada por su responsable.

### gemini-3.5-flash-lite
- Proveedor: Google, Gemini Developer API, capa gratuita.
- Uso: crítica y diagnóstico de traducciones por IDs.
- Configuración: POST `generateContent`; autenticación `x-goog-api-key`; `responseMimeType: application/json`, `temperature: 0.2`; plazo de 120 segundos; cadencia de al menos 15 segundos entre llamadas.
- Tamaño completo medido: 100 frases. 14 lotes de 100 en 15,1 a 78,0 segundos; media 31,0 segundos; IDs 100/100. En el conjunto de la crítica: 15 de 16 lotes completos. Lote de 10: 36,5 segundos.
- Estado: listo para crítica por lotes de 100. Cuota citada en su panel: 15 RPM y 250K TPM.

### gemini-3.7-flash → gemini-3.8-flash
- Proveedor: Google, Gemini Developer API.
- Enrutamiento vigente: el identificador `gemini-3.7-flash` dirige las solicitudes a `gemini-3.8-flash`, según la ficha oficial y la nota del 8 de octubre de 2026.
- Uso medido con el identificador solicitado `gemini-3.7-flash`: crítica comparada por lotes de 10 a 50 frases.
- Configuración medida: POST `generateContent`; autenticación `x-goog-api-key`; `responseMimeType: application/json`, `temperature: 0.2`; plazo de 120 segundos; cadencia de al menos 15 segundos entre llamadas.
- Medición de hoy: 10 frases en 16,3 segundos; 50 en 56,6 segundos. Registro de pensamiento: 1.640 y 4.001 tokens, respectivamente.
- Estado: herramienta en espera para usos puntuales; el tamaño completo medido es 50 frases. Cuota de referencia del proyecto: 20 llamadas al día.

### antigravity-preview-09-2026
- Proveedor: Google, Interactions API; modelo base predeterminado `gemini-3.8-flash`.
- Uso: revisión técnica con búsqueda y trabajo por pasos.
- Configuración medida: POST `https://generativelanguage.googleapis.com/v1beta/interactions`; autenticación `x-goog-api-key`; `Api-Revision: 2026-05-20`; `agent: antigravity-preview-09-2026`, `environment: remote`, `stream: true`; plazo global de 110 segundos; lectura SSE por evento; conservación de deltas de texto y metadatos de interacción.
- Medición de hoy: consulta técnica completa, HTTP 200 y estado `completed` en 92,48 segundos. Uso informado: 92.229 tokens totales, 84.130 de entrada, 50.529 de entrada en caché, 2.459 de salida, 5.640 de pensamiento y 3 búsquedas de Google.
- Estado: acceso y respuesta completa verificados con esta configuración. Control de consumo: registro de uso por interacción y autorización de gasto por tarea.

## Generación: históricos del mapa (tribunal, ladrillazos, empaquetados)

- gemini-3.7-flash (Google, gratis, 20 RPD): campeón histórico del tribunal (9/10); el único que vio el sueño en ambos extremos del arco.
- gemini-3.8-flash (7/10) y gemini-3.6-flash (1/10): 20 RPD cada uno, muros 503 frecuentes y los fallos cuentan.
- gemini-3.5-flash: ladrillazo completo (41.7K tokens).
- gemini-3-flash-preview: completo pero leyó menos. gemini-2.5-flash: 404, cerrado a usuarios nuevos.
- antigravity-preview: ficha operativa vigente en la sección de configuración, con el identificador `antigravity-preview-09-2026`.
- Pesados de OpenRouter para escritura: "fueron un desastre" (su veredicto).

## Por probar

### Jina (jina-embeddings-v3, jina-embeddings-v4)
- Proveedor: Jina AI.
- Sirve para: embeddings.
- Gratis: key auto-generada con 10M tokens iniciales, sin tarjeta; 100 RPM y 100K TPM en free key. No hay recarga mensual: agotados los tokens, se compran paquetes.
- Modelos: la familia actual es v5 (febrero de 2026): v5-text-small y v5-text-nano, multilingües, licencia CC-BY-NC-4.0, y v5-omni (texto, imagen, audio y video en un solo espacio). Siguen disponibles v3 (multilingüe, 89 idiomas, castellano incluido, 1,024 dimensiones, contexto 8K) y v4 (más capaz pero más lento; gratis vía API por licencia no comercial Qwen Research License).
- Estado: por probar.

### Mistral (mistral-embed)
- Proveedor: Mistral, La Plateforme.
- Sirve para: embeddings.
- Free tier existe, pero la key no sirve hasta pasar la verificación de la cuenta (típicamente teléfono) y los límites por modelo solo se ven en la consola.
- Estado: por probar, prioridad menor (alta fricción de alta).

## Fuentes

- docs.cohere.com/docs/models y docs.cohere.com/reference/embed (modelos, 96 textos por llamada, embedding_types)
- docs.cohere.com/docs/rate-limits y cohere.com/pricing (límites trial, key auto-generada)
- jina.ai/embeddings (free key, límites) y jina.ai/news/jina-embeddings-v5-text-distilling-4b-quality-into-sub-1b-multilingual-embeddings (familia v5)
- docs.voyageai.com/docs/pricing (200 millones de tokens gratis por cuenta en la familia voyage-4; verificado el 17 de octubre de 2026)
- docs.mistral.ai/admin/billing-usage/usage-limits (free mode y verificación)
- La bóveda del Drive (motores archivados por obra) y las bitácoras del garaje para los motores ya usados

## Fuentes de configuración operativa (13 de octubre de 2026)

- https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api
- https://ai.google.dev/gemini-api/docs/antigravity-agent
- https://ai.google.dev/gemini-api/docs/interactions/streaming
- https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash
- https://ai.google.dev/gemini-api/docs/changelog
- Mediciones de traducción 26B y prueba Antigravity; registros de los responsables de Lear31B y críticaGemini, comunicados el 13 de octubre.

Este registro es el censo completo del taller, al 17 de octubre de 2026. Distingue lo usado, lo detenido y lo que aún no se ha probado. No contiene claves.

© 2026 Osmancito
