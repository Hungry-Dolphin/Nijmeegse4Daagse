# Nijmeegse vierdaagse ticket scraping bot
Dit script gebruikt multi-threading en proxies om proberen een ticket te krijgen voor de Nijmeegse vierdaagse.

Elke browser window zal net zo lang de pagina refreshen tot er een ticket beschikbaar is. Zodra deze is gevonden zullen alle andere browser windows sluiten. Je moet vervolgens zelf dan nog alle gegevens invullen in de openstaande browser window.

Dit is puur bedoeld om zelf een ticket te krijgen. Je kan de tickets niet doorverkopen dus het scalpen heeft 0 zin.

# Note
Ik weet niet of dit script werkt of niet, tot nu toe zijn er nog geen tickets gekomen welke beschikbaar waren. 

Zonder het gebruik van proxies heb je geen voordeel ten opzichte van gewoon handmatig de pagina refreshen.
Het krijgen van een ticket komt voornamelijk uit op geluk. Je moet net zodra er tickets zijn de pagina refreshen. 
Zonder het gebruik van proxies is het maar mogelijk om een keer per ~7 seconden te refreshen. In het algemeen zullen tickets zeker binnen een paar seconden weg zijn. Dus duimen dat jij de eerste bent die het ziet.

# Trivia over de werking van de website
- Je kan handmatig de pagina refreshen om opnieuw te zoeken naar tickets. Dit werkt, maar als je dit te vaak doet krijg je een rate limit
- Tot nu toe ben ik niet echt tegen anti-bot measures gelopen (de rate limit zal ook voor mensen zijn) ik vermoed dat ik niet de enige ben die dit bot. Zelfs met 7 browser sessies van verschillende proxies heb ik nog geen beschibare tickets gezien.