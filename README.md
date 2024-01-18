# TiNKA-Egzaminas
# Vardu, vietoviu pavadinimu ir imoniu pavadinimu identifikavimo tekte sistemos koncepcija.

Sistemos koncepcijos GUI veikimui pasirinktas web interfeisas, kuris yra sudarytas python aplinkoje naudojant Flask Api.
Sistemos funkcionalumui naudojamas tik vienas web puslapis uzejus i kuri naudotojas gali ivesti savo teksto uzklausa ir paspausti mygtuka rezultato gavimui.

Ivedus teksta ir paspaudzius mygtuka "Isvesti" puslapis siuncia uzklausa serveriui kur tekstas paduodamas i Named Entity Recognition modeli "
bert-base-NER". Modelio veikimo rezultatas apdorojamas paprastu scriptu sudarytu is for ciklo su if salygomis kur gauti rezultatai skirstomi i vardus, vietoves ir imones dictionary kintamajame. Modelio isejimo apdorojimo rezultatas grazinamas naudotojui i puslapi kur atvaizduojamas tryse eilutese: Vardai, vietoves ir imones.  

Modelis "bert-base-NER" ikeliamas i python aplinka naudojant bibleoteka "transformers".
