# 02 — Concorrenza: chi vende già peperoncino online (Italia, Europa, marketplace)

Studio di fattibilità e-commerce Kalab (Scalea, CS — oltre 350 varietà di peperoncino).
Ricerca svolta solo via web (WebSearch + WebFetch), **data di consultazione: 02/10/2026** per tutte le fonti, salvo diversa indicazione. Nessun contatto, nessun acquisto.

Legenda: **DATO** = letto sulla pagina indicata · **STIMA** = dedotto, non letto · **n.d.** = non disponibile / pagina non apribile.

---

## Riassunto (da leggere per primo)

1. **I cinque concorrenti più forti per Kalab**, in ordine di pericolosità:
   - **DiavoloPiccante / RoyalChili** (Monterotondo, Roma) — l'unico italiano con un catalogo "enciclopedico" a prezzo unitario: 172 varietà di semi, 166 secchi, 169 polveri, fresco stagionale, piante. È il modello più vicino a "350 varietà". Prezzi bassissimi (semi da 0,99 €, polvere 0,99 €/g, secco 0,99 €/frutto), spedizione semi 2,99 €, fresco 5,99 €. Ha anche la versione francese (royalchili.com). [F7][F8][F9][F10]
   - **Peperita** (Bibbona, LI) — il marchio "premium bio" italiano: 18 varietà coltivate, polveri da 12 g a 4,95–11,50 €, salse 70 g a 6,95 €, kit regalo fino a 131 €, spedizione in UE 13,90 € flat, gratis in Italia da 75 €. Molto forte nel retail e nelle gastronomie. [F1][F2][F3]
   - **Pepperworld Hot Shop** (Weyhe, Germania) — il più grande negozio europeo di piccante: >900 articoli, "banca semi più completa della Germania", piante, salse, dal 2001. Sito bloccato al nostro fetch (403), dati da fonti terze. [F30][F31]
   - **Chili Food** (Germania) — >250.000 clienti dichiarati, 4,9/5 su 1.322 valutazioni, fresco+secco+semi+piante+salse, sito in 6 lingue compreso l'italiano, spedizione DE 5,90 € gratis da 75 €. [F32]
   - **Westlandpeppers** (De Lier, Paesi Bassi) — l'unico che spedisce **fresco in tutta Europa, tutto l'anno** (serre proprie apr–nov, import Spagna/Israele/Marocco in inverno); spedizione in Italia 27,65 €, nessuna soglia gratis, reclami entro 1 giorno. [F33][F34][F35]
2. **Fasce di prezzo tipiche** (dettaglio nella tabella "prezzi di mercato"): fresco 3,90–13,60 €/kg in Calabria, 8–20 €/kg per varietà esotiche (Alba 5,50 € / 250 g = 22 €/kg); polvere 45–100 g 3,50–6 € da aziende calabresi, 12 g a 4,95–11,50 € (= 400–950 €/kg) nel premium bio; salse/creme 90–200 g 4,50–15 €; sott'olio 180–280 g 4,49–17,99 €; bustina semi 0,99–5,90 € (Italia), 2,75–4,95 € (UE); piantina 2,70–5 €; box/kit 13,90–131 €; abbonamento 12 €/mese (unico trovato, Chilli No. 5, UK).
3. **Vuoti di mercato** (sezione E): nessuno in Italia spedisce fresco con garanzia dichiarata e consegna in tutta l'UE; nessun negozio italiano ha un sito davvero multilingua (lo hanno i tedeschi); nessuno in Italia dichiara più di ~172 varietà in vendita (il database Pepperfriends ne censisce 480 ma non è un negozio); gli abbonamenti al piccante non esistono in Italia; nessun negozio collega il proprio brand al Campionato italiano mangiatori di peperoncino di Diamante, che si tiene a 20 km da Scalea; le ricerche "varietà + Scoville" sono presidiate da siti editoriali (peperonciniperhobby.it, mondodelpeperoncino.it), non da negozi.
4. **Attenzione**: i grandi marketplace (Amazon, Etsy, eBay) e i motori di ricerca si sono chiusi alla nostra lettura automatica (403/503/CAPTCHA): i dati marketplace sono parziali e vanno completati a mano (vedi "Buchi e dubbi").

---

## A. Concorrenti italiani

