# STATO — kalab

Aggiornato: 04/10/2026 (sera)

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
- Costo creme ~1 € a vasetto (Luciano). Polveri e sott'olio: stime allineate, da chiedere.
- Catalogo fase 1 solo **non deperibile**; le 300 varietà = tirature limitate in polvere + racconto.
- **Niente ore nei conti**: sito, contenuti, traduzioni li fa Claude Code. Davide al massimo scende per
  i video social, che NON sono nell'accordo (mai discussi con Luciano).
- Obiettivo: **equilibrio** fra B2Brand e Kalab, la percentuale può salire o scendere. Proposta:
  **«metà del guadagno»** (vendite nette − listino costi prodotto − imballo − spedizione non pagata −
  commissioni − resi − pubblicità − piattaforma, metà a testa; B2Brand anticipa e recupera per prima).
  Pareggia a ogni volume. Alternativa a scaglioni sulla merce netta: 50% fino a 100 ordini/mese, 42%
  fino a 250, 39% sopra. Il 50% fisso a 150 ordini dà B2Brand 1.350 €, Kalab 735 €.
- 1.000 € al mese a testa: ~145 ordini/mese (medio: nov 2028; ambizioso: dic 2027).
- Corsa quotidiana all'hub: **no** (~2.000 €/mese, 13 €/pacco a 150 ordini); magazzino conto terzi
  vicino all'hub tra 150 e 300 ordini/mese.
- Il foglio ha l'interruttore «Modello» (margine/percentuale) nelle Ipotesi e il foglio «Equilibrio».

## Da fare
- Incontro con Luciano: proporre «metà del guadagno» col foglio Equilibrio; listino dei costi di
  prodotto; numeri del Natale scorso; accesso al sito (domande cap. 13). Decidere i video social.
- Commercialista: associazione in partecipazione e IVA sulla quota di utili (cap. 7.3).
- Preventivi corrieri con la domanda sul deposito campano (cap. 4.7).
- Davide: Keyword Planner e Meta Ads Manager in lettura (cap. 14).
- Avvocato e commercialista: cap. 7.
