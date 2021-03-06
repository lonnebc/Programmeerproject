#Design

##Framework mapping

Om een duidelijk beeld te krijgen van de user interface heb ik een vergelijkbare schets gemaakt. Hierbij zal uit de barchart de 'huidige' banenmarkt weergeven worden. Recht hiervan komt er een menu waar je kunt klikken op verschillende kenmerken. De barchart zal dan interactief zijn, dan zodra je klikt op iets uit het menu, de barchart zich hierop aanpast. Verder komt er onder de barchart een soort 'zoekbalk' waar je de sector in kan typen, en hier met de letters die je intypt er voorselectie wordt weergeven. Je kunt dan klikken op een cd sectoren, en hier zien welke soort banen er bij deze sector horen. 

Idee: tree map op basis van sector OF degree. (denk nu aan sector) 
Hierbij ook filtereren op:
- kansrijke beroepen (WEL STUDEREN)
- minder kansrijke beroepen (NIET STUDEREN)



![](doc/userinterface.png)

Zoekfunctie voorbeeld: http://www.brightpointinc.com/download/autocomplete-source-code/
Barchars: http://mbostock.github.io/d3/talk/20111116/bar-hierarchy.html

###Data

De data is afkomstig van een Amerikaanse Databank: U.S. Bureau of Labor Statistics. Hier kun je de data in een CSV formaat downloaden. Vervolgens zal het omgezet worden in verschillende JSON bestanden, zodat je een goed overzicht hebt van welke data in welke visualisatie gebruikt wordt. Verder zal er op D3-wijze in JavaScript geprogrammeerd worden, welke compatible is met een html bestand. 

###Doel

Middelbare scholieren vinden het vaak lastig om een geschikte studie te kiezen, met als gevolg veel studieswitchers. Dit kost de verse studenten danwel hun ouders niet alleen veel geld, maar is ook voor de overheid een grote uitgave. 

####Bronnen:

http://www.hbostart.nl/ik-weet-echt-niet-welke-studie-ik-moet-kiezen/ (studiekeuze lastig)
http://www.trajectum.hu.nl/node/11011 (kosten studieswitchers)
http://www.brightpointinc.com/download/radial-progress-source-code/
http://bl.ocks.org/zbjornson/2547496


#-------
- a list of classes and public methods (and their return types and/or arguments) that you’ve decided to implement
- advanced sketches of UIs that clearly explain which features are connected to which underlying classes
- a list of APIs and frameworks that you will be using to provide functionality in your app
- a list of data sources, and database tables and fields (and their types) that you’ve decided to implement

If your application has multiple independent programs working together (e.g. to clean your dataset) you need to provide a high-level overview of these components and then provide a lowel-level overview of the inner workings of each component.

