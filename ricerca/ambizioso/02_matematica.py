# -*- coding: utf-8 -*-
"""Matematica del traguardo, scenario ambizioso Kalab (filone 2, 04/10/2026).
Solo stdlib, Python 3.9. Stampa le tabelle usate in ricerca/ambizioso/02_benchmark_e_numeri.md.
Uso: python3 ricerca/ambizioso/02_matematica.py   (legge margini e stagionalità da scenari/)"""

PESI = [0.85, 0.95, 1.00, 0.95, 0.85, 0.65, 0.65, 0.75, 1.00, 1.00, 1.35, 2.00]  # gen..dic, dal modello (ipotesi.py)
MESI = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
AVVIO = 3  # marzo 2027 = mese 1
REG = {1: 100, 2: 250, 3: 450}
POOL = 17.24     # margine da dividere a ordine, AOV 28,17 (modello)
AOV = 28.17
PIATTAFORMA = {1: 100, 2: 120, 3: 150}
ADV = {1: 500, 2: 1000, 3: 1500}


def cal(m):
    return (AVVIO - 1 + m - 1) % 12


def anno(m):
    return (m - 1) // 12 + 1


def etichetta(m):
    c = cal(m)
    y = 2027 + (AVVIO - 1 + m - 1) // 12
    return "%s %d" % (MESI[c], y)


def ordini_modello(m):
    a = anno(m)
    ramp = min(1.0, m / 6.0) if a == 1 else 1.0
    return round(REG[a] * ramp * PESI[cal(m)])


# --- percorso "liscio": anno 1 come il modello; anni 2-3 tendenza lineare continua con le stesse somme annue
mod = [ordini_modello(m) for m in range(1, 37)]
T = [sum(mod[0:12]), sum(mod[12:24]), sum(mod[24:36])]


def somma_pesata(start, a, b):
    # tendenza lineare da a (al mese start-1) a b (al mese start+11), pesata con la stagionalità
    s = 0.0
    for k in range(1, 13):
        m = start + k - 1
        s += PESI[cal(m)] * (a + (b - a) * k / 12.0)
    return s


def risolvi(start, a, totale):
    lo, hi = a, a * 10
    for _ in range(200):
        mid = (lo + hi) / 2
        if somma_pesata(start, a, mid) < totale:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


x24 = risolvi(13, 100.0, T[1])
x36 = risolvi(25, x24, T[2])


def tendenza(m):
    if m <= 12:
        return REG[1] * (min(1.0, m / 6.0))
    if m <= 24:
        return 100.0 + (x24 - 100.0) * (m - 12) / 12.0
    return x24 + (x36 - x24) * (m - 24) / 12.0


liscio = [mod[m - 1] if m <= 12 else tendenza(m) * PESI[cal(m)] for m in range(1, 37)]

# --- riacquisto: ordini di ritorno generati da OGNI cliente nuovo, mese per mese dopo il primo ordine
RIACQ = {
    "basso": (0.30, 0.12, 0.06),   # 20% ricompra x 1,5 ordini; poi 40% e 20% del primo anno
    "medio": (0.54, 0.22, 0.11),   # 30% x 1,8
    "alto": (0.80, 0.32, 0.16),    # 40% x 2,0
}


def curva(r12, r24, r36):
    c = [0.0] * 37  # c[k] = ordini di ritorno attesi k mesi dopo il primo ordine
    c[1] = 0.25 * r12
    c[2] = 0.125 * r12
    c[3] = 0.125 * r12
    for k in range(4, 13):
        c[k] = 0.50 * r12 / 9
    for k in range(13, 25):
        c[k] = r24 / 12
    for k in range(25, 37):
        c[k] = r36 / 12
    return c


def coorti(target, livello):
    c = curva(*RIACQ[livello])
    nuovi, ritorno = [], []
    for m in range(1, 37):
        r = sum(nuovi[j - 1] * c[m - j] for j in range(1, m))
        n = max(0.0, target[m - 1] - r)
        nuovi.append(n)
        ritorno.append(r)
    return nuovi, ritorno


def media(lst, a, b):
    return sum(lst[a - 1:b]) / (b - a + 1)


