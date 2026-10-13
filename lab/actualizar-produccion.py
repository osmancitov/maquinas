#!/usr/bin/env python3
"""Genera la página y su archivo de lectura desde pendientes y logros públicos."""
import argparse, html, json, re
from pathlib import Path
from datetime import datetime

root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--pendientes',type=Path,required=True)
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

entries=sorted(json.loads((root/'data/produccion.json').read_text()),key=lambda e:e['date'],reverse=True)
months=['','enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
blocks=[];md=[]
for e in entries:
 d=datetime.fromisoformat(e['date']);date=f'{d.day} de {months[d.month]} de {d.year}'
 link=f'<p><a href="{html.escape(e["url"],quote=True)}">Leer</a></p>' if e.get('url') else ''
 blocks.append(f'<article><p class="fecha">{date}</p><h3>{html.escape(e["title"])}</h3><p>{html.escape(e["detail"])}</p>{link}</article>')
 md.append(f'### {e["title"]}\n\n{date}. {e["detail"]}\n'+(f'\n[Leer]({e["url"]})\n' if e.get('url') else ''))
# La misma información se conserva legible en el repositorio.
(root/'md/pendientes.md').write_text(source)
(root/'md/cgbabd_diario-maquina-principal.md').write_text('# Diario de la máquina principal\n\nOsmancito, con la asistencia de Instinct\n\n## Actividad actual\n\n'+source+'\n## Trabajos realizados\n\n'+'\n'.join(md))
page='''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Diario de la máquina principal · Sala de máquinas</title>
<meta name="description" content="Actividad actual y trabajos realizados con la asistencia de Instinct, de lo más reciente a lo más antiguo.">
<link rel="icon" href="https://osmancitov.github.io/favicon.ico">
<meta property="og:type" content="article">
<meta property="og:title" content="Diario de la máquina principal">
<meta property="og:description" content="Actividad actual y trabajos realizados, de lo más reciente a lo más antiguo.">
<meta property="og:url" content="https://osmancitov.github.io/maquinas/html/cgbabd_diario-maquina-principal.html">
<meta property="og:image" content="https://osmancitov.github.io/maquinas/img/cgbabd-mesa-produccion.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="720">
<meta property="og:image:alt" content="Una asistente revisa manuscritos junto a una fila de libros terminados, en claroscuro de Rembrandt.">
<style>html{color-scheme:dark}body{background:#0d1117;color:#f0f6fc;font:18px/1.65 system-ui,sans-serif;margin:auto;max-width:680px;padding:24px}a{color:#4493f8}img{display:block;width:100%;height:auto;margin:24px 0}h1,h2,h3{line-height:1.25}h2{margin-top:36px}h3{font-size:1.12em}li{margin:12px 0}article{border-top:1px solid #30363d;padding:20px 0}article p{margin:10px 0}.fecha{color:#9198a1;font-size:.9em}code{overflow-wrap:anywhere}a{overflow-wrap:anywhere}nav a{display:inline-block;padding:10px 0}</style>
</head>
<body>
<main>
<h1>Diario de la máquina principal</h1>
<img src="../img/cgbabd-mesa-produccion.jpg" alt="Mesa de trabajo: una asistente revisa manuscritos junto a los libros terminados" width="1280" height="720">
<p>Osmancito, con la asistencia de Instinct</p>
<section aria-labelledby="actividad"><h2 id="actividad">Actividad actual</h2>
PENDING
</section>
<section aria-labelledby="trabajos"><h2 id="trabajos">Trabajos realizados</h2>
<p>Resultados confirmados, de lo más reciente a lo más antiguo. Las tareas canceladas no aparecen como éxitos.</p>
HISTORY
</section>
<nav><a href="../maquinas.html">Sala de máquinas</a></nav>
</main>
</body>
</html>
'''.replace('PENDING',markdown(source)).replace('HISTORY','\n'.join(blocks))
(root/'html/cgbabd_diario-maquina-principal.html').write_text(page)
print('Actualizados md/pendientes.md, md/cgbabd_diario-maquina-principal.md y html/cgbabd_diario-maquina-principal.html')
