# Anàlisis de l'audiència de Twitch
### Febrer 2023
El propòsit d’aquest anàlisis és analitzar i extraure conclusions de dades objectives tretes de l’API de Twitch, per examinar el comportament dels seus usuaris, des de l’streamer fins a l’audiència, donant resposta a cinc preguntes.

En aquest moment, redactant aquest article, 1.519.070 persones es troben consumint continguts de la plataforma repartits en els 69.949 canals que estan emetent en directe en aquest instant, segons indica twitchtracker.com. Així doncs, serà interessant analitzar com es repeteix aquesta audiència en un període de temps concret, per entendre com funciona a llarg plaç.

#### Quina ha estat l’evolució d’espectadors (captura a captura) durant el període?

En l’interval de temps del mes de febrer, podem començar a identificar comportaments. Els espectadors o viewers, són xifres que permeten identificar les tendències, com és el cas d’aquesta anàlisi. Si observem el gràfic 1, veiem que la línia és creixent, per tant, hi ha hagut un augment d’espectadors que comença el dia 1 amb 25.377.510 viewers i culmina el dia 28 amb un total de 46.056.029. Però, aquest augment, no ha estat exponencial sinó que distingim fins a 5 pics d’audiència, sent el més notable a final de mes, el 26 amb 39.082.398 espectadors i el 28 amb 46.056.029, que és a causa del retorn a la plataforma d’un famós streamer, que deixa titulars com; !Auronplay vuelve a Twitch! Regreso para los Squid Craft 2. Per altre costat, el dia 26 es va celebrar, amb Ibai com a amfitrió, el gran premi de Twitch, una carrera de karts entre 22 streamers.

<img width="898" alt="image" src="https://user-images.githubusercontent.com/125387521/232328484-203aff04-feea-45bc-9258-621d50733562.png">
Gràfic 1

A partir d’aquestes mateixes dades, i responent a la mateixa pregunta, podem comprovar el comportament cíclic de la plataforma a través de les hores. Posant com a exemple, el dia 9, comença la jornada al cim del pic, a la 1h amb 1.937.158 espectadors, que augmenta fins a 1.982.260 i cau en picat a les 4h fins a les 11h que assoleix el seu mínim amb 219.879 viewers. Tot seguit, de 15h a 20h creix exponencialment i de 20h a 3h de la matinada, es repeteix el pic i l’endemà es renova el cicle. L’explicació més fàcil a aquest fet, és la trobada entre dues audiències hispanoparlants i en conseqüència caldrà confirmar en següents preguntes, l’augment també de canals emetent en directe.

<img width="901" alt="image" src="https://user-images.githubusercontent.com/125387521/232328541-6793554e-b9fc-44a9-82fe-7f1b2cb8be2c.png">    
Gràfic 2

#### Quines són les categories més vistes i en quines hores de directe s’han realitzat?

És necessari saber com aquesta audiència es reparteix en les diferents categories de jocs, i com es comporten aquestes. Aquelles categories amb més volum de viewers, en primer lloc, Just Chating, 186.414.128 espectadors, val a dir que aquesta categoria representa part de l’inici i final de la majoria d’emissions, ja que traduint el nom és “només parlar”. En segon lloc, Minecraft, amb 55.968.573 viewers i League of Legends amb 49.425.785. En canvi, si focalitzem en la quantitat acumulada d’hores de directe, les categories passen a ser, Fortnite amb un total de 2.147.446 hores, seguit del Valorant amb 2.128.695 hores. Si valorem les dues mètriques conjuntament, en destaca com anteriorment just Chating. Altres categories que també destaquen; Hogwarts Legacy, Call of Duty i el FIFA 23.

<img width="383" alt="image" src="https://user-images.githubusercontent.com/125387521/232328594-27225996-065c-4c82-b32e-5da10da520c9.png"> <img width="149" alt="image" src="https://user-images.githubusercontent.com/125387521/232328634-423ebefb-69fb-4ace-9e69-8f74f943b52e.png">
  
Gràfic 3


#### Com han evolucionat (captura a captura) aquestes categories al llarg del mes?

Sabent que aquestes categories són les més destacables de la plataforma, cal analitzar el seu comportament durant el període cíclic d’un mes. Observem que la categoria més estable a simple vista, és Just Chating, que ens confirma la suposició de comportament en l’anterior pregunta. Després en destaca l’etiqueta de Sports, dins d’aquí hi podem trobar tota mena de continguts relacionats amb l’execució de l’esport. M’arriscaré a dir, que sembla a ser degut a l’emissió en directe de la Kings League, fenomen que analitzaré posteriorment, perquè trobem 5 pics, el primer, del dia 5 de febrer amb 8.162.182 espectadors, i l’últim, el 26 amb més de 7 milions. En tercer lloc, el dia 7 de febrer tenim un pic de més de 5.000.000 espectadors, a causa de l’estrena del joc Hogwarts Legacy, que sorprèn en la seva evolució, perquè tant en streams com en espectadors, cau bruscament. I, en últim lloc, a grans trets també en destaca el dia 27 un clímax de 7.667.708 espectadors en la categoria Special Events, que es manté sota mínim durant la resta de més, recorrent a anteriors preguntes, podria encaixar-hi l’esdeveniment d’Ibai Llanos.

