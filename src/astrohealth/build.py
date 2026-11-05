"""Single pipeline: raw NASA files -> clean UTMB tables (utmb/) + unified demo dataset (demo/).
Replaces tidy_utmb.py + build_demo.py after the independent audit (verificacion/01-03).

usage:  make data   (or: python -m astrohealth.build, with src/ on PYTHONPATH)
Every correction applied is logged to utmb/registro_correcciones.csv.
"""
import csv, glob, math, os, random, re, statistics as st
from datetime import date, datetime

from astrohealth.config import ROOT, RAW_NLSP as RAW, INTERIM as U, PROCESSED as OUT
ROOT, RAW, U, OUT = str(ROOT), str(RAW), str(U), str(OUT)
os.makedirs(U, exist_ok=True)
os.makedirs(OUT, exist_ok=True)
SEED = 2026
LOG = []


def log(tipo, sujeto, detalle):
    LOG.append({'tipo': tipo, 'sujeto': sujeto, 'detalle': detalle})


def files(folder_pat, exclude=()):
    out = []
    for p in sorted(glob.glob(os.path.join(RAW, folder_pat, '**', '*'), recursive=True)):
        b = os.path.basename(p)
        if os.path.isfile(p) and not b.endswith('.md5sum') and 'readme' not in b.lower() \
                and not any(e in b for e in exclude):
            out.append(p)
    return out


def rows(p):
    with open(p, encoding='utf-8-sig', errors='replace', newline='') as f:
        return list(csv.DictReader(f))


def nk(h):
    return re.sub(r'[^a-z0-9]', '', (h or '').lower())


def get(r, *cands):
    """value for the first header whose normalized name is in cands (order of cands = priority)."""
    m = {nk(k): v for k, v in r.items() if k}
    for c in cands:
        v = m.get(c)
        if v not in (None, '') and str(v).strip() not in ('', 'NA', 'N/A', 'nan'):
            return str(v).strip()
    return None


def num(v):
    if v is None:
        return None
    m = re.match(r'^\s*[<>]?\s*(-?\d+(?:\.\d+)?)', str(v))
    return float(m.group(1)) if m else None


def pdate(s):
    if not s:
        return None
    m = re.match(r'^\s*(\d{1,2})/(\d{1,2})/(\d{4})', str(s))
    if m:
        try:
            return date(int(m.group(3)), int(m.group(1)), int(m.group(2)))
        except ValueError:
            return None
    m = re.match(r'^\s*(\d{4})-(\d{2})-(\d{2})', str(s))
    return date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None


def hours(v):
    """'7:44', '7:44:00', '0:14', '0', '7.5' -> hours"""
    if v is None:
        return None
    s = str(v).strip()
    m = re.match(r'^(\d+):(\d{1,2})(?::(\d{1,2}))?$', s)
    if m:
        return round(int(m.group(1)) + int(m.group(2)) / 60 + int(m.group(3) or 0) / 3600, 3)
    return num(s)


def write(path, data, fields=None):
    if not data:
        print('VACIO', path); return
    fields = fields or list(data[0].keys())
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader(); w.writerows(data)
    print(f'{os.path.relpath(path, ROOT)}: {len(data)} filas')


FASE = {'PRE_TEST': 'pre', 'IN_TEST': 'mision', 'POST_TEST': 'post'}
PLAUS = {'pulso_lpm': (30, 200), 'pas_mmhg': (70, 220), 'pad_mmhg': (35, 140), 'resp_rpm': (6, 40),
         'temp_c': (34.0, 40.5), 'peso_kg': (30, 200)}

# =============================================================== 1. VITALS
vit_raw = []
for p in files('CRF_*Vitals*') + files('CRF_CFT70_VITALS'):
    b = os.path.basename(p)
    if 'Campaign_1' in p and b.endswith('_All'):
        log('archivo_omitido', '', f'{b}: duplica los archivos Subject_1..3 de la campaña 1')
        continue
    camp = 'CFT70' if 'CFT70' in p else ('C1' if 'Campaign_1' in p else 'C3')
    for r in rows(p):
        s = get(r, 'subject')
        d = pdate(get(r, 'date', 'testdate'))
        if not s or not d:
            continue
        rec = {'campana': camp, 'sujeto': s, 'fecha': d, 'fase': FASE.get(get(r, 'testphase'), get(r, 'testphase')),
               'br_day': num(get(r, 'brday'))}
        t = num(get(r, 'bodytempcelsius', 'temperaturebodycelsius', 'bodytemp'))
        if t is None:
            f_ = num(get(r, 'temperaturebodyfahrenheit'))
            t = round((f_ - 32) * 5 / 9, 2) if f_ is not None else None
        vals = {'pulso_lpm': num(get(r, 'pulsebpm', 'pulse')),
                'pas_mmhg': num(get(r, 'sysbpmmhg', 'bloodpressuresystolic', 'sysbp')),
                'pad_mmhg': num(get(r, 'diabpmmhg', 'bloodpressurediastolic', 'diabp')),
                'resp_rpm': num(get(r, 'respraterpm', 'respirationraterpm', 'respirationrate', 'resprate')),
                'temp_c': t,
                'peso_kg': num(get(r, 'weightkg', 'weight'))}
        for k, v in vals.items():
            lo, hi = PLAUS[k]
            if v is not None and not (lo <= v <= hi):
                log('valor_imposible', s, f'{d} {k}={v} -> vacío')
                v = None
            rec[k] = v
        vit_raw.append(rec)

