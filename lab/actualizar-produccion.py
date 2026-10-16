#!/usr/bin/env python3
"""Genera las tres páginas: Estado actual (desde md/pendientes.md), Historial de tareas (desde md/cgbabd_historial.md) e Historial social (desde md/cgbabf_historial-social.md).

FUENTES (no hay carpeta data/ ni json):
  md/pendientes.md        Estado actual. Se edita a mano durante el día; el bloque "## Hecho hoy" es lo logrado hoy y el bloque
                          "## Sociales" es el estado de las tareas sociales y de interacción con los mercados:
                          X, Slack, Element/Matrix, Mastodon, Bluesky, LinkedIn y toda otra red donde Osmancito deja huella y tiene contacto con el mundo.
                          Una viñeta por frente: red, cuenta y lo logrado hoy.
                          Cada reporte va directo y corto: un renglón por frente o por interacción, sin detalle. Presupuesto
                          inicial: unas 500 palabras en total en esa sección; si las interacciones crecen, se agrupan por red.
  md/cgbabf_historial-social.md  Historial social. Un bloque "## fecha larga" por día, el más reciente arriba, con las viñetas
                          que ese día tuvo "## Sociales".
  md/cgbabd_historial.md  Historial de tareas. Cada trabajo es un bloque "### Título" con "fecha. detalle" y, si hay, "[Leer](url)".
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
     deja "## Hecho hoy" de Estado en "- Nada todavía.", pasa las viñetas de "## Sociales" al principio del
     historial social bajo la fecha del día que termina y deja ese bloque en "- Nada todavía.", y regenera los md y html de las tres páginas.
  5. Contadores (💬 mensajes · 🎙️ palabras de voz · ✉️ correos · 🎖️ medallas, todos del día en Caracas) y bloque "Corriendo ahora"/"Pendiente de Osmancito": ajustarlos a mano en md/pendientes.md antes del paso 4
     y reponerlos desde datos vivos cada vez que se actualiza Status (las medallas: cada emoji 🎖 individual, no los mensajes que lo contienen, en los mensajes de WhatsApp del usuario
     en WhatsApp, del día de Caracas; en observaciones phone_messages, service WhatsApp, author user, se cuentan las apariciones del emoji; solo WhatsApp, no correo); la línea de fecha y hora se reescribe sola en UTC-4, sin etiqueta.
  6. git add -A && git commit -m "Cierra el día" && git push (token de Drive .github_key, sin espacios, nunca impreso)
     y comprobar las tres páginas en vivo.
Sin opciones, solo regenera las páginas desde los md (no mueve nada).
"""
import argparse, html, re
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description='Regenera Estado actual, Historial de tareas e Historial social; ver cabecera para el cierre del día.')
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
S='cgbabf_historial-social'
soc_path=root/f'md/{S}.md'
soc=soc_path.read_text()
soc_intro,*soc_blocks=re.split(r'\n(?=## )',soc.rstrip('\n')+'\n')
soc_days=[]
for b in soc_blocks:
 head,*bl=b.strip().split('\n',1)
 soc_days.append((head.removeprefix('## ').strip(),[l[2:] for l in (bl[0] if bl else '').splitlines() if l.startswith('- ')]))
if a.cierra_dia:
 # Estado: lo logrado hoy ya pasó al historial.
 mf=re.search(r'## Sociales\n((?:- .*\n?)+)',source)
 dia=datetime.fromisoformat(a.fecha) if a.fecha else (now-timedelta(days=1) if now.hour<12 else now)
 hoy=[l[2:] for l in (mf[1].splitlines() if mf else []) if l.startswith('- ') and 'Nada todavía' not in l]
 if hoy:
  fl=fecha_larga(dia.strftime('%Y-%m-%d'))
  if soc_days and soc_days[0][0]==fl: soc_days[0]=(fl,hoy+soc_days[0][1])
  else: soc_days.insert(0,(fl,hoy))
  print(f'Cierre social: {len(hoy)} frentes pasan al historial social ({fl}).')
 source=re.sub(r'(## Sociales\n)(?:- .*\n?)+',r'\1- Nada todavía.\n',source)
 source=re.sub(r'(## Hecho hoy\n)(?:- .*\n?)+',r'\1- Nada todavía.\n',source)
 source=re.sub(r'^(?:Actualizado: )?.*UTC-4\.?$',lambda m:f'{now.day} de {months[now.month]} de {now.year}, {now:%H:%M} UTC-4.',source,count=1,flags=re.M)
# Mantén el formato de fecha y hora sin etiqueta, y los contadores compactos en cada regeneración.
lines=source.splitlines()
lines=[re.sub(r'^##\s+(?:Lo suyo|Suyo)\s*$', '## Pendiente de Osmancito', line) for line in lines]
counters=[]; kept=[]
# Formato fijo: 💬 mensajes enviados · 🎙️ palabras de voz · ✉️ correos · 🎖️ medallas de WhatsApp (todos del día).
emo={'mensajes':'💬','palabras':'🎙️','correos':'✉️','medallas':'🎖️'}
orden=['mensajes','palabras','correos','medallas']
pat=r'(?:(💬|🎙️?|✉️?|🎖️?)\s*(\d[\d.]*))|(?:(\d[\d.]*)\s+(mensajes enviados|mensajes|palabras voz|palabras|correos|medallas))'
key={'💬':'mensajes','🎙':'palabras','✉':'correos','🎖':'medallas','mensajes enviados':'mensajes','mensajes':'mensajes','palabras voz':'palabras','palabras':'palabras','correos':'correos','medallas':'medallas'}
vals={}
for line in lines:
 found=re.findall(pat,line,re.I)
 if found and '·' in line:
  for e,n1,n2,w in found:
   k=key[(e.rstrip('\ufe0f') if e else w.lower())]; vals[k]=n1 or n2
 else: kept.append(line)
