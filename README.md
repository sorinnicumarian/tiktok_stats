# TikTok Bot Detection Project

## Misiune

**Vreau, împreună, să ajutăm la găsirea botilor care au interferat alegerile prezidențiale, prin manipulare mediatică și socială pe TikTok.**

Încerc să ajut, fiindcă, din păcate, autoritățile sunt depășite. Există un dosar deschis la SIE (Serviciul de Informații Externe), care constată că au fost folosite zeci de mii de conturi false de pe TikTok, coordonate, posibili suspecti fiind China, Rusia, Iran, după cum spune Dragoș Pătraru în acest video: [Dragoș Pătraru - YouTube](https://www.youtube.com/live/Uqi7AvfkNvU?si=PvC1H54z1EX7mIoY&t=1079).

## Autor

Sunt un simplu programator, îngrijorat de soarta țării. Găsești mai multe informații despre mine pe [LinkedIn](https://www.linkedin.com/in/sorinnicumarian/).

**Email**: sorinmarian.it@gmail.com

## Proiect

Acest proiect este, deocamdată, un simplu fișier Python care face requesturi printr-o librărie neoficială TikTok, numită [TikAPI](https://tikapi.io/), pentru a strânge date despre anumite hashtaguri folosite de Călin Georgescu. Am inceput cu #echilibrusiverticalitate, conform [G4Media](https://www.g4media.ro/expert-forum-campania-echilibrusiverticalitate-de-pe-tiktok-a-fost-a-lui-calin-georgescu-cum-a-crescut-calin-georgescu-in-sondaje-studiu.html)

### Manual de Utilizare

1. Am folosit Python, VS Code, și un virtual environment. E nevoie de VS Code, Python3 și pip. Pași de instalare:
   1.1. `python3 get-pip.py`  
   1.2. `pip3 install TikTokApi pandas openpyxl playwright`  
   1.3. `python3 -m venv tiktok_env`  
   1.4. `source tiktok_env/bin/activate`                                    

2. **TikAPI Account**: Pentru a folosi acest proiect, trebuie să creezi un cont trial pe TikAPI, la care poți adăuga un card Revolut pentru a beneficia de 2000 de requesturi într-o lună. Cheia salveaz-o într-un fișier separat numit `config.json`, sub numele de `tikapi_key`.
   
3. **Fetching Video Data**: Scriptul actual adună informații despre video-uri și autori de pe TikTok, dar nu sunt încă foarte relevante pentru detectarea botilor. Cu ajutor, putem găsi o direcție mai bună.

4. **JSON Responses**: Deocamdată, scriptul caută câmpuri de bază cum ar fi vizualizările, comentariile și like-urile. Trebuie un filtru mai specific pentru a identifica conturile false.

## Contribuie

Cum poți ajuta?  
1. Găsirea unor câmpuri mai relevante pentru descoperirea botilor:  
   - Se pot căuta în debug în răspunsurile JSON de la TikAPI.  
   - Se pot căuta pe TikTok sau alte cazuri de interferență politică pentru câmpuri mai relevante, sau alte modalitati.  

2. Dacă dorești să ajuți, poți să mă contactezi pe email sau direct prin comentarii/Pull Requests pe GitHub.

## Concluzie

Sper ca, strângând aceste date și trimițându-le către o sursă media de încredere, să aducem mai multă obiectivitate în mass-media legat de acest fenomen de manipulare, să putem ajuta autoritățile să își facă meseria și să protejeze mai bine cetățenii, contribuind astfel la o democrație mai puternică. Este esențial ca fiecare persoană să poată vota conștient și informat, fără a fi manipulat de conturi false sau influențe externe.

## License

This project is open-source and available under the [MIT License](LICENSE).
