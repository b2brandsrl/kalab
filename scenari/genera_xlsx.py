#!/usr/bin/env python3
"""Genera scenari_kalab.xlsx: modello di fattibilità con ipotesi modificabili.

Tutte le celle AZZURRE sono ipotesi che Davide può cambiare; il resto è formula.
I valori di partenza sono quelli del report (REPORT_fattibilita_kalab.md), con la fonte accanto.
Eseguire: python3 scenari/genera_xlsx.py  → scrive scenari_kalab.xlsx nella cartella del progetto.
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

from ipotesi import CATEGORIE, SCENARI, COSTI_B2B, STAGIONE, ACCORDI, NOTE_LEGGIMI, CORSA_HUB, TRE_PL

AZZ = PatternFill("solid", fgColor="DDEBF7")   # ipotesi modificabile
GRI = PatternFill("solid", fgColor="F2F2F2")   # intestazione
VER = PatternFill("solid", fgColor="E2EFDA")   # risultato chiave
B = Font(bold=True)
thin = Side(style="thin", color="BFBFBF")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)

wb = Workbook()

# ---------------------------------------------------------------- Leggimi
ws = wb.active; ws.title = "Leggimi"
ws.column_dimensions["A"].width = 110
for i, riga in enumerate(NOTE_LEGGIMI, 1):
    c = ws.cell(row=i, column=1, value=riga)
    if i == 1: c.font = Font(bold=True, size=14)
    c.alignment = Alignment(wrap_text=True, vertical="top")

# ---------------------------------------------------------------- Ipotesi per categoria
wi = wb.create_sheet("Ipotesi")
hdr = ["Categoria", "Prezzo medio al pubblico (€, IVA incl.)", "IVA %", "Costo prodotto (€)", "Imballo (€)",
       "Spedizione pagata dal cliente (€)", "Spedizione costo vero (€)", "Commissione pagamento %",
       "Commissione pagamento fissa (€)", "Tasso resi/perdite %", "Quota del mix ordini %", "Fonte / nota"]
for j, h in enumerate(hdr, 1):
    c = wi.cell(row=1, column=j, value=h); c.font = B; c.fill = GRI; c.alignment = Alignment(wrap_text=True); c.border = BOX
wi.row_dimensions[1].height = 48
for i, cat in enumerate(CATEGORIE, 2):
    vals = [cat["nome"], cat["prezzo"], cat["iva"], cat["costo"], cat["imballo"], cat["sped_cliente"],
            cat["sped_vera"], cat["comm_pct"], cat["comm_fix"], cat["resi"], cat["mix"], cat["fonte"]]
    for j, v in enumerate(vals, 1):
        c = wi.cell(row=i, column=j, value=v); c.border = BOX
        if 2 <= j <= 11: c.fill = AZZ
wi.column_dimensions["A"].width = 26; wi.column_dimensions["L"].width = 70
for col in "BCDEFGHIJK": wi.column_dimensions[col].width = 14
n_cat = len(CATEGORIE); last = n_cat + 1
r = last + 2
wi.cell(row=r, column=1, value="Controllo: il mix deve fare 100%").font = B
wi.cell(row=r, column=11, value=f"=SUM(K2:K{last})").fill = VER
r += 2
wi.cell(row=r, column=1, value="Quota B2Brand sull'incasso (ipotesi base)").font = B
wi.cell(row=r, column=2, value=ACCORDI["quota_base"]).fill = AZZ
wi.cell(row=r, column=3, value="Il 50% proposto da Kalab. Cambiare qui per vedere l'effetto ovunque.")
QUOTA = f"Ipotesi!$B${r}"
r += 1
wi.cell(row=r, column=1, value="Base di calcolo della quota").font = B
wi.cell(row=r, column=2, value=ACCORDI["base"]).fill = AZZ
wi.cell(row=r, column=3, value='"lordo" = sull\'incasso IVA inclusa; "netto" = incasso senza IVA, senza spedizione incassata, senza commissioni di pagamento')
BASE = f"Ipotesi!$B${r}"
r += 1
wi.cell(row=r, column=1, value="Obiettivo B2Brand: euro di cassa al mese").font = B
wi.cell(row=r, column=2, value=ACCORDI.get("obiettivo_mese", 1000)).fill = AZZ
wi.cell(row=r, column=3, value="Quota incassata meno spese vive e pubblicità, prima delle tasse. Le ore di B2Brand sono a parte (foglio Scenari, colonne «costo pieno»).")
OBIETTIVO = f"Ipotesi!$B${r}"

# ---------------------------------------------------------------- Unit economics
wu = wb.create_sheet("Conti per prodotto")
hdr = ["Categoria", "Prezzo pubblico", "IVA", "Netto IVA", "Spedizione incassata", "Commissioni pagamento",
       "Incasso netto (base 'netto')", "Base di calcolo quota", "Quota B2Brand (€)", "Resta a Kalab (lordo)",
       "Costo prodotto", "Imballo", "Spedizione vera", "Perdite per resi", "Margine Kalab (€)", "Margine Kalab % sul prezzo",
       "Margine Kalab % sul suo incasso"]
for j, h in enumerate(hdr, 1):
    c = wu.cell(row=1, column=j, value=h); c.font = B; c.fill = GRI; c.alignment = Alignment(wrap_text=True); c.border = BOX
wu.row_dimensions[1].height = 48
for i in range(2, last + 1):
    I = f"Ipotesi!"
    f = {
        1: f"={I}A{i}",
        2: f"={I}B{i}",
        3: f"=B{i}-B{i}/(1+{I}C{i})",
        4: f"=B{i}-C{i}",
        5: f"={I}F{i}",
        6: f"=(B{i}+E{i})*{I}H{i}+{I}I{i}",
        7: f"=D{i}-F{i}",
        8: f'=IF({BASE}="lordo",B{i}+E{i},G{i})',
        9: f"=H{i}*{QUOTA}",
        10: f"=D{i}+E{i}-F{i}-I{i}",
        11: f"={I}D{i}",
        12: f"={I}E{i}",
        13: f"={I}G{i}",
        14: f"=(B{i}+{I}G{i})*{I}J{i}",
        15: f"=J{i}-K{i}-L{i}-M{i}-N{i}",
        16: f"=O{i}/B{i}",
        17: f"=IF(J{i}=0,0,O{i}/J{i})",
    }
    for j, v in f.items():
        c = wu.cell(row=i, column=j, value=v); c.border = BOX
        if j in (9, 15): c.fill = VER
        if j in (16, 17): c.number_format = "0%"
        elif j >= 2: c.number_format = "0.00"
wu.column_dimensions["A"].width = 26
for j in range(2, 18): wu.column_dimensions[get_column_letter(j)].width = 13
r = last + 2
wu.cell(row=r, column=1, value="Medie pesate sul mix ordini").font = B
wu.cell(row=r, column=2, value=f"=SUMPRODUCT(B2:B{last},Ipotesi!K2:K{last})").number_format = "0.00"
wu.cell(row=r, column=9, value=f"=SUMPRODUCT(I2:I{last},Ipotesi!K2:K{last})").number_format = "0.00"
wu.cell(row=r, column=15, value=f"=SUMPRODUCT(O2:O{last},Ipotesi!K2:K{last})").number_format = "0.00"
wu.cell(row=r, column=16, value=f"=O{r}/B{r}").number_format = "0%"
wu.cell(row=r, column=7, value=f"=SUMPRODUCT(G2:G{last},Ipotesi!K2:K{last})").number_format = "0.00"
wu.cell(row=r, column=8, value=f"=SUMPRODUCT((B2:B{last}+E2:E{last}),Ipotesi!K2:K{last})").number_format = "0.00"
wu.cell(row=r, column=12, value=f"=SUMPRODUCT(L2:L{last},Ipotesi!K2:K{last})").number_format = "0.00"
wu.cell(row=r, column=13, value=f"=SUMPRODUCT(M2:M{last},Ipotesi!K2:K{last})").number_format = "0.00"
wu.cell(row=r + 2, column=1, value="Medie pesate: G = incassato netto medio per ordine; H = incasso lordo medio (merce + spedizione); L = imballo medio; M = spedizione vera media.")
for j in (2, 7, 8, 9, 15, 16): wu.cell(row=r, column=j).fill = VER
SCONTRINO = f"'Conti per prodotto'!$B${r}"
QUOTA_ORD = f"'Conti per prodotto'!$I${r}"
MARG_ORD = f"'Conti per prodotto'!$O${r}"
NETTO_MEDIO = f"'Conti per prodotto'!$G${r}"
LORDO_MEDIO = f"'Conti per prodotto'!$H${r}"
r += 1
wu.cell(row=r, column=1, value="Letture: colonna O = quanto resta a Kalab per ordine dopo prodotto, imballo, spedizione e quota B2Brand. Se è vicino a zero o negativo, con quella quota Kalab lavora gratis.")

# ---------------------------------------------------------------- Costi B2Brand
wc = wb.create_sheet("Costi B2Brand")
hdr = ["Voce", "Una tantum (€)", "Mensile anno 1 (€)", "Mensile anno 2 (€)", "Mensile anno 3 (€)", "Fonte / nota", "Tipo (cassa = soldi che escono; ore = tempo di B2Brand a 35 €/h)"]
for j, h in enumerate(hdr, 1):
    c = wc.cell(row=1, column=j, value=h); c.font = B; c.fill = GRI; c.border = BOX
for i, v in enumerate(COSTI_B2B, 2):
    for j, x in enumerate([v["voce"], v["una_tantum"], v["m1"], v["m2"], v["m3"], v["fonte"], v["tipo"]], 1):
        c = wc.cell(row=i, column=j, value=x); c.border = BOX
        if 2 <= j <= 5: c.fill = AZZ
lc = len(COSTI_B2B) + 1
wc.cell(row=lc + 1, column=1, value="TOTALE").font = B
for j, col in zip(range(2, 6), "BCDE"):
    c = wc.cell(row=lc + 1, column=j, value=f"=SUM({col}2:{col}{lc})"); c.fill = VER; c.font = B
wc.cell(row=lc + 2, column=1, value="di cui SOLO CASSA").font = B
for j, col in zip(range(2, 6), "BCDE"):
    c = wc.cell(row=lc + 2, column=j, value=f'=SUMIF($G$2:$G${lc},"cassa",{col}2:{col}{lc})'); c.fill = VER
wc.cell(row=lc + 3, column=1, value="Nel foglio Scenari le spese vive (cassa) e le ore sono in colonne separate: «netto di cassa» = soldi in tasca; «costo pieno» = anche le ore pagate a 35 €/h.")
wc.column_dimensions["A"].width = 44; wc.column_dimensions["F"].width = 70; wc.column_dimensions["G"].width = 20
for col in "BCDE": wc.column_dimensions[col].width = 18
CASSA_SETUP = f"'Costi B2Brand'!$B${lc+2}"
ORE_SETUP = f"('Costi B2Brand'!$B${lc+1}-'Costi B2Brand'!$B${lc+2})"
CASSA_MENS = {a: f"'Costi B2Brand'!${c}${lc+2}" for a, c in ((1, "C"), (2, "D"), (3, "E"))}
ORE_MENS = {a: f"('Costi B2Brand'!${c}${lc+1}-'Costi B2Brand'!${c}${lc+2})" for a, c in ((1, "C"), (2, "D"), (3, "E"))}

# ---------------------------------------------------------------- Stagionalità
wsg = wb.create_sheet("Stagionalità")
wsg.cell(row=1, column=1, value="Mese").font = B
wsg.cell(row=1, column=2, value="Peso del mese (media = 1,00)").font = B
wsg.cell(row=1, column=3, value="Nota").font = B
mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
for i, (m, p, nota) in enumerate(zip(mesi, STAGIONE["pesi"], STAGIONE["note"]), 2):
    wsg.cell(row=i, column=1, value=m)
    c = wsg.cell(row=i, column=2, value=p); c.fill = AZZ
    wsg.cell(row=i, column=3, value=nota)
wsg.cell(row=14, column=1, value="Somma (deve fare 12)").font = B
wsg.cell(row=14, column=2, value="=SUM(B2:B13)").fill = VER
wsg.column_dimensions["C"].width = 80

# ---------------------------------------------------------------- Scenari
wsc = wb.create_sheet("Scenari")
wsc.cell(row=1, column=1, value="Ipotesi per scenario (celle azzurre)").font = Font(bold=True, size=12)
hdr = ["Parametro", "Prudente", "Medio", "Ambizioso", "Nota"]
for j, h in enumerate(hdr, 1):
    c = wsc.cell(row=2, column=j, value=h); c.font = B; c.fill = GRI; c.border = BOX
righe = [
    ("Ordini al mese, media anno 1", "ordini1"),
    ("Ordini al mese, media anno 2", "ordini2"),
    ("Ordini al mese, media anno 3", "ordini3"),
    ("Mesi di rampa prima del regime (anno 1)", "rampa"),
    ("Budget pubblicità mensile anno 1 (€, pagato da B2Brand)", "adv1"),
    ("Budget pubblicità mensile anno 2 (€)", "adv2"),
    ("Budget pubblicità mensile anno 3 (€)", "adv3"),
]
for i, (lab, k) in enumerate(righe, 3):
    wsc.cell(row=i, column=1, value=lab).border = BOX
    for j, s in enumerate(("prudente", "medio", "ambizioso"), 2):
        c = wsc.cell(row=i, column=j, value=SCENARI[s][k]); c.fill = AZZ; c.border = BOX
    wsc.cell(row=i, column=5, value=SCENARI["note"].get(k, ""))
wsc.column_dimensions["A"].width = 52; wsc.column_dimensions["E"].width = 70
R0 = 3  # riga ordini1
# ordini necessari per l'obiettivo
wsc.cell(row=10, column=1, value="Ordini al mese necessari per l'obiettivo, anno 1").font = B
wsc.cell(row=11, column=1, value="Ordini al mese necessari per l'obiettivo, anno 2").font = B
wsc.cell(row=12, column=1, value="Ordini al mese necessari per l'obiettivo, anno 3").font = B
for bi in range(3):
    col_s = get_column_letter(2 + bi)
    for a in (1, 2, 3):
        c = wsc.cell(row=9 + a, column=2 + bi, value=f"=ROUND(({OBIETTIVO}+{CASSA_MENS[a]}+{col_s}${R0 + 3 + a})/{QUOTA_ORD},0)")
        c.fill = VER; c.border = BOX
wsc.cell(row=10, column=5, value="= (obiettivo + spese vive del mese + pubblicità dello scenario) ÷ quota di B2Brand per ordine. Le ore di B2Brand non sono contate.")
start = 16
wsc.cell(row=start - 1, column=1, value="Proiezione mese per mese (formule). Netto di cassa = soldi in tasca a B2Brand; costo pieno = anche le ore a 35 €/h.").font = Font(bold=True, size=12)
cols = ["Mese", "Anno", "Ordini", "Incasso online (€)", "Quota B2Brand (€)", "Margine Kalab (€)",
        "Spese vive B2Brand (€)", "Pubblicità (€)", "Netto di cassa B2Brand (€)", "Cumulato di cassa (€)",
        "Ore interne (valore €)", "Netto a costo pieno (€)", "Cumulato a costo pieno (€)",
        "(appoggio) mese sopra obiettivo", "(appoggio) mese cassa in attivo", "(appoggio) mese costo pieno in attivo"]
for bi, s in enumerate(("Prudente", "Medio", "Ambizioso")):
    c0 = 1 + bi * (len(cols) + 1)
    col_s = get_column_letter(2 + bi)  # B, C, D nelle ipotesi
    wsc.cell(row=start, column=c0, value=s).font = Font(bold=True, size=12)
    for j, h in enumerate(cols):
        c = wsc.cell(row=start + 1, column=c0 + j, value=h); c.font = B; c.fill = GRI; c.alignment = Alignment(wrap_text=True); c.border = BOX
    wsc.row_dimensions[start + 1].height = 42
    L = lambda k: get_column_letter(c0 + k)
    for m in range(1, 37):
        rr = start + 1 + m
        anno = (m - 1) // 12 + 1
        mese_cal = (STAGIONE["mese_avvio"] - 1 + (m - 1)) % 12 + 2  # riga in Stagionalità
        ordini_base = f"{col_s}${R0 + anno - 1}"
        rampa = f"{col_s}${R0 + 3}"
        if anno == 1:
            ordini = f"=ROUND({ordini_base}*MIN(1,{m}/{rampa})*Stagionalità!$B${mese_cal},0)"
        else:
            ordini = f"=ROUND({ordini_base}*Stagionalità!$B${mese_cal},0)"
        vals = [m, anno, ordini,
                f"={L(2)}{rr}*{SCONTRINO}",
                f"={L(2)}{rr}*{QUOTA_ORD}",
                f"={L(2)}{rr}*{MARG_ORD}",
                f"={CASSA_MENS[anno]}" + (f"+{CASSA_SETUP}" if m == 1 else ""),
                f"={col_s}${R0 + 3 + anno}",
                f"={L(4)}{rr}-{L(6)}{rr}-{L(7)}{rr}",
                f"={L(8)}{rr}" if m == 1 else f"={L(9)}{rr-1}+{L(8)}{rr}",
                f"={ORE_MENS[anno]}" + (f"+{ORE_SETUP}" if m == 1 else ""),
                f"={L(8)}{rr}-{L(10)}{rr}",
                f"={L(11)}{rr}" if m == 1 else f"={L(12)}{rr-1}+{L(11)}{rr}",
                f'=IF({L(8)}{rr}>={OBIETTIVO},{L(0)}{rr},"")',
                f'=IF(AND({L(0)}{rr}>1,{L(9)}{rr}>=0),{L(0)}{rr},"")',
                f'=IF(AND({L(0)}{rr}>1,{L(12)}{rr}>=0),{L(0)}{rr},"")']
        for j, v in enumerate(vals):
            c = wsc.cell(row=rr, column=c0 + j, value=v); c.border = BOX
            if 3 <= j <= 12: c.number_format = "#,##0"
            if j == 8: c.fill = VER
            if j >= 13: c.font = Font(color="808080")
    rs = start + 1 + 36 + 2
    first, lastm = start + 2, start + 1 + 36
    def anno_rng(k, a): return f"{L(k)}{first + 12*(a-1)}:{L(k)}{first + 12*a - 1}"
    rows = [
        ("Ordini anno 1 / 2 / 3", [f"=SUM({anno_rng(2,a)})" for a in (1, 2, 3)]),
        ("Incasso online anno 1 / 2 / 3", [f"=SUM({anno_rng(3,a)})" for a in (1, 2, 3)]),
        ("Quota B2Brand anno 1 / 2 / 3", [f"=SUM({anno_rng(4,a)})" for a in (1, 2, 3)]),
        ("Netto di CASSA B2Brand anno 1 / 2 / 3", [f"=SUM({anno_rng(8,a)})" for a in (1, 2, 3)]),
        ("…media al mese", [f"=SUM({anno_rng(8,a)})/12" for a in (1, 2, 3)]),
        ("Netto a COSTO PIENO anno 1 / 2 / 3", [f"=SUM({anno_rng(11,a)})" for a in (1, 2, 3)]),
        ("Margine Kalab anno 1 / 2 / 3", [f"=SUM({anno_rng(5,a)})" for a in (1, 2, 3)]),
        ("Primo mese con netto di cassa ≥ obiettivo", [f'=IF(MIN({L(13)}{first}:{L(13)}{lastm})=0,"oltre 36",MIN({L(13)}{first}:{L(13)}{lastm}))']),
        ("Primo mese col cumulato di cassa ≥ 0", [f'=IF(MIN({L(14)}{first}:{L(14)}{lastm})=0,"oltre 36",MIN({L(14)}{first}:{L(14)}{lastm}))']),
        ("Primo mese col cumulato a costo pieno ≥ 0", [f'=IF(MIN({L(15)}{first}:{L(15)}{lastm})=0,"oltre 36",MIN({L(15)}{first}:{L(15)}{lastm}))']),
        ("Esposizione massima di cassa (€)", [f"=MIN(0,MIN({L(9)}{first}:{L(9)}{lastm}))"]),
    ]
    for k, (lab, fs) in enumerate(rows):
        wsc.cell(row=rs + k, column=c0, value=lab).font = B
        for i2, f in enumerate(fs):
            c = wsc.cell(row=rs + k, column=c0 + 3 + i2, value=f); c.fill = VER; c.number_format = "#,##0"
    for j in range(len(cols)):
        wsc.column_dimensions[get_column_letter(c0 + j)].width = 13 if j else 8

# ---------------------------------------------------------------- Logistica: corsa all'hub vs magazzino conto terzi
wl = wb.create_sheet("Logistica")
wl.cell(row=1, column=1, value="Corsa pomeridiana all'hub contro magazzino conto terzi (3PL), per prodotti non deperibili").font = Font(bold=True, size=12)
par = [
    ("Km di andata Scalea → hub (Battipaglia)", CORSA_HUB["km_andata"], "rome2rio, 149 km, 1 h 44 (letto il 04/10/2026)"),
    ("Ore di guida di andata", CORSA_HUB["ore_andata"], "rome2rio 1 h 44; arrotondato"),
    ("Carburante di andata (€)", CORSA_HUB["carburante_andata"], "rome2rio 24-35 € a tratta"),
    ("Usura, gomme, manutenzione (€/km)", CORSA_HUB["usura_km"], "STIMA"),
    ("Ore al deposito (consegna pacchi)", CORSA_HUB["ore_al_deposito"], "STIMA"),
    ("Corse al mese", CORSA_HUB["giorni_al_mese"], "una ogni giorno lavorativo"),
    ("Valore di un'ora di chi guida (€)", CORSA_HUB["valore_ora"], "IPOTESI: un'ora tolta al campo o al laboratorio"),
    ("3PL: picking + packing per ordine (€)", TRE_PL["pick_pack"], "Tissquad 01/04/2026: picking 0,80-1,50 + packing 0,50-1,00"),
    ("3PL: materiali per pacco (€)", TRE_PL["materiali"], "Tissquad: 0,50-1,00"),
    ("3PL: costo di un pallet al mese (€)", TRE_PL["pallet_mese"], "Tissquad: 25-50 €/pallet/mese"),
    ("3PL: pallet occupati", TRE_PL["pallet_n"], "IPOTESI: 2 pallet di vasetti bastano per 2-3 mesi"),
    ("3PL: rifornimento al mese da Scalea (€)", TRE_PL["rifornimento_mese"], "STIMA: una corsa al mese o un bancale col corriere"),
    ("3PL: spedizione dall'hub, 0-2 kg (€)", TRE_PL["spedizione_da_hub"], "Tissquad: Nord 3,50-5,00; da Scalea oggi 7-7,50 (03)"),
]
for i, (lab, v, nota) in enumerate(par, 3):
    wl.cell(row=i, column=1, value=lab).border = BOX
    c = wl.cell(row=i, column=2, value=v); c.fill = AZZ; c.border = BOX
    wl.cell(row=i, column=3, value=nota)
P = {k: f"Logistica!$B${3+i}" for i, k in enumerate(["km", "ore", "carb", "usura", "dep", "corse", "ora", "pp", "mat", "pallet", "npallet", "rifo", "sped3pl"])}
r = 3 + len(par) + 1
wl.cell(row=r, column=1, value="Una corsa (andata e ritorno): euro").font = B
wl.cell(row=r, column=2, value=f"=2*{P['carb']}+2*{P['km']}*{P['usura']}").fill = VER
wl.cell(row=r+1, column=1, value="Una corsa: ore").font = B
wl.cell(row=r+1, column=2, value=f"=2*{P['ore']}+{P['dep']}").fill = VER
wl.cell(row=r+2, column=1, value="Al mese: euro / ore").font = B
wl.cell(row=r+2, column=2, value=f"=B{r}*{P['corse']}").fill = VER
wl.cell(row=r+2, column=3, value=f"=B{r+1}*{P['corse']}").fill = VER
CORSA_MESE = f"Logistica!$B${r+2}"; ORE_MESE = f"Logistica!$C${r+2}"
r += 4
hdr = ["Ordini al mese", "Corsa: € per ordine", "Corsa con il tempo: € per ordine", "3PL: € per ordine", "3PL meno risparmio di spedizione e imballo"]
for j, h in enumerate(hdr, 1):
    c = wl.cell(row=r, column=j, value=h); c.font = B; c.fill = GRI; c.alignment = Alignment(wrap_text=True); c.border = BOX
wl.row_dimensions[r].height = 36
risparmio = f"('Conti per prodotto'!$M${last+2}-{P['sped3pl']})"
for k, o in enumerate((50, 100, 150, 300, 600, 1000), 1):
    rr = r + k
    wl.cell(row=rr, column=1, value=o).fill = AZZ
    wl.cell(row=rr, column=2, value=f"={CORSA_MESE}/A{rr}").number_format = "0.00"
    wl.cell(row=rr, column=3, value=f"=({CORSA_MESE}+{ORE_MESE}*{P['ora']})/A{rr}").number_format = "0.00"
    wl.cell(row=rr, column=4, value=f"={P['pp']}+{P['mat']}+({P['pallet']}*{P['npallet']}+{P['rifo']})/A{rr}").number_format = "0.00"
    wl.cell(row=rr, column=5, value=f"=D{rr}-{risparmio}-'Conti per prodotto'!$L${last+2}").number_format = "0.00"
wl.cell(row=r + 8, column=1, value="Lettura: la corsa costa uguale con 50 o con 1.000 ordini, quindi pesa per ordine solo quando i volumi sono alti. Il 3PL costa per ordine ma toglie l'imballo e la spedizione da Calabria (più cara e con un giorno in più). Colonna E: costo netto del 3PL rispetto a spedire da Scalea; vicino a zero = conviene già.")
wl.column_dimensions["A"].width = 46; wl.column_dimensions["C"].width = 60
for col in "BDE": wl.column_dimensions[col].width = 18

# ---------------------------------------------------------------- Confronto accordi
wa = wb.create_sheet("Confronto accordi")
wa.cell(row=1, column=1, value="Cosa succede a un ordine medio con diversi accordi (scenario medio, anno 1)").font = Font(bold=True, size=12)
hdr = ["Accordo", "Base (lordo/netto)", "Quota %", "B2Brand per ordine (€)", "Kalab margine per ordine (€)", "Kalab margine % prezzo", "Commento"]
for j, h in enumerate(hdr, 1):
    c = wa.cell(row=2, column=j, value=h); c.font = B; c.fill = GRI; c.alignment = Alignment(wrap_text=True); c.border = BOX
wa.row_dimensions[2].height = 40
for i, a in enumerate(ACCORDI["alternative"], 3):
    wa.cell(row=i, column=1, value=a["nome"]).border = BOX
    c = wa.cell(row=i, column=2, value=a["base"]); c.fill = AZZ; c.border = BOX
    c = wa.cell(row=i, column=3, value=a["quota"]); c.fill = AZZ; c.number_format = "0%"; c.border = BOX
    wa.cell(row=i, column=4, value=f'=IF(B{i}="lordo",{LORDO_MEDIO},{NETTO_MEDIO})*C{i}').number_format = "0.00"
    wa.cell(row=i, column=5, value=f"={MARG_ORD}+{QUOTA_ORD}-D{i}").number_format = "0.00"
    wa.cell(row=i, column=6, value=f"=E{i}/{SCONTRINO}").number_format = "0%"
    wa.cell(row=i, column=7, value=a["commento"])
    wa.cell(row=i, column=4).fill = VER; wa.cell(row=i, column=5).fill = VER
wa.cell(row=len(ACCORDI["alternative"]) + 4, column=1, value="Lettura: l'ordine medio è quello del foglio Conti (mix di categorie). Il margine di Kalab è dopo prodotto, imballo, spedizione vera e perdite. Per vedere l'effetto sui 36 mesi, cambiare quota e base nel foglio Ipotesi.")
wa.column_dimensions["A"].width = 52; wa.column_dimensions["G"].width = 80
for col in "BCDEF": wa.column_dimensions[col].width = 14

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scenari_kalab.xlsx")
wb.save(out)
print("scritto", out)