# anchor per subject = median over IN rows of (date - BR_Day) -> calendar date of bed-rest day 0
def anchors(recs):
    offs = {}
    for x in recs:
        if x['fase'] == 'mision' and x['br_day'] is not None:
            offs.setdefault(x['sujeto'], []).append(x['fecha'].toordinal() - int(x['br_day']))
    return {s: int(st.median(o)) for s, o in offs.items()}


A = anchors(vit_raw)
# fix year typos (e.g. 2001 instead of 2004) when the corrected date is consistent with BR_Day
for x in vit_raw:
    a = A.get(x['sujeto'])
    if a is None:
        continue
    rel = x['fecha'].toordinal() - a
    if not -120 <= rel <= 300:
        fixed = None
        for y in (date.fromordinal(a).year, date.fromordinal(a).year + 1):
            try:
                cand = x['fecha'].replace(year=y)
            except ValueError:
                continue
            if -120 <= cand.toordinal() - a <= 300:
                fixed = cand; break
        if fixed:
            log('fecha_corregida', x['sujeto'], f'{x["fecha"]} -> {fixed} (año mal tipeado)')
            x['fecha'] = fixed
        else:
            log('fila_descartada', x['sujeto'], f'{x["fecha"]}: fecha imposible')
            x['descartar'] = True
vit_raw = [x for x in vit_raw if not x.get('descartar')]

# dedupe subject-day (keep the record with more filled values)
vit = {}
for x in vit_raw:
    k = (x['sujeto'], x['fecha'])
    filled = sum(x[v] is not None for v in PLAUS)
    if k in vit:
        log('duplicado', x['sujeto'], f'{x["fecha"]}: registro duplicado del mismo día')
        if filled <= sum(vit[k][v] is not None for v in PLAUS):
            continue
    vit[k] = x
A = anchors(vit.values())
for x in vit.values():
    a = A.get(x['sujeto'])
    x['dia_mision'] = x['fecha'].toordinal() - a if a is not None else None
    if x['fase'] == 'mision' and x['br_day'] is not None and x['dia_mision'] is not None \
            and abs(x['br_day'] - x['dia_mision']) > 1:
        log('br_day_inconsistente', x['sujeto'], f'{x["fecha"]}: BR_Day {x["br_day"]:.0f}, por fecha {x["dia_mision"]}; se usa la fecha')
mission_len = {}
for x in vit.values():
    if x['fase'] == 'mision' and x['dia_mision'] is not None:
        mission_len[x['sujeto']] = max(mission_len.get(x['sujeto'], 0), x['dia_mision'])

# =============================================================== 2. SLEEP (actigraphy, campaign 1)
sleep = {}
for p in files('BRSMACT_*'):
    if 'Query_Result' in p:
        log('archivo_omitido', '', f'{os.path.basename(p)}: exportación de consulta ambigua; se usa el archivo principal')
        continue
    for r in rows(p):
        s, d = get(r, 'subject'), pdate(get(r, 'date'))
        dur = hours(get(r, 'sleepdurationhours', 'sleepduration'))
        if not s or not d or dur is None:
            continue
        lat = hours(get(r, 'sleeplatencyhours', 'sleeplatency'))
        sleep[(s, d)] = {'sujeto': s, 'fecha': d, 'fase': FASE.get(get(r, 'testphase')), 'br_day': num(get(r, 'brday')),
                         'sueno_h': dur, 'sueno_eficiencia_pct': num(get(r, 'sleepefficiency', 'sleepefficiencypct')),
                         'sueno_latencia_min': round(lat * 60) if lat is not None else None}