| # | Negozio | Sede | Cosa vende | Varietà dichiarate | Prezzi letti (DATO, 02/10/2026) | Spedizione | Europa | Piattaforma | Marketplace / recensioni / social | Posizionamento | Fonte |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Peperita** · peperita.it | Bibbona (LI), Toscana | polveri, salse/concentrati, condimenti, triti freschi, paté, marmellate, salamoia, pasta, cosmetica. **No semi, no piante, no fresco intero** | 18 varietà coltivate | Polveri 12 g: 4,95 € (Caienna, Jalapeño, Scotch Bonnet) · 8,95 € (Naga, Bhut Jolokia, 7 Pod, Scorpion) · 11,50 € (Carolina Reaper); Salsa 101/100 70 g 6,95 €; scaglie Caienna 60 g 4,90 €; borsellino 10 polveri 39,80 €; kit "Cubo" 16 polveri 131,05 € | Italia 6,90 € (<28,90 €), 4,90 € (28,91–75 €), **gratis >75 €**; UE (FR, DE, AT, BE, NL…) **13,90 € flat fino a 30 kg**; ES/PT 12,90–22,90 €; CH 17,90–44,90 €; 3–7 gg, SDA/DHL/FedEx | **Sì** | n.d. (nessun indizio esplicito) | Trustpilot 4,1/5 su 7 recensioni; social FB/IG/YT/Flickr; Instagram follower n.d. | "La via Toscana al Peperoncino", bio certificato, numerazione 1–17 della piccantezza, kit regalo | [F1][F2][F3][F4] |
| 2 | **DiavoloPiccante** · diavolopiccante.it (gemello FR: royalchili.com) | Monterotondo (RM) | semi, fresco (ago–nov), secco, polveri, piante, salsa "Diavolito", sale, olio, semi ortaggi, fertilizzanti, ebook | **172 semi · 166 secchi · 169 polveri** (conteggi di categoria) | Semi 0,99–5,90 € a bustina (Dorset Naga 0,99 €, Naga Morich 1,30 €, Moruga 1,90 €, Rimmerhus 5,90 €); **polvere 0,99 €/g** (tutte le varietà); **secco 0,99 €/frutto** (bustine ~15 g); fresco a pezzo: Habanero 3–4,90 €, Carolina Reaper 5–6 €, Calabrese 4,49 €, mix 4,99–5,99 € | semi 2,99 €; fresco e piante 5,99 €; **fresco spedito solo il lunedì**, in contenitori alimentari trasparenti; soglia gratis non indicata; estero non indicato | n.d. (FR tramite RoyalChili) | PrestaShop | IG @diavolopiccanteworld, FB; follower n.d. | "boutique del piccante", 100% naturale, newsletter | [F7][F8][F9][F10][F11] |
| 3 | **Mr. Pepper** · mr-pepper.it | Ardea (RM), Agro Pontino | fresco, secco intero, polveri, creme in purezza, confetture, salse, olio EVO, sott'olio, piantine, kit degustazione | ~9 citate (Reaper, Moruga, 7 Pot, Fatalii, Aji Amarillo, Jalapeño, Habanero, Diavolicchio, Cayenna) | Crema Carolina Reaper 30 g 4,50 €; olio EVO Reaper 100 ml 8,90 €; **box mix fresco 1,2 kg 25 €** (≈20,8 €/kg); kit Reaper 30,30 € | **gratis >49 €**, 24/48 h Italia | n.d. | PrestaShop (MDN Informatica) | FB; follower n.d. | coltivazione diretta, filiera corta, senza conservanti | [F12] |
| 4 | **Assopepper** · assopepper.com | Sicilia | fresco, secco, polvere, intero, semi, piante ("peperoncini dal mondo coltivati in Sicilia"); vende anche su Amazon | n.d. | n.d. — **sito 403 al fetch** | n.d. | n.d. | n.d. | Amazon sì (link in F13) | focus super-hot | [F13][F14] |
| 5 | **Vendita Peperoncini Online** · venditapeperoncinionline.it | n.d. | piante in vaso ø5,5 e ø14 | "oltre 100 varietà" | piante 3–5 € | corriere SDA 24/48 h; costi n.d. | n.d. | n.d. (carrello, wishlist) | FB/IG/YT | "Crea il tuo angolo piccante", testimonianze | [F15] |
| 6 | **Pepperitalia** · pepperitalia.eu | San Cesareo (RM) | piante peperoncino, aromatiche, da frutto; semi su piattaforma separata | n.d. | n.d. (prezzi non in pagina) | "spedizione gratuita in Italia" (snippet) | n.d. | Jimdo | FB, WhatsApp | km zero, no pesticidi | [F16] |
| 7 | **Il Giardino delle Meraviglie** · ilgiardinodellemeraviglie.it | Vittoria (RG), Sicilia | piante di peperoncino vaso 17 | 55 varietà | **prezzi solo dopo login** | n.d. | n.d. | proprietaria, PayPal | IG @giardinomsicily | vivaio, varietà regionali + esotiche | [F17] |
| 8 | **AgriPetGarden** · agripetgarden.it | Conselve (PD) | piante peperoncino vaso 10,5 con cartellino | 23 varietà | 3,95–4,50 € (Habanero Chocolate 3,95; Reaper 4,35; Samba Mix 4,50) | **gratis >69 €**, 24/48 h | n.d. | proprietaria | n.d. | "più grande selezione online" | [F18] |
| 9 | **La Casetta Bio** · shop.lacasettabio.it | Massignano (AP) | piantine (anche "senza vasetto"), semi | 16 prodotti piantine | piantine 2,70–3,20 € (Reaper 3,20; Dorset Naga 3,00) | spedisce lun–mar; costi n.d. | n.d. | PrestaShop | n.d. | bio | [F19] |
| 10 | **Semi Rari** · semirari.it | Milano | semi peperoncino (import) | 18 varietà | 4,90–5,90 € a bustina; kit 13,90 € | "da determinare" | n.d. | PrestaShop | FB | semi rari importati | [F20] |
| 11 | **Botanis** · botanis.it | Italia | semi | 31 prodotti | **3,99 € / 50 semi** (tutte) | n.d. | "spedizioni internazionali" | Shopify | IG/TikTok @botanis.it | super-hot (X Uno, Reaper) | [F21] |
| 12 | **Sfizi di Calabria** (Galasso srl) · sfizidicalabria.com | Santa Maria del Cedro (CS) — **Riviera dei Cedri, a 10 km da Scalea** | sott'olio (macinato 180 g, diavolicchio intero 280 g, rondelle 280 g), fresco diavolicchio 1 kg, creme Habanero/Bhut/Reaper/Scorpion, condimento 10 cl | n.d. | 4,49–17,99 €; crema Reaper 17,99 → 12,99 € | Italia **5,90 €**, gratis >149 €, BRT 24/48 h; **estero 1–10 kg: DE/AT 18,90 €, ES 19,90 €, FR 25,90 €** | **Sì** | Scaboo | FB/IG/YT | conserve calabresi | [F22][F23] |
| 13 | **Fattoria Biò** · shop.fattoriabio.it | Camigliatello Silano (CS) | polvere, scaglie, sott'olio, macinato sott'olio (bio) | n.d. | polvere da 3,50 €; scaglie da 3,50 €; vasetto sott'olio 7,00 €; macinato sott'olio 4,90 € | Italia 4,90 € (0–10 kg), **gratis >69 €**; estero n.d. | n.d. | **Shopify** | n.d. | bio calabrese, numero verde | [F24][F25][F26] |
| 14 | **Favella** · favella.it | Corigliano Rossano (CS), dal 1932, 240 ha | fresco (100 g / 500 g / 1,2 kg), sott'olio 90 g | n.d. | **fresco da 2,00 €/100 g** (=20 €/kg); sott'olio 6,60 € | gratis >75 €; **shelf-life dichiarata ~10 gg dalla raccolta** | n.d. | Shopify | Trustpilot linkato (voto n.d., pagina 404); IG favella_group | serre a energia pulita, no OGM | [F27][F28] |
| 15 | **Sibarizia** · sibarizia.it | Corigliano Calabro (CS) | fresco Amando al kg + tipici | — | **fresco 5,00 € (1,3 kg)** ≈ 3,85 €/kg (snippet: 3,90 €/kg) | gratis >99,90 € | n.d. | WooCommerce | recensioni on-site | 30–60k SHU | [F29] |
| 16 | **Agricola Conforti** · agricolaconforti.it | San Giorgio Albanese (CS) | fresco Pizzitano 1 kg | — | **8,90 €/kg** (esaurito) | gratis >39,90 € | n.d. | WooCommerce | — | 15–30k SHU | [F36] |
| 17 | **Val d'Esaro** · valdesaro.it | San Lorenzo del Vallo (CS) | fresco 100 g/1 kg/box 5 kg; secco "Piccantello" 2,70 €; scaglie 3,40 €; trito 6 €; rondelle 6 €; confettura 3,70 € | — | **fresco 13,60 € (1 kg)**; box 5 kg spedizione gratis | spedisce lun–mer "per garantire freschezza" | n.d. | PrestaShop | — | — | [F37] |
| 18 | **Le Fresie Conserve** · lefresieconserve.it | Cassano allo Ionio (CS) | fresco vaschetta 125 g, piccante calabrese | — | **4,50 € / 125 g** (=36 €/kg) | Italia **9,90 €**, gratis >100 €, 24/48 h; **Europa 72/96 h** | **Sì** | PrestaShop | — | — | [F38] |
| 19 | **Società Agricola Alba** · albapeperoncinoshoponline.it | Bellaria (RN) | fresco vaschette 250 g, piante, ricette | 13 referenze fresche | **4,50–6,00 € / 250 g** (Reaper, Moruga, Naga 6 €; Habanero 5,50 €; Cayenna 4,50 €) = 18–24 €/kg; tutto esaurito al 02/10 | "spedizione gratuita nei seguenti Paesi" (lista non espansa) | probabile | Jimdo | FB | — | [F39] |
| 20 | **Nero di Calabria** · shop.nerodicalabria.com | Calabria | polvere 45 g, ripieni di 'nduja, confettura, crema Habanero 90 g | — | **polvere 45 g 6,00 €** (133 €/kg); crema Habanero 90 g 11 €; confettura 200 g 11 € | n.d. | n.d. | proprietaria | FB/YT | bio | [F40] |
| 21 | **TuttoCalabria** · tuttocalabria.com | Marcellinara (CZ) | sott'olio interi/tondi/rondelle/crunchy, salse, polvere, grani, ripieni; **presente su Amazon** | — | salsa aglio 6 €; MielHOT 6,50 €; peperoncini a pezzi 5,20 €; Olio Santo 6 € | Italia 3–4 gg gratis >70 €; **Europa 5–7 gg gratis >120 €** | **Sì** | proprietaria | IG/FB @tuttocalabria; Amazon: polvere 500 g 4,7/5 (22 rec.) | industriale-artigianale, export | [F41][F42] |
| 22 | **Delizie di Calabria** · deliziedicalabria.it | Catanzaro | ripieni sott'olio, salse, spezie; linea export | — | **shop "in costruzione"**: vende via telefono/WhatsApp e rivenditori (es. tritato 950 g su italyfoodshop.it) | — | — | — | FB/IG/YT/LinkedIn | famiglia dal 1989 | [F43] |
| 23 | **Accademia Italiana del Peperoncino** · peperoncino.org | **Diamante (CS)** | shop: semi (gratis ai soci, solo spese), libri, cataloghi, gadget, cravatte Marinella; "Atlante delle varietà" | — | — | — | — | — | — | associazione, gradi accademici, circuito ITALIAPIC, co-organizza il Peperoncino Festival | [F44] |
| 24 | **Pepperfriends** (associazione) · pepperfriends.org / .com | Caldiero (VR) | semi per i soci; **database varietà** | **480 varietà nel database, 277 con semi disponibili** | n.d. (costo tessera non trovato) | — | — | ASP classico + forum | — | riferimento degli appassionati italiani dal 2000s | [F45][F46][F47] |