if vals:
 while kept and not kept[-1].strip(): kept.pop()
 kept.append(' · '.join(f'{emo[k]} {vals[k]}' for k in orden if k in vals))
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

STYLE='''<link rel="stylesheet" href="/css/base.css">
<style>html{color-scheme:dark}body{margin:auto;max-width:680px;padding:24px}a{color:#4493f8}img{display:block;width:100%;height:auto;margin:24px 0}h1,h2,h3{line-height:1.25}h2{margin-top:36px}h3{font-size:1.12em}li{margin:12px 0}article{border-top:1px solid #30363d;padding:20px 0}article p{margin:10px 0}.fecha{color:#9198a1;font-size:.9em}code{overflow-wrap:anywhere}a{overflow-wrap:anywhere}nav a{display:inline-block;padding:10px 0}</style>'''

blocks=[];md=[]
for e in entries:
 date=e['date']
 link=f'<p><a href="{html.escape(e["url"],quote=True)}">Leer</a></p>' if e.get('url') else ''
 blocks.append(f'<article><p class="fecha">{date}</p><h3>{html.escape(e["title"])}</h3><p>{html.escape(e["detail"])}</p>{link}</article>')
 md.append(f'### {e["title"]}\n\n{date}. {e["detail"]}\n'+(f'\n[Leer]({e["url"]})\n' if e.get('url') else ''))
H='cgbabd_historial'
E='cgbabd_status'
hist_md='# Historial de tareas\n\nOsmancito, con la asistencia de Instinct\n\nTrabajos terminados hasta ayer, del más reciente al más antiguo.\n\n'+'\n'.join(md)
if draft: hist_md=hist_md.rstrip('\n')+'\n\n<!-- BORRADOR-DEL-DIA\n'+'\n'.join(draft)+'\n-->\n'
estado_md='# Estado actual\n\nOsmancito, con la asistencia de Instinct\n\n'+source
if a.dry_run:
 print('DRY RUN: no se escribe nada.');print('--- historial (primeras líneas) ---');print('\n'.join(hist_md.splitlines()[:24]));print('--- borrador restante:',len(draft),'líneas ---');print('--- estado ---');print(estado_md)
 raise SystemExit(0)
SOC_INTRO='# Historial social\n\nOsmancito, con la asistencia de Instinct\n\nLo que se hizo cada día en X, Slack, Element/Matrix, Mastodon, Bluesky, LinkedIn y las demás redes donde Osmancito deja huella y tiene contacto con el mundo, del día más reciente al más antiguo.\n'
soc_md=SOC_INTRO+''.join('\n## '+d+'\n\n'+'\n'.join('- '+x for x in items)+'\n' for d,items in soc_days)
(root/'md/pendientes.md').write_text(source)
(root/f'md/{S}.md').write_text(soc_md)
(root/f'md/{H}.md').write_text(hist_md)
(root/f'md/{E}.md').write_text(estado_md)
def page(title,desc,slug,body,img='cgbabd-mesa-produccion.jpg',w=1280,h=720,alt='Una asistente revisa manuscritos junto a una fila de libros terminados, en claroscuro de Rembrandt.',alt_corto='Mesa de trabajo: una asistente revisa manuscritos junto a los libros terminados'):
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
<meta property="og:image" content="https://osmancitov.github.io/maquinas/img/{img}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="{w}">
<meta property="og:image:height" content="{h}">
<meta property="og:image:alt" content="{alt}">
CSS
</head>
<body>
<main>
<h1>{title}</h1>
<img src="../img/{img}" alt="{alt_corto}" width="{w}" height="{h}">
<p>Osmancito, con la asistencia de Instinct</p>
{body}
<nav><a href="../maquinas.html">Sala de máquinas</a></nav>
</main>
</body>
</html>
""".replace('CSS',STYLE)
(root/f'html/{H}.html').write_text(page('Historial de tareas','Trabajos terminados hasta ayer, de lo más reciente a lo más antiguo.',H,'<p>Trabajos terminados hasta ayer, del más reciente al más antiguo.</p>\n<section aria-label="Historial de tareas">\n'+'\n'.join(blocks)+'\n</section>'))
soc_html='<p>Lo que se hizo cada día en X, Slack, Element/Matrix, Mastodon, Bluesky, LinkedIn y las demás redes donde Osmancito deja huella y tiene contacto con el mundo, del día más reciente al más antiguo.</p>\n'+'\n'.join(f'<section><h2>{html.escape(d)}</h2>\n<ul>\n'+'\n'.join(f'<li>{inline(x)}</li>' for x in items)+'\n</ul></section>' for d,items in soc_days)
(root/f'html/{S}.html').write_text(page('Historial social','Lo que se hizo cada día en las redes donde Osmancito deja huella.',S,soc_html,img='cgbabf-historial-social.jpg',w=1280,h=640,alt='Una asistente iza banderas de señales en un puerto al atardecer, hacia muchos barcos lejanos, al estilo de Claudio de Lorena.',alt_corto='Puerto al atardecer: una asistente iza banderas de señales hacia los barcos lejanos'))
(root/f'html/{E}.html').write_text(page('Estado actual','Qué corre ahora, qué se hizo hoy y qué queda pendiente.',E,markdown(source)))
print('Actualizados md/pendientes.md, md/'+E+'.md, md/'+H+'.md, md/'+S+'.md y sus tres páginas html')