# =============================================================== 3. COGNITION (WinSCAT)
cog = {}
for p in files('MR085G_*'):
    for r in rows(p):
        s, d = get(r, 'subject'), pdate(get(r, 'date'))
        if not s or not d:
            continue
        k = (s, d, get(r, 'run'), get(r, 'time'))
        if k in cog:
            log('duplicado', s, f'{d}: sesión WinSCAT duplicada'); continue
        cog[k] = {'sujeto': s, 'fecha': d, 'fase': FASE.get(get(r, 'testphase')), 'br_day': num(get(r, 'brday')),
                  'campana': (get(r, 'campaign') or 'C1')[:2], 'tipo_test': get(r, 'test'), 'corrida': num(get(r, 'run')),
                  'cog_memoria_trabajo_ms': num(get(r, 'cptrt')), 'cog_memoria_trabajo_precision_pct': num(get(r, 'cpta')),
                  'cog_matematica_ms': num(get(r, 'mthrt')), 'cog_matematica_precision_pct': num(get(r, 'mtha')),
                  'cog_emparejamiento_ms': num(get(r, 'mtsrt')), 'cog_emparejamiento_precision_pct': num(get(r, 'mtsa')),
                  'cog_codigo_diferido_ms': num(get(r, 'cddrt')), 'cog_codigo_diferido_precision_pct': num(get(r, 'cdda'))}
# session index per subject (practice effect)
by_s = {}
for c in sorted(cog.values(), key=lambda c: (c['sujeto'], c['fecha'], c['corrida'] or 0)):
    by_s.setdefault(c['sujeto'], []).append(c)
for s, L in by_s.items():
    for i, c in enumerate(L, 1):
        c['sesion_n'] = i

# =============================================================== 4. TILT (campaign 3; campaign 1 excluded)
log('dato_excluido', '', 'Tilt campaña 1: el archivo MR001G_Campaign_1_Tilt_HR es idéntico al de DBP en el origen; no hay pulso verificable')
tilt = []
for p in files('MR001G_Campaign_3_Tilt'):
    R = rows(p)
    if not R or 'stage' not in {nk(k) for k in R[0]}:
        continue
    hr = lambda r: num(get(r, 'hr', 'hrdinamap'))
    sup = [hr(r) for r in R if (get(r, 'stage') or '').lower().startswith('supine') and hr(r) is not None]
    til = [hr(r) for r in R if (get(r, 'stage') or '').lower().startswith('tilt') and hr(r) is not None]
    sbs = [num(get(r, 'sbp')) for r in R if (get(r, 'stage') or '').lower().startswith('supine') and num(get(r, 'sbp')) is not None]
    sbt = [num(get(r, 'sbp')) for r in R if (get(r, 'stage') or '').lower().startswith('tilt') and num(get(r, 'sbp')) is not None]
    if not sup or not til:
        continue
    r0 = R[0]
    s = get(r0, 'subject')
    tilt.append({'sujeto': s, 'fecha': pdate(get(r0, 'date')), 'fase': FASE.get(get(r0, 'testphase')),
                 'br_day': num(get(r0, 'brday')), 'pulso_acostado': round(st.mean(sup), 1), 'pulso_inclinado': round(st.mean(til), 1),
                 'aumento_pulso_lpm': round(st.mean(til) - st.mean(sup), 1),
                 'pas_acostado': round(st.mean(sbs), 1) if sbs else None, 'pas_inclinado': round(st.mean(sbt), 1) if sbt else None,
                 'minutos_inclinado_con_dato': len(til)})

# =============================================================== 5. LABS (UTMB + Inspiration4)
CANON = [(r'^glucose$', 'glucosa'), (r'^albumin$', 'albumina'), (r'^creatinine$', 'creatinina'),
         (r'^alkaline phosphatase( \(alp\))?$', 'fosfatasa_alcalina'), (r'^(c-reactive protein|crp)$', 'pcr'),
         (r'^white blood cell count$', 'leucocitos'), (r'^lymphocytes$', 'linfocitos_pct'),
         (r'^absolute lymphocytes$', 'linfocitos_abs'), (r'^absolute neutrophils$', 'neutrofilos_abs'),
         (r'^neutrophils$', 'neutrofilos_pct'), (r'^mcv$', 'vcm'), (r'^rdw$', 'rdw'), (r'^hemoglobin$', 'hemoglobina'),
         (r'^hematocrit$', 'hematocrito'), (r'^platelet count$', 'plaquetas'), (r'^sodium$', 'sodio'),
         (r'^potassium$', 'potasio'), (r'^calcium$', 'calcio'),
         (r'^(urea nitrogen \(bun\)|blood urea nitrogen( \(bun\))?)$', 'bun'),
         (r'^(alt|alanine aminotransferase( \(alt\))?)$', 'alt'), (r'^(ast|aspartate aminotransferase( \(ast\))?)$', 'ast')]
