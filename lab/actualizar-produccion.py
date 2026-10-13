#!/usr/bin/env python3
"""Genera las dos páginas del diario: el estado actual (desde pendientes) y el historial de trabajos terminados antes de hoy."""
import argparse, html, json, re
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--pendientes',type=Path,default=root/'md/pendientes.md')
p.add_argument('--incluye-hoy',action='store_true',help='incluye en el historial los trabajos de hoy')
a=p.parse_args()
source=a.pendientes.read_text()
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

today=datetime.now(ZoneInfo('America/Caracas')).date()
entries=sorted(json.loads((root/'data/produccion.json').read_text()),key=lambda e:e['date'],reverse=True)
if not a.incluye_hoy: entries=[e for e in entries if datetime.fromisoformat(e['date']).date()<today]
months=['','enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
blocks=[];md=[]
for e in entries:
 d=datetime.fromisoformat(e['date']);date=f'{d.day} de {months[d.month]} de {d.year}'
 link=f'<p><a href="{html.escape(e["url"],quote=True)}">Leer</a></p>' if e.get('url') else ''
 blocks.append(f'<article><p class="fecha">{date}</p><h3>{html.escape(e["title"])}</h3><p>{html.escape(e["detail"])}</p>{link}</article>')
 md.append(f'### {e["title"]}\n\n{date}. {e["detail"]}\n'+(f'\n[Leer]({e["url"]})\n' if e.get('url') else ''))
(root/'md/pendientes.md').write_text(source)
H='cgbabd_historial'
E='cgbabd_status'
(root/f'md/{H}.md').write_text('# Trabajos realizados\n\nOsmancito, con la asistencia de Instinct\n\nTrabajos terminados hasta el día anterior, del más reciente al más antiguo. Lo de hoy está en [Estado actual]('+E+'.md).\n\n'+'\n'.join(md))
(root/f'md/{E}.md').write_text('# Estado actual\n\nOsmancito, con la asistencia de Instinct\n\n'+source)
def page(title,desc,slug,body,other):
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
<nav><a href="{other[0]}.html">{other[1]}</a> · <a href="../maquinas.html">Sala de máquinas</a></nav>
</main>
</body>
</html>
""".replace('CSS',STYLE)
(root/f'html/{H}.html').write_text(page('Trabajos realizados','Trabajos terminados hasta el día anterior, de lo más reciente a lo más antiguo.',H,'<p>Trabajos terminados hasta el día anterior, del más reciente al más antiguo. Lo de hoy está en <a href="'+E+'.html">Estado actual</a>.</p>\n<section aria-label="Trabajos realizados">\n'+'\n'.join(blocks)+'\n</section>',(E,'Estado actual')))
(root/f'html/{E}.html').write_text(page('Estado actual','Qué corre ahora, qué se hizo hoy y qué queda pendiente.',E,markdown(source),(H,'Trabajos realizados')))
print('Actualizados md/pendientes.md, md/'+E+'.md, md/'+H+'.md y sus dos páginas html')
