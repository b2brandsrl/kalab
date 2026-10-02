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

from ipotesi import CATEGORIE, SCENARI, COSTI_B2B, STAGIONE, ACCORDI, NOTE_LEGGIMI

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
        8: f'=IF({BASE}="lordo",B{i},G{i})',
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
for j in (2, 9, 15, 16): wu.cell(row=r, column=j).fill = VER
SCONTRINO = f"'Conti per prodotto'!$B${r}"
QUOTA_ORD = f"'Conti per prodotto'!$I${r}"
MARG_ORD = f"'Conti per prodotto'!$O${r}"
r += 1
wu.cell(row=r, column=1, value="Letture: colonna O = quanto resta a Kalab per ordine dopo prodotto, imballo, spedizione e quota B2Brand. Se è vicino a zero o negativo, con quella quota Kalab lavora gratis.")

# ---------------------------------------------------------------- Costi B2Brand
wc = wb.create_sheet("Costi B2Brand")
hdr = ["Voce", "Una tantum (€)", "Mensile anno 1 (€)", "Mensile anno 2 (€)", "Mensile anno 3 (€)", "Fonte / nota"]
for j, h in enumerate(hdr, 1):
    c = wc.cell(row=1, column=j, value=h); c.font = B; c.fill = GRI; c.border = BOX
for i, v in enumerate(COSTI_B2B, 2):
    for j, x in enumerate([v["voce"], v["una_tantum"], v["m1"], v["m2"], v["m3"], v["fonte"]], 1):
        c = wc.cell(row=i, column=j, value=x); c.border = BOX
        if 2 <= j <= 5: c.fill = AZZ
lc = len(COSTI_B2B) + 1
wc.cell(row=lc + 1, column=1, value="TOTALE").font = B
for j, col in zip(range(2, 6), "BCDE"):
    c = wc.cell(row=lc + 1, column=j, value=f"=SUM({col}2:{col}{lc})"); c.fill = VER; c.font = B
wc.column_dimensions["A"].width = 44; wc.column_dimensions["F"].width = 70
for col in "BCDE": wc.column_dimensions[col].width = 18
SETUP = f"'Costi B2Brand'!$B${lc+1}"
MENS = {1: f"'Costi B2Brand'!$C${lc+1}", 2: f"'Costi B2Brand'!$D${lc+1}", 3: f"'Costi B2Brand'!$E${lc+1}"}

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
# tabella mensile per 36 mesi, per scenario
start = 12
wsc.cell(row=start - 1, column=1, value="Proiezione mese per mese (formule)").font = Font(bold=True, size=12)
cols = ["Mese", "Anno", "Ordini", "Incasso online (€)", "Quota B2Brand (€)", "Resta a Kalab lordo (€)",
        "Margine Kalab (€)", "Costi fissi B2Brand (€)", "Pubblicità (€)", "Risultato B2Brand mese (€)", "Cumulato B2Brand (€)"]
