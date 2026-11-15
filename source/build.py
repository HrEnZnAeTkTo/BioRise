from pathlib import Path
import base64,json,re
ROOT=Path(__file__).parent
assets={p.stem:'data:'+('image/svg+xml' if p.suffix=='.svg' else 'image/webp')+';base64,'+base64.b64encode(p.read_bytes()).decode() for p in (ROOT/'dist/assets').iterdir()}
lorem='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
config={'version':1,'texts':{},'styles':{},'images':{},'links':{},'theme':{'accent':'#858969','bg':'#faf9f6','surface':'#ffffff','ink':'#282b26','muted':'#6b6f65','line':'#dedfd5'},'settings':{'phone':'','email':'','address':'','mapUrl':'','misUrl':'','endpoint':'','privacyUrl':'','licenseUrl':'','socialUrl':'','bookingMode':'demo'},'doctors':[{'id':'doctor-'+str(i),'name':'Lorem ipsum dolor','specialty':'Lorem ipsum','experience':'Lorem ipsum dolor sit amet'} for i in range(1,4)],'analyses':[{'id':'analysis-'+str(i),'name':'Lorem ipsum '+x,'group':g,'price':'Lorem ipsum','term':'Lorem ipsum'} for i,(x,g) in enumerate([('dolor sit amet','a'),('consectetur adipiscing','a'),('sed do eiusmod','b'),('tempor incididunt','b'),('ut labore et dolore','c'),('magna aliqua','c')],1)],'drips':[{'id':'drip-'+str(i+1),'name':(['Красота в ресурсе','Лёгкость изнутри','Комфорт изнутри']+[ 'Lorem ipsum' for _ in range(13)])[i],'asset':'label-%02d'%(idx),'color':color,'group':grp} for i,(idx,color,grp) in enumerate([(5,'#c47eaf','a'),(3,'#98bc5d','b'),(2,'#a49ac3','c'),(1,'#eeb047','c'),(8,'#9ec0e1','b'),(6,'#a782b3','a'),(4,'#e7a498','c'),(7,'#6cb88c','b'),(9,'#75baa9','c'),(10,'#df6f9b','b'),(11,'#edb05f','b'),(12,'#6abfcf','c'),(13,'#36afcf','c'),(14,'#eca69e','c'),(15,'#66a597','b'),(16,'#97bb68','a')])], 'schedule':{'days':[1,2,3,4,5,6],'times':['09:00','10:30','12:00','14:00','15:30','17:00']}}
if (ROOT/'config.json').exists():
 config=json.loads((ROOT/'config.json').read_text())
else:
 (ROOT/'config.json').write_text(json.dumps(config,ensure_ascii=False,indent=2))
def safe_json(v):return json.dumps(v,ensure_ascii=False).replace('<','\\u003c')
css=(ROOT/'src/style.css').read_text();runtime=(ROOT/'src/app.js').read_text();editor=(ROOT/'src/editor.js').read_text()
base='''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Бенц Медикал ВРН — забота о вашем здоровье"><meta name="theme-color" content="#858969"><title>Бенц Медикал ВРН</title><style>CSS</style></head><body><a class="skip" href="#main">К содержимому</a><div id="app"></div><div id="toast" role="status" aria-live="polite"></div><script id="site-data" type="application/json">DATA</script><script id="asset-data" type="application/json">ASSETS</script><script id="site-runtime">RUNTIME</script>EDITOR</body></html>'''
base=base.replace('CSS',css).replace('DATA',safe_json(config)).replace('ASSETS',safe_json(assets)).replace('RUNTIME',runtime)
(ROOT/'dist/index.html').write_text(base.replace('EDITOR','<script data-editor>'+editor+'</script>'))
(ROOT/'dist/site.html').write_text(base.replace('EDITOR',''))
print('Built',len((ROOT/'dist/index.html').read_bytes()),'bytes; 16 label assets embedded')