LAB_PLAUS = {'glucosa': (50, 400), 'hemoglobina': (7, 20), 'plaquetas': (50, 800), 'leucocitos': (1, 30),
             'neutrofilos_abs': (500, 15000), 'albumina': (2, 6), 'creatinina': (0.3, 3), 'rdw': (9, 25), 'vcm': (60, 120)}


def canon(name):
    n = re.sub(r'\s+', ' ', name.strip().lower())
    for pat, c in CANON:
        if re.search(pat, n):
            return c
    return re.sub(r'[^a-z0-9]+', '_', n).strip('_')


UNIT_EQ = {'thou/mm3': '10^3/ul', 'thousand/ul': '10^3/ul', 'k/ul': '10^3/ul', 'relative%': '%'}


def unorm(u):
    u = re.sub(r'\s+', '', (u or '').strip().lower())
    return UNIT_EQ.get(u, u)


labs = []
for p in files('MR010G_*'):
    for r in rows(p):
        par = get(r, 'parametername')
        raw = get(r, 'measuredvalue')
        v = num(raw)
        if not par or v is None:
            continue
        s = get(r, 'subject')
        mark = re.sub(r'^\s*[<>]?\s*-?\d+(?:\.\d+)?', '', raw).strip() if raw else ''
        if raw.strip().startswith(('<', '>')):
            mark = (raw.strip()[0] + ' ' + mark).strip()
        unit = get(r, 'units') or ''
        c = canon(par)
        if 'spe' in (get(r, 'group') or '').lower():   # serum protein electrophoresis: different method
            c = c + '_electroforesis'
        if c == 'pcr' and unorm(unit) == 'mg/l':
            v, unit = round(v / 10, 4), 'mg/dL'
            mark = (mark + ' convertido de mg/L').strip()
        d = pdate(get(r, 'date'))
        a = A.get(s)
        labs.append({'fuente': 'UTMB (reposo en cama)', 'sujeto': s, 'fecha': d,
                     'fase': FASE.get(get(r, 'testphase')), 'dia_relativo': d.toordinal() - a if d and a else None,
                     'referencia_dia': 'día 1 = primer día en cama', 'analito': c, 'analito_original': par,
                     'valor': v, 'marca_origen': mark, 'unidad': unit,
                     'rango_normal': (get(r, 'normalrange') or '').replace('\n', ' ')})


def i4_day(tp):
    m = re.match(r'([LR])([+-])(\d+)', tp or '')
    if not m:
        return None, None
    return ('pre', -int(m.group(3))) if m.group(1) == 'L' else ('post', int(m.group(3)))


I4REF = 'negativo = días antes del lanzamiento; positivo = días tras aterrizar'
for r in rows(os.path.join(ROOT, 'data', 'raw', 'osdr', 'osdr-inspiration4-clinico.csv')):
    ph, dr = i4_day(r['timepoint'])
    labs.append({'fuente': 'Inspiration4 OSD-569 (vuelo real)', 'sujeto': r['subject_id'], 'fecha': None, 'fase': ph,
                 'dia_relativo': dr, 'referencia_dia': I4REF, 'analito': canon(r['analyte']), 'analito_original': r['analyte'],
                 'valor': num(r['value']), 'marca_origen': '', 'unidad': r['units'], 'rango_normal': f"{r['ref_min']} - {r['ref_max']}"})
for r in rows(os.path.join(ROOT, 'data', 'raw', 'osdr', 'osd-575', 'CMP.csv')):
    ph, dr = i4_day(r['timepoint'])
    labs.append({'fuente': 'Inspiration4 OSD-575 (vuelo real)', 'sujeto': r['SUBJECT_ID'], 'fecha': None, 'fase': ph,
                 'dia_relativo': dr, 'referencia_dia': I4REF, 'analito': canon(r['ANALYTE']), 'analito_original': r['ANALYTE'],
                 'valor': num(r['VALUE']), 'marca_origen': '', 'unidad': r['UNITS'], 'rango_normal': f"{r['RANGE_MIN']} - {r['RANGE_MAX']}"})
for r in rows(os.path.join(ROOT, 'data', 'raw', 'osdr', 'osd-575', 'cardio_eve.csv')):
    if r['Analyte'].strip().upper() != 'CRP' or r['Unit'].strip().lower() != 'pg/ml':
        continue
    ph, dr = i4_day(r['Timepoint'])
    v = num(r['Concentration'])
    labs.append({'fuente': 'Inspiration4 OSD-575 panel Eve (vuelo real)', 'sujeto': r['ID'], 'fecha': None, 'fase': ph,
                 'dia_relativo': dr, 'referencia_dia': I4REF, 'analito': 'pcr', 'analito_original': 'CRP',
                 'valor': round(v / 1e7, 4) if v is not None else None, 'marca_origen': 'convertido de pg/ml (÷1e7)',
                 'unidad': 'mg/dL', 'rango_normal': ''})
