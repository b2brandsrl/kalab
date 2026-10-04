# Kalab — Scenario ambizioso · Filone 2: BENCHMARK DI CRESCITA E MATEMATICA DEL TRAGUARDO

Ricerca desk del 04/10/2026, solo web e file locali. Metodo: 22 ricerche web su 25 consentite, poi
pagine aperte una per una (WebFetch). Tre documenti che WebFetch non sa leggere sono stati scaricati e
letti in locale: l'API Eurostat (JSON, letto con Python) e due PDF (ECDB e CustomersAI, testo estratto
con PDFKit di macOS). I conti sono in `ricerca/ambizioso/02_matematica.py` (riusa `scenari/calcola.py`
e `scenari/ipotesi.py`): `python3 ricerca/ambizioso/02_matematica.py` li rifà in un secondo.

**Legenda.** DATO = numero con fonte e data, tra parentesi quadre il numero della fonte (§4).
**STIMA:** = numero nostro, costruito con il metodo scritto accanto. **IPOTESI:** = scelta nostra per far
girare i conti, si cambia. Quando un benchmark è USA, globale o di un'agenzia, è scritto nella riga.

Il traguardo (scenario ambizioso del report, cap. 11): ordini al mese a regime 100 / 250 / 450 negli
anni 1 / 2 / 3 (anno 1 = marzo 2027-febbraio 2028); vendite 27.600 / 84.500 / 152.100 €; ordine medio
28,17 €; margine da dividere 17,24 € a ordine; pubblicità 500 / 1.000 / 1.500 € al mese; piattaforma
100 / 120 / 150 € al mese; dicembre pesa 2 volte un mese medio.

---

## Riassunto in 15 righe