blocks = {}
for bi, s in enumerate(("Prudente", "Medio", "Ambizioso")):
    c0 = 1 + bi * (len(cols) + 1)
    blocks[s] = c0
    col_s = get_column_letter(2 + bi)  # B, C, D nelle ipotesi
    wsc.cell(row=start, column=c0, value=s).font = Font(bold=True, size=12)
    for j, h in enumerate(cols):
        c = wsc.cell(row=start + 1, column=c0 + j, value=h); c.font = B; c.fill = GRI; c.alignment = Alignment(wrap_text=True); c.border = BOX
    wsc.row_dimensions[start + 1].height = 42
    for m in range(1, 37):
        rr = start + 1 + m
        anno = (m - 1) // 12 + 1
        mese_cal = (STAGIONE["mese_avvio"] - 1 + (m - 1)) % 12 + 2  # riga in Stagionalità
        L = lambda k: get_column_letter(c0 + k)
        ordini_base = f"{col_s}${R0 + anno - 1}"
        rampa = f"{col_s}${R0 + 3}"
        if anno == 1:
            ordini = f"=ROUND({ordini_base}*MIN(1,{m}/{rampa})*Stagionalità!$B${mese_cal},0)"
        else:
            ordini = f"=ROUND({ordini_base}*Stagionalità!$B${mese_cal},0)"
        adv = f"={col_s}${R0 + 3 + anno}"
        vals = [m, anno, ordini,
                f"={L(2)}{rr}*{SCONTRINO}",
                f"={L(2)}{rr}*{QUOTA_ORD}",
                f"={L(3)}{rr}-{L(4)}{rr}",
                f"={L(2)}{rr}*{MARG_ORD}",
                f"={MENS[anno]}" + (f"+{SETUP}" if m == 1 else ""),
                adv,
                f"={L(4)}{rr}-{L(7)}{rr}-{L(8)}{rr}",
                f"={L(9)}{rr}" if m == 1 else f"={L(10)}{rr-1}+{L(9)}{rr}"]
        for j, v in enumerate(vals):
            c = wsc.cell(row=rr, column=c0 + j, value=v); c.border = BOX
            if j >= 3: c.number_format = "#,##0"
    # riepilogo
    rs = start + 1 + 36 + 2
    L = lambda k: get_column_letter(c0 + k)
    first, lastm = start + 2, start + 1 + 36
    rows = [
        ("Incasso online 12 mesi", f"=SUM({L(3)}{first}:{L(3)}{first+11})"),
        ("Incasso online 36 mesi", f"=SUM({L(3)}{first}:{L(3)}{lastm})"),
        ("Ordini 12 mesi", f"=SUM({L(2)}{first}:{L(2)}{first+11})"),
        ("Ordini 36 mesi", f"=SUM({L(2)}{first}:{L(2)}{lastm})"),
        ("Quota B2Brand 12 mesi", f"=SUM({L(4)}{first}:{L(4)}{first+11})"),
        ("Quota B2Brand 36 mesi", f"=SUM({L(4)}{first}:{L(4)}{lastm})"),
        ("Costi B2Brand 12 mesi (fissi+adv)", f"=SUM({L(7)}{first}:{L(8)}{first+11})"),
        ("Costi B2Brand 36 mesi (fissi+adv)", f"=SUM({L(7)}{first}:{L(8)}{lastm})"),
        ("Risultato B2Brand 12 mesi", f"={L(10)}{first+11}"),
        ("Risultato B2Brand 36 mesi", f"={L(10)}{lastm}"),
        ("Margine Kalab 12 mesi", f"=SUM({L(6)}{first}:{L(6)}{first+11})"),
        ("Margine Kalab 36 mesi", f"=SUM({L(6)}{first}:{L(6)}{lastm})"),
        ("Mese di rientro di B2Brand (cumulato ≥ 0 e resta)", f'=IFERROR(INDEX({L(0)}{first}:{L(0)}{lastm},MATCH(TRUE,INDEX({L(10)}{first}:{L(10)}{lastm}>=0,0),0)),"oltre 36 mesi")'),
        ("Esposizione massima di B2Brand (€)", f"=MIN(0,MIN({L(10)}{first}:{L(10)}{lastm}))"),
    ]
    for k, (lab, f) in enumerate(rows):
        wsc.cell(row=rs + k, column=c0, value=lab).font = B
        c = wsc.cell(row=rs + k, column=c0 + 3, value=f); c.fill = VER; c.number_format = "#,##0"
    for j in range(len(cols)):
        wsc.column_dimensions[get_column_letter(c0 + j)].width = 13 if j else 8

# ---------------------------------------------------------------- Confronto accordi
wa = wb.create_sheet("Confronto accordi")
wa.cell(row=1, column=1, value="Cosa succede a un ordine medio con diversi accordi (scenario medio, anno 1)").font = Font(bold=True, size=12)
hdr = ["Accordo", "Quota B2Brand sul lordo (equivalente)", "B2Brand per ordine (€)", "Kalab margine per ordine (€)", "Kalab margine % prezzo", "Commento"]
for j, h in enumerate(hdr, 1):
    c = wa.cell(row=2, column=j, value=h); c.font = B; c.fill = GRI; c.alignment = Alignment(wrap_text=True); c.border = BOX
wa.row_dimensions[2].height = 40
for i, a in enumerate(ACCORDI["alternative"], 3):
    wa.cell(row=i, column=1, value=a["nome"]).border = BOX
    c = wa.cell(row=i, column=2, value=a["quota"]); c.fill = AZZ; c.number_format = "0%"; c.border = BOX
    # B2Brand per ordine = scontrino * quota ; Kalab = scontrino_margine_pre_quota - quota
    wa.cell(row=i, column=3, value=f"={SCONTRINO}*B{i}").number_format = "0.00"
    wa.cell(row=i, column=4, value=f"={MARG_ORD}+{QUOTA_ORD}-C{i}").number_format = "0.00"
    wa.cell(row=i, column=5, value=f"=D{i}/{SCONTRINO}").number_format = "0%"
    wa.cell(row=i, column=6, value=a["commento"])
wa.column_dimensions["A"].width = 46; wa.column_dimensions["F"].width = 80
for col in "BCDE": wa.column_dimensions[col].width = 16

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scenari_kalab.xlsx")
wb.save(out)
print("scritto", out)
