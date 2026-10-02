#!/usr/bin/env python3
"""Gemello in Python del foglio Excel: stessi conti, stampa i risultati per il report."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ipotesi import CATEGORIE, SCENARI, COSTI_B2B, STAGIONE, ACCORDI

def conti(cat, quota, base):
    B = cat["prezzo"]; C = B - B / (1 + cat["iva"]); D = B - C; E = cat["sped_cliente"]
    F = (B + E) * cat["comm_pct"] + cat["comm_fix"]; G = D - F
    H = (B + E) if base == "lordo" else G
    I = H * quota; J = D + E - F - I
    N = (B + cat["sped_vera"]) * cat["resi"]
    O = J - cat["costo"] - cat["imballo"] - cat["sped_vera"] - N
    return dict(prezzo=B, netto_iva=D, comm=F, netto=G, base=H, quota=I, resta=J, margine=O, pct=O / B, pct_suo=(O / J if J else 0))

def medie(quota, base):
    s = q = m = 0
    for c in CATEGORIE:
        r = conti(c, quota, base); s += r["prezzo"] * c["mix"]; q += r["quota"] * c["mix"]; m += r["margine"] * c["mix"]
    return s, q, m

def scenario(nome, quota, base, solo_cassa=False):
    p = SCENARI[nome]; S, Q, M = medie(quota, base)
    voci = [v for v in COSTI_B2B if solo_cassa is False or v["tipo"] == "cassa"]
    setup = sum(v["una_tantum"] for v in voci)
    mens = {1: sum(v["m1"] for v in voci), 2: sum(v["m2"] for v in voci), 3: sum(v["m3"] for v in voci)}
    ore_setup = sum(v["una_tantum"] for v in COSTI_B2B if v["tipo"] == "ore") / 35.0
    ore_mens = {a: sum(v[f"m{a}"] for v in COSTI_B2B if v["tipo"] == "ore") / 35.0 for a in (1, 2, 3)}
    cum = 0; rows = []; rientro = None; minimo = 0
    for m in range(1, 37):
        anno = (m - 1) // 12 + 1
        peso = STAGIONE["pesi"][(STAGIONE["mese_avvio"] - 1 + m - 1) % 12]
        base_o = p[f"ordini{anno}"]
        ordini = round(base_o * (min(1, m / p["rampa"]) if anno == 1 else 1) * peso)
        incasso = ordini * S; quota_b = ordini * Q; marg_k = ordini * M
        fissi = mens[anno] + (setup if m == 1 else 0); adv = p[f"adv{anno}"]
        ris = quota_b - fissi - adv; cum += ris; minimo = min(minimo, cum)
        if rientro is None and cum >= 0 and m > 1: rientro = m
        rows.append((m, anno, ordini, incasso, quota_b, marg_k, fissi, adv, ris, cum))
    def somma(k, a, b): return sum(r[k] for r in rows[a:b])
    return dict(scontrino=S, quota_ordine=Q, margine_ordine=M,
                ordini12=somma(2, 0, 12), ordini36=somma(2, 0, 36), incasso12=somma(3, 0, 12), incasso36=somma(3, 0, 36),
                quota12=somma(4, 0, 12), quota36=somma(4, 0, 36), costi12=somma(6, 0, 12) + somma(7, 0, 12), costi36=somma(6, 0, 36) + somma(7, 0, 36),
                ris12=rows[11][9], ris36=rows[35][9], margk12=somma(5, 0, 12), margk36=somma(5, 0, 36), rientro=rientro, esposizione=minimo, rows=rows,
                ore36=ore_setup + 12 * (ore_mens[1] + ore_mens[2] + ore_mens[3]), ore12=ore_setup + 12 * ore_mens[1])

if __name__ == "__main__":
    quota = float(sys.argv[1]) if len(sys.argv) > 1 else ACCORDI["quota_base"]
    base = sys.argv[2] if len(sys.argv) > 2 else ACCORDI["base"]
    print(f"== quota B2Brand {quota:.0%} su base '{base}' ==")
    print(f"{'ordine tipo':48} {'prezzo':>7} {'quota':>7} {'resta':>7} {'margine':>8} {'%prezzo':>8}")
    for c in CATEGORIE:
        r = conti(c, quota, base)
        print(f"{c['nome'][:48]:48} {r['prezzo']:7.2f} {r['quota']:7.2f} {r['resta']:7.2f} {r['margine']:8.2f} {r['pct']:8.0%}")
    S, Q, M = medie(quota, base)
    print(f"{'MEDIA PESATA':48} {S:7.2f} {Q:7.2f} {'':7} {M:8.2f} {M/S:8.0%}")
    ln = sum(conti(c, quota, base)["netto"] * c["mix"] for c in CATEGORIE); ll = sum((c["prezzo"] + c["sped_cliente"]) * c["mix"] for c in CATEGORIE)
    print(f"   incassato netto medio per ordine {ln:.2f} € · incasso lordo medio (merce+spedizione) {ll:.2f} € · margine Kalab prima della quota {M+Q:.2f} €")
    for nome in ("prudente", "medio", "ambizioso"):
        s = scenario(nome, quota, base)
        print(f"\n-- {nome.upper()} --  ordini 12m {s['ordini12']}  36m {s['ordini36']} | incasso 12m {s['incasso12']:,.0f} €  36m {s['incasso36']:,.0f} €")
        print(f"   B2Brand: quota 12m {s['quota12']:,.0f}  36m {s['quota36']:,.0f} | costi 12m {s['costi12']:,.0f}  36m {s['costi36']:,.0f} | risultato 12m {s['ris12']:,.0f}  36m {s['ris36']:,.0f} | rientro mese {s['rientro']} | esposizione max {s['esposizione']:,.0f}")
        print(f"   Kalab: margine 12m {s['margk12']:,.0f}  36m {s['margk36']:,.0f}")
        k = scenario(nome, quota, base, solo_cassa=True)
        ore = s['ore36']
        print(f"   SOLO CASSA: costi vivi 12m {k['costi12']:,.0f}  36m {k['costi36']:,.0f} | risultato di cassa 12m {k['ris12']:,.0f}  36m {k['ris36']:,.0f} | rientro mese {k['rientro']} | esposizione {k['esposizione']:,.0f} | ore B2Brand 36m {ore:,.0f} → {(k['ris36']/ore if ore else 0):,.1f} €/ora")
