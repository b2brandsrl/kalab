# -*- coding: utf-8 -*-
"""Ipotesi del modello Kalab (aggiornate il 04/10/2026: costi veri di Luciano, catalogo solo non deperibile, 50% sul netto, obiettivo 1.000 €/mese).
Ipotesi del modello Kalab. Ogni voce dice da dove viene (fonte nel report) o se è STIMA.
Le righe sono «ordini tipo» per categoria: il prezzo è lo scontrino medio di quell'ordine (IVA inclusa,
spedizione esclusa), il costo è quello della merce dentro l'ordine."""

CATEGORIE = [
    dict(nome="Polveri e secco (4 vasetti 12-15 g o 2 + sacchetti)", prezzo=28.0, iva=0.10, costo=4.0, imballo=0.8,
         sped_cliente=5.90, sped_vera=7.00, comm_pct=0.02, comm_fix=0.25, resi=0.01, mix=0.30,
         fonte="Prezzi: Peperita 12 g 4,95-11,50 €, calabresi 50-100 g 3,50-6 € (ricerca 02/04). Costo STIMA ~1 €/vasetto, in linea col dato di Luciano sulle creme (04/10). Spedizione: secco 1 kg Italia 6-11 € a listino, 7 € con tariffa negoziata (03)."),
    dict(nome="Creme e salse (3 vasetti a 7,50 €)", prezzo=22.5, iva=0.10, costo=3.0, imballo=1.2,
         sped_cliente=5.90, sped_vera=7.50, comm_pct=0.02, comm_fix=0.25, resi=0.02, mix=0.35,
         fonte="DATO KALAB: prezzo 7,50 €/crema (kalab.it); costo ~1 €/vasetto (Luciano, riferito da Davide il 04/10/2026)."),
    dict(nome="Sott'olio e conserve (2 vasetti + 1 crema)", prezzo=24.0, iva=0.10, costo=4.0, imballo=1.5,
         sped_cliente=5.90, sped_vera=8.00, comm_pct=0.02, comm_fix=0.25, resi=0.02, mix=0.10,
         fonte="Prezzi 4,49-9 € a vasetto (02). Costo STIMA 1,5 €/vasetto (più olio delle creme; da chiedere a Luciano). Vetro pesante (1,5-2 kg): spedizione 8 € (03)."),
    dict(nome="Semi (4 bustine)", prezzo=14.0, iva=0.10, costo=1.6, imballo=0.3,
         sped_cliente=2.90, sped_vera=3.00, comm_pct=0.02, comm_fix=0.25, resi=0.01, mix=0.0,
         fonte="Prezzi 1-5 €/bustina (02); costo STIMA 0,35 € (04). Plico postale. ATTENZIONE: vincolo legge sementiera (04 §4)."),
    dict(nome="Piantine (5 vasi, solo marzo-giugno)", prezzo=25.0, iva=0.10, costo=10.0, imballo=2.5,
         sped_cliente=8.90, sped_vera=9.50, comm_pct=0.02, comm_fix=0.25, resi=0.08, mix=0.0,
         fonte="Prezzi 2,70-5 €/vaso (02); costo STIMA 1,5-2 € (04). Serve RUOP + passaporto piante. Resi alti: viva."),
    dict(nome="Kit degustazione / box regalo", prezzo=38.0, iva=0.10, costo=6.0, imballo=2.0,
         sped_cliente=5.90, sped_vera=7.00, comm_pct=0.02, comm_fix=0.25, resi=0.02, mix=0.25,
         fonte="Prezzi 25-45 € (02/04); costo STIMA 5 vasetti a ~1 € + astuccio. Picco nov-dic."),
    dict(nome="Fresco 1 kg isotermico, solo Italia 24 h", prezzo=20.0, iva=0.04, costo=4.5, imballo=4.0,
         sped_cliente=9.90, sped_vera=15.00, comm_pct=0.02, comm_fix=0.25, resi=0.10, mix=0.0,
         fonte="Prezzi 12-24 €/kg varietà nominate (02). Costo STIMA; imballo isotermico+gel STIMA 3-5 €; espresso 24 h 12-18 € negoziato (03 §costo a pacco: 17-25 € tutto compreso). Resi 10% = esperienza Natale scorso."),
]