<img width="487" alt="image" src="https://user-images.githubusercontent.com/125387521/232328676-f16b2db5-96ba-4e42-844c-34dab555eb97.png">   <img width="102" alt="image" src="https://user-images.githubusercontent.com/125387521/232328701-7d0bf9b5-fe2c-4d6c-bfd0-8c42db43c787.png">          
Gràfic 4


#### Quina és la distribució dels streamers si els classifiquem per volums d’audiència i hores realitzades?

Ara que saben quines són les categories amb més impacte, fa falta veure quins són els streamers que hi contribueixen. Fixant-nos en el gràfic 5, el primer que en destaca és la Kings League, superior en espectadors a la resta, amb un total de 43.710.847 al llarg del mes. Aquest fenomen es tracta de trobaments de futbol 7 amb una duració curta de 40 minuts, que combina el joc convencional amb noves regles per oferir espectacle. Hi ha gent que fins i tot afirma que la Kings League és una nova lliga de futbol adaptada a internet “més tiktokera” com deixen anar alguns titulars. El que està clar és que funciona en línia, amb 48 hores de directe repartides en 28 dies i un estadi, l’Spotify Camp Nou, amb més de 92.500 espectadors físicament presents, que ha fet aixecar totes les alarmes.

Per sota també trobem el famós streamer, Ibai Llanos, que ha acumulat 75 hores de directe i més de 29 milions de viewers. Seguit per IlloJuan, que ha superat les 123 hores de vídeo en temps real i més de 24 milions d’espectadors.

El que em crida l’atenció en aquest gràfic, però, és que en general, els streamers amb menys espectadors, les hores de directe són més altes, que els grans streamers. Sent així el cas d'OscarFilms, que arriba fins a les 613 hores al mes amb 711.667 viewers, comparat amb El Spreen, que ha fet poc més de 56 hores, aconsegueix una xifra desorbitada de més de 19 milions. Per tant, és el cas de molts streamers que han de fer moltes més hores de directe per a aconseguir una retribució econòmica.

<img width="419" alt="image" src="https://user-images.githubusercontent.com/125387521/232328794-2e4feea5-e378-4a7b-92ba-ca7b1ed329b0.png"><img width="103" alt="image" src="https://user-images.githubusercontent.com/125387521/232328995-7feefcec-2767-4c36-8150-c6d53a59c24c.png">
Gràfic 5

<img width="899" alt="image" src="https://user-images.githubusercontent.com/125387521/232328923-7dca805b-e5f1-4417-88a3-4166cad4d1b3.png">
Gràfic 6


#### Quina ha estat l’evolució (captura a captura) de la desviació estàndard en el volum d’espectadors? En quins moments les audiències es troben més polaritzades i en quins moments la distribució es més uniforme?

En últim lloc, és interessant saber i analitzar la desviació d’aquesta audiència, d’aquesta manera sabem quins moments al llarg del mes tenen pics d’audiència molt allunyats dels altres. El gràfic 7 descriu aquesta desviació que com podem veure és cíclica, tret de 5 pics, un d’ells molt elevat. Els tres primers compten amb una desviació de 3.000 – 4.000, mentre que els dos últims, un s’eleva fins al 8.333, sent aquest el més allunyat, i l’altre decau fins a 6.768.

<img width="877" alt="image" src="https://user-images.githubusercontent.com/125387521/232329114-8b920ee1-cb8b-4324-9ee2-e4ada0d2c8e4.png">          
Gràfic 7

<img width="708" alt="image" src="https://user-images.githubusercontent.com/125387521/232329620-29cdd415-ab0d-4272-bbc7-faee72ff9892.png">
Gràfic 8

Com a conclusió d’aquest anàlisis, n’extrec que l’audiència de Twitch segueix sempre una mateixa rutina, de la mateixa manera que els seus creadors de continguts. Streamers com Ibai Llanos o Illo Juan, segueixen un horari on agrupen a la majoria d’aquesta audiència que abans i després de les seves emissions, es reparteixen entre els altres streamers sense tant renom. Per altre costat, no per fer més directes gèneres més, ja que s’ha vist que els grans creadors són els que menys directes realitzen, pel fet que ja tenen un nom a la plataforma i una audiència fidelitzada.
