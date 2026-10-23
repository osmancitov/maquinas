# Todas las reglas

Todas las reglas vigentes tal como están guardadas en la memoria de Instinct, cada una numerada con su fecha y su fuente, agrupadas por tema. Estado al 23 de octubre de 2026. Sirve para marcar cuáles están obsoletas.

## Escritura pública

56. Toda escritura pública debe cumplir con [dominio-cero.md](https://github.com/osmancitov/osmancitov.github.io/blob/main/md/dominio-cero.md). *(2026-10-23)*
2. Las imágenes adicionales dentro de una entrada se nombran aammdd_titulo-de-la-entrada_titulo-de-la-imagen.jpg: la fecha en seis cifras es la de la entrada, la misma para todas sus imágenes. *(2026-10-22 · escritura-publica)*
3. Las URL largas no aparecen como texto visible del enlace (rompen el scroll horizontal del teléfono): se usa una etiqueta corta. *(escritura-publica)*
4. Listas en las páginas índice: lo más nuevo arriba; a igual fecha, orden por lógica de la obra. *(escritura-publica)*

## Journal y títulos

13. Parejas: «esto y esto» - título de dos palabras, cada una nombrando lo que hace una parte. *(journal-y-titulos)*
14. La prosa lírica es ley de la casa. *(2026-10-05 · journal-y-titulos)*
17. Títulos del Taller: artículo más sustantivo, como un plato en un menú; de 3 a 6 palabras, sin dos puntos ni gerundios, de largo parecido; los créditos van dentro del cuaderno, no en el título de la lista. *(2026-10-06 · journal-y-titulos)*


## El sitio

21. Navegación en árbol, no en malla: cada puerta lleva a las de arriba y abajo en el árbol; cada índice tiene opción de bajar al repo y cada repo de subir al html. *(2026-10-05 · hotel-sitio)*
22. Portada muda + parlanchina: cada repo tiene dos html en la raíz -`index.html` (solo la imagen; un clic lleva a la parlanchina) y el html con el nombre del repo (el texto del README y las entradas; un clic en su imagen lleva al repo). Las cinco imágenes del lobby abren la parlanchina de cada sala. *(2026-10-09 · hotel-sitio)*
23. Los enlaces html se quedan en html: si hay versión HTML de la entrada, se enlaza directo a esa, sin dobles enlaces «HTML»/«markdown»; las entradas sin html enlazan al visor de GitHub del .md. *(2026-10-09 · hotel-sitio)*
24. Enlaces de vuelta: cada parlanchina termina con «volver» a la portada del lobby; el «volver» de una vitrina va a la parlanchina de su sala; el pie de una entrada vuelve a la parlanchina de su sala. *(2026-10-09 · hotel-sitio)*
27. La palabra de enlace del lobby es «Lobby», no «GitHub»; sin título «osmancito» (ya está implícito en la URL). *(hotel-sitio)*
28. El panel About de cada repo lleva el enlace al sitio; los topics/tags se quitaron por bloat. *(hotel-sitio)*
29. Cada página y su README se espejan: el texto de la parlanchina es el texto del README (qué es la sala, de dónde viene el nombre, lista de entradas). *(2026-10-09 · hotel-sitio)*
30. Los README abren con la fila Lobby · Destilería · Taller · Journal · Capilla, enlazando README con README y la sala actual en negrita; después, la palabra de la sala definida. Sin imágenes en los README: la navegación va primero. Los README padres enlazan a los README de las carpetas hijas. *(2026-10-06 · hotel-sitio)*
31. Pelado hasta el hueso: máxima simpleza, el HTML mínimo, quitar todo lo innecesario; filosofía Jenga: quitar hasta que ya no se pueda quitar nada. *(2026-10-06 · hotel-sitio)*
33. theme-color: rojo puro #FF0000 en el lobby, como prueba de la barra del navegador del teléfono; resultado sin confirmar. *(2026-10-07 · hotel-sitio)*
35. El peso se mide y se celebra («que los números sean el bautizo»): una página pesada roba más; debe correr en «una mini pdm». *(hotel-sitio)*
36. La vitrina de la bodega-103 conserva su aspecto marrón viejo a propósito: «testimonio de una época», «referencia de museo»; las bodegas nuevas usan el estilo vigente de la casa. *(2026-10-09 · hotel-sitio)*
37. Actualizar el README con cada nueva entrada en cualquiera de los repos. *(hotel-sitio)*
38. Las listas van de lo más nuevo a lo más viejo, como un blog; la numeración queda pegada a las entradas. *(hotel-sitio)*
40. Patrón de sala: todas las salas siguen el mismo patrón; ninguna lo rompe. *(2026-10-07 · hotel-sitio)*
42. «quitar quitar y quitar y seguir quitando»: recorta taglines, citas, divisores y pies con agresividad; palabras de pie llanas («volver», «Subir»). *(hotel-sitio)*
43. No llamar «sociales» a las imágenes, ni en prosa ni en nombres de archivo: ese es el término interno de GitHub. *(hotel-sitio)*
44. Checklist de sala nueva: imagen de puerta, JPG al 75 %, og tags, listado en el lobby, fila de navegación en cada README, sección de entradas en el README. *(2026-10-07 · hotel-sitio)*
45. Imágenes de puertas: hechas con el Pintor de Imágenes, cada puerta con su propio estilo de pintor, puesta como Social preview del repo y og:image; JPG al 75 %. *(2026-10-07 · hotel-sitio)*
47. Las puertas se quedan en la paleta oscura y cálida de la casa (para cambiar una se sobrescribe el mismo archivo); los dibujos de las entradas son libres: «de día de noche, con total libertad». *(2026-10-16 · hotel-sitio)*
49. Toda entrada visible en HTML tiene su propia página HTML: ningún clic salta al visor de Markdown de GitHub. MD y HTML son gemelos («morochos, gemelos, espejos»): siempre cambian juntos. *(2026-10-13 · hotel-sitio)*
50. Páginas movidas o reemplazadas: sin redirecciones y sin rastro -«que borres la vieja, que no dejes rastro»-; cuando una página se muda de repo, cada enlace interno al lugar viejo se reescribe. Una página borrada puede mencionarse en el Historial como texto, sin enlace. *(2026-10-13 · hotel-sitio)*
52. Títulos de obras en Title Case («El Libro de Arena», «El Otro»): en títulos de página, og tags, índices de sala y prosa; las citas y los nombres de archivo quedan intactos. *(hotel-sitio)*
53. Él navega el sitio, no las rutas: mientras trabaja una página va a la sala y busca la entrada; decir «está en Bodega 110» es suficiente. *(2026-10-13 · hotel-sitio)*




## Commits

55. Identidad de commits. Todo commit, de cualquier repositorio de osmancitov, se firma con el correo personal de Osmancito como autor y como committer. Ningún agente ni proceso usa otra identidad ni la configura por su cuenta; si no puede firmar así, se detiene y avisa. *(2026-10-19)*
