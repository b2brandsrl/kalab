#!/usr/bin/env python3
"""Gemello in Python del foglio Excel: stessi conti, stampa i risultati per il report.

Uso:  python3 scenari/calcola.py [margine|percentuale] [quota] [lordo|netto]
      (senza argomenti usa i valori di ipotesi.ACCORDI)

Due modelli di accordo:
- «percentuale»: B2Brand prende una quota della base (merce netta o tutto l'incasso) e paga lei
  pubblicità e piattaforma.
- «margine»: metà a testa di quello che resta dopo prodotto, imballo, spedizione, commissioni,
  pubblicità e piattaforma. B2Brand anticipa i costi e se li riprende per prima nei mesi buoni;
  Kalab non mette mai soldi di tasca (al peggio, in un mese, rientra solo dei costi del prodotto).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ipotesi import CATEGORIE, SCENARI, COSTI_B2B, STAGIONE, ACCORDI, CORSA_HUB, TRE_PL


def conti(cat, quota, base):
    B = cat["prezzo"]; C = B - B / (1 + cat["iva"]); D = B - C; E = cat["sped_cliente"]
    F = (B + E) * cat["comm_pct"] + cat["comm_fix"]; G = D - F
    H = (B + E) if base == "lordo" else G
    I = H * quota; J = D + E - F - I
    N = (B + cat["sped_vera"]) * cat["resi"]
    O = J - cat["costo"] - cat["imballo"] - cat["sped_vera"] - N
    return dict(prezzo=B, netto=G, quota=I, margine=O, pct=O / B)


def medie(quota, base):
    s = q = m = n = 0
    for c in CATEGORIE:
        r = conti(c, quota, base)
        s += r["prezzo"] * c["mix"]; q += r["quota"] * c["mix"]; m += r["margine"] * c["mix"]; n += r["netto"] * c["mix"]
    return dict(scontrino=s, quota=q, margine_k=m, netto=n, pool=m + q)  # pool = margine da dividere per ordine


def costi_mese(anno):
    return sum(v[f"m{anno}"] for v in COSTI_B2B)


def setup():
    return sum(v["una_tantum"] for v in COSTI_B2B)


def scenario(nome, modello, quota, base, obiettivo):
    p = SCENARI[nome]; md = medie(quota, base)
    rows = []; R = 0.0; cum_b = cum_k = 0.0
    for m in range(1, 37):
        anno = (m - 1) // 12 + 1
        peso = STAGIONE["pesi"][(STAGIONE["mese_avvio"] - 1 + m - 1) % 12]
        ordini = round(p[f"ordini{anno}"] * (min(1, m / p["rampa"]) if anno == 1 else 1) * peso)
        costi = costi_mese(anno) + (setup() if m == 1 else 0) + p[f"adv{anno}"]
        lordo_k = ordini * md["pool"]                  # quello che resta a Kalab prima di versare a B2Brand
        if modello == "margine":
            pool = lordo_k - costi
            T = min(lordo_k, costi + R + 0.5 * max(0.0, pool - R))
            R = max(0.0, R - pool)
        else:
            T = ordini * md["quota"]
        netto_b = T - costi; netto_k = lordo_k - T
        cum_b += netto_b; cum_k += netto_k
        rows.append(dict(m=m, anno=anno, ordini=ordini, incasso=ordini * md["scontrino"], netto_b=netto_b, netto_k=netto_k, cum_b=cum_b, cum_k=cum_k))
    def tot(k, a): return sum(r[k] for r in rows[12 * (a - 1):12 * a])
    primo = next((r["m"] for r in rows if r["netto_b"] >= obiettivo), None)
    rientro = next((r["m"] for r in rows if r["m"] > 1 and r["cum_b"] >= 0), None)
    return dict(md=md, rows=rows, primo=primo, rientro=rientro, esposizione=min(r["cum_b"] for r in rows),
                ordini=[tot("ordini", a) for a in (1, 2, 3)], incasso=[tot("incasso", a) for a in (1, 2, 3)],
                netto_b=[tot("netto_b", a) for a in (1, 2, 3)], netto_k=[tot("netto_k", a) for a in (1, 2, 3)])


def ordini_per_obiettivo(modello, quota, base, obiettivo, adv, anno=1):
    md = medie(quota, base); F = costi_mese(anno) + adv
    return (2 * obiettivo + F) / md["pool"] if modello == "margine" else (obiettivo + F) / md["quota"]


def equilibrio(ordini, F, quota, base):
    """Percentuale della merce netta che dà a B2Brand e Kalab la stessa cifra, e quanto prende ciascuno."""
    md = medie(quota, base)
    q = md["pool"] / (2 * md["netto"]) + F / (2 * md["netto"] * ordini)
    return q, (md["pool"] * ordini - F) / 2


def corsa_hub():
    c = CORSA_HUB
    euro = 2 * c["carburante_andata"] + 2 * c["km_andata"] * c["usura_km"]
    ore = 2 * c["ore_andata"] + c["ore_al_deposito"]
    return dict(euro=euro, ore=ore, euro_mese=euro * c["giorni_al_mese"], ore_mese=ore * c["giorni_al_mese"])


def tre_pl_per_ordine(o):
    t = TRE_PL
    return t["pick_pack"] + t["materiali"] + (t["pallet_mese"] * t["pallet_n"] + t["rifornimento_mese"]) / max(o, 1)


if __name__ == "__main__":
    modello = sys.argv[1] if len(sys.argv) > 1 else ACCORDI.get("modello", "percentuale")
    quota = float(sys.argv[2]) if len(sys.argv) > 2 else ACCORDI["quota_base"]
    base = sys.argv[3] if len(sys.argv) > 3 else ACCORDI["base"]
    ob = ACCORDI.get("obiettivo_mese", 1000)
    md = medie(quota, base)
    print(f"== modello '{modello}'" + (f" · quota {quota:.0%} su '{base}'" if modello != "margine" else "") + f" · obiettivo {ob} €/mese ==")
    print(f"ordine medio {md['scontrino']:.2f} € · merce netta {md['netto']:.2f} € · margine da dividere {md['pool']:.2f} € a ordine")
    print(f"spese fisse B2Brand: avvio {setup()} € · piattaforma {costi_mese(1)}/{costi_mese(2)}/{costi_mese(3)} €/mese")
    print("\n-- EQUILIBRIO: % della merce netta che pareggia, e € a testa al mese --")
    for o, adv in ((50, 300), (100, 400), (150, 400), (200, 500), (300, 600), (500, 800)):
        F = costi_mese(1) + adv; q, x = equilibrio(o, F, quota, base)
        b50 = o * md["netto"] * 0.5 - F; k50 = o * (md["pool"] - md["netto"] * 0.5)
        print(f"   {o:4} ordini, pubblicità {adv:4} € → pareggio al {q:5.1%} · {x:7,.0f} € a testa · (col 50% fisso: B2B {b50:7,.0f} / Kalab {k50:7,.0f})")
    for nome in ("prudente", "medio", "ambizioso"):
        p = SCENARI[nome]; s = scenario(nome, modello, quota, base, ob)
        need = [ordini_per_obiettivo(modello, quota, base, ob, p[f"adv{a}"], a) for a in (1, 2, 3)]
        print(f"\n-- {nome.upper()} -- ordini/mese a regime {p['ordini1']}/{p['ordini2']}/{p['ordini3']}, pubblicità {p['adv1']}/{p['adv2']}/{p['adv3']}")
        print(f"   ordini/anno {s['ordini']} · vendite/anno {[round(x) for x in s['incasso']]}")
        print(f"   B2Brand netto/anno {[round(x) for x in s['netto_b']]} · al mese {[round(x/12) for x in s['netto_b']]}")
        print(f"   Kalab   netto/anno {[round(x) for x in s['netto_k']]} · al mese {[round(x/12) for x in s['netto_k']]}")
        print(f"   primo mese B2Brand ≥ {ob}: {s['primo']} · rientro B2Brand mese {s['rientro']} · esposizione {s['esposizione']:,.0f} · ordini/mese per l'obiettivo {[round(x) for x in need]}")
    h = corsa_hub()
    print(f"\n== CORSA ALL'HUB: {h['euro']:.0f} € e {h['ore']:.1f} h a corsa · {h['euro_mese']:,.0f} € e {h['ore_mese']:.0f} h al mese ==")
    for o in (50, 150, 300, 1000):
        print(f"   {o:5} ordini/mese: corsa {h['euro_mese']/o:6.2f} €/pacco · magazzino conto terzi {tre_pl_per_ordine(o):5.2f} €/pacco")