Note sui nomi del brief non trovati: "Azienda Agricola Mezzaluna" risulta un agriturismo toscano (olio, vino) senza peperoncino [F5]; "Peperoncino.it", "Il Re del Peperoncino", "La Bottega del Peperoncino", "Capsicum Diamante", "Fuoco Verde", "Pepe Rosso" **non sono emersi** come negozi online attivi nelle ricerche (il budget ricerche si è esaurito prima di una verifica diretta: vedi Buchi). Altri negozi di semi citati da mondodelpeperoncino.it: Cascina Beneficio, Draxpeppers, Spacepeppers, Alfo Wild Pepper (FB), Semi Strani (Amazon) [F6].

---

## B. Concorrenti europei

| # | Negozio | Paese/sede | Cosa vende | Varietà / articoli | Prezzi letti (DATO) | Spedizione | Fresco? come | Piattaforma | Recensioni / social | Fonte |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Pepperworld Hot Shop** · pepperworldhotshop.com | Weyhe (DE), dal 2001 | semi, piante, chili crudi, spezie, salse, kit coltivazione, liofilizzati, rub | **>900 articoli**; "banca semi più completa della Germania" | **n.d. — sito 403 in tutte le lingue** | n.d. | sì ("chili crudi") — modalità n.d. | n.d. (Shopware STIMA) | Trusted Shops n.d.; X @PWHotShop; rivista pepperworld.com | [F30][F31][F48] |
| 2 | **Chili Food** · chili-food.de | Germania (prefisso 06322, Palatinato) | fresco, secco, semi, piante, salse, polveri, snack, libri | n.d. ("250.000 clienti") | n.d. (catalogo e pagina spedizioni **ECONNREFUSED** al 2° tentativo) | **DE 5,90 €, gratis >75 €**; ordine entro le 12 → spedito in giornata DHL | sì — dettagli n.d. | proprietaria, **6 lingue incl. italiano** | **4,9/5 su 1.322 valutazioni** (EHI/BVH) | [F32] |
| 3 | **Chili-Shop24** · chili-shop24.de | DE | — | — | **sito irraggiungibile (ECONNREFUSED)** | — | — | — | — | — |
| 4 | **Westlandpeppers** · shop.westlandpeppers.com | De Lier (NL), coltivatore | fresco, secco, salse, mix | — | fresco: cayenne da 4,06 € (500 g/1 kg/5 kg), Jalapeño da 2,62 €, Rawit da 7,63 €, Pepper Mix 75 g 2,39 € | **IT 27,65 € (fino a 17 kg), DE 14,85 €, BE 10,20–26,55 €; nessuna soglia gratis**; IT 2–4 gg; ordine entro 9:30 → spedito in giornata; 25 paesi UE | **sì, tutto l'anno**: serre NL apr–nov, import ES/IL/MA in inverno; scatola export rinforzata; **no reso sul fresco, reclamo entro 1 giorno con foto** | WooCommerce | Trustpilot **4,2/5 su 12 recensioni** | [F33][F34][F35][F49][F50] |
| 5 | **Chilibrothers** (BE/NL) | — | — | — | **dominio .be e .nl non risolvono** | — | — | — | — | — |
| 6 | **South Devon Chilli Farm** · southdevonchillifarm.co.uk | Devon (UK) | fresco (lug–nov), semi, secco, piante, salse, conserve, cioccolato | ~34 referenze fresche | fresco: Habanero arancio da 5,75 £, Reaper da 8,40 £, Scorpion 7,35 £, Jalapeño 6,30 £, Poblano 5,20 £, Lucky Dip 7,95 £ (peso confezione n.d.) | UK: DPD 1–2 gg; **gratis >60 £ con codice**; **ordini verso l'Europa SOSPESI (Brexit)** | sì — "raccolto, imballato e spedito la stessa mattina"; no weekend | Shopify | 26 recensioni sul Reaper; FB/IG/TikTok/YT | [F51][F52][F53] |
| 7 | **Sea Spring Seeds** · seaspringseeds.co.uk | West Dorset (UK) | semi, piante, fresco Dorset Naga | >30 varietà semi | semi **2,00–3,00 £**, superhot 5,00 £; collezioni 20–70 £ | **no UE né Irlanda del Nord (Brexit)** | sì (Dorset Naga) | WooCommerce | FB/X/YT | creatori del Dorset Naga, famiglia Michaud | [F54][F55] |
| 8 | **Hot-Headz** · hot-headz.com | Stroud (UK), 30 anni | salse (decine di marchi), snack, spezie, regali, sfide | >100 prodotti | 1,00–13,99 £ (Marie Sharp's 4,99; gift set 13,99) | calcolatore mondiale; no soglia visibile | no | WooCommerce | 4,5–5 stelle on-site; IG/FB/X | [F56] |
| 9 | **Chilli Pepper Pete** · chillipepperpete.com | UK | — | — | **certificato SSL scaduto, sito non apribile** | — | — | — | — | — |
| 10 | **Chilli No. 5** · chilli-no5.com | UK (WhatsApp +44) | salse gourmet, **abbonamento** | — | **abbonamento 144 €/anno (=12 €/mese), 2 bottiglie/mese, valore dichiarato 18 €/mese** | gratis >50 £/50 € UK ed Europa | no | WooCommerce | 0 recensioni sul prodotto; badge Trustpilot | [F57] |
| 11 | **Le Comptoir du Piment – Maison Lukuya** · lecomptoirdupiment.com | Souraïde, Paesi Baschi (FR) | piment d'Espelette AOP e derivati, salumi, conserve | 1 varietà (Espelette) | n.d. | n.d. | no | n.d. | FB | AOP, territorio | [F58] |
| 12 | **La Sauce Piquante** · sauce-piquante.fr | Francia | fresco (>20 varietà), semi (**348 varietà**), piante (6), secchi, salse | 348 semi | **sito 406 al fetch** | 48 h (snippet) | sì (snippet) | PrestaShop (STIMA da URL) | n.d. | [F59][F60] |
| 13 | **RoyalChili** · royalchili.com | gemello FR di DiavoloPiccante (Monterotondo) | semi, fresco ago–dic, piante apr–lug, secco/polvere, salse | "una delle banche semi più complete" | n.d. ("à définir") | n.d. | sì | PrestaShop | FB | [F10] |
| 14 | **Pepperseeds.eu** | Benelux | semi | **~300 varietà**, "più grande fornitore del Benelux" | **2,75–4,95 €** a bustina (Jalapeño Lemon Spice 3,85; Capperino F1 3,95) | "ordinato entro le 17 spedito oggi"; costi n.d. | no | BigCommerce | garanzia germinazione | [F61] |
| 15 | **Magic Garden Seeds** · magicgardenseeds.it | Germania (sito in italiano) | semi | **109 varietà** peperoncino | 2,59–4,99 € (Cayenna bio 2,59; Bhut Jolokia 2,99; Rocoto 4,99; set 9,99) | **tutta Europa, gratis >50 €** | no | proprietaria | — | [F62] |
| 16 | **Semillas.de** | Germania | semi | 22 varietà chili (62 prodotti) | **3,90 € flat** | **UE gratis >40 €** | no | Shopify | — | [F63][F64] |
| 17 | **MikelSimon** · mikelsimon.com | Oliva (Valencia, ES) | semi chili e pomodoro | >100 varietà | **1,75–3,25 € / 10 semi** (Reaper Golden 2,75); pack 9,95–22,95 € | **gratis >30 €**; 28 lingue, 17 valute | no | PrestaShop | FB | [F65] |
| 18 | **Vida Picante** · vidapicante.com | Spagna | semi, salse | — | **sito 503** | "gratis 24–48 h" (snippet) | — | — | — | [F66] |
| 19 | **Chilibaron** · chilibaron.ch | Hirzel (CH), dal 2010 | semi, piante, salse, fresco stagionale, secco | **>300 semi, ~70 piante, >90 salse** | n.d. in home | CH; UE n.d. | sì, stagionale locale | WooCommerce | **Google 5/5 su 77** ; IG @chilibaron.ch | [F67] |
| 20 | **Sämereien.ch** | Svizzera | semi | **418 articoli** chili/paprika | CHF 2,75–6,90 | gratis >100 CHF | no | proprietaria | — | [F68] |
| 21 | **Tschida Tschili** · tschidatschili.at | Illmitz (AT) | salse 100 g, piante (>50 var.), pomodori | >50 | salse **7,50–9,50 €** | "spedizione veloce in tutta Europa" | no | Shopify | premi internazionali; FB/IG/TikTok | [F69] |
| 22 | **Lubera** · lubera.com/at | Austria/CH | semi (10 var.) e piante | 10 | **4,09 € / 15–20 semi** bio; Habanero 6,25 € | "gratis per tutti gli ordini" | no | proprietaria | — | [F70] |
| 23 | **Hot-Sauce.de** | DE | **dominio in vendita a 1.399 €** (nessun negozio attivo) | — | — | — | — | — | — | [F71] |

**Chi spedisce fresco e come** (sintesi): Westlandpeppers (tutto l'anno, 25 paesi UE, 27,65 € verso l'Italia, scatola rinforzata, reclamo entro 1 giorno) · South Devon Chilli Farm (solo UK, stessa mattina, lug–nov) · DiavoloPiccante (Italia, solo il lunedì, 5,99 €, ago–nov) · Favella (Italia, shelf-life 10 gg) · Val d'Esaro (Italia, spedisce lun–mer) · Le Fresie (Italia + Europa 72/96 h, vaschetta 125 g) · Alba (vaschette 250 g, esaurite) · Chili Food e Chilibaron (fresco stagionale, dettagli n.d.) · La Sauce Piquante (FR, 48 h, >20 varietà, non verificato). **Nessuno dichiara una garanzia "arriva fresco o rimborsato".**

---

## C. Marketplace

**Limite forte**: Amazon.it (503/403), Etsy (403) ed eBay (403) hanno rifiutato tutte le letture dirette; DuckDuckGo ha risposto con CAPTCHA e Bing con risultati fuori tema. Quello che segue viene dai soli snippet della prima ricerca [F72] e va completato a mano (vedi Buchi).

### Amazon.it — "peperoncino calabrese" / "polvere peperoncino" (snippet, 02/10/2026)
| Prodotto (ASIN) | Marca | Formato | Recensioni / voto | Prime | Prezzo |
|---|---|---|---|---|---|
| Peperoncino Rosso Dolce Calabrese macinato (B09S6T513S) | Valsapori (da pagina prodotto) | 100 g | **4,3/5 su 1.048** · n. 18 cat. Peperoncino | n.d. | n.d. |
| Peperoncino Calabrese polvere dolce (B07WHQS5BP) | il Gallo al Grill | 100 g | 4,3/5 su 50 · non disponibile | n.d. | n.d. |
| Peperoncino Calabrese polvere piccante (B07WFLQSBT) | il Gallo al Grill | 100 g | 3,8/5 su 71 · non disponibile | n.d. | n.d. |
| Calabrian Chilli Powder 100% puro dolce (B0813W4MTJ) | TuttoCalabria | 500 g | 4,7/5 su 22 | n.d. | n.d. |
| Polvere piccante 500 g (B0813WTBCJ) · dolce 1 kg (B0813LBMMW) | TuttoCalabria | 500 g / 1 kg | n.d. | n.d. | n.d. |
| Peperoncino Piccante Calabrese in Polvere (B0917RVNYH) | n.d. | n.d. | n.d. | n.d. | n.d. |

Lettura: su Amazon il "peperoncino calabrese" è dominato da **polvere/tritato in formati 100 g–1 kg a prezzo basso**, da marchi industriali o rivenditori (Valsapori, TuttoCalabria, il Gallo al Grill); nessun risultato di varietà singola o di fresco. "Salsa piccante" e "semi peperoncino" su Amazon: **non rilevati** (ricerca bloccata). Assopepper e "Semi Strani" (Carlo Martini) vendono semi su Amazon [F6][F13].

### Etsy (snippet [F73], 02/10/2026)
Mercato "semi di peperoncino" presente su etsy.com/it; esempi: "Cal Wonder Pepper Organic Heirloom" 3,00 €; "9 hottest chiles in the world" 90 semi 12,95 €. Numero venditori e piantine: **n.d.** (pagina 403).

### eBay.it (snippet [F73])
Inserzioni "Bustina semi peperoncino ornamentale" (116476806029) e "Semi di peperoncino" (185552090874): prezzi n.d. (pagine 403). ZR Giardinaggio e Peragashop vendono bustine a ~4,90 € e ~3–3,85 € sui propri siti [F73].

---

## D. Chi ha davvero "350 varietà" da raccontare?

| Soggetto | Varietà dichiarate (DATO) | Vende? | Contenuti enciclopedici | Fonte |
|---|---|---|---|---|
| **Pepperfriends** (associazione, VR) | **480 nel database, 277 con semi disponibili** | semi solo ai soci | sì: scheda per varietà con SHU, colore, specie, foto; PDF scaricabile | [F45][F46][F47] |
| **Sämereien.ch** (CH) | 418 articoli chili/paprika | sì, semi | filtri per piccantezza, non schede narrative | [F68] |
| **La Sauce Piquante** (FR) | 348 varietà di semi | sì | n.d. (sito non apribile) | [F59][F60] |
| **Chilibaron** (CH) | >300 semi, 70 piante, 90 salse | sì | n.d. | [F67] |
| **Pepperseeds.eu** (Benelux) | ~300 | sì | filtri per piccantezza | [F61] |
| **Pepperworld Hot Shop** (DE) | >900 articoli (non varietà) | sì | rivista pepperworld.com con articoli per varietà (non un database numerato) | [F30][F48] |
| **DiavoloPiccante** (IT) | 172 semi / 166 secchi / 169 polveri | sì | schede con SHU per prodotto | [F7][F8][F9] |
| **Magic Garden Seeds** (DE, sito IT) | 109 | sì | — | [F62] |
| **MikelSimon** (ES) | >100 | sì | — | [F65] |
| **Vendita Peperoncini Online** (IT) | >100 piante | sì | — | [F15] |
| **Accademia Italiana del Peperoncino** (Diamante) | "Atlante delle varietà" (numero n.d.) | semi ai soci | sì, atlante fotografico | [F44] |
| **Peperita** | 18 | sì | numerazione 1–17 della piccantezza | [F1] |

**Chi si posiziona su Google con schede varietà / Scoville (Italia)**: i siti editoriali **peperonciniperhobby.it** (Matteo Cereda — schede per le 5 specie di Capsicum, pagina Scala Scoville, non vende) [F74] e **mondodelpeperoncino.it** (blog + "Database Varietà" + "Scala Scoville Completa 2025", collegato allo shop Cascina Beneficio) [F75]; in Germania **chilipflanzen.com** (guide di coltivazione + shop semi/piante) [F76] e la rivista **pepperworld.com** [F48]. Il database Pepperfriends è il più grande ma è in ASP anni 2000, senza e-commerce. **Nessun negozio italiano presidia la coppia "scheda varietà + prodotto acquistabile" su centinaia di varietà**: DiavoloPiccante ci va vicino sui numeri ma con schede brevi.

Lettura per Kalab: 350 varietà *coltivate* sarebbero il numero più alto dichiarato da un'azienda agricola in Italia (DiavoloPiccante 172) e sopra la maggior parte dei negozi europei di semi (300–418, che però sono rivenditori, non coltivatori). Il valore sta nel raccontarle una per una: oggi lo fa solo un'associazione (Pepperfriends) con un sito vecchio.

---

## E. Dove c'è spazio

1. **Fresco spedito in tutta Europa con garanzia**: in Italia nessuno spedisce fresco fuori dai confini (Le Fresie promette "Europa 72/96 h" ma solo vaschette 125 g; DiavoloPiccante solo il lunedì in Italia; Favella shelf-life 10 gg). L'unico europeo è Westlandpeppers, a 27,65 € di spedizione verso l'Italia e senza reso. Spazio per "raccolto oggi, consegnato in 48 h, garanzia freschezza" con imballo dedicato, almeno su Italia + DE/AT/FR/BE/NL.
2. **Varietà singole fresche**: i calabresi vendono "peperoncino calabrese" generico al kg (3,85–13,60 €/kg); le varietà esotiche fresche in confezioni da 250 g le vende solo Alba (esaurite) e Mr. Pepper (box mix). A 18–24 €/kg le varietà nominate valgono 4–5 volte il generico.
3. **Sito multilingua**: i negozi italiani sono solo in italiano (Favella e Fattoria Biò hanno l'inglese via Shopify); Chili Food è in 6 lingue, MikelSimon in 28. Un sito IT/EN/DE/FR da Scalea sarebbe unico fra i produttori italiani.
4. **Abbonamento**: non esiste in Italia; in UE solo Chilli No. 5 (salse, 12 €/mese, UK). Un "box del mese" con varietà diverse (fresco in stagione, secco/polvere d'inverno) non ha concorrenti.
5. **Le gare**: il Campionato italiano mangiatori di peperoncino (porzioni da 50 g crude, pane e olio) si tiene al Peperoncino Festival di Diamante (9–13 settembre 2026, 34ª edizione, Accademia Italiana del Peperoncino) [F44][F77]: nessun negozio online lo usa come storytelling o come prodotto (es. "il kit della gara", classifica, allenamento). Kalab è a 20 km.
6. **Enciclopedia + negozio**: le ricerche "varietà/Scoville" le vincono blog senza prodotto; chi mette 350 schede con foto, SHU, specie, ricetta e bottone "compra fresco/secco/semi" prende quel traffico.
7. **Semi rari a prezzo medio**: in Italia i semi rari costano 4,90–5,90 € (Semi Rari), 3,99 € (Botanis), 0,99–5,90 € (DiavoloPiccante); in UE 2,75–4,95 €. Con 350 varietà autoprodotte Kalab può stare a 2,50–3,50 € con margine e battere i rivenditori sulla provenienza ("semi dal campo, non importati").
8. **Piantine**: mercato attivo (2,70–5 €), ma stagionale (mar–giu) e logisticamente delicato; i vivai del Nord spediscono gratis sopra 69 €. Spazio solo se abbinato alle varietà rare.
9. **Premium bio**: Peperita presidia il "bio toscano" con polveri da 12 g a 400–950 €/kg: la Calabria non ha un equivalente premium con varietà nominate (Fattoria Biò e Nero di Calabria vendono polvere generica 45–100 g a 3,50–6 €).
10. **Recensioni**: tutti i concorrenti italiani hanno poche recensioni esterne (Peperita 7 su Trustpilot, Westland 12); Chili Food ne ha 1.322 e Chilibaron 77 su Google. Un sistema recensioni da subito è un vantaggio a basso costo.

---

## Prezzi di mercato per categoria (min / tipico / max — DATO salvo indicazione)

| Categoria | Min | Tipico | Max | Esempi e link |
|---|---|---|---|---|
| **Fresco al kg** (generico calabrese) | 3,85 €/kg Sibarizia (5 € / 1,3 kg) [F29] | 8,90–13,60 €/kg Conforti [F36] / Val d'Esaro [F37] | 20 €/kg Favella (2 € / 100 g) [F27]; 36 €/kg Le Fresie (4,50 € / 125 g) [F38] | Westland NL cayenne da 4,06 € (peso n.d.) [F49] |
| **Fresco varietà nominate** | 12 €/kg DiavoloPiccante Habanero 3 € a confezione (peso n.d., STIMA) [F8] | 18–22 €/kg Alba 4,50–5,50 € / 250 g [F39]; Mr. Pepper box 1,2 kg 25 € [F12] | 24 €/kg Alba Reaper/Naga 6 € / 250 g [F39]; UK Reaper 8,40 £ a confezione [F51] | — |
| **Secco intero ~50 g** | 2,70 € Val d'Esaro "Piccantello" (peso n.d.) [F37] | 3,40–4,90 € scaglie (Val d'Esaro 3,40; Peperita 60 g 4,90) [F37][F2] | DiavoloPiccante 0,99 €/frutto → STIMA 10–15 € per 50 g di superhot [F9] | — |
| **Polvere 50–100 g** | 3,50 € Fattoria Biò [F24] | 6,00 € / 45 g Nero di Calabria (133 €/kg) [F40] | 4,95–11,50 € / **12 g** Peperita (412–958 €/kg) [F2]; DiavoloPiccante 0,99 €/g = 99 € / 100 g [F11] | Amazon 100 g industriale: prezzo n.d., 1.048 recensioni [F72] |
| **Salsa/crema 100–200 g** | 4,50 € / 30 g Mr. Pepper crema Reaper [F12] | 6,00–6,95 € (Peperita 70 g 6,95; TuttoCalabria 6,00) [F2][F41]; AT 7,50–9,50 € / 100 g [F69] | 11 € / 90 g Nero di Calabria [F40]; 17,99 € crema Reaper Sfizi [F22] | UK salse 4,99–6,99 £ [F56] |
| **Sott'olio 200–300 g** | 4,49 € Sfizi di Calabria [F22] | 6,60–7,00 € (Favella 90 g 6,60; Fattoria Biò vasetto 7,00) [F27][F24] | 15 € / 180 g ripieni 'nduja Nero di Calabria [F40]; 17,99 € Sfizi [F22] | — |
| **Bustina semi (~10 semi)** | 0,99 € DiavoloPiccante [F7] | 2,75–3,99 € (Pepperseeds.eu, Magic Garden, Botanis 50 semi 3,99, MikelSimon 10 semi 1,75–3,25) [F61][F62][F21][F65] | 4,90–5,90 € Semi Rari [F20]; 5 £ superhot Sea Spring [F55]; 4,09 € Lubera bio [F70] | Etsy kit 90 semi 12,95 € [F73] |
| **Piantina** | 2,70 € La Casetta Bio [F19] | 3,00–4,50 € (Vendita Peperoncini Online 3–5; AgriPetGarden 3,95–4,50) [F15][F18] | 5 € [F15]; Giardino delle Meraviglie prezzi dietro login [F17] | — |
| **Box regalo / kit** | 13,90 € Green Cube Semi Rari [F20] | 25–40 € (Mr. Pepper box fresco 25; kit Reaper 30,30; Peperita borsellino 10 polveri 39,80) [F12][F2] | 131,05 € Peperita Cubo 16 polveri [F2] | UK gift set 13,99 £ [F56] |
| **Abbonamento** | — | **12 €/mese (144 €/anno), 2 bottiglie/mese, Chilli No. 5 UK** [F57] | — | Nessun abbonamento trovato in Italia |

---

## Fonti (tutte consultate il 02/10/2026)

- [F1] https://www.peperita.it/ — home: sede, categorie, 18 varietà, top prodotti, soglia 75 €
- [F2] https://www.peperita.it/it/prodotti/polveri/ — listino polveri 12 g
- [F3] https://www.peperita.it/it/spedizioni/ — tariffe Italia/UE/CH
- [F4] https://www.trustpilot.com/review/peperita.it — 4,1/5, 7 recensioni
- [F5] https://www.aziendaagricoladellamezzaluna.com/ (via ricerca) — Mezzaluna = agriturismo toscano
- [F6] https://www.mondodelpeperoncino.it/semi-peperoncino-online-dove-comprare/ — elenco venditori semi italiani
- [F7] https://diavolopiccante.it/6-semi-peperoncino — 172 varietà, prezzi 0,99–5,90 €
- [F8] https://diavolopiccante.it/7-peperoncino-fresco — fresco solo lunedì, 5,99 €
- [F9] https://diavolopiccante.it/8-piante-peperoncino (categoria = secchi) — 166 secchi a 0,99 €/frutto
- [F10] https://royalchili.com/fr/ — gemello francese
- [F11] https://diavolopiccante.it/9-piante-peperoncino (categoria = polveri) — 169 polveri a 0,99 €/g
- [F12] https://www.mr-pepper.it/ — Ardea, PrestaShop, gratis >49 €, box fresco 1,2 kg 25 €
- [F13] https://www.assopepper.com/ — 403 (dati da snippet ricerca)
- [F14] https://www.assopepper.com/semi-e-piante/semi-di-peperoncino/ — 403
- [F15] https://venditapeperoncinionline.it/ — >100 varietà piante, 3–5 €
- [F16] https://www.pepperitalia.eu/ — San Cesareo, Jimdo
- [F17] https://www.ilgiardinodellemeraviglie.it/it/piante-di-peperoncini-piccanti-varieta.html — 55 varietà, prezzi dietro login
- [F18] https://www.agripetgarden.it/piante-acquario-laghetto/piante-peperoncino-piccante.html — 23 varietà, 3,95–4,50 €, gratis >69 €
- [F19] https://www.shop.lacasettabio.it/it/27-piantine-ortaggi- — 2,70–3,20 €
- [F20] https://www.semirari.it/17-semi-peperoncini — Milano, 18 varietà, 4,90–5,90 €
- [F21] https://botanis.it/en/collections/semi-di-piante-di-peperoncino — 31 prodotti, 3,99 € / 50 semi, Shopify
- [F22] https://www.sfizidicalabria.com/peperoncino-in-olio.html — S. Maria del Cedro, 4,49–17,99 €
- [F23] https://www.sfizidicalabria.com/spedizioni.html — 5,90 € Italia, estero DE/AT 18,90 €, ES 19,90 €, FR 25,90 €
- [F24] https://shop.fattoriabio.it/en/collections/peperoncino-calabrese — prezzi polvere/scaglie/sott'olio, Shopify
- [F25] https://shop.fattoriabio.it/ — gratis >69 €
- [F26] https://shop.fattoriabio.it/pages/costi-di-spedizione — tariffe per peso
- [F27] https://favella.it/en/products/fresh-hot-chili-pepper — 2 €/100 g, shelf-life 10 gg, gratis >75 €
- [F28] https://favella.it/ — sede, 1932, social
- [F29] https://www.sibarizia.it/product/peperoncino-calabrese-fresco/ — 5 € / 1,3 kg, gratis >99,90 €
- [F30] https://pepperworld.com/25-jahre-pepperworld-hot-shop-von-der-idee-zur-institution/ (via ricerca) — dal 2001, >900 articoli
- [F31] https://www.pepperworldhotshop.com/en/ e /de/ — 403
- [F32] https://www.chili-food.de/ — 4,9/5 su 1.322, DE 5,90 € gratis >75 €, 6 lingue
- [F33] https://shop.westlandpeppers.com/en/ (via ricerca) — 25 paesi UE, serre NL
- [F34] https://shop.westlandpeppers.com/en/veel-gestelde-vragen/?lang=en — IT 27,65 €, DE 14,85 €, reclami 1 giorno
- [F35] https://www.trustpilot.com/review/shop.westlandpeppers.com — 4,2/5 su 12
- [F36] https://www.agricolaconforti.it/prodotto/peperoncino-piccante-fresco/ — 8,90 €/kg, gratis >39,90 €
- [F37] https://www.valdesaro.it/piccanti-di-calabria-e-specialit%C3%A0-tipiche/46-peperoncino-piccante-fresco.html — 13,60 €/kg, spedisce lun–mer
- [F38] https://www.lefresieconserve.it/spezie-piccanti/1209-peperoncino-calabrese-fresco.html — 4,50 € / 125 g, 9,90 € sped., Europa 72/96 h
- [F39] https://www.albapeperoncinoshoponline.it/peperoncino-fresco — vaschette 250 g 4,50–6 €
- [F40] https://shop.nerodicalabria.com/Peperoncino_piccante_in_polvere — 6 € / 45 g
- [F41] https://www.tuttocalabria.com/ — gratis Italia >70 €, Europa >120 €
- [F42] https://www.amazon.it/Peperoncino-Calabrese-polvere-puro-dolce/dp/B0813W4MTJ (snippet ricerca) — 4,7/5 su 22
- [F43] https://www.deliziedicalabria.it/ — shop in costruzione
- [F44] https://www.peperoncino.org/ — Accademia, Diamante, shop semi/libri
- [F45] https://www.pepperfriends.org/dbpf/lista3.asp — 277 varietà con semi
- [F46] https://www.pepperfriends.org/dbpf/lista2.asp — 480 varietà nel database
- [F47] http://www.pepperfriends.com/forum/forum/88-associazione-pepperfriends/ — sede Caldiero (VR)
- [F48] https://pepperworld.com/ — rivista, link shop
- [F49] https://shop.westlandpeppers.com/en/spaanse-peper-cayenne/ — cayenne da 4,06 €, Jalapeño 2,62 €, Rawit 7,63 €
- [F50] https://shop.westlandpeppers.com/en/product/pepermix/ — mix 75 g 2,39 €, WooCommerce
- [F51] https://southdevonchillifarm.co.uk/online-shop/fresh-chillies — prezzi fresco, Shopify
- [F52] https://southdevonchillifarm.co.uk/policies/shipping-policy — Europa sospesa
- [F53] https://southdevonchillifarm.co.uk/index.php (via ricerca) — gratis >60 £ con codice
- [F54] https://www.seaspringseeds.co.uk/ — no UE
- [F55] https://www.seaspringseeds.co.uk/product-category/seeds/chilli-seeds/ — 2–5 £
- [F56] https://www.hot-headz.com/ — Stroud, 1–13,99 £
- [F57] https://chilli-no5.com/it/acquistare-prodotti/abbonamento-salsa-piccante/abbonamento-mensile-salse-piccanti/ — 144 €/anno
- [F58] https://www.lecomptoirdupiment.com/ (via ricerca) — Espelette
- [F59] https://www.sauce-piquante.fr/en/39-chili-seeds (snippet) — 348 varietà
- [F60] https://www.sauce-piquante.fr/en/56-fresh-chili-peppers — 406
- [F61] https://pepperseeds.eu/ — ~300 varietà, 2,75–4,95 €
- [F62] https://www.magicgardenseeds.it/Peperoncini — 109 varietà, gratis >50 €
- [F63] https://www.semillas.de/ — 3,90 €, UE gratis >40 €
- [F64] https://www.semillas.de/collections/all — 22 chili
- [F65] https://www.mikelsimon.com/?id_lang=14 — Oliva, 1,75–3,25 € / 10 semi, gratis >30 €
- [F66] https://vidapicante.com/ — 503
- [F67] https://chilibaron.ch/ — >300 semi, 70 piante, 90 salse, Google 5/5 su 77
- [F68] https://www.saemereien.ch/chilisamen-kaufen-paprika-saatgut-bestellen — 418 articoli
- [F69] https://www.tschidatschili.at/ — salse 7,50–9,50 €, Shopify
- [F70] https://www.lubera.com/at/shop/chili-samen_kat-635.html — 4,09 € / 15–20 semi
- [F71] https://www.hot-sauce.de/ — dominio in vendita
- [F72] ricerca web "Amazon.it peperoncino calabrese polvere" (snippet): B09S6T513S 4,3/5 su 1.048; il Gallo al Grill; TuttoCalabria
- [F73] ricerca web "Etsy semi di peperoncino" (snippet): Etsy 3,00 € e 12,95 €/90 semi; eBay 116476806029 e 185552090874; ZR Giardinaggio ~4,90 €
- [F74] https://www.peperonciniperhobby.it/ — editoriale, Matteo Cereda
- [F75] https://www.mondodelpeperoncino.it/ — blog + database varietà + Scoville
- [F76] https://www.chilipflanzen.com/ — guide DE + shop
- [F77] https://www.cosenzachannel.it/societa/peperoncino-festival-2026-diamante-date-eventi-qjfu5r2x — festival 9–13/09/2026, gara 50 g
- [F78] https://www.peperonciniperhobby.it/altri-siti-sul-peperoncino/ — elenco siti internazionali (Reimer Seeds 3.900 articoli, Pepper Joe's, Nicky's Seeds…)

---

## Buchi e dubbi

1. **Marketplace quasi al buio**: Amazon.it, Etsy ed eBay hanno bloccato la lettura automatica; i dati sono da snippet (una sola scheda con 1.048 recensioni). Serve una mezz'ora a mano con un browser vero per: primi 10 risultati di "peperoncino calabrese", "polvere peperoncino", "salsa piccante", "semi peperoncino"; prezzi; Prime; numero venditori Etsy di semi e piantine; eBay semi.
2. **Pepperworld Hot Shop** (il n. 1 europeo) risponde 403: mancano prezzi, spedizione UE, Trusted Shops. **Chili-Shop24** e **Chilibrothers** irraggiungibili (DNS/connessione); **Chilli Pepper Pete** con certificato scaduto; **La Sauce Piquante** 406; **Vida Picante** 503; **Assopepper** 403.
3. **Follower Instagram**: nessun dato — Instagram non è leggibile da fetch e i motori di ricerca si sono chiusi (budget WebSearch esaurito a 200 chiamate; DuckDuckGo CAPTCHA; Bing fuori tema). Da raccogliere a mano per: Peperita, DiavoloPiccante, Mr. Pepper, Favella, TuttoCalabria, Pepperworld, Chili Food, Westlandpeppers, Chilibaron.
4. **Nomi del brief non verificati**: "Peperoncino.it", "Il Re del Peperoncino", "La Bottega del Peperoncino", "Capsicum Diamante", "Fuoco Verde", "Pepe Rosso", "Peperoncino di Diamante / Semi di Peperoncino": non sono emersi nelle ricerche fatte; potrebbero esistere con altro dominio o essere solo negozi fisici.
5. **Aziende di Diamante e della Riviera dei Cedri**: trovata solo Sfizi di Calabria (S. Maria del Cedro). Una ricerca mirata (anche su Google Maps) sulle aziende agricole di Diamante, Belvedere, Scalea con shop proprio è da fare.
6. **Peso delle confezioni fresche** di DiavoloPiccante e South Devon non indicato: le conversioni a €/kg per quelle righe sono STIME.
7. **Pepperfriends**: costo tessera e modalità di cessione semi non trovati (pagina reindirizza a forum/privacy).
8. **Chili Food**: catalogo e pagina spedizioni hanno rifiutato la connessione dopo la home; manca il prezzo verso l'Italia.
9. **Recensioni Google** dei concorrenti italiani: non raccolte (richiedono Maps).
10. **Prezzi Amazon** per i prodotti citati: non letti (pagina prodotto resa solo in JavaScript).
