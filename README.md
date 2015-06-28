# HDO-transcript-generator POC

## Requirements

Docker https://www.docker.com/

## Usage

Clone this repo and build it.

    $ git clone https://github.com/ivarref/hdo-transcript-generator.git
    $ cd hdo-transcript-generator

    # Build it (this will take a while):
    # This will build a generator for Heikki Holmås.
    # (Change the Dockerfile to someone else as needed.)
    $ docker build --tag=ivarref/rnn .

    # After some time:
    $ docker run -ti ivarref/rnn /bin/bash
    (inside container)
    root@1234 $ ./find_lowest_checkpoint.py /opt/cv
    *** and the lowest checkpoint file is:
    /opt/cv/lm_lstm_epoch37.24_0.9575.t7
    root@1234 $ /root/torch/install/bin/th sample.lua /opt/cv/lm_lstm_epoch37.24_0.9575.t7 -gpuid -1 -primetext fattigdom -length 2500

    ... Profit?

## Sample Heikki Holmås about 'fattigdom'

    fattigdomspeker rundt nok den private næringslivet. Men jeg mener at man
    får få til en nedgang i arbeidsløshet. En av de tingene som vi har
    foreslått. nemlig at regjeringen står for ikke hvordan den forskjellene
    mellom rike og fattige i de våre land til en loppgjør å øke UNICEF eller i
    fellesskapet som lever enn den de som driver kulturarbeid som de i
    meldingen kommer at det er riktig å bruke disse perspektivene.  Et eksempel
    til hvilke viktigste igjen, er at Kristelig Folkeparti hadde vært redd for
    å være av Høyre i dag: «Mennesker øker menneskerettigheter, ville være god
    dømmes dokument og forplikter til Tord Lien - som landets barnehagedekning
    kommer til å elskere over grensene lite siste tid på Kristelig Folkeparti
    tre ganger et mye i enkelte medlemmer av klimaforliket, er å gi kommunene i
    fattigere land. En av de tingene vi er nødt til å la vednykkende. Jeg er
    ute og varger på de rammes listene på okkupart fra komtunne ansvar for å
    behandle hele år foe å få muligheten til å sørge for at politikerne når de
    foreslår fattigdom. Den kan se at et verdisyn og den forrige regjeringen
    trekker galskult i demokrati? Når vil statsråd Da oppføre et spørsmål er:
    «Vi i Norge har rerest økonomiske.  Så er jeg ikke glad for at jeg mener at
    alle de andre siden dårlige tiden som har vært mye viktigere er fra den
    gang.  Spørsmålet mitt er helt slik at Regjeringen betaler – det har ført
    til at hun stiller nettopp fordi norske regjeringspartier mener skal ikke
    legge fram noen pådriver er alle tiltaket for neste punkt for ytterligere
    befolkning, vil jeg si at regjeringen blir enklere for utdanning, men sist
    går vi klart full på om en helt presentert som tallet når en revisjon om
    kollektivtrafikk og mennesker som har rett til å løse disse tredelene.
    Siden jeg kjenner bostedsløse når det gjelder barn, for å bremse utsatte
    muslimske politiske innvandring, har om utenriksministeren og flertallet
    går inn for en flere utdanning, som nå har tatt et peker formuesskatt.
    Denne komiteen skal komme tilbake til det arbeidet pre penger i dette kjøp
    i andre land her i sted. Det å bruke land, i sårbart samfunn dersom vi ikke
    skal inkludere mennesker når det gjelder åpenhet. Det ikke er forskning som
    undergangen stremte, og det vi understreker å sørge for å støtte folk seg i
    familiegjenforening og de samme samfunnets rikeste. Og sett i dag.Nå gjør
    vi vårt imot.  Objeftingen for folk til statsbudsjettet. 

