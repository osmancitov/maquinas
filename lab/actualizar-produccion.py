#!/usr/bin/env python3
"""Genera las dos páginas: Estado actual (desde md/pendientes.md) y Trabajos realizados (desde md/cgbabd_historial.md).

FUENTES (no hay carpeta data/ ni json):
  md/pendientes.md        Estado actual. Se edita a mano durante el día; el bloque "## Hecho hoy" es lo logrado hoy.
  md/cgbabd_historial.md  Trabajos realizados. Cada trabajo es un bloque "### Título" con "fecha. detalle" y, si hay, "[Leer](url)".
                          Al final tiene un bloque oculto <!-- BORRADOR-DEL-DIA ... --> con los trabajos de hoy, aún sin publicar,
                          una línea por trabajo: "AAAA-MM-DD | título | detalle | url (opcional)".

DURANTE EL DÍA
  Cada trabajo terminado se anota en dos sitios: como viñeta en "## Hecho hoy" de md/pendientes.md, y como línea del
  borrador del día en el historial (con --anota, ver abajo). El historial publicado no muestra el borrador.

PROCEDIMIENTO DE MEDIANOCHE (00:00 UTC-4, el día que termina es el de ayer)
  1. git pull --rebase origin main
  2. Revisar el borrador: que tenga todo lo terminado ese día. Lo que falte se añade con
       python3 lab/actualizar-produccion.py --anota "Título" "Detalle en una o dos frases" ["url"] --fecha AAAA-MM-DD
  3. Probar sin escribir:  python3 lab/actualizar-produccion.py --cierra-dia --dry-run
  4. Cerrar el día:        python3 lab/actualizar-produccion.py --cierra-dia
     Esto hace: pasa las líneas del borrador al principio del historial como bloques con su fecha, vacía el borrador,
     deja "## Hecho hoy" de Estado en "- Nada todavía." y regenera los md y html de las dos páginas.
  5. Contadores y bloque "Corriendo ahora"/"Pendiente de Osmancito": ajustarlos a mano en md/pendientes.md antes del paso 4
     si cambian; la línea "Actualizado:" se reescribe sola con la hora UTC-4.
  6. git add -A && git commit -m "Cierra el día" && git push (token de Drive .github_key, sin espacios, nunca impreso)
     y comprobar las dos páginas en vivo.
Sin opciones, solo regenera las páginas desde los md (no mueve nada).
"""
import argparse, html, re
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description='Regenera Estado actual y Trabajos realizados; ver cabecera para el cierre del día.')
p.add_argument('--pendientes',type=Path,default=root/'md/pendientes.md')
p.add_argument('--cierra-dia',action='store_true',help='mueve el borrador del día al historial y vacía "Hecho hoy"')
p.add_argument('--anota',nargs='+',metavar=('TITULO','DETALLE'),help='añade al borrador: título, detalle y url opcional')
p.add_argument('--fecha',help='fecha AAAA-MM-DD para --anota (por defecto hoy)')
p.add_argument('--dry-run',action='store_true',help='muestra lo que haría sin escribir nada')
a=p.parse_args()
caracas=ZoneInfo('America/Caracas')
now=datetime.now(caracas)
months=['','enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
def fecha_larga(iso):
 d=datetime.fromisoformat(iso[:10]);return f'{d.day} de {months[d.month]} de {d.year}'

H='cgbabd_historial'
E='cgbabd_status'
hist_path=root/f'md/{H}.md'
hist=hist_path.read_text()
# Borrador del día: bloque oculto al final del historial.
m=re.search(r'\n?<!-- BORRADOR-DEL-DIA\n(.*?)-->\s*$',hist,re.S)
draft=[l.strip() for l in (m[1].splitlines() if m else []) if l.strip()]
body_md=hist[:m.start()] if m else hist
# Entradas publicadas: bloques "### Título".
entries=[]
rest=body_md.split('\n### ',1)
intro=rest[0].rstrip()+'\n'
for blk in (('### '+rest[1]).split('\n### ') if len(rest)>1 else []):
 blk=blk.removeprefix('### ')
 mm=re.match(r'(.*?)\n\n(\d+ de \w+ de \d{4})\. (.*?)(?:\n\n\[Leer\]\((.*?)\))?\s*$',blk,re.S)
 if mm: entries.append(dict(title=mm[1],date=mm[2],detail=mm[3].strip(),url=mm[4] or ''))

if a.anota:
 t=a.anota[0];dt=a.anota[1] if len(a.anota)>1 else '';u=a.anota[2] if len(a.anota)>2 else ''
 f=a.fecha or now.strftime('%Y-%m-%d')
 draft.insert(0,' | '.join([f,t,dt]+([u] if u else [])))
if a.cierra_dia:
 new=[]
 for l in draft:
  f,t,dt,*u=[x.strip() for x in l.rstrip(' |').split(' | ')]
  new.append(dict(title=t,date=fecha_larga(f),detail=dt,url=u[0] if u else ''))
 print(f'Cierre del día: {len(new)} trabajos pasan al historial.')
 entries=new+entries
 draft=[]

source=a.pendientes.read_text()
if a.cierra_dia:
 # Estado: lo logrado hoy ya pasó al historial.
 source=re.sub(r'(## Hecho hoy\n)(?:- .*\n?)+',r'\1- Nada todavía.\n',source)
 source=re.sub(r'^Actualizado:.*$',lambda m:f'Actualizado: {now.day} de {months[now.month]} de {now.year}, {now:%H:%M} UTC-4.',source,count=1,flags=re.M)
# Mantén la etiqueta temporal y los contadores compactos en cada regeneración.
lines=source.splitlines()
lines=[re.sub(r'^##\s+(?:Lo suyo|Suyo)\s*$', '## Pendiente de Osmancito', line) for line in lines]
counters=[]; kept=[]
for line in lines:
 found=re.findall(r'(\d[\d.]*)\s+(mensajes enviados|mensajes|palabras voz|palabras|correos)',line,re.I)
 if found:
  labels={'mensajes enviados':'mensajes','mensajes':'mensajes','palabras voz':'palabras','palabras':'palabras','correos':'correos'}
  counters.extend(f'{number} {labels[label.lower()]}' for number,label in found)
 else: kept.append(line)
if counters:
 while kept and not kept[-1].strip(): kept.pop()
 kept.append(' · '.join(counters))
source='\n'.join(kept).rstrip()+'\n'
# El contenido se escapa: un archivo de texto no puede insertar código en la página.
def inline(s):
 s=html.escape(s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
 return s

def markdown(s):
 out=[]; listing=False
 for line in s.splitlines():
  if line.startswith('- '):
   if not listing: out.append('<ul>');listing=True
   out.append('<li>'+inline(line[2:])+'</li>');continue
  if listing: out.append('</ul>');listing=False
  if not line.strip(): continue
  m=re.match(r'^(#{1,6}) (.*)',line)
  if m:
   n=min(len(m[1])+1,6);out.append(f'<h{n}>'+inline(m[2])+f'</h{n}>')
  else: out.append('<p>'+inline(line)+'</p>')
 if listing: out.append('</ul>')
 return '\n'.join(out)

STYLE='''<style>html{color-scheme:dark}body{background:#0d1117;color:#f0f6fc;font:18px/1.65 system-ui,sans-serif;margin:auto;max-width:680px;padding:24px}a{color:#4493f8}img{display:block;width:100%;height:auto;margin:24px 0}h1,h2,h3{line-height:1.25}h2{margin-top:36px}h3{font-size:1.12em}li{margin:12px 0}article{border-top:1px solid #30363d;padding:20px 0}article p{margin:10px 0}.fecha{color:#9198a1;font-size:.9em}code{overflow-wrap:anywhere}a{overflow-wrap:anywhere}nav a{display:inline-block;padding:10px 0}</style>'''

blocks=[];md=[]
for e in entries:
 date=e['date']
 link=f'<p><a href="{html.escape(e["url"],quote=True)}">Leer</a></p>' if e.get('url') else ''
 blocks.append(f'<article><p class="fecha">{date}</p><h3>{html.escape(e["title"])}</h3><p>{html.escape(e["detail"])}</p>{link}</article>')
 md.append(f'### {e["title"]}\n\n{date}. {e["detail"]}\n'+(f'\n[Leer]({e["url"]})\n' if e.get('url') else ''))
H='cgbabd_historial'
E='cgbabd_status'
hist_md='# Trabajos realizados\n\nOsmancito, con la asistencia de Instinct\n\nTrabajos terminados hasta ayer, del más reciente al más antiguo. Lo de hoy está en [Estado actual]('+E+'.md).\n\n'+'\n'.join(md)
if draft: hist_md=hist_md.rstrip('\n')+'\n\n<!-- BORRADOR-DEL-DIA\n'+'\n'.join(draft)+'\n-->\n'
estado_md='# Estado actual\n\nOsmancito, con la asistencia de Instinct\n\n'+source
if a.dry_run:
 print('DRY RUN: no se escribe nada.');print('--- historial (primeras líneas) ---');print('\n'.join(hist_md.splitlines()[:24]));print('--- borrador restante:',len(draft),'líneas ---');print('--- estado ---');print(estado_md)
 raise SystemExit(0)
(root/'md/pendientes.md').write_text(source)
(root/f'md/{H}.md').write_text(hist_md)
(root/f'md/{E}.md').write_text(estado_md)
def page(title,desc,slug,body):
 return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Sala de máquinas</title>
<meta name="description" content="{desc}">
<link rel="icon" href="https://osmancitov.github.io/favicon.ico">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://osmancitov.github.io/maquinas/html/{slug}.html">
<meta property="og:image" content="https://osmancitov.github.io/maquinas/img/cgbabd-mesa-produccion.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="720">
<meta property="og:image:alt" content="Una asistente revisa manuscritos junto a una fila de libros terminados, en claroscuro de Rembrandt.">
CSS
</head>
<body>
<main>
<h1>{title}</h1>
<img src="../img/cgbabd-mesa-produccion.jpg" alt="Mesa de trabajo: una asistente revisa manuscritos junto a los libros terminados" width="1280" height="720">
<p>Osmancito, con la asistencia de Instinct</p>
{body}
<nav><a href="../maquinas.html">Sala de máquinas</a></nav>
</main>
</body>
</html>
""".replace('CSS',STYLE)
(root/f'html/{H}.html').write_text(page('Trabajos realizados','Trabajos terminados hasta ayer, de lo más reciente a lo más antiguo.',H,'<p>Trabajos terminados hasta ayer, del más reciente al más antiguo. Lo de hoy está en <a href="'+E+'.html">Estado actual</a>.</p>\n<section aria-label="Trabajos realizados">\n'+'\n'.join(blocks)+'\n</section>'))
(root/f'html/{E}.html').write_text(page('Estado actual','Qué corre ahora, qué se hizo hoy y qué queda pendiente.',E,markdown(source)))
print('Actualizados md/pendientes.md, md/'+E+'.md, md/'+H+'.md y sus dos páginas html')
