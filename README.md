# Programmeerproject
Minor programmeren UvA 
Lonneke Lammers
10371672

Proposal: Datavisualisatie Baanperspectieven 

Mijn voorstel is om tijdens het programmeerproject een datavisualisatie te maken van soorten banen en de werkgelegenheidsperspectieven hiervan. Hierbij wil ik de verschillende banen op alfabetische volgorde van links naar rechts in een barchart weergeven, met een  interactive functie dat wanneer je klikt op een chart/banensector, er een tooltip tevoorschijn komt met meer informatie. 

(Een deel van) de volgende informatie wil ik zichtbaar maken in de visualisatie:
- employment in 2014
- employment change
- job openings 2014-2024
- 2014 median annual wage
- work experience in a related occupation
- typical on-the-job training
- typical entry-level education

De data ben ik van plan te scrapen vanaf: http://data.bls.gov/projections/occupationProj 
Dit is data afkomstig van een Amerikaanse Databank: U.S. Bureau of Labor Statistics. Omdat dit een zeer uitgebreide Databank is en ik op het cbs geen goed vergelijkbare Nederlandse versie kan vinden gebruik ik deze data.

Ik zal de data om moeten zetten in een goed leesbaar csv bestand, en dit vervolgens verwerken in javascript + d3 in html. 

![](doc/barchart-blocks.png)