ACCORDI = dict(
    quota_base=0.50,
    base="netto",
    obiettivo_mese=1000,
    alternative=[
        dict(nome="50% dell'incasso lordo (proposta di Kalab)", base="lordo", quota=0.50, commento="Quota su merce + spedizione incassata, IVA inclusa: la lettura letterale di «50% dell'incasso»."),
        dict(nome="50% dell'incassato netto (senza IVA, spedizione e commissioni)", base="netto", quota=0.50, commento="Stessa percentuale, base più piccola: è la prassi del settore (07 B1e)."),
        dict(nome="40% dell'incassato netto", base="netto", quota=0.40, commento="Primo scaglione proposto: fino al rientro documentato dell'anticipo di B2Brand."),
        dict(nome="30% dell'incassato netto", base="netto", quota=0.30, commento="Secondo scaglione, dopo il rientro. Fascia alta dell'outsourcing italiano (15-30%, 07)."),
        dict(nome="20% dell'incassato netto", base="netto", quota=0.20, commento="Terzo scaglione sopra una soglia annua. Sotto, B2Brand non copre nemmeno le ore."),
        dict(nome="10% netto sugli ordini B2B passati dal sito", base="netto", quota=0.10, commento="Per ristoranti, bar e botteghe che ordinano dal sito con listino riservato: volumi alti, margine basso."),
    ],
)

SCENARI = dict(
    prudente=dict(ordini1=20, ordini2=40, ordini3=60, rampa=6, adv1=300, adv2=300, adv3=300),
    medio=dict(ordini1=50, ordini2=120, ordini3=200, rampa=6, adv1=400, adv2=600, adv3=800),
    ambizioso=dict(ordini1=100, ordini2=250, ordini3=450, rampa=6, adv1=500, adv2=1000, adv3=1500),
    note=dict(
        ordini1="STIMA. Oggi kalab.it ha 13 prodotti e ~10 pagine indicizzate: si parte da zero. 500 €/mese di pubblicità danno 10-17 ordini (05 §5.2); il resto da SEO, newsletter, eventi.",
        ordini2="STIMA. Anno 2: schede varietà indicizzate, recensioni, secondo Natale, Germania aperta.",
        ordini3="STIMA. Anno 3: catalogo completo, 3-4 lingue, B2B (Ankorstore/Faire) fuori da questo conto.",
        rampa="Mesi per arrivare a regime nel primo anno (crescita lineare).",
        adv1="Pagata da B2Brand. Sotto 300 €/mese Google Shopping non impara (05 §5).",
    ),
)

COSTI_B2B = [
    dict(tipo="ore", voce="Costruzione negozio (Shopify/Woo, tema, app, feed Merchant): ore interne B2Brand", una_tantum=3000, m1=0, m2=0, m3=0,
         fonte="STIMA 85 ore × 35 €/h di costo interno. Valore di mercato 3.000-7.000 € (07 B2)."),
    dict(tipo="cassa", voce="Foto: shooting 60-80 referenze + ambiente (campi, Casa Kalab)", una_tantum=1500, m1=0, m2=0, m3=0,
         fonte="STIMA 1.500-3.500 € freelance (07 B2)."),
    dict(tipo="ore", voce="Testi: 60-100 schede prodotto + 50 schede varietà iniziali", una_tantum=1000, m1=0, m2=0, m3=0,
         fonte="STIMA 3 giornate di copy interno."),
    dict(tipo="cassa", voce="Traduzioni EN+DE (DeepL + revisione umana)", una_tantum=1500, m1=0, m2=0, m3=0,
         fonte="STIMA 1.500-3.000 € (07 B2); umane 7.000-11.500 € per 4 lingue."),
    dict(tipo="cassa", voce="Piattaforma + app + dominio", una_tantum=0, m1=100, m2=120, m3=150,
         fonte="Shopify Basic 27 €/mese + app 50-150 € (07 B2, listino Shopify 02/10/2026)."),
    dict(tipo="ore", voce="Gestione mensile: ordini, assistenza, contenuti, newsletter, campagne (ore interne)", una_tantum=0, m1=700, m2=900, m3=1100,
         fonte="STIMA 20-30 ore/mese × 35 €/h. E-commerce manager in Italia 32-38 k€/anno (Indeed, 07)."),
    dict(tipo="ore", voce="Manutenzione tecnica e monitoraggio", una_tantum=0, m1=50, m2=50, m3=50,
         fonte="Keidea: 50-150 €/mese base (07 B2)."),
    dict(tipo="ore", voce="Schede varietà nuove (SEO): 10-15 al mese", una_tantum=0, m1=200, m2=200, m3=150,
         fonte="STIMA 6 ore/mese. Senza, le 350 varietà restano una promessa."),
]