labs = [l for l in labs if l['valor'] is not None]

# unit consistency per canonical analyte
units = {}
for l in labs:
    units.setdefault(l['analito'], {}).setdefault(unorm(l['unidad']), 0)
    units[l['analito']][unorm(l['unidad'])] += 1
for l in labs:
    l['unidad_mixta'] = 'si' if len(units[l['analito']]) > 1 else ''
    lo_hi = LAB_PLAUS.get(l['analito'])
    l['atipico'] = ''
    if lo_hi and not (lo_hi[0] <= l['valor'] <= lo_hi[1]):
        l['atipico'] = 'si'
        if l['analito'] == 'hemoglobina' and 70 <= l['valor'] <= 200:
            l['atipico'] = 'si: probable error de coma decimal (g/L o x10)'
# known source problem: Inspiration4 C003 at L-92 has shifted CBC columns
for l in labs:
    if l['fuente'].startswith('Inspiration4 OSD-569') and l['sujeto'] == 'C003' and l['dia_relativo'] == -92:
        l['atipico'] = l['atipico'] or 'si: columnas desplazadas en el origen (C003, L-92)'

# =============================================================== 6. EVENTS (all symptom files, case-insensitive)
ev = []
for p in sorted(glob.glob(os.path.join(RAW, '*', '**', '*'), recursive=True)):
    if not os.path.isfile(p) or 'symptom' not in p.lower() or p.endswith('.md5sum') or 'readme' in p.lower():
        continue
    for r in rows(p):
        s = get(r, 'subject')
        raw_d = get(r, 'date')
        d = pdate(raw_d)
        if raw_d and not d:
            log('fecha_ilegible', s, f'evento con fecha "{raw_d}"')
        a = A.get(s)
        ev.append({'sujeto': s, 'fecha': d, 'hora': get(r, 'time', 'occurtime'),
                   'fase': FASE.get(get(r, 'testphase'), get(r, 'testphase')),
                   'dia_mision': d.toordinal() - a if d and a else None,
                   'sintoma': get(r, 'symptom', 'symptomcomplaint'), 'dolor_0a10': get(r, 'painscore'),
                   'descripcion': get(r, 'comments'), 'accion': get(r, 'action', 'actiontaken'),
                   'intervencion': get(r, 'intervention'), 'resultado': get(r, 'outcome', 'resolution')})

# =============================================================== 7. UTMB clean tables + summaries
def iso(d):
    return d.isoformat() if isinstance(d, date) else (d or '')


vit_list = sorted(vit.values(), key=lambda x: (x['sujeto'], x['fecha']))
write(os.path.join(U, 'utmb_vitales_diarios.csv'),
      [{**x, 'fecha': iso(x['fecha'])} for x in vit_list],
      ['campana', 'sujeto', 'fecha', 'fase', 'br_day', 'dia_mision'] + list(PLAUS))
write(os.path.join(U, 'utmb_sueno_actigrafia.csv'), [{**x, 'fecha': iso(x['fecha'])} for x in sorted(sleep.values(), key=lambda x: (x['sujeto'], x['fecha']))])
write(os.path.join(U, 'utmb_cognicion_winscat.csv'), [{**x, 'fecha': iso(x['fecha'])} for x in sorted(cog.values(), key=lambda c: (c['sujeto'], c['fecha']))])
write(os.path.join(U, 'utmb_tilt_ortostatico.csv'), [{**x, 'fecha': iso(x['fecha'])} for x in tilt])
write(os.path.join(U, 'utmb_laboratorio.csv'), [{**l, 'fecha': iso(l['fecha'])} for l in labs if l['fuente'].startswith('UTMB')])


def summ(values):
    vals = [v for v in values if v is not None]
    if len(vals) < 3:
        return None
    q = st.quantiles(vals, n=20, method='inclusive')
    return len(vals), round(st.mean(vals), 2), round(st.stdev(vals), 2), round(q[0], 2), round(q[-1], 2)


lines = []
def add(var, data, key, label=None):
    for ph in ('pre', 'mision', 'post'):
        r = summ([x.get(key) for x in data if x['fase'] == ph])
        if r:
            lines.append({'variable': label or var, 'fase': ph, 'n': r[0], 'media': r[1], 'de': r[2], 'p5': r[3], 'p95': r[4]})


for k in PLAUS:
    add(k, vit_list, k)
for k in ('sueno_h', 'sueno_eficiencia_pct', 'sueno_latencia_min'):
    add(k, list(sleep.values()), k)