if __name__ == "__main__":
    print("Somme annue modello:", T, "| tendenza fine anno 2:", round(x24, 1), "fine anno 3:", round(x36, 1))
    print("\n== Percorso mese per mese: modello a gradini vs percorso liscio ==")
    for m in range(1, 37):
        print("%2d %-9s modello %4d  liscio %6.1f  (tendenza %6.1f)" % (m, etichetta(m), mod[m - 1], liscio[m - 1], tendenza(m)))
    print("somme liscio:", [round(sum(liscio[i:i + 12])) for i in (0, 12, 24)])

    print("\n== Trimestri (media mensile ordini) ==")
    for q in range(12):
        a, b = 3 * q + 1, 3 * q + 3
        print("T%-2d %s-%s  modello %6.1f  liscio %6.1f" % (q + 1, etichetta(a), etichetta(b), media(mod, a, b), media(liscio, a, b)))

    for liv in ("basso", "medio", "alto"):
        nuovi, rit = coorti(liscio, liv)
        print("\n== Coorti, riacquisto %s ==" % liv)
        for y in (1, 2, 3):
            a, b = 12 * (y - 1) + 1, 12 * y
            tot = sum(liscio[a - 1:b]); n = sum(nuovi[a - 1:b]); r = sum(rit[a - 1:b])
            print(" anno %d: ordini %5.0f  nuovi clienti %5.0f (%.0f/mese)  ordini di ritorno %5.0f (%.0f/mese)  quota ritorno %.0f%%" % (y, tot, n, n / 12, r, r / 12, 100 * r / tot))
        for q in range(12):
            a, b = 3 * q + 1, 3 * q + 3
            o = sum(liscio[a - 1:b]); r = sum(rit[a - 1:b]); n = sum(nuovi[a - 1:b])
            print("   T%-2d nuovi/mese %6.1f  ritorno/mese %6.1f  quota ritorno %4.0f%%" % (q + 1, n / 3, r / 3, 100 * r / o))
        # mesi di regime: dicembre di ogni anno
        for m in (10, 22, 34):
            print("   %s: ordini %.0f, nuovi %.0f, ritorno %.0f" % (etichetta(m), liscio[m - 1], nuovi[m - 1], rit[m - 1]))


# ---------------------------------------------------------------- parte 2: visite, email, pubblicità, ordine medio
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "scenari"))
from calcola import conti
from ipotesi import CATEGORIE


def pool_con_aov(aov, sped_cliente=None, f_imb=1.2, extra_sped=0.5):
    """Margine da dividere a ordine se l'ordine medio sale ad aov: prezzo e costo merce scalati,
    imballo +20%, spedizione vera +0,50 € (più peso). sped_cliente=None = come oggi (5,90 €)."""
    base = sum(c["prezzo"] * c["mix"] for c in CATEGORIE)
    f = aov / base
    tot = 0.0
    for c in CATEGORIE:
        if c["mix"] == 0:
            continue
        d = dict(c)
        d["prezzo"] = c["prezzo"] * f
        d["costo"] = c["costo"] * f
        if f > 1:
            d["imballo"] = c["imballo"] * f_imb
            d["sped_vera"] = c["sped_vera"] + extra_sped
        if sped_cliente is not None:
            d["sped_cliente"] = sped_cliente
        r = conti(d, 0.5, "netto")
        tot += (r["margine"] + r["quota"]) * c["mix"]
    return tot