STAGIONE = dict(
    mese_avvio=3,   # mese di calendario del mese 1 del piano (3 = marzo 2027: ottobre+4 mesi di costruzione)
    pesi=[0.85, 0.95, 1.00, 0.95, 0.85, 0.65, 0.65, 0.75, 1.00, 1.00, 1.35, 2.00],
    note=["dopo Natale; semi iniziano", "semi (Trends IT picco feb-mar)", "semi + piantine", "piantine (Trends: apr-mag)", "piantine",
          "estate: minimo (Trends giu-lug)", "minimo", "raccolta: ricerche al massimo ma si compra in azienda/sagre", "Festival Diamante 9-13/9; raccolta",
          "secco nuovo; inizio regali", "Black Friday; picco 'sauce piquante' FR", "Natale: picco acquisti online 5 e 16-17 dic (idealo)"],
)

NOTE_LEGGIMI = [
    "Scenari Kalab × B2Brand — come usare questo foglio (aggiornato il 04/10/2026)",
    "",
    "Le celle AZZURRE sono ipotesi: cambiale e tutto il resto si ricalcola. Le celle VERDI sono i risultati da guardare.",
    "",
    "Cosa è cambiato il 04/10: costo vero delle creme (~1 € a vasetto, da Luciano); catalogo solo non deperibile (polveri, secco, creme, sott'olio, kit e box: semi, piantine e fresco a mix zero); accordo 50% calcolato sulla merce netta; obiettivo di B2Brand 1.000 € di cassa al mese; nuovo foglio Logistica.",
    "",
    "Fogli:",
    "• Ipotesi — un «ordine tipo» per categoria: prezzo, IVA, costi, spedizione, commissioni, quota del mix. In fondo: percentuale di B2Brand, base di calcolo («netto» = merce senza IVA e senza commissioni, la spedizione passa a Kalab al costo; «lordo» = tutto l'incasso, IVA e spedizione comprese) e obiettivo mensile di B2Brand.",
    "• Conti per prodotto — per ogni ordine tipo: quanto va a B2Brand e quanto resta a Kalab dopo prodotto, imballo, spedizione e perdite (colonna O).",
    "• Costi B2Brand — quello che B2Brand anticipa e spende ogni mese, diviso in «cassa» (soldi che escono) e «ore» (tempo interno a 35 €/h).",
    "• Stagionalità — peso di ogni mese (media = 1), da Google Trends e dai dati del Natale online.",
    "• Scenari — in alto le leve (ordini, pubblicità) e gli ordini al mese che servono per l'obiettivo; sotto, 36 mesi per scenario con netto di cassa e netto a costo pieno; in fondo il riepilogo (primo mese sopra l'obiettivo, rientro, esposizione).",
    "• Logistica — quanto costa a ordine la corsa pomeridiana all'hub contro un magazzino conto terzi vicino all'hub.",
    "• Confronto accordi — lo stesso ordine medio con percentuali e basi diverse.",
    "",
    "Avvertenze:",
    "• I costi di polveri, sott'olio e kit sono ancora STIME allineate al dato delle creme: vanno chiesti a Luciano.",
    "• «Netto di cassa» è prima delle tasse di B2Brand. La quota è senza IVA: se Kalab è nel regime speciale agricolo, l'IVA sulla fattura di B2Brand per lui è un costo (report, cap. 7).",
    "• Il mese 1 del piano è marzo 2027. Si cambia in scenari/ipotesi.py (mese_avvio) e si rigenera con: python3 scenari/genera_xlsx.py",
]


# Mix a zero = fuori dal catalogo della fase 1 (semi, piantine, fresco): decisione di Davide del 04/10/2026,
# «prodotti chiaramente vendibili e non deperibili». Restano nel foglio per poterli riaccendere.

# Il viaggio pomeridiano verso un hub (idea di Davide). Fonte distanza: rome2rio, Scalea→Battipaglia
# 149 km, 1 h 44, carburante 24-35 € a tratta (letto il 04/10/2026). Usura e manutenzione: STIMA.
CORSA_HUB = dict(km_andata=149, ore_andata=1.75, carburante_andata=30.0, usura_km=0.10,
                 ore_al_deposito=0.5, giorni_al_mese=22, valore_ora=15.0)

# Magazzino conto terzi (3PL) vicino a un hub: Tissquad 01/04/2026 (picking 0,80-1,50 €, packing
# 0,50-1,00 €, materiali 0,50-1,00 €, pallet 25-50 €/mese; spedizione 0-2 kg Nord 3,50-5 €).
TRE_PL = dict(pick_pack=2.0, materiali=0.75, pallet_mese=40.0, pallet_n=2, rifornimento_mese=90.0,
              spedizione_da_hub=5.0)