for k in ('cog_memoria_trabajo_ms', 'cog_memoria_trabajo_precision_pct', 'cog_matematica_ms', 'cog_emparejamiento_ms', 'cog_codigo_diferido_ms'):
    add(k, list(cog.values()), k)
add('tilt_aumento_pulso_lpm', tilt, 'aumento_pulso_lpm')
add('tilt_minutos_inclinado_con_dato', tilt, 'minutos_inclinado_con_dato')
ul = [l for l in labs if l['fuente'].startswith('UTMB') and not l['atipico']]
for an in ('glucosa', 'hemoglobina', 'leucocitos', 'calcio', 'potasio', 'sodio', 'creatinina', 'albumina', 'pcr'):
    for un in sorted({unorm(l['unidad']) for l in ul if l['analito'] == an}):
        add(f'lab:{an} ({un})', [{'fase': l['fase'], 'v': l['valor']} for l in ul if l['analito'] == an and unorm(l['unidad']) == un], 'v')
write(os.path.join(U, 'utmb_resumen_por_fase.csv'), lines)

# individual change IN - PRE
chg = []
for k in ('pulso_lpm', 'pas_mmhg', 'pad_mmhg', 'temp_c', 'peso_kg'):
    ds = []
    for s in {x['sujeto'] for x in vit_list}:
        pre = [x[k] for x in vit_list if x['sujeto'] == s and x['fase'] == 'pre' and x[k] is not None]
        inn = [x[k] for x in vit_list if x['sujeto'] == s and x['fase'] == 'mision' and x[k] is not None]
        if len(pre) >= 3 and len(inn) >= 10:
            ds.append(st.mean(inn) - st.mean(pre))
    if len(ds) > 2:
        chg.append({'variable': k, 'n_sujetos': len(ds), 'cambio_medio': round(st.mean(ds), 2), 'de': round(st.stdev(ds), 2),
                    'min': round(min(ds), 2), 'max': round(max(ds), 2)})
write(os.path.join(U, 'utmb_cambio_individual.csv'), chg)

# =============================================================== 8. DEMO daily table
day = {}
def rec(s, d, fase, br, camp):
    k = (s, d)
    if k not in day:
        day[k] = {'fuente': 'UTMB', 'campana': camp, 'sujeto': s, 'fecha': d, 'fase': fase, 'br_day': br}
    return day[k]


for x in vit_list:
    r = rec(x['sujeto'], x['fecha'], x['fase'], x['br_day'], x['campana'])
    r.update({k: x[k] for k in PLAUS})
for x in sleep.values():
    rec(x['sujeto'], x['fecha'], x['fase'], x['br_day'], 'C1').update(
        {k: x[k] for k in ('sueno_h', 'sueno_eficiencia_pct', 'sueno_latencia_min')})
for c in cog.values():
    rec(c['sujeto'], c['fecha'], c['fase'], c['br_day'], c['campana']).update(
        {k: c[k] for k in c if k.startswith('cog_') or k in ('sesion_n', 'tipo_test')})
for t in tilt:
    if t['fecha']:
        rec(t['sujeto'], t['fecha'], t['fase'], t['br_day'], 'C3').update(
            {'tilt_aumento_pulso_lpm': t['aumento_pulso_lpm'], 'tilt_minutos_inclinado': t['minutos_inclinado_con_dato']})

A_all = dict(A)
offs = {}
for (s, d), x in day.items():
    if s not in A_all and x['fase'] == 'mision' and x['br_day'] is not None:
        offs.setdefault(s, []).append(d.toordinal() - int(x['br_day']))
for s, o in offs.items():
    A_all[s] = int(st.median(o))
for (s, d), x in day.items():
    a = A_all.get(s)
    x['dia_mision'] = d.toordinal() - a if a is not None else None
    if x['fase'] == 'mision' and x['dia_mision'] is not None and x['dia_mision'] <= 0:
        log('fase_corregida', s, f'{d}: etiquetado IN pero es anterior al día 1 -> pre')
        x['fase'] = 'pre'

subjects = sorted({s for s, _ in day})
aid = {s: f'UTMB-{i + 1:02d}' for i, s in enumerate(subjects)}
by_subj = {}
for (s, d), x in sorted(day.items(), key=lambda kv: kv[0]):
    x['astronauta_id'] = aid[s]
    by_subj.setdefault(s, []).append(x)