def stampa_parte2():
    print("\n\n======== PARTE 2 ========")
    print("pool a 28,17 €:", round(pool_con_aov(28.17), 2))
    for a in (30, 33, 35, 38, 40):
        print("pool a %d €: spedizione pagata %.2f · spedizione gratis %.2f" % (a, pool_con_aov(a), pool_con_aov(a, sped_cliente=0.0)))

    print("\n== Visite al mese ==")
    for o in (100, 250, 450):
        print(o, [round(o / cr) for cr in (0.010, 0.015, 0.025)], "dicembre (x2):", [round(2 * o / cr) for cr in (0.010, 0.015, 0.025)])

    print("\n== Mesi di regime per anno (liscio), clienti nuovi e di ritorno ==")
    for liv in ("basso", "medio", "alto"):
        nuovi, rit = coorti(liscio, liv)
        for (a, b, nome) in ((7, 12, "anno1 regime set27-feb28"), (13, 24, "anno2"), (25, 36, "anno3")):
            o = media(liscio, a, b); n = media(nuovi, a, b); r = media(rit, a, b)
            print(" %-6s %-26s ordini/mese %5.0f nuovi %5.0f ritorno %5.0f (%.0f%%)" % (liv, nome, o, n, r, 100 * r / o))

    # pubblicità
    print("\n== Pubblicità: quanti clienti nuovi compra il budget ==")
    nuovi_m, _ = coorti(liscio, "medio")
    for (y, a, b) in ((1, 7, 12), (2, 13, 24), (3, 25, 36)):
        n = media(nuovi_m, a, b)
        for cac in (25, 35, 50):
            da_adv = ADV[y] / cac
            print(" anno %d budget %4d €: CAC %d € -> %5.1f clienti nuovi/mese = %4.0f%% dei %5.0f che servono; per comprarli tutti servirebbero %6.0f €/mese" % (y, ADV[y], cac, da_adv, 100 * da_adv / n, n, n * cac))
    for y in (1, 2, 3):
        for cpc in (0.55, 0.70, 1.00):
            print(" anno %d: visite pagate con %d € a CPC %.2f = %5.0f" % (y, ADV[y], cpc, ADV[y] / cpc))
    for aov, cr in ((28.17, 0.015), (28.17, 0.02), (33, 0.018), (40, 0.02), (40, 0.025)):
        p = pool_con_aov(aov)
        print(" margine per visita: AOV %.2f CR %.1f%% -> %.2f €/visita (solo primo ordine); con riacquisto medio x1,54 nei 12 mesi -> %.2f" % (aov, 100 * cr, p * cr, p * cr * 1.54))

    # email
    print("\n== Email: lista che serve per avere il 20% degli ordini dall'email ==")
    for o, quota in ((100, 0.15), (100, 0.20), (250, 0.20), (250, 0.25), (450, 0.25)):
        vis = o / 0.015
        flussi = vis * 0.02 * 0.02 + o * (0.7022 / 0.2978) * 0.35 * 0.03
        for por in (0.0008, 0.0017, 0.0026):
            camp = max(0.0, o * quota - flussi)
            L = camp / (4 * por)
            print(" ordini %d, quota email %.0f%%: flussi %.1f ordini; campagne %.1f ordini; POR %.2f%% -> lista %6.0f" % (o, 100 * quota, flussi, camp, 100 * por, L))


def simula_kpi():
    print("\n== KPI per trimestre ==")
    CR = [0.008, 0.010, 0.012, 0.015, 0.014, 0.014, 0.016, 0.019, 0.017, 0.017, 0.019, 0.022]
    AOVQ = [28, 28, 30, 33, 31, 31, 33, 36, 34, 34, 36, 40]
    nuovi, rit = coorti(liscio, "medio")
    lista = 0.0
    for q in range(12):
        a, b = 3 * q + 1, 3 * q + 3
        o = media(liscio, a, b)
        vis = o / CR[q]
        y = anno(a)
        for m in range(a, b + 1):
            v = liscio[m - 1] / CR[q]
            lista = lista * (1 - 0.015) + v * 0.02 + nuovi[m - 1] * 0.30
        camp = lista * 4 * 0.0017
        flussi = vis * 0.02 * 0.02 + o * (0.7022 / 0.2978) * 0.35 * 0.03
        quota_email = min(1.0, (camp + flussi) / o)
        r = media(rit, a, b)
        p = pool_con_aov(AOVQ[q])
        guad = o * p - ADV[y] - PIATTAFORMA[y]
        vend = o * AOVQ[q]
        print("T%-2d %s-%s ordini %5.0f (dic/picco %4.0f) visite %6.0f CR %.1f%% AOV %d € vendite/mese %6.0f € ritorno %3.0f%% lista fine %5.0f email %3.0f%% pool %.2f guadagno/mese %6.0f € (a testa %5.0f)" % (
            q + 1, etichetta(a), etichetta(b), o, max(liscio[a - 1:b]), vis, 100 * CR[q], AOVQ[q], vend, 100 * r / o, lista, 100 * quota_email, p, guad, guad / 2))


if __name__ == "__main__":
    stampa_parte2()
    simula_kpi()
