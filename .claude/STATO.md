# STATO — kalab

Aggiornato: 04/10/2026

## Cos'è
Studio di fattibilità per un e-commerce di **Kalab** (KALAB di Luciano Fortunato, Orsomarso/Scalea,
300+ varietà di peperoncino) gestito da B2Brand a percentuale. Nessun codice: è ricerca.
Repo: `b2brandsrl/kalab` su GitHub.

## Consegnato
- `REPORT_fattibilita_kalab.md` (pagina semplice + 15 capitoli; aggiornato il 04/10: pag. 1, cap. 4.7
  nuovo sul viaggio all'hub, 6, 7.2, 11, 12) e `scenari_kalab.xlsx` (8 fogli, nuovo foglio Logistica).
  Copie in `~/Drive/claude-code-logs/kalab/`.
- Ricerca in `ricerca/01..08`.
- Modello: `scenari/ipotesi.py` → `scenari/calcola.py` (stampa) e `scenari/genera_xlsx.py` (Excel).
  Rigenerare: `python3 scenari/genera_xlsx.py`. Il foglio è stato ricalcolato con pycel e torna
  identico a calcola.py (04/10).

## Decisioni (04/10, Davide)
- Il 50% lo ha proposto Luciano e resta, ma **sulla merce netta** (senza IVA, spedizione, commissioni):
  sul totale incassato Kalab resterebbe a 0,20 € a ordine.
- Costo creme: ~1 € a vasetto (dato di Luciano). Polveri e sott'olio: stime allineate, da chiedere.
- Catalogo fase 1 solo **non deperibile** (creme, polveri e secco monovarietali, kit, box). Le 300
  varietà = tirature limitate in polvere + racconto. Fresco, piantine, semi: fase 2.
- Obiettivo B2Brand: **1.000 € netti di cassa al mese** → servono ~120-160 ordini/mese (medio: nov 2028;
  ambizioso: nov 2027).
- Corsa quotidiana all'hub: **no** per i non deperibili (~2.000 €/mese e 88 ore; 13 €/pacco a 150
  ordini). Al suo posto: ritiro del corriere in azienda, poi magazzino conto terzi vicino all'hub
  tra 150 e 300 ordini/mese.

## Da fare
- Incontro con Luciano: 50% sulla merce netta scritto con un esempio; costi di polveri e sott'olio;
  numeri del Natale scorso; accesso al sito (domande cap. 13).
- Preventivi corrieri con la domanda sul deposito campano (cap. 4.7).
- Davide: Keyword Planner e Meta Ads Manager in lettura (cap. 14).
- Avvocato e commercialista: cap. 7.
