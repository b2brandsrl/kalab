#!/usr/bin/env python3
"""Gemello in Python del foglio Excel: stessi conti, stampa i risultati per il report.

Uso:  python3 scenari/calcola.py [quota] [lordo|netto]
      (senza argomenti usa quota e base di ipotesi.ACCORDI)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ipotesi import CATEGORIE, SCENARI, COSTI_B2B, STAGIONE, ACCORDI, CORSA_HUB, TRE_PL

ORA_B2B = 35.0  # valore di un'ora interna di B2Brand (lo stesso dei Costi B2Brand)


def conti(cat, quota, base):
    B = cat["prezzo"]; C = B - B / (1 + cat["iva"]); D = B - C; E = cat["sped_cliente"]
    F = (B + E) * cat["comm_pct"] + cat["comm_fix"]; G = D - F
    H = (B + E) if base == "lordo" else G
    I = H * quota; J = D + E - F - I
    N = (B + cat["sped_vera"]) * cat["resi"]
    O = J - cat["costo"] - cat["imballo"] - cat["sped_vera"] - N
    return dict(prezzo=B, netto=G, quota=I, resta=J, margine=O, pct=O / B)


def medie(quota, base):
    s = q = m = n = 0
    for c in CATEGORIE:
        r = conti(c, quota, base)
        s += r["prezzo"] * c["mix"]; q += r["quota"] * c["mix"]; m += r["margine"] * c["mix"]; n += r["netto"] * c["mix"]
    return s, q, m, n


def costi_mese(anno):
    cassa = sum(v[f"m{anno}"] for v in COSTI_B2B if v["tipo"] == "cassa")
    ore = sum(v[f"m{anno}"] for v in COSTI_B2B if v["tipo"] == "ore")
    return cassa, ore


def setup():
    cassa = sum(v["una_tantum"] for v in COSTI_B2B if v["tipo"] == "cassa")
    ore = sum(v["una_tantum"] for v in COSTI_B2B if v["tipo"] == "ore")
    return cassa, ore


def scenario(nome, quota, base, obiettivo):
    p = SCENARI[nome]; S, Q, M, _ = medie(quota, base)
    set_cassa, set_ore = setup()
    rows = []; cum_cassa = cum_pieno = 0; primo_obiettivo = None
    for m in range(1, 37):
        anno = (m - 1) // 12 + 1
        peso = STAGIONE["pesi"][(STAGIONE["mese_avvio"] - 1 + m - 1) % 12]
        ordini = round(p[f"ordini{anno}"] * (min(1, m / p["rampa"]) if anno == 1 else 1) * peso)
        incasso = ordini * S; quota_b = ordini * Q; marg_k = ordini * M
        cassa, ore = costi_mese(anno)
        if m == 1: cassa += set_cassa; ore += set_ore
        adv = p[f"adv{anno}"]
        netto_cassa = quota_b - cassa - adv
        netto_pieno = netto_cassa - ore
        cum_cassa += netto_cassa; cum_pieno += netto_pieno
        if primo_obiettivo is None and netto_cassa >= obiettivo: primo_obiettivo = m
        rows.append(dict(m=m, anno=anno, ordini=ordini, incasso=incasso, quota=quota_b, marg_k=marg_k,
                         cassa=cassa, adv=adv, ore=ore, netto_cassa=netto_cassa, netto_pieno=netto_pieno,
                         cum_cassa=cum_cassa, cum_pieno=cum_pieno))
    def tot(k, a, b): return sum(r[k] for r in rows[a:b])
    rientro_cassa = next((r["m"] for r in rows if r["m"] > 1 and r["cum_cassa"] >= 0 and all(x["cum_cassa"] >= 0 for x in rows[r["m"] - 1:])), None)
    rientro_pieno = next((r["m"] for r in rows if r["m"] > 1 and r["cum_pieno"] >= 0 and all(x["cum_pieno"] >= 0 for x in rows[r["m"] - 1:])), None)
    return dict(S=S, Q=Q, M=M, rows=rows,
                ordini=[tot("ordini", 0, 12), tot("ordini", 12, 24), tot("ordini", 24, 36)],
                incasso=[tot("incasso", 0, 12), tot("incasso", 12, 24), tot("incasso", 24, 36)],
                quota=[tot("quota", 0, 12), tot("quota", 12, 24), tot("quota", 24, 36)],
                netto_cassa=[tot("netto_cassa", 0, 12), tot("netto_cassa", 12, 24), tot("netto_cassa", 24, 36)],
                netto_pieno=[tot("netto_pieno", 0, 12), tot("netto_pieno", 12, 24), tot("netto_pieno", 24, 36)],
                marg_k=[tot("marg_k", 0, 12), tot("marg_k", 12, 24), tot("marg_k", 24, 36)],
                ore=[tot("ore", 0, 12) / ORA_B2B, tot("ore", 12, 24) / ORA_B2B, tot("ore", 24, 36) / ORA_B2B],
                primo_obiettivo=primo_obiettivo, rientro_cassa=rientro_cassa, rientro_pieno=rientro_pieno,
                esposizione=min(r["cum_cassa"] for r in rows))


def ordini_per_obiettivo(quota, base, obiettivo, adv, anno=1, con_ore=False):
    _, Q, _, _ = medie(quota, base)
    cassa, ore = costi_mese(anno)
    return (obiettivo + cassa + adv + (ore if con_ore else 0)) / Q


def corsa_hub():
    c = CORSA_HUB
    km = 2 * c["km_andata"]
    euro = 2 * c["carburante_andata"] + km * c["usura_km"]
    ore = 2 * c["ore_andata"] + c["ore_al_deposito"]
    return dict(km=km, euro=euro, ore=ore, euro_mese=euro * c["giorni_al_mese"], ore_mese=ore * c["giorni_al_mese"],
                euro_mese_con_tempo=(euro + ore * c["valore_ora"]) * c["giorni_al_mese"])


def tre_pl_per_ordine(ordini_mese):
    t = TRE_PL
    fissi = t["pallet_mese"] * t["pallet_n"] + t["rifornimento_mese"]
    return t["pick_pack"] + t["materiali"] + fissi / max(ordini_mese, 1)


if __name__ == "__main__":
    quota = float(sys.argv[1]) if len(sys.argv) > 1 else ACCORDI["quota_base"]
    base = sys.argv[2] if len(sys.argv) > 2 else ACCORDI["base"]
    obiettivo = ACCORDI.get("obiettivo_mese", 1000)
    print(f"== quota B2Brand {quota:.0%} su base '{base}' · obiettivo B2Brand {obiettivo} €/mese di cassa ==")
    print(f"{'ordine tipo':46} {'prezzo':>7} {'a B2B':>7} {'Kalab':>7} {'%':>5}  mix")
    for c in CATEGORIE:
        r = conti(c, quota, base)
        print(f"{c['nome'][:46]:46} {r['prezzo']:7.2f} {r['quota']:7.2f} {r['margine']:7.2f} {r['pct']:5.0%}  {c['mix']:.0%}")
    S, Q, M, N = medie(quota, base)
    print(f"{'MEDIA PESATA (ordine medio)':46} {S:7.2f} {Q:7.2f} {M:7.2f} {M/S:5.0%}   netto medio {N:.2f}")
    for nome in ("prudente", "medio", "ambizioso"):
        p = SCENARI[nome]; s = scenario(nome, quota, base, obiettivo)
        need = [ordini_per_obiettivo(quota, base, obiettivo, p[f"adv{a}"], a) for a in (1, 2, 3)]
        need_ore = [ordini_per_obiettivo(quota, base, obiettivo, p[f"adv{a}"], a, True) for a in (1, 2, 3)]
        print(f"\n-- {nome.upper()} -- ordini/mese a regime {p['ordini1']}/{p['ordini2']}/{p['ordini3']} (anno 1/2/3)")
        print(f"   ordini/anno {s['ordini']} · incasso/anno {[round(x) for x in s['incasso']]}")
        print(f"   B2Brand quota/anno {[round(x) for x in s['quota']]} · netto di CASSA/anno {[round(x) for x in s['netto_cassa']]} · media mese {[round(x/12) for x in s['netto_cassa']]}")
        print(f"   B2Brand netto a costo pieno (ore a 35 €) /anno {[round(x) for x in s['netto_pieno']]} · ore/anno {[round(x) for x in s['ore']]}")
        print(f"   primo mese con ≥ {obiettivo} € di cassa: {s['primo_obiettivo']} · rientro cassa mese {s['rientro_cassa']} · rientro pieno mese {s['rientro_pieno']} · esposizione {s['esposizione']:,.0f}")
        print(f"   ordini/mese per {obiettivo} € di cassa: {[round(x) for x in need]} · con le ore pagate: {[round(x) for x in need_ore]}")
        print(f"   Kalab margine/anno {[round(x) for x in s['marg_k']]}")
    h = corsa_hub()
    print(f"\n== CORSA ALL'HUB (andata e ritorno Scalea-Battipaglia) ==")
    print(f"   {h['km']} km, {h['euro']:.0f} € (carburante + usura), {h['ore']:.1f} ore · al mese: {h['euro_mese']:,.0f} € e {h['ore_mese']:.0f} ore · con il tempo a {CORSA_HUB['valore_ora']:.0f} €/h: {h['euro_mese_con_tempo']:,.0f} €")
    print(f"   {'ordini/mese':>12} {'corsa €/ordine':>15} {'con tempo':>10} {'3PL €/ordine':>13}")
    for o in (50, 100, 150, 300, 600, 1000):
        print(f"   {o:12} {h['euro_mese']/o:15.2f} {h['euro_mese_con_tempo']/o:10.2f} {tre_pl_per_ordine(o):13.2f}")
