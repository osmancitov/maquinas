# Los motores de lectura

13 de octubre de 2026

Un motor, aquí, es un modelo que recibe textos y devuelve un resultado. Algunos traducen o revisan frases. Otros convierten cada fragmento en una lista de números, llamada vector, que permite buscar pasajes parecidos. Esa segunda operación se llama embedding: no escribe una traducción ni decide por sí sola qué significa una obra.

## Traducir y revisar

- **Gemma 4 26B, de Google**: completó las 1.479 frases de Macbeth. En las pruebas del taller, los paquetes de 50 dieron resultados completos; los de 100 no. La cobertura quedó cerrada, pero la revisión literaria de las frases recuperadas sigue en curso.
- **Gemma 4 31B, de Google**: se probó con Lear. La corrida se detuvo por sus resultados insuficientes. No está trabajando ahora.
- **Gemini 3.5 flash-lite, de Google**: revisa traducciones en grupos de 100 frases. Terminó la revisión de la tercera voz de Macbeth y está revisando las 236 frases recuperadas de Gemma. Sus notas orientan la lectura: una puntuación alta no sustituye la revisión humana.
- **Gemini Flash**: se hicieron pruebas de lectura y de crítica con varios modelos. Los ensayos registrados como 3.7 y 3.8 quedan en espera; no se mezclan sus notas con las de flash-lite.
- **Antigravity**: una prueba técnica obtuvo una respuesta completa. Se conserva como ensayo, no como una tarea en ejecución.

## Buscar semejanzas entre pasajes

Los siguientes modelos se usaron para producir vectores y comparar fragmentos. Sus resultados pertenecen a obras y pruebas concretas, no a una clasificación universal.

- **NVIDIA Nemotron 3 Embed 1B**: usado con Macbeth y El libro de arena. Dio buenos resultados en las comparaciones del taller.
- **Google Gemini Embedding 001 y 2**: usados con Macbeth, Lear y El libro de arena, según el modelo. Las corridas se repartieron de acuerdo con los límites de uso disponibles.
- **Perplexity PPLX Embed 0.6B**: usado con Macbeth; destacó en varias comparaciones de semejanza.
- **Voyage 4, 4 lite y 4 large**: los tres se probaron con Macbeth. La variante large destacó al buscar pasajes vecinos.
- **Alibaba Qwen3 Embedding 8B** y **OpenAI text-embedding-3-small**: usados con Macbeth y conservados para comparación.
- **Liquid LFM 2.5 Embedding 350M**: usado con Macbeth. Su límite de texto por fragmento es menor que el de otros modelos probados.

## Candidatos

Cohere, Jina y Mistral figuran como opciones para futuras pruebas de embeddings. Estar en esta lista no significa que ya hayan sido usados ni que haya una corrida programada.

## Costos y alcance

Se da prioridad al acceso gratuito. Algunas pruebas de embeddings usaron servicios de pago con autorización puntual; eso no es permiso para un gasto nuevo. Los límites de uso cambian por proveedor y cuenta, por lo que se verifican antes de cada corrida.

Este registro resume el censo del taller consultado el 13 de octubre de 2026. Distingue lo usado, lo detenido y lo que aún no se ha probado. No contiene claves ni instrucciones de acceso.

Osmancito, con la asistencia de Instinct