rng = random.Random(SEED)
RATE = 0.4  # mSv/day, within ~0.2-0.5 mSv/day reported for ISS (Shavers et al. 2023)
for s, recs in by_subj.items():
    hr_pre = [x['pulso_lpm'] for x in recs if x['fase'] == 'pre' and x.get('pulso_lpm')]
    hr_base = st.mean(hr_pre) if hr_pre else 70
    hrv_base, mood_base = rng.gauss(45, 12), rng.uniform(6.5, 8.0)
    L = mission_len.get(s) or max([x['dia_mision'] or 0 for x in recs if x['fase'] == 'mision'] or [1])
    for x in recs:
        dm = x['dia_mision'] or 0
        dip = 0.0
        if x['fase'] == 'mision':
            frac = min(1, max(0, dm / L))
            dip = 0.6 * frac + 0.8 * math.exp(-((frac - 0.75) ** 2) / 0.01)
        x['animo_0a10_sim'] = round(min(10, max(0, rng.gauss(mood_base - dip, 0.6))), 1)
        hr = x.get('pulso_lpm') or hr_base
        x['hrv_rmssd_ms_sim'] = round(max(8, hrv_base * math.exp(-0.025 * (hr - hr_base)) + rng.gauss(0, 4)), 1)
        x['spo2_pct_sim'] = round(min(100, max(93, rng.gauss(97.6, 0.7))), 1)
        x['radiacion_msv_dia_sim'] = RATE if x['fase'] == 'mision' else 0.0
        days_exposed = min(max(dm, 0), L) if x['fase'] == 'mision' else (L if x['fase'] == 'post' else 0)
        x['radiacion_msv_acum_sim'] = round(RATE * days_exposed, 2)   # calendar-based, not row-based

VARS = {'pulso_lpm': 6.0, 'pas_mmhg': 8.0, 'pad_mmhg': 6.0, 'temp_c': 0.3, 'peso_kg': 1.0, 'resp_rpm': 1.5, 'hrv_rmssd_ms_sim': 6.0}
bases = []
for s, recs in by_subj.items():
    pre = [x for x in recs if x['fase'] == 'pre']
    if sum(1 for x in pre if x.get('pulso_lpm') is not None) < 3:
        pre = [x for x in recs if x['fase'] == 'mision'][:7] or recs[:7]
    b = {'astronauta_id': aid[s], 'sujeto': s, 'n_dias_base': len(pre)}
    for v, floor in VARS.items():
        vals = [x[v] for x in pre if x.get(v) is not None]
        if len(vals) >= 2:
            m, sd = st.mean(vals), max(st.stdev(vals), floor)
            b[f'{v}_media'], b[f'{v}_de'] = round(m, 2), round(sd, 2)
            for x in recs:
                if x.get(v) is not None:
                    x[f'z_{v}'] = round((x[v] - m) / sd, 2)
    bases.append(b)
for x in day.values():
    zs = [x.get(f'z_{v}') for v in ('pulso_lpm', 'pas_mmhg', 'pad_mmhg', 'temp_c') if x.get(f'z_{v}') is not None]
    w = max(zs, key=abs) if zs else None
    x['estado_vitales'] = '' if w is None else ('verde' if abs(w) < 2 else ('amarillo' if abs(w) < 3 else 'rojo'))

daily_fields = ['astronauta_id', 'fuente', 'campana', 'sujeto', 'fecha', 'fase', 'br_day', 'dia_mision',
                'pulso_lpm', 'pas_mmhg', 'pad_mmhg', 'resp_rpm', 'temp_c', 'peso_kg',
                'sueno_h', 'sueno_eficiencia_pct', 'sueno_latencia_min',
                'tipo_test', 'sesion_n', 'cog_memoria_trabajo_ms', 'cog_memoria_trabajo_precision_pct', 'cog_matematica_ms',
                'cog_matematica_precision_pct', 'cog_emparejamiento_ms', 'cog_emparejamiento_precision_pct',
                'cog_codigo_diferido_ms', 'cog_codigo_diferido_precision_pct',
                'tilt_aumento_pulso_lpm', 'tilt_minutos_inclinado',
                'animo_0a10_sim', 'hrv_rmssd_ms_sim', 'spo2_pct_sim', 'radiacion_msv_dia_sim', 'radiacion_msv_acum_sim',
                'z_pulso_lpm', 'z_pas_mmhg', 'z_pad_mmhg', 'z_temp_c', 'z_peso_kg', 'estado_vitales']
daily = sorted(day.values(), key=lambda x: (x['astronauta_id'], x['fecha']))
write(os.path.join(OUT, 'demo_diario.csv'), [{**x, 'fecha': iso(x['fecha'])} for x in daily], daily_fields)
write(os.path.join(OUT, 'demo_lineas_base.csv'), bases,
      ['astronauta_id', 'sujeto', 'n_dias_base'] + [f'{v}_{k}' for v in VARS for k in ('media', 'de')])

for l in labs:
    l['astronauta_id'] = aid.get(l['sujeto'], f"UTMB-x{l['sujeto']}") if l['fuente'].startswith('UTMB') else f"I4-{l['sujeto']}"