1. **Visite** — STIMA: per 100 / 250 / 450 ordini al mese servono circa **6.700 / 16.700 / 30.000 visite al mese** con la conversione mediana dei piccoli negozi Shopify (1,4-1,5 %, Littledata, 09/2026 [B2]); 10.000 / 25.000 / 45.000 se si resta all'1 %, 4.000 / 10.000 / 18.000 se si arriva al 2,5 %. A dicembre il doppio.
2. **Conversione**: il «4,58 % del food» che circola è dei grandi brand (Dynamic Yield [B3]); i piccoli negozi stanno all'1,4 % [B2], il Food & Drink britannico all'1,58 % (IRP, ago 2026 [B6]), l'Italia intorno all'1 % (fonte terza non verificabile [B8]). IPOTESI di obiettivo: 0,8 % all'apertura, 1,5 % a fine anno 1, 2,2 % a fine anno 3.
3. **Ordine medio**: 28 € è **un terzo** del food online (79-81 $ [B4][B37]; 119 £ nel Food & Drink UK [B6]; 130 € l'enogastronomia italiana [B37]). È la leva più forte che c'è.
4. **Ordine medio a 40 €** — STIMA dal modello: con spedizione pagata dal cliente il margine da dividere sale da 17,24 a **25,04 € a ordine (+45 %)** e lo stesso guadagno del piano arriva con **317 ordini al mese invece di 450** nel terzo anno. Con spedizione gratis a tutti, invece, a 40 € il margine è solo 19,26 €: la soglia di spedizione gratuita va messa **sopra 45-49 €**.
5. **Riacquisto**: nei consumabili ricompra entro un anno il 30-40 % dei clienti; metà dei secondi ordini arriva entro 30 giorni, tre quarti entro 90 (B&S Co, 156.000 clienti, USA [B12]). STIMA: con un riacquisto «medio» i clienti di ritorno fanno il **22 % degli ordini nell'anno 1, 28 % nell'anno 2, 35 % nell'anno 3**.
6. **Clienti nuovi** — STIMA (riacquisto medio): per il piano ne servono circa **760 / 2.160 / 3.490 all'anno**, cioè 64 / 180 / 291 al mese in media.
7. **Pubblicità** — STIMA: con 500 / 1.000 / 1.500 € al mese e un costo di 25-50 € per cliente nuovo, la pubblicità porta **10-60 clienti nuovi al mese: l'11-22 % di quelli che servono**. Per comprarli tutti a 35 € servirebbero 3.100 / 6.300 / 10.200 € al mese. **L'80-90 % dei clienti nuovi deve arrivare da canali gratuiti** (Google organico e schede Shopping gratuite, social, stampa, passaparola, B2B).
8. **Quanto vale una visita** — STIMA: oggi 0,26 € di margine (17,24 € × 1,5 %), mentre un clic su Google Shopping costa 0,55-0,66 €/$ [B37]. La pubblicità perde sul primo ordine e rientra solo con riacquisti e ordine medio più alto (0,50-0,77 € a visita a 40 €). Costo per cliente nuovo sostenibile: **circa 20 € oggi, 29 € con ordine medio 40 €**.
9. **Email**: vale il 19 % del fatturato nell'account Klaviyo medio (CustomersAI, 619 brand, 03/2026 [B19]), 27 % secondo Klaviyo 2025 (citato da terzi [B15]), 8,6 % nel Food & Drink UK contando l'ultimo clic [B6]. STIMA: per avere il 20-25 % degli ordini dall'email servono **~2.200 iscritti a 100 ordini al mese, ~5.500-7.300 a 250, ~13.000 a 450**.
10. **Popup**: si iscrive il 2,1 % di chi lo vede (Omnisend, 1,24 miliardi di visualizzazioni nel 2025 [B24]); 4,8 % su Wisepops [B25]; con uno sconto 2,4 % contro 1,7 %. STIMA: lista di ~1.750 iscritti a febbraio 2028, ~5.500 a febbraio 2029, ~10.800 a febbraio 2030.
11. **Carrello**: si abbandona il 70,22 % dei carrelli (Baymard, 50 studi, 09/2025 [B18]); il 40 % per i costi extra; un checkout fatto bene vale +35 % di conversione. **Recensioni**: con 5 recensioni la probabilità d'acquisto è +270 % rispetto a zero (Spiegel, 2017 [B27]).
12. **Natale**: in Italia novembre + dicembre fanno il **24 % delle vendite online dell'anno** e dicembre vale 1,4-1,5 volte un mese medio (Eurostat, tutte le merci, 2022-2025 [B1]). Il modello Kalab mette il 28 % e dicembre a 2 volte: plausibile per un negozio di regali, da verificare col Natale vero di Kalab.
13. **Crescita** — STIMA: passare da 100 ordini al mese (febbraio 2028) a 3.000 nell'anno 2 vuol dire salire senza soste fino a **~360 al mese destagionalizzati a febbraio 2029 (×3,6 in un anno)** e fare **~630 ordini a dicembre 2028 e ~980 a dicembre 2029** (circa 49 per giorno lavorativo). Il foglio scenari ha un gradino irrealistico a marzo 2028: i KPI qui usano una crescita continua con gli stessi totali annui.
14. **Abbonamenti**: dopo 6 mesi resta il 45 % degli abbonati, dopo 12 il 33 % (Recharge, 15.000 negozi [B32]) → STIMA: 9 % di abbandono al mese, vita media ~11 mesi; 100 abbonati = 100 ordini al mese assicurati con ~9 abbonati nuovi al mese; un box «a sorpresa» perde però il 12-18 % al mese (fonti terze [B15]).
15. **Regali**: il 34 % delle famiglie regala un cesto enogastronomico, spesa media 48 € (Coldiretti/Ixè, 12/2025 [B34]); il 44 % compra i regali solo o soprattutto online (Altroconsumo, 12/2025 [B35]). **Regali aziendali: nessun dato pubblico italiano** su mercato e calendario; regola fiscale utile: gli omaggi ai clienti fino a 50 € a pezzo sono deducibili al 100 % [B36]. Buchi principali al §5.

---

## 1. Benchmark

Prima di leggere le tabelle: i numeri vengono da tre mondi diversi e non vanno mischiati.
**Grandi negozi** (Dynamic Yield, ECDB): conversione intorno al 3 %. **Piccoli negozi Shopify**
(Littledata): 1,4 %. **Agenzie e consulenti** (B&S Co, Eightx, Branvas, Foundry): campioni propri,
metodi non verificabili, quasi sempre USA. Kalab va confrontato con i piccoli negozi.

### 1.1 Tasso di conversione (totale, telefono, canale, paese)

| Cosa | Valore | Fonte, data | Note |
|---|---|---|---|
| Piccoli negozi Shopify, mediana | **1,4 %**; buoni (top 20 %) 2,6 %; top 10 % 3,4 %; ultimi 20 % 0,5 % | Littledata, 421 negozi Shopify, 29/06-26/09/2026, generato 02/10/2026 [B2] | globale; il food non è pubblicato (meno di 30 negozi) |
| Telefono e computer, piccoli negozi | mediana 1,5 % per entrambi; top 10 % computer 5,2 %, telefono 3,9 % | Littledata [B2] | |
| Mondo, primo trimestre 2026 | 1,4 % | Statista citato da Shopify, 22/08/2026 [B5] | |
| Grandi brand, media | 2,71 %; telefono 2,88 %, tablet 2,82 %, computer 2,31 %; EMEA 2,86 % | Dynamic Yield, media 12 mesi fino ad agosto [2026] [B3] | |
| **Food & Beverage**, grandi brand | **4,58 %** | Dynamic Yield [B3]; ripreso da Shopify 22/08/2026 [B5] | mescola spesa, caffè, integratori |
| Food & Beverage | 2,6 % | Triple Whale (05 [7], pagina 403) [B37] | |
| Regno Unito, tutte le categorie | 2,23 % (agosto 2025: 1,85 %) | IRP Commerce, agosto 2026 [B6] | negozi clienti IRP |
| **Regno Unito, Food & Drink** | **1,58 %** (agosto 2025: 1,16 %) | IRP Commerce, agosto 2026 [B6] | l'unico dato europeo food trovato |
| Per paese, tutte le categorie, 2025 | Paesi Bassi 3,99 %, Regno Unito 3,67 %, Francia 3,36 %, **Germania 3,33 %**, Svezia 2,51 %, USA 3,40 % | ECDB, «E-Commerce KPI and Benchmarks Report 2026», 07/2026 [B7] | grandi negozi; l'Italia non c'è |
| **Italia** | **~1,0 %** (Francia 1,2 %, Paesi Bassi 1,8 %, Danimarca 1,9 %) | IRP Commerce/Rocking Web via Landmark Global, citato da Eightx 12/06/2026 [B8] | **non verificato**: la pagina Landmark è bloccata |
| Italia | 1,6 % | Sendcloud, agg. 13/03/2026 [B9] | nessuna fonte citata: da non usare |
| Computer contro telefono | computer 3,7 %, telefono 2 %; il telefono porta il 69,9 % del traffico 2026 | Contentsquare citato da Shopify 22/08/2026 [B5] | |
| Quota di visite da telefono | mediana 70 % (top 10 % 88 %) | Littledata [B2] | |
| UK Food & Drink: vendite per dispositivo | telefono 55,9 %, computer 41,7 %, tablet 2,4 % | IRP, agosto 2026 [B6] | |
| Regali gastronomici (Grips, paesi non dichiarati) | conversione 3,5-4,0 %; il **61 % del fatturato da computer** | Grips Intelligence, 40+ negozi, agosto 2026 [B10] | chi regala compra dal computer |
| Meta (Facebook/Instagram), food | conversione 1,54 %, CTR 2,06 % | Lebesgue, 09/03/2026 [B11] | paesi non dichiarati |
| Google Shopping / Search, e-commerce | 1,91 % / 2,81 % | WordStream via Store Growers, 01/2026 (05 [3]) [B37] | USA |
| UK Food & Drink: da dove arrivano le vendite | Google a pagamento 62,5 %, email 8,63 %, affiliazione (AWIN) 4,51 %, Bing a pagamento 2,05 %, Facebook a pagamento 0,37 % | IRP, agosto 2026 [B6] | ultimo clic |
| Per canale | email 5,3 %, Google organico 2,8 %, search a pagamento 2,4 %, social 1,1 % | Wolfgang Digital 2024 [B38] | **solo da snippet**: lo studio aperto è del 2014 |
| Imbuto dei piccoli negozi | aggiunta al carrello 6,5 % delle visite; checkout completato 53 %; ricavo per visita 1,94 $ | Littledata [B2] | |

**Lettura.** Per un negozio nuovo, piccolo, italiano e con prodotti da 7,50 € il riferimento giusto è
1,0-1,5 %. Il 2,5 % è da «primo 20 %». Il Regno Unito mostra due cose utili: nel food online conta
moltissimo Google a pagamento (62,5 % delle vendite) e chi regala compra spesso dal computer.

### 1.2 Ordine medio

| Cosa | Valore | Fonte, data | Note |
|---|---|---|---|
| Piccoli negozi Shopify, mediana | 110 $ (top 20 % 288 $) | Littledata [B2] | tutti i settori |
| Grandi brand, mondo / EMEA | 192 $ / 224 $; computer 260 $, telefono 172 $ | Dynamic Yield [B4] | |
| **Food & Beverage** | **81 $** (agosto) | Dynamic Yield [B4] | la serie mensile salta (14 $ a luglio): dato fragile |
| **Food & Beverage** | **~79 $** (luglio 2025-giugno 2026) | Shopify/Ryze, 24/08/2026 (05 [6]) [B37] | globale |
| UK Food & Drink | 118,93 £ (agosto 2025: 103,08 £); prezzo medio di un articolo 28,67 £ | IRP, agosto 2026 [B6] | |
| Per paese, tutte le categorie, 2025 | Germania 120 €, Regno Unito 106 €, Francia 104 €, Svezia 107 €, Paesi Bassi 76 €, USA 137 € | ECDB 07/2026 [B7] | |
| Zooplus (cibo per animali, acquisto ricorrente) | 65 €, 3,1 ordini all'anno | ECDB [B7] | il modello «spesa che ritorna» |
| **Enogastronomia online, Italia** | **~130 €** | Osservatorio eCommerce B2c, 05/2025 (01 [F18]) [B37] | |
| Spesa alimentare online, Italia | STIMA: ~33 € a ordine (261 € l'anno ÷ 8 acquisti) | Netcomm 2024 (01 [F21]) [B37] | spesa, non nicchia |
| Regali gastronomici (Grips, paesi non dichiarati) | 100-200 $ | Grips, agosto 2026 [B10] | |
| **Kalab oggi (modello)** | **28,17 €** | report cap. 6 [B37] | |

**Lettura.** 28 € è tre volte sotto ogni benchmark del food online. Non è «sbagliato» (le creme costano
7,50 €), ma ogni visita rende meno e la pubblicità costa uguale (§2.5).

### 1.3 Clienti che ricomprano e tempo fra due ordini

| Cosa | Valore | Fonte, data | Note |
|---|---|---|---|
| Clienti che ricomprano entro 365 giorni, tutti i settori | 18,8 % (81,2 % compra una volta sola) | B&S Co., 156.110 clienti, 14/02/2026 [B12] | agenzia USA |
| **Idem, consumabili** (integratori, food & beverage, alcolici) | **22-44 %, tipico 30-40 %** | B&S Co. [B12] | |
| **Tempo al secondo ordine** (chi ricompra) | 6,3 % lo stesso giorno; 15,9 % entro 7 giorni; **50,3 % entro 30; 76,4 % entro 90**; 96,3 % entro 365. Mediana 15-35 giorni | B&S Co. [B12] | portafoglio misto |
| Consumabili: mediana giorni al secondo ordine | 27-68 (integratori) | Eightx, 30/05/2026 [B13] | secondaria |
| Riacquisto a 12 mesi | consumabili 35-45 %; bellezza 30-40 %; abbigliamento 25-32 % | Eightx [B13] (cita B&S, Finsi, Prooflytics, Storeleads) | secondaria |
| Ordini all'anno, food & beverage | 2-4 senza abbonamento; 6-9 con abbonamento; chi compra una volta fa 1,3 ordini in tutta la vita | Eightx, 27/06/2026 [B14] | secondaria |
| Ordini all'anno per abbonato | 4,4 | Recharge 2024 Subscriber Trends, citato da Eightx [B14] | secondaria |
| Fatturato DTC da clienti di ritorno | 60 % | Swell 2026, citato da Foundry CRO 12/05/2026 [B15] | secondaria |
| Riacquisto medio dei negozi Shopify | 28,2 % | Shopify, citato da Eightx [B14] | secondaria |
| **Food online in Italia** | **oltre il 70 % degli ordini sono riacquisti** | Netcomm/NIQ, 25/06/2025 (01 [F20]) [B37] | spesa alimentare: non è il caso di una nicchia |
| Acquisti online all'anno per persona (tutti i negozi) | Germania 12,4; Francia 10,5; Regno Unito 18,6; Paesi Bassi 13,5; USA 27,7 | ECDB [B7] | livello paese |

**Lettura per Kalab.** Nessuna fonte misura condimenti o salse piccanti. **IPOTESI** usate nei conti
(§2.3), dentro le forchette dei consumabili: ricompra entro 12 mesi il 20 % (basso), 30 % (medio) o
40 % (alto) dei clienti nuovi, con 1,5 / 1,8 / 2,0 ordini in più. Il ritorno di una crema è
probabilmente più lento di un integratore da 30 giorni, e chi compra un regalo a Natale ricompra meno:
da misurare dal primo Natale.

### 1.4 Valore del cliente nel tempo (LTV)

| Cosa | Valore | Fonte, data | Note |
|---|---|---|---|
| Ricavo per cliente, piccoli negozi Shopify | mediana 143 $ (top 20 % 384 $) nei 90 giorni del campione | Littledata [B2] | tutti i settori |
| Regola LTV/CAC | almeno 3 a 1 (forchetta del settore 2-5) | LoyaltyLion, 12/06/2025 [B16] | |
| Food & beverage in abbonamento | LTV/CAC 3-4 volte, rientro in 2-5 mesi | Eightx, 27/06/2026 [B17] | secondaria |
| Abbonamento caffè, 12 mesi | 400-900 $ | Northstar, citato da Foundry CRO [B15] | secondaria |
| **Kalab, STIMA** (riacquisto medio) | 1,54 ordini in 12 mesi e 1,76 in 24 → **43 € / 50 € di vendite** con ordine medio 28 €; 62 € / 70 € a 40 €. In margine da dividere: **27 € / 30 €** a 28 €; 39 € / 44 € a 40 € | §2.3 e §2.5 | |

### 1.5 Costo per acquisire un cliente (CAC) per canale

| Cosa | Valore | Fonte, data | Note |
|---|---|---|---|
| Food & Beverage, piccoli brand | ~53 $ (il più basso fra i settori: moda 66 $, bellezza 61 $) | Shopify 2021, citato da LoyaltyLion 12/06/2025 [B16] | dato vecchio |
| DTC food & beverage | 45-53 $ | Swell 2026, citato da Foundry CRO [B15] | secondaria |
| Per canale, tutti i DTC 2025 | email/SMS 8-15 $; Google organico ~31 $; TikTok ~46 $; Meta ~53 $; Google Ads ~62 $; creator a pagamento ~65 $; media ~87 $ | Eightx, 27/06/2026 (cita Triple Whale, Northbeam, Vovv, ATTN) [B17] | agenzia, USA |
| Food & beverage per canale | Meta 25-60 $; Google 30-70 $; TikTok 15-40 $; media a pagamento 30-65 $ | Eightx [B17] | agenzia, USA |
| Meta, food 2026 | CAC 20,47 $; CPM 8,21 $; CTR 2,06 %; conversione 1,54 % | Lebesgue, 09/03/2026 [B11] | paesi non dichiarati |
| Google Shopping, e-commerce | CPC 0,66 $; conversione 1,91 %; costo per ordine 38,87 $ | WordStream via Store Growers, 01/2026 (05 [3]) [B37] | USA |
| Meta, Italia | CPM 6,06-7,20 $; CPC 1,05 $ (Germania +40-50 %) | Lebesgue, AdAmigo (05 [4][5]) [B37] | tutti i settori |
| **Kalab, STIMA** | Shopping Italia 0,55 € ÷ 1,5-2,5 % = **22-37 €**; Meta su pubblico freddo 1 € ÷ 1-1,5 % = 67-100 €; remarketing molto meno | 05 §5.2 | da rifare dopo 30 giorni di campagne |

### 1.6 Carrello abbandonato

| Cosa | Valore | Fonte, data |
|---|---|---|
| Media di 50 studi | **70,22 %** | Baymard Institute, agg. 22/09/2025 [B18] |
| Perché si abbandona al checkout | costi extra troppo alti (spedizione, tasse) **40 %**; consegna lenta 20 %; poca fiducia per la carta 19 %; obbligo di creare un account 18 %; checkout lungo 17 %; errori del sito 17 %; resi poco chiari 13 %; totale non visibile prima 12 %; carta rifiutata 10 %; pochi metodi di pagamento 9 % (a parte il 42 % che «stava solo guardando») | Baymard [B18] |
| Guadagno possibile con un checkout migliore | **+35,26 % di conversione** (grandi siti) | Baymard [B18] |
| Piccoli negozi Shopify | mediana 78 %; top 20 % 65 %; top 10 % 56 % | Littledata [B2] |
| Per paese, 2025 | Germania 64,6 %, Regno Unito 63,2 %, Francia 71,1 %, Paesi Bassi 59,9 %, Svezia 75,5 %, USA 71,9 % | ECDB [B7] |
| Europa (dato del 2018) | 56 % degli acquisti non conclusi per consegna troppo cara, 39 % per consegna troppo lenta | Netcomm/Comieco, 15/01/2018 [B31] |

### 1.7 Email e SMS: quanto pesano sul fatturato

| Cosa | Valore | Fonte, data | Note |
|---|---|---|---|
| **Email sul fatturato totale**, account Klaviyo medio | **19 %**; clic medio 7,3 % | CustomersAI, 619 brand, 740 milioni di email, 300 milioni $ di ricavi, 18/03/2026 [B19] | Shopify, soprattutto USA |
| Idem | 27 % | Klaviyo 2025 (265.000 negozi), citato da Foundry CRO 12/05/2026 [B15] | **non verificato**: i report Klaviyo sono dietro modulo [B23] |
| Food & beverage | tipico 25-35 % (i migliori 35-45 %) | Eightx, 29/05/2026 (Flypost 50 brand; B&S 14 brand) [B22] | agenzie |
| Livelli di maturità | niente programma 0-8 %; medio 12-20 %; forte 20-30 % | Eightx (Flypost) [B22] | |
| **UK Food & Drink, ultimo clic** | **8,63 % delle vendite** | IRP, agosto 2026 [B6] | misura più severa |
| Flussi automatici (benvenuto, carrello, post-acquisto) | 37 % dei ricavi email dal 2 % degli invii (Omnisend) · 41 % dal 5,3 % (Klaviyo 2025) | Branvas 08/05/2026 [B21]; Foundry CRO [B15] | |
| Campagne: chi riceve e ordina | media 0,08 % (top 10 % 0,44 %); **food & beverage 0,17 %** | InboxAlly su dati Klaviyo (167.000 brand), 05/03/2026 [B20] | |
| Idem | media 0,16 % (apertura 31,0 %, clic 1,69 %, 0,32 $ per destinatario); **food & beverage 0,26 %** (apertura 31,2 %, clic 1,70 %) | Branvas su Klaviyo 2026, 08/05/2026 [B21] | le due fonti non concordano |
| Flussi: chi riceve e ordina | media 1,42 % (top 10 % 4,93 %); food & beverage 1,72 % · media 2,11 % (2,54 $ per destinatario) | InboxAlly [B20] · Branvas [B21] | |
| Ricavo per destinatario dei flussi | benvenuto 2,35 $; carrello abbandonato 3,07 $; navigazione abbandonata 0,95 $; post-acquisto 0,38 $ | InboxAlly [B20] | |
| SMS | aggiunge il 5-15 % di ricavi dove c'è già l'email; i flussi SMS fanno il 45,2 % dei ricavi SMS dal 7,6 % degli invii | Eightx [B22]; Klaviyo 2025 via Foundry [B15] | USA; per l'Italia nessun dato trovato |
| Un caso di salsa piccante | Red Clay Hot Sauce: 32 % del fatturato online attribuito a Klaviyo | solo snippet [B38] | non verificato |

### 1.8 Iscrizioni alla newsletter dai popup

| Cosa | Valore | Fonte, data |
|---|---|---|
| **Media, per visualizzazione** | **2,1 % nel 2025** (2,3 % nel 2024) su 1,24 miliardi di visualizzazioni e 26,4 milioni di email raccolte | Omnisend, 09/02/2026 [B24] |
| Solo computer / telefono | 1,4 % / 2,2 % | Omnisend [B24] |
| Con sconto / senza | 2,4 % / 1,7 % | Omnisend [B24] |
| Con ruota della fortuna / senza | 3,5 % / 2,0 % | Omnisend [B24] |
| Ritardo migliore | 6-10 secondi (2,4 %); subito 1,9 % | Omnisend [B24] |
| Scala | sotto 1,5 % male; 1,5-3 % nella media; 3-5 % buono; oltre 5 % ottimo | Omnisend [B24] |
| Media Wisepops | **4,82 %** (anno prima 4,65 %); telefono 4,98 %, computer 3,67 %; e-commerce 6,88 %; con sconto 7,45 % contro 4,60 % | Wisepops, ~1 miliardo di visualizzazioni, 30/09/2025 [B25] |
| Klaviyo, mediana | 2,3 % | citato da CrazyEgg [B26]: non verificato alla fonte |

### 1.9 Recensioni e conversione

| Cosa | Valore | Fonte, data |
|---|---|---|
| **5 recensioni contro nessuna** | **+270 % di probabilità d'acquisto**; i vantaggi calano dopo le prime 5 | Medill Spiegel Research Center (dati PowerReviews), 2017 [B27] |
| Prodotti economici / costosi | +190 % / +380 % | Spiegel [B27] |
| Voto che vende di più | 4,0-4,7 stelle (il 5 pieno sembra finto) | Spiegel [B27] |
| Bollino «acquirente verificato» | +15 % | Spiegel [B27] |
| Almeno una recensione contro nessuna | +76,7 % di conversione (1,5 milioni di pagine prodotto) | PowerReviews, citato da Amazon 24/10/2023 [B28] |
| Recensioni Amazon mostrate sul sito | +38 % di conversione (8 negozi, 10.000-1 milione di visite al mese) | Amazon Buy with Prime, 24/10/2023 [B28] |
| Spesa alimentare online | 72 % compra più volentieri un prodotto mai provato se ha recensioni; 93 % le legge almeno ogni tanto | PowerReviews, USA, 19/09/2017 [B29] |

Nessun dato 2024-2026 indipendente trovato: i numeri recenti sono dei venditori di software per recensioni.

### 1.10 Soglia di spedizione gratuita e ordine medio

| Cosa | Valore | Fonte, data |
|---|---|---|
| **Ordini con spedizione gratis contro a pagamento** (mediana per negozio) | **123 $ contro 80 $ (+54 %)** | Metorik, 65 milioni di ordini WooCommerce del 2025, 6.000+ negozi, 15/07/2026 [B30] |
| Media pesata di tutto il mercato | 96 $ contro 116 $ (i grandi danno la spedizione gratis anche agli ordini piccoli) | Metorik [B30] |
| Negozi di caffè | 239 $ contro 129 $ (+85 %) | Metorik [B30] |
| Clienti che aggiungono articoli per arrivare alla soglia | 71 % degli e-shopper europei | Netcomm/Comieco, 15/01/2018 [B31] |
| Italia | ~70 % delle consegne gratuite; costo medio a spedizione 2,8 €; 60 % dei 33 negozi intervistati con soglia, 18,2 % sempre gratis | Netcomm/Comieco 2018 [B31] (dato vecchio) |
| Negozio di salse piccanti (USA) | +28 % di ordine medio con sconti a scaglioni e spedizione gratis | Skailama (01 [F49]) [B37] |
| **Kalab, STIMA** | margine da dividere a ordine: 40 € con spedizione pagata **25,04 €**; 40 € gratis 19,26 €; **38 € gratis 17,81 € (come oggi)**; 45 € gratis 22,89 €; 49 € gratis 25,78 € | modello (§2.6) |

### 1.11 Peso di novembre-dicembre sull'anno

Dato ufficiale europeo: indice mensile del fatturato del «commercio al dettaglio via posta o internet»
(NACE G4791), dati grezzi, tutte le merci (Eurostat, aggiornato 03/10/2026 [B1]). Calcolo mio sugli
indici mensili.

| Paese | Nov + dic sull'anno 2022 | 2023 | 2024 | **2025** | Dicembre / mese medio 2025 | Novembre / mese medio 2025 |
|---|---|---|---|---|---|---|
| **Italia** | 24,6 % | 23,7 % | 23,8 % | **24,4 %** | **1,47** | 1,45 |
| Germania | 20,3 % | 20,0 % | 21,4 % | 20,2 % | 1,21 | 1,22 |
| Francia | 21,7 % | 21,9 % | 21,2 % | 22,2 % | 1,37 | 1,30 |
| Spagna | 21,6 % | 21,9 % | 21,7 % | 22,6 % | 1,45 | 1,26 |

- In Italia, prima del 2021, dicembre pesava di più (2019: 26,0 % e dicembre 1,77 volte la media).
  IPOTESI: il Black Friday ha spostato acquisti a novembre (da allora novembre vale quanto dicembre).
- **Regali gastronomici** (Grips, paesi non dichiarati), STIMA [B10]: 790 milioni $ di vendite nel 2025 (media 66 al
  mese) contro 42 milioni ad agosto 2026 → un mese «normale» vale circa 0,64 volte la media, quindi
  novembre-dicembre potrebbero pesare il 40-45 % dell'anno. Dato grezzo, da prendere come ordine di
  grandezza.
- Calendario (01 [F25], [B34]): picchi online il 5 e il 16-17 dicembre (idealo); 5 milioni di italiani
  concentrano i regali nella settimana prima di Natale (Coldiretti/Ixè).
- **Il modello Kalab** dà a novembre + dicembre il 27,9 % dell'anno (dicembre 2,0, novembre 1,35): sta
  fra il commercio online generale italiano (24 %) e i negozi di soli regali (40 % e oltre). IPOTESI
  ragionevole, da tarare con il Natale scorso di Kalab (domanda 2 del report, cap. 13).

### 1.12 Abbonamenti

| Cosa | Valore | Fonte, data | Note |
|---|---|---|---|
| **Abbonati ancora attivi dopo 6 / 12 mesi** | **45 % / 33 %** | Recharge, «2023 State of Subscription Commerce», 01/2023, 15.000+ negozi [B32] | tutti i settori |
| Abbonati che modificano un ordine / di questi, quanti saltano | 35 % / 39 % | Recharge [B32] | |
| Food & beverage | ordine medio più alto fra i settori (2021-2022) | Recharge [B32] | |
| Abbandono mensile food & beverage | 6,6-6,8 % (settembre-dicembre 2022) | Recharge, solo snippet [B38] | non verificato |
| Abbonamenti di riordino (caffè, filtri) | 4-7 % al mese | Eightx e Finsi 2026, citati da Foundry CRO [B15] | secondaria |
| **Box «a sorpresa»** (snack, meal kit) | **12-18 % al mese** | idem [B15] | il «peperoncino del mese» è di questo tipo |
| Caffè | 5-10 % al mese; 28 % disdice nei primi 3 mesi | Eightx, 03/05/2026 [B33] | secondaria |
| STIMA da Recharge | 33 % vivi dopo 12 mesi → **~9 % al mese**, vita media **~11 mesi** | calcolo: 0,33^(1/12) | |

### 1.13 Regali di Natale in Italia (famiglie e aziende)

| Cosa | Valore | Fonte, data |
|---|---|---|
| Spesa per i regali, Natale 2025 | 9,6 miliardi € | Coldiretti/Ixè, AGI 20/12/2025 [B34] |
| **Famiglie che regalano un cesto enogastronomico** | **34 %, spesa media 48 €** | Coldiretti/Ixè [B34] |
| Budget regali | 11 % sotto 50 €; 44 % fra 50 e 150 €; 24 % fino a 300 €; 21 % oltre | Coldiretti/Ixè [B34] |
| Ultima settimana | 5 milioni di italiani concentrano i regali nella settimana prima di Natale | Coldiretti/Ixè [B34] |
| **Regali comprati online** | **44 % solo o soprattutto online**; 25,6 % metà e metà; 9 % solo in negozio; sotto i 34 anni 54,6 % online | Altroconsumo, oltre 2.000 intervistati, 16/12/2025 [B35] |
| Budget regali a testa | 208 € (128 adulti + 80 bambini), su 592 € di spese di Natale | Altroconsumo [B35] |
| Food & beverage fra i regali | 10 % | Accenture via Cribis (01 [F26]) [B37] |
| **Regali aziendali: mercato, spesa media, calendario** | **NON TROVATO** (due ricerche dedicate) | — |
| Omaggi ai clienti | deducibili al 100 % (e IVA detraibile) se il valore del singolo omaggio non supera **50 €**; un cesto si valuta per intero | LeggiOggi, 11/12/2023 [B36] |
| Omaggi ai dipendenti | soglia di 258,23 € a periodo d'imposta | LeggiOggi 2023 [B36]; le soglie alzate per il 2025-2027 **non verificate**: commercialista |

**IPOTESI di calendario aziendale** (nessuna fonte): listino e campioni entro fine settembre, ordini da
metà ottobre a metà novembre, consegne entro il 10 dicembre. Da chiedere a Blend e ai primi clienti B2B.

---

## 2. La matematica del traguardo

### 2.1 Le formule (in parole)

- **Visite** = ordini ÷ tasso di conversione.
- **Ordini** = ordini di clienti nuovi + ordini di clienti che tornano.
- **Ordini di ritorno del mese** = per ogni mese passato, clienti nuovi di quel mese × probabilità che
  tornino dopo quei mesi. **Clienti nuovi che servono** = ordini obiettivo − ordini di ritorno.
- **Clienti da pubblicità** = budget ÷ CAC; **CAC** = costo per clic ÷ conversione.
- **Iscritti a fine mese** = iscritti del mese prima − 1,5 % + visite × 2 % + clienti nuovi × 30 %.
- **Ordini da email** = iscritti × 4 campagne × 0,17 % + iscritti nuovi × 2 % (benvenuto) + carrelli
  abbandonati con email × 3 %.
- **Margine per visita** = margine da dividere a ordine × conversione.
- **LTV in margine** (24 mesi) = margine a ordine × (1 + ordini di ritorno per cliente in 24 mesi).
  **CAC sostenibile** = LTV ÷ 1,5.
- **Guadagno da dividere al mese** = ordini × margine a ordine − pubblicità − piattaforma (come il
  report; l'avvio da 500 € è escluso).

**IPOTESI** usate (tutte modificabili nello script):

| Leva | Basso | Medio | Alto | Da dove |
|---|---|---|---|---|
| Conversione | 1,0 % | 1,5 % | 2,5 % | §1.1: Italia ~1 %, Littledata 1,4 %, top 20 % 2,6 % |
| Ordini di ritorno per ogni cliente nuovo, primi 12 mesi | 0,30 (20 % ricompra × 1,5 ordini) | 0,54 (30 % × 1,8) | 0,80 (40 % × 2,0) | §1.3: consumabili 22-44 %, F&B 2-4 ordini l'anno |
| Idem, secondo e terzo anno | 40 % e 20 % del primo anno | | | nessuna fonte |
| Quando tornano (dei ritorni del primo anno) | 25 % nel primo mese, 25 % nel 2°-3°, 50 % fra il 4° e il 12° | | | più lento di B&S (50 % entro 30 giorni [B12]): una crema dura più di un integratore |
| Popup | 1,5 % | 2 % | 3 % | Omnisend 2,1 %, con ruota 3,5 % [B24] |
| Consenso alla newsletter al checkout | 30 % dei clienti nuovi | | | nessuna fonte |
| Uscite dalla lista | 1,5 % al mese | | | nessuna fonte |
| Ordini per campagna (per iscritto) | 0,08 % | 0,17 % | 0,26 % | InboxAlly, Branvas [B20][B21] |
| Carrelli: con email / recuperati | 35 % / 3 % | | | Baymard 70,22 % [B18]; carrello 3,07 $ per destinatario [B20] |
| Costo per clic medio della pubblicità | 0,55 € | 0,70 € | 1,00 € | 05 §5 (Shopping 0,55 €, Meta ~1 €) |
| CAC pubblicità | 25 € | 35 € | 50 € | §1.5 |

### 2.2 Visite al mese che servono

STIMA: visite = ordini ÷ conversione.

| Ordini al mese | Conversione 1,0 % | **1,5 %** | 2,5 % | Al giorno (1,5 %) |
|---|---|---|---|---|
| **100** (anno 1) | 10.000 | **6.667** | 4.000 | 222 |
| **250** (anno 2) | 25.000 | **16.667** | 10.000 | 556 |
| **450** (anno 3) | 45.000 | **30.000** | 18.000 | 1.000 |
| Dicembre anno 1 (200 ordini) | 20.000 | 13.333 | 8.000 | 444 |
| Dicembre anno 2 (500 nel modello; 630 con crescita continua, §3) | 50.000-63.000 | 33.333-42.000 | 20.000-25.200 | 1.111-1.400 |
| Dicembre anno 3 (900; 980) | 90.000-98.000 | 60.000-65.300 | 36.000-39.200 | 2.000-2.180 |

### 2.3 Clienti nuovi e clienti di ritorno

STIMA: simulazione mese per mese (formula al §2.1) sul percorso di ordini del §3, con le tre ipotesi di
riacquisto. Medie mensili.

| Periodo | Ordini al mese | Riacquisto basso: nuovi / di ritorno | **Medio** | Alto |
|---|---|---|---|---|
| Anno 1 a regime (set 2027-feb 2028) | 119 | 101 / 18 (15 %) | **90 / 29 (25 %)** | 79 / 40 (33 %) |
| Anno 2 (mar 2028-feb 2029) | 250 | 206 / 44 (18 %) | **180 / 70 (28 %)** | 159 / 91 (37 %) |
| Anno 3 (mar 2029-feb 2030) | 450 | 347 / 103 (23 %) | **291 / 159 (35 %)** | 247 / 203 (45 %) |
| **Clienti nuovi in un anno** (anni 1 / 2 / 3) | 978 / 3.000 / 5.400 ordini | 849 / 2.475 / 4.165 | **764 / 2.164 / 3.492** | 687 / 1.903 / 2.966 |

**Lettura.** Anche con un riacquisto «alto», più della metà degli ordini del terzo anno viene da clienti
nuovi. Il negozio deve trovare **~290 clienti nuovi al mese nel terzo anno** (scenario medio). Il
riacquisto aiuta, ma non sostituisce l'acquisizione: passare da riacquisto medio ad alto risparmia ~45
clienti nuovi al mese.

### 2.4 Newsletter: quanti iscritti, quanti ordini

STIMA: lista che serve perché l'email porti il 15-25 % degli ordini (benchmark: 19 % [B19]; 25-35 %
food secondo le agenzie [B22]; 8,6 % in UK contando l'ultimo clic [B6]). Ordini dai flussi (benvenuto +
carrello) calcolati con le IPOTESI del §2.1; il resto deve venire dalle campagne (4 al mese).

| Ordini al mese | Quota email | Ordini da email | di cui flussi | Iscritti che servono (campagne a 0,08 % / **0,17 %** / 0,26 %) |
|---|---|---|---|---|
| 100 | 15 % | 15 | 5 | 3.080 / **1.450** / 950 |
| 100 | 20 % | 20 | 5 | 4.640 / **2.190** / 1.430 |
| 250 | 20 % | 50 | 13 | 11.610 / **5.460** / 3.570 |
| 250 | 25 % | 63 | 13 | 15.510 / **7.300** / 4.770 |
| 450 | 25 % | 113 | 23 | 27.930 / **13.140** / 8.590 |

**Quanti iscritti arrivano davvero** (STIMA, popup 2 % + 30 % dei clienti nuovi − 1,5 % al mese, con le
visite del §3): ~1.750 a febbraio 2028, ~5.500 a febbraio 2029, ~10.800 a febbraio 2030. Con queste liste
l'email porta, nella simulazione, il 13-15 % degli ordini nell'anno 1, il 13-19 % nell'anno 2 e il
16-23 % nell'anno 3: sotto il 19-27 % dei benchmark. Per il 25 % del terzo anno mancano ~2.300 iscritti:
servono popup migliori (ruota 3,5 % [B24]) o contenuti che raccolgono contatti (guida alla scala di
Scoville, «la varietà del mese»).

### 2.5 Pubblicità: quanti soldi, a che costo per cliente

**Quanti clienti nuovi compra il budget del piano** (STIMA; clienti nuovi che servono = riacquisto medio,
§2.3):

| Anno | Budget al mese | Clienti nuovi che servono al mese | Con CAC 25 € | Con CAC 35 € | Con CAC 50 € | Budget per comprarli tutti a 35 € |
|---|---|---|---|---|---|---|
| 1 (a regime) | 500 € | 90 | 20 (22 %) | 14 (16 %) | 10 (11 %) | 3.140 € |
| 2 | 1.000 € | 180 | 40 (22 %) | 29 (16 %) | 20 (11 %) | 6.310 € |
| 3 | 1.500 € | 291 | 60 (21 %) | 43 (15 %) | 30 (10 %) | 10.190 € |

**Visite pagate e visite da trovare gratis** (STIMA, costo per clic 0,70 €, conversione 1,5 %): anno 1
714 visite pagate su 6.667 (11 %); anno 2 1.429 su 16.667 (9 %); anno 3 2.143 su 30.000 (7 %). **Più
del 90 % delle visite deve arrivare senza pagare il clic.** Per confronto, nel Food & Drink britannico
Google a pagamento porta il 62,5 % delle vendite [B6]: il piano ambizioso chiede l'equilibrio opposto.

**Quanto vale una visita** (STIMA: margine da dividere × conversione):

| Ordine medio | Conversione | Margine per visita, primo ordine | Con i riacquisti dei 12 mesi (× 1,54) |
|---|---|---|---|
| 28,17 € | 1,5 % | **0,26 €** | 0,40 € |
| 28,17 € | 2,0 % | 0,34 € | 0,53 € |
| 33 € | 1,8 % | 0,36 € | 0,55 € |
| 40 € | 2,0 % | **0,50 €** | 0,77 € |
| 40 € | 2,5 % | 0,63 € | 0,96 € |

Un clic su Google Shopping costa 0,66 $ (USA [B37]); in Italia l'IPOTESI di 05 è 0,40-0,70 €. Su Meta
food il clic costa circa 0,40 $ (CPM 8,21 $ con CTR 2,06 %, Lebesgue [B11]; STIMA). Con l'ordine medio di
oggi la pubblicità a freddo **perde sul primo ordine** e rientra solo con i riacquisti; con 40 € e il 2 %
sta in piedi.

**CAC sostenibile** (STIMA: LTV in margine sui 24 mesi):

| Ordine medio | Riacquisto | Ordini in 24 mesi | LTV in margine | CAC massimo a pareggio | **con margine di sicurezza (LTV ÷ 1,5)** | regola «3 a 1» [B16] |
|---|---|---|---|---|---|---|
| 28,17 € | basso | 1,42 | 24,5 € | 24 € | 16 € | 8 € |
| 28,17 € | **medio** | 1,76 | 30,3 € | 30 € | **20 €** | 10 € |
| 28,17 € | alto | 2,12 | 36,5 € | 37 € | 24 € | 12 € |
| 40 € | basso | 1,42 | 35,6 € | 36 € | 24 € | 12 € |
| 40 € | **medio** | 1,76 | 44,1 € | 44 € | **29 €** | 15 € |
| 40 € | alto | 2,12 | 53,1 € | 53 € | 35 € | 18 € |

**Lettura.** I benchmark dicono 20-65 $ per un cliente food (§1.5). Con 28 € di ordine medio solo le
campagne migliori (Shopping su ricerche precise, remarketing, Meta food al livello Lebesgue) stanno sotto
i 20 €. La pubblicità serve, ma come acceleratore: il grosso dei clienti nuovi va trovato con Google
organico, schede Shopping gratuite, social, stampa, creator pagati in prodotto, Blend e B2B.

### 2.6 Ordine medio da 28 a 40 €: cosa cambia

STIMA dal modello del report: prezzo e costo della merce crescono insieme (più vasetti per ordine),
imballo +20 %, spedizione vera +0,50 € per il peso; commissioni, resi e IVA come nel modello.

| | **28,17 € (oggi)** | **40 €, spedizione pagata (5,90 €)** | 40 €, spedizione gratis a tutti |
|---|---|---|---|
| Margine da dividere a ordine | 17,24 € | **25,04 € (+45 %)** | 19,26 € (+12 %) |
| Ordini all'anno per le stesse vendite del piano (27,6 / 84,5 / 152,1 mila €) | 978 / 3.000 / 5.400 | **689 / 2.113 / 3.804** (57 / 176 / 317 al mese) | uguali |
| Guadagno da dividere al mese, stesse vendite (anni 1 / 2 / 3) | 805 / 3.190 / 6.108 € | 838 / 3.290 / 6.288 € | 506 / 2.272 / 4.455 € |
| Stessi ordini del piano: vendite all'anno | 27,6 / 84,5 / 152,1 mila € | 39,1 / 120,0 / 216,0 mila € | uguali |
| Guadagno da dividere al mese, stessi ordini | 805 / 3.190 / 6.108 € | **1.441 / 5.141 / 9.619 €** | 970 / 3.695 / 7.017 € |
| Ordini al mese per il guadagno del piano nell'anno 3 | 450 | **~317** | ~403 |
| Visite al mese per lo stesso guadagno, anno 3 (1,5 %) | 30.000 | **~21.100** | ~26.900 |

- **Soglia di spedizione gratuita.** Il margine scende di ~5,8 € a ogni ordine che non paga la
  spedizione. A 38 € con spedizione gratis il margine è 17,8 €, quasi quello di oggi (17,24 €); a 49 €
  con spedizione gratis arriva a 25,8 €. Esempio misto (STIMA): 60 % degli ordini a 32 € con spedizione pagata e 40 % a 55 €
  con spedizione gratis → ordine medio 41,2 €, margine 23,60 €. Regola pratica: **soglia gratuita a
  49 €** (come nel report, cap. 12), box a 39-49 € che la superano con un vasetto in più.
- **Da dove arriva l'ordine medio più alto** (benchmark §1.10): +54 % di ordine medio nei negozi con
  soglia (Metorik [B30]); +28 % nel caso di salse USA con scaglioni (01 [F49]); i box regalo a 38-49 €
  pesano di più a novembre-dicembre.
- **Risultato.** Portare l'ordine medio da 28 a 40 € vale, nel terzo anno, quanto **~130 ordini al mese
  in più**: meno pacchi per Luciano, meno visite da trovare, pubblicità più sostenibile.

---

## 3. Gli 8 KPI da guardare ogni mese, trimestre per trimestre

**Prima una correzione al percorso.** Nel foglio scenari l'anno 2 parte a marzo 2028 già a 250 ordini
al mese (da 95 di febbraio: ×2,6 in un mese) e l'anno 3 a 450. Qui gli obiettivi seguono una **crescita
continua** con gli **stessi totali annui del modello** (978 / 3.000 / 5.400 ordini) e la stessa
stagionalità. Anno 1 identico al modello; poi la tendenza (ordini al mese senza stagionalità) sale da
100 a febbraio 2028 a **358 a febbraio 2029** e **516 a febbraio 2030** (STIMA). Conseguenza: primavera
2028 più bassa del modello, Natali più alti (630 ordini a dicembre 2028, 980 a dicembre 2029).

### I KPI

| # | KPI | Come si misura | Perché |
|---|---|---|---|
| 1 | **Ordini al mese** | ordini pagati dal sito, esclusi B2B e omaggi | è il traguardo |
| 2 | **Visite al mese** (sessioni) | GA4 o statistiche Shopify | §2.2: il volume che serve |
| 3 | **Tasso di conversione** | ordini ÷ visite | la leva che costa meno |
| 4 | **Ordine medio** | € IVA inclusa, spedizione esclusa | §2.6: vale ~130 ordini al mese |
| 5 | **% ordini da clienti di ritorno** | ordini di chi ha già comprato ÷ ordini | §2.3 |
| 6 | **Iscritti alla newsletter** (e % vendite da email) | lista con consenso attivo; vendite attribuite | §2.4: il canale che non si paga a clic |
| 7 | **CAC della pubblicità** (massimo) | spesa ÷ clienti nuovi portati dalle campagne | §2.5: sotto questo valore la pubblicità si ripaga |
| 8 | **Guadagno da dividere al mese** | ordini × margine − pubblicità − piattaforma | è quello che va a B2Brand e Kalab |

### Valori obiettivo per trimestre (STIMA, medie mensili del trimestre)

| Trim. | Mesi | 1 Ordini al mese (mese di picco) | 2 Visite al mese | 3 Conv. | 4 Ordine medio | 5 Ordini di ritorno | 6 Iscritti a fine trim. (vendite da email) | 7 CAC max | 8 Guadagno da dividere al mese (con ordine medio fermo a 28 €) |
|---|---|---|---|---|---|---|---|---|---|
| T1 | mar-mag 2027 | 30 (42) | 3.800 | 0,8 % | 28 € | ≥ 8 % | 250 (≥ 10 %) | 30 € | −80 € (−80 €) |
| T2 | giu-ago 2027 | 57 (75) | 5.700 | 1,0 % | 28 € | ≥ 17 % | 620 (≥ 10 %) | 30 € | 380 € (390 €) |
| T3 | set-nov 2027 | 112 (135) | 9.300 | 1,2 % | 30 € | ≥ 19 % | 1.200 (≥ 10 %) | 21 € | 1.390 € (1.330 €) |
| T4 | dic 2027-feb 2028 | 127 (200) | 8.400 | 1,5 % | 33 € | ≥ 30 % | 1.750 (≥ 10 %) | 23 € | 1.930 € (1.580 €) |
| T5 | mar-mag 2028 | 132 (140) | 9.500 | 1,4 % | 31 € | ≥ 30 % | 2.300 (≥ 12 %) | 22 € | 1.330 € (1.160 €) |
| T6 | giu-ago 2028 | 143 (172) | 10.200 | 1,4 % | 31 € | ≥ 34 % | 2.900 (≥ 12 %) | 22 € | 1.520 € (1.340 €) |
| T7 | set-nov 2028 | 306 (396) | 19.100 | 1,6 % | 33 € | ≥ 22 % | 4.100 (≥ 12 %) | 23 € | 5.000 € (4.160 €) |
| T8 | dic 2028-feb 2029 | 419 (630) | 22.000 | 1,9 % | 36 € | ≥ 29 % | 5.500 (≥ 12 %) | 26 € | 8.150 € (6.100 €) |
| T9 | mar-mag 2029 | 358 (371) | 21.100 | 1,7 % | 34 € | ≥ 36 % | 6.700 (≥ 15 %) | 24 € | 5.760 € (4.520 €) |
| T10 | giu-ago 2029 | 290 (328) | 17.100 | 1,7 % | 34 € | ≥ 45 % | 7.500 (≥ 15 %) | 24 € | 4.360 € (3.350 €) |
| T11 | set-nov 2029 | 519 (644) | 27.300 | 1,9 % | 36 € | ≥ 30 % | 9.200 (≥ 15 %) | 26 € | 9.850 € (7.300 €) |
| T12 | dic 2029-feb 2030 | 633 (980) | 28.800 | 2,2 % | 40 € | ≥ 35 % | 10.800 (≥ 15 %) | 29 € | 14.190 € (9.260 €) |

Come sono costruiti:
- **1**: percorso a crescita continua (sopra). Per confronto, il modello a gradini del foglio dà per
  trimestre 30 / 57 / 112 / 127 / 233 / 171 / 279 / 317 / 420 / 307 / 503 / 570.
- **3 e 4**: IPOTESI. Conversione da 0,8 % (negozio nuovo, nessuna recensione) all'1,5 % di fine anno 1
  (mediana Littledata [B2]) e al 2,2 % del terzo anno (verso il top 20 %, 2,6 %); più alta nei trimestri
  di Natale per chi compra un regalo e per i clienti che tornano (IPOTESI, nessuna fonte). Ordine medio da
  28 a 40 € con box e soglia a 49 €, più alto a Natale.
- **2** = 1 ÷ 3. **5** = simulazione con riacquisto medio (§2.3): la quota scende nei trimestri di
  Natale perché arrivano molti clienti nuovi. **6** = simulazione del §2.4; la quota di vendite da email
  è il minimo che la simulazione dà in ogni anno (13-23 %), arrotondato per difetto: 10 / 12 / 15 %.
- **7** = LTV in margine (riacquisto medio, 24 mesi) all'ordine medio del trimestre ÷ 1,5; nei primi due
  trimestri si accettano 30 € perché le campagne devono imparare.
- **8** = come il report, con l'ordine medio del trimestre; tra parentesi con l'ordine medio fermo a 28 €
  (cioè lo scenario del report). In T1 è negativo perché pubblicità e piattaforma partono prima degli
  ordini.
- **Coerenza con i punti di controllo del report** (cap. 12): dopo 6 mesi almeno 50 ordini al mese (T2:
  57), dopo 12 mesi almeno 100 (T4: 127).

**Per arrivarci: da dove vengono i clienti nuovi** (STIMA, riacquisto medio, budget del piano al CAC
massimo del trimestre):

| Trim. | Clienti nuovi al mese | da pubblicità | da canali gratuiti | Visite non pagate al mese |
|---|---|---|---|---|
| T1 | 28 | 17 | 11 | 3.100 (81 %) |
| T2 | 47 | 17 | 31 | 5.000 (88 %) |
| T3 | 90 | 24 | 67 | 8.600 (92 %) |
| T4 | 89 | 22 | 67 | 7.700 (92 %) |
| T5 | 93 | 45 | 48 | 8.000 (85 %) |
| T6 | 95 | 45 | 49 | 8.800 (86 %) |
| T7 | 237 | 43 | 194 | 17.700 (93 %) |
| T8 | 297 | 38 | 258 | 20.600 (94 %) |
| T9 | 230 | 63 | 167 | 18.900 (90 %) |
| T10 | 159 | 63 | 97 | 14.900 (87 %) |
| T11 | 365 | 58 | 307 | 25.200 (92 %) |
| T12 | 411 | 52 | 359 | 26.600 (93 %) |

Il budget fisso per anno lavora male: in primavera 2028 compra metà dei clienti nuovi, a Natale meno di
un sesto. **IPOTESI**: spostare il budget sui trimestri forti (settembre-dicembre e febbraio-aprile).

**Spie da guardare insieme ai KPI** (non sono obiettivi, sono allarmi): recensioni (almeno 5 sui 10
prodotti più venduti entro T2: dopo 5 il vantaggio cala [B27]); carrello abbandonato sopra il 78 %
(mediana Littledata [B2]); resi e pacchi rotti sopra il 3 % (report cap. 12); prodotti esauriti fra i 10
più venduti; ordini per giorno lavorativo a dicembre (10 nel 2027, ~31 nel 2028, ~49 nel 2029: capacità
di confezionamento di Kalab, non analizzata qui).

---

## 4. Fonti

Tutte aperte il 04/10/2026, salvo dove scritto. «Secondaria» = la fonte cita un dato di altri.

- [B1] Eurostat, «Turnover and volume of sales in wholesale and retail trade - monthly data» (sts_trtu_m), NACE G4791 «Retail sale via mail order houses or via Internet», dati grezzi (NSA), fatturato netto, indice 2021=100, aggiornato 03/10/2026. API: https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sts_trtu_m?geo=IT&geo=DE&geo=FR&geo=ES&nace_r2=G4791&s_adj=NSA&unit=I21&sinceTimePeriod=2019-01&lang=EN (scaricata con curl e letta in Python: WebFetch restituiva numeri sbagliati).
- [B2] Littledata, «Shopify eCommerce Benchmarks (2026)», 421 negozi, 29/06-26/09/2026, generato 02/10/2026 — https://www.littledata.io/average ; https://www.littledata.io/average/ecommerce-conversion-rate-(all-devices)
- [B3] Dynamic Yield, «eCommerce Conversion Rate Benchmarks» (media 12 mesi, ultimo mese agosto) — https://marketing.dynamicyield.com/benchmarks/conversion-rate/
- [B4] Dynamic Yield, «Average Order Value Benchmarks» — https://marketing.dynamicyield.com/benchmarks/average-order-value/
- [B5] Shopify, «Ecommerce Conversion Rate: Benchmarks & Metrics», 22/08/2026 (cita Statista Q1 2026, Dynamic Yield, Contentsquare) — https://www.shopify.com/blog/ecommerce-conversion-rate
- [B6] IRP Commerce, «UK eCommerce Market Data», agosto 2026, tutte le categorie e Food & Drink — https://www.irpcommerce.com/en/gb/ecommercemarketdata.aspx ; https://www.irpcommerce.com/en/gb/ecommercemarketdata.aspx?Market=9
- [B7] ECDB (ecommerceDB), «E-Commerce KPI and Benchmarks Report 2026», 07/2026, PDF di 19 pagine — https://static.ecdb.com/media/2026/07/ecdb-e-commerce-kpi-and-benchmarks-report-2026-14366.pdf
- [B8] Eightx, «EU Ecommerce KPI Benchmarks 2026», 12/06/2026 (Italia 1,0 % da IRP Commerce/Rocking Web via Landmark Global; la pagina Landmark non si apre) — https://eightx.co/blog/eu-ecommerce-kpi-benchmark
- [B9] Sendcloud, «Tasso di conversione ecommerce: come aumentarlo», agg. 13/03/2026 (nessuna fonte per l'1,6 %) — https://www.sendcloud.com/it/blog/tasso-di-conversione-ecommerce-come-aumentarlo/
- [B10] Grips Intelligence, «Gourmet Food Gifts» e «Gourmet Food», dati agosto 2026 — https://gripsintelligence.com/insights/industries/food-beverages-tobacco/gourmet-food-gifts ; https://gripsintelligence.com/insights/industries/food-beverages-tobacco/gourmet-food
- [B11] Lebesgue, «Facebook benchmarks by industry: CTR, CPM, CR and CAC», 09/03/2026 — https://lebesgue.io/facebook-ads/facebook-benchmarks-by-industry-ctr-cpm-cr-and-cac
- [B12] B&S Co., «Repeat Purchase Rate Benchmarks», 14/02/2026 — https://bsandco.us/blog-post/repeat-purchase-rate-benchmarks
- [B13] Eightx, «Average ecommerce time to second purchase by vertical (2026)», 30/05/2026 — https://eightx.co/blog/average-ecommerce-time-to-second-purchase-by-vertical-2026
- [B14] Eightx, «Average purchase frequency (orders per customer per year) by vertical», 27/06/2026 — https://eightx.co/blog/average-purchase-frequency-orders-customer-yr-by-vertical
- [B15] Foundry CRO, «DTC food & beverage marketing benchmarks 2026», 12/05/2026 (secondaria: cita Klaviyo 2025, Swell, Eightx, Finsi, Northstar, Metrilo) — https://foundrycro.com/blog/dtc-food-beverage-marketing-benchmarks-2026/
- [B16] LoyaltyLion, «Average customer acquisition cost in ecommerce», 12/06/2025 (cita Shopify, dati 2021) — https://loyaltylion.com/blog/blog-average-cac-ecommerce
- [B17] Eightx, «Average CAC by marketing channel», 27/06/2026 — https://eightx.co/blog/average-cac-by-marketing-channel
- [B18] Baymard Institute, «Cart Abandonment Rate Statistics», agg. 22/09/2025 — https://baymard.com/lists/cart-abandonment-rate
- [B19] CustomersAI, «2026 Ecommerce Email Benchmarks Report», agg. 18/03/2026, PDF — https://customers.ai/wp-content/uploads/2026/03/CustomersAI-2026-Klaviyo-Email-Marketing-Benchmark-Report.pdf
- [B20] InboxAlly, «Klaviyo Email Benchmarks: Insights From 167,000 Brands», 05/03/2026 — https://www.inboxally.com/blog/klaviyo-email-benchmarks
- [B21] Branvas, «Ecommerce email marketing benchmarks», 08/05/2026 — https://branvas.com/blogs/news/ecommerce-email-marketing-benchmarks
- [B22] Eightx, «Average ecommerce email revenue share by vertical (2026)», 29/05/2026 — https://eightx.co/blog/average-ecommerce-email-revenue-share-by-vertical-2026
- [B23] Klaviyo, pagine dei report di benchmark 2026 (dati dietro modulo; 196.000 e 110.000 brand) — https://www.klaviyo.com/marketing-resources/email-benchmarks-by-industry ; https://www.klaviyo.com/marketing-resources/benchmark-report
- [B24] Omnisend, «Email popup statistics», 09/02/2026 — https://www.omnisend.com/blog/email-popup-statistics/
- [B25] Wisepops, «Popup statistics», 30/09/2025 — https://wisepops.com/blog/popup-stats
- [B26] CrazyEgg, «50+ Popup Statistics» (cita Klaviyo, Omnisend, Wisepops, Sleeknote) — https://www.crazyegg.com/blog/popup-statistics/
- [B27] Medill Spiegel Research Center, «How Online Reviews Influence Sales», 2017 — https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/
- [B28] Amazon Buy with Prime, «Turn customer reviews into sales», 24/10/2023 (cita anche PowerReviews) — https://buywithprime.amazon.com/blog/turn-customer-reviews-into-sales
- [B29] PowerReviews, «Online is the new frontier in grocery shopping», 19/09/2017 — https://www.powerreviews.com/new-frontier-in-grocery-shopping/
- [B30] Metorik, «Free shipping statistics», 15/07/2026 — https://metorik.com/blog/free-shipping-statistics
- [B31] Netcomm con Comieco, comunicato «La logistica è il motore dell'e-commerce italiano», 15/01/2018 (PDF) — https://www.comieco.org/downloads/9249/5306/Cs_Logistica%20e%20Packaging%20nelle-commerce.pdf
- [B32] Recharge, «2023 State of Subscription Commerce», 01/2023 — https://getrecharge.com/resources/industry-report/
- [B33] Eightx, «Average subscription churn rate by category», 03/05/2026 — https://www.eightx.co/blog/average-subscription-churn-rate-by-category
- [B34] AGI, «Natale, regali e cesti» (indagine Coldiretti/Ixè), 20/12/2025 — https://www.agi.it/cronaca/news/2025-12-20/natale-regali-cesti-coldiretti-34732758/
- [B35] Altroconsumo, «Spese di Natale degli italiani», 16/12/2025 — https://www.altroconsumo.it/vita-privata-famiglia/viaggi-tempo-libero/news/spese-natale-italiani
- [B36] LeggiOggi, «Regali aziendali di Natale e opportunità fiscali», 11/12/2023 — https://www.leggioggi.it/regali-aziendali-di-natale-e-opportunita-fiscali/
- [B37] File locali del progetto: `ricerca/01_mercato.md` (fonti F18, F20, F21, F25, F26, F49), `ricerca/05_seo_adv.md` §5 (fonti 3, 4, 5, 6, 7), `REPORT_fattibilita_kalab.md` cap. 6, 11, 12, 13; `scenari/ipotesi.py` e `scenari/calcola.py` (margine 17,24 €, ordine medio 28,17 €, stagionalità).
- [B38] Visti solo negli estratti dei motori di ricerca, **non verificati**: Wolfgang Digital 2024 (conversione per canale); Recharge, abbandono food & beverage 6,6-6,8 % (2022); Red Clay Hot Sauce, 32 % del fatturato da Klaviyo; Ringly, 44 % delle disdette dei box nei primi 90 giorni; Grips, «−50 % da dicembre a maggio» nei cesti regalo.

---

## 5. Buchi e dubbi

1. **Nessun benchmark per condimenti o salse piccanti**: conversione, riacquisto e tempi fra due ordini
   vengono da «food & beverage» (che mescola spesa, caffè, integratori) o da portafogli misti di agenzie
   USA. Il primo dato vero sarà quello di kalab.it: chiedere a Luciano statistiche e ordini (report cap.
   13, domande 1-2).
2. **Italia**: la conversione all'1 % arriva da una catena di tre fonti con l'originale non apribile;
   l'1,6 % di Sendcloud non ha fonte. Nessun dato italiano verificato su conversione, carrello e
   riacquisto per l'e-commerce alimentare di nicchia.
3. **Klaviyo**: i report 2025-2026 (email per settore, peso sul fatturato) sono dietro un modulo; i
   numeri arrivano da siti terzi che non concordano (ordini per campagna 0,08-0,26 %; email sul fatturato
   19-27 %). Non ho compilato il modulo: è vietato dalla consegna.
4. **Abbonamenti food**: l'abbandono mensile food & beverage di Recharge (6,6-6,8 %) è solo in un
   estratto; il report aperto è del 2023 e dà la media di tutti i settori. Il box «la varietà del mese» è
   un abbonamento a sorpresa: fonti terze dicono 12-18 % di abbandono al mese, cioè vita media di 6-8 mesi.
5. **Regali aziendali**: mercato italiano, spesa media per regalo e calendario degli ordini NON TROVATI
   in due ricerche dedicate (solo report globali a pagamento). Soglie dei fringe benefit 2025-2027 da
   verificare col commercialista.
6. **Stagionalità del food online in Italia**: Eurostat dà tutte le merci, non il food; per i regali
   gastronomici c'è solo Grips (paesi non dichiarati, dati grezzi). Il peso 2,0 di dicembre del modello resta un'IPOTESI.
7. **Curva di ritorno**: la distribuzione dei secondi ordini (50 % entro 30 giorni) è di un portafoglio
   USA con integratori e cosmetica; per le creme ho rallentato i ritorni (IPOTESI). I clienti di Natale
   comprano regali e probabilmente ritornano meno: da misurare dal primo Natale.
8. **Il foglio scenari ha un gradino** a marzo 2028 (da 95 a 250 ordini) e a marzo 2029: i KPI qui
   usano una crescita continua con gli stessi totali annui. Conviene allineare `scenari/ipotesi.py`
   (scelta che spetta a chi tiene il modello).
9. **Costi pubblicitari italiani**: nessun CPC Google italiano gratuito (stesso buco di 05); i dati Meta
   food non dichiarano i paesi. I CAC del §2.5 vanno rifatti dopo 30 giorni di campagne vere.
10. **Margine a 40 €**: costruito scalando il modello; i costi veri di polveri, sott'olio e box sono
    ancora stime (report cap. 6). Con il listino di Luciano il margine a 40 € può cambiare di qualche euro.
11. **Fonti di agenzia** (Eightx, B&S Co, Branvas, Foundry CRO, CustomersAI): campioni propri e metodi
    non verificabili; vanno usate come ordine di grandezza, mai come numero unico.
12. **Wolfgang Digital**: lo studio scaricabile è del 2014 (inutile); i numeri 2024 per canale sono solo
    da snippet.
13. **Capacità di Kalab a dicembre**: il piano chiede ~49 ordini per giorno lavorativo a dicembre 2029;
    chi li confeziona e dove non è materia di questo filone (vedi logistica, report cap. 4.7).
14. **Budget di ricerca**: 22 ricerche web su 25; il resto con pagine aperte direttamente.