write(os.path.join(OUT, 'demo_laboratorio.csv'), [{**l, 'fecha': iso(l['fecha'])} for l in labs],
      ['fuente', 'astronauta_id', 'sujeto', 'fecha', 'fase', 'dia_relativo', 'referencia_dia', 'analito', 'analito_original',
       'valor', 'marca_origen', 'unidad', 'unidad_mixta', 'rango_normal', 'atipico'])

SYM = [(r'head|^ha\b|cefalea', 'Dolor de cabeza'), (r'sleep|insomn', 'Dificultad para dormir'),
       (r'constip', 'Estreñimiento'), (r'dry skin|xerosis', 'Piel seca'), (r'dizz|vertig|lighthead', 'Mareo'),
       (r'nause|vomit', 'Náusea o vómito'), (r'back', 'Dolor de espalda'), (r'pain|sore|ache', 'Dolor (otro)'),
       (r'^other$', 'Otro')]
for e in ev:
    e['astronauta_id'] = aid.get(e['sujeto'], f"UTMB-x{e['sujeto']}")
    s = (e['sintoma'] or '').strip().lower()
    e['categoria'] = next((c for pat, c in SYM if re.search(pat, s)), e['sintoma'] or 'Sin dato')
ev.sort(key=lambda e: (e['astronauta_id'], iso(e['fecha'])))
write(os.path.join(OUT, 'demo_eventos.csv'), [{**e, 'fecha': iso(e['fecha'])} for e in ev],
      ['astronauta_id', 'sujeto', 'fecha', 'hora', 'fase', 'dia_mision', 'categoria', 'sintoma', 'dolor_0a10', 'descripcion', 'accion',
       'intervencion', 'resultado'])

prof = []
for s in subjects:
    recs = by_subj[s]
    has = lambda k: any(x.get(k) is not None for x in recs)
    prof.append({'astronauta_id': aid[s], 'fuente': 'UTMB (reposo en cama, análogo de microgravedad)', 'sujeto': s,
                 'campana': recs[0]['campana'], 'dias_totales': len(recs),
                 'dias_mision': sum(1 for x in recs if x['fase'] == 'mision'),
                 'vitales': 'si' if has('pulso_lpm') else 'no', 'sueno': 'si' if has('sueno_h') else 'no',
                 'cognicion': 'si' if has('cog_memoria_trabajo_ms') else 'no', 'tilt': 'si' if has('tilt_aumento_pulso_lpm') else 'no',
                 'laboratorio': 'si' if any(l['sujeto'] == s and l['fuente'].startswith('UTMB') for l in labs) else 'no',
                 'eventos': sum(1 for e in ev if e['sujeto'] == s)})
lab_only = sorted({l['sujeto'] for l in labs if l['fuente'].startswith('UTMB')} - set(subjects))
for s in lab_only:
    prof.append({'astronauta_id': f'UTMB-x{s}', 'fuente': 'UTMB (reposo en cama, análogo de microgravedad)', 'sujeto': s,
                 'campana': 'C3', 'dias_totales': '', 'dias_mision': '', 'vitales': 'no', 'sueno': 'no', 'cognicion': 'no',
                 'tilt': 'no', 'laboratorio': 'si', 'eventos': sum(1 for e in ev if e['sujeto'] == s)})
for sid in sorted({l['sujeto'] for l in labs if l['fuente'].startswith('Inspiration4')}):
    prof.append({'astronauta_id': f'I4-{sid}', 'fuente': 'Inspiration4 (vuelo real, 3 días, sept. 2021)', 'sujeto': sid,
                 'campana': 'Inspiration4', 'dias_totales': '', 'dias_mision': 3, 'vitales': 'no', 'sueno': 'no',
                 'cognicion': 'no', 'tilt': 'no', 'laboratorio': 'si', 'eventos': 0})
write(os.path.join(OUT, 'demo_astronautas.csv'), prof)
write(os.path.join(U, 'registro_correcciones.csv'), LOG, ['tipo', 'sujeto', 'detalle'])

# PhenoAge input coverage (subject-date with all 9)
PH = ['albumina', 'creatinina', 'glucosa', 'pcr', 'linfocitos_pct', 'vcm', 'rdw', 'fosfatasa_alcalina', 'leucocitos']
for src in ('UTMB', 'Inspiration4'):
    g = {}
    for l in labs:
        if l['fuente'].startswith(src) and l['analito'] in PH and not l['atipico']:
            g.setdefault((l['sujeto'], l['dia_relativo']), set()).add(l['analito'])
    full = sum(1 for v in g.values() if len(v) == 9)
    print(f'PhenoAge {src}: {full} de {len(g)} sujeto-fechas con las 9 entradas')
