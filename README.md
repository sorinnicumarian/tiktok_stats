# TikTok Bot Detection Project - EN

## Mission

**I want us to work together to help identify bots that interfered with the presidential elections through media and social manipulation on TikTok.**

I'm trying to help because, unfortunately, the authorities are overwhelmed. There is an open investigation at SIE (the Romanian Foreign Intelligence Service), which confirms that tens of thousands of fake TikTok accounts were used in a coordinated manner. The possible suspects are China, Russia, and Iran, as mentioned by Dragoș Pătraru in this video: [Dragoș Pătraru - YouTube](https://www.youtube.com/live/Uqi7AvfkNvU?si=PvC1H54z1EX7mIoY&t=1079).

## Author

I'm just a simple programmer, concerned about the fate of my country. You can find more about me on [LinkedIn](https://www.linkedin.com/in/sorinnicumarian/).

**Email**: sorinnicumarian@gmail.com

## Project

This project is currently just a simple Python script that makes requests through an unofficial TikTok library called [TikAPI](https://tikapi.io/), to gather data about specific hashtags used by Călin Georgescu. I started with the hashtag `#echilibrusiverticalitate`, as mentioned in this [G4Media article](https://www.g4media.ro/expert-forum-campania-echilibrusiverticalitate-de-pe-tiktok-a-fost-a-lui-calin-georgescu-cum-a-crescut-calin-georgescu-in-sondaje-studiu.html).

### Usage Instructions

1. The script uses Python, VS Code, and a virtual environment. You'll need Python 3, pip, and optionally VS Code. Setup steps:
   1.1. `python3 get-pip.py`  
   1.2. `pip3 install TikTokApi pandas openpyxl playwright`  
   1.3. `python3 -m venv tiktok_env`  
   1.4. `source tiktok_env/bin/activate`                                    

2. **TikAPI Account**: Create a free trial account at TikAPI. You can use a Revolut card to activate the account and get up to 2000 requests per month. Save your API key in a separate file named `config.json` with the field `tikapi_key`.

3. **Fetching Video Data**: The current script collects basic information about videos and authors on TikTok. These aren't very useful for bot detection yet, but with help, we can improve the direction.

4. **JSON Responses**: The script currently looks for basic fields like views, comments, and likes. More specific filters are needed to detect fake accounts.

## Contribute

How you can help:
1. Identify more relevant fields for bot detection:  
   - Explore the JSON responses from TikAPI in debug mode.  
   - Look for similar political interference cases or TikTok data leaks to inspire better filtering.

2. If you'd like to contribute, feel free to email me or open issues/pull requests on GitHub.

## Conclusion

Hopefully, by collecting and submitting this data to a trusted media source, we can increase transparency around this manipulation phenomenon, assist authorities in doing their job better, and contribute to a stronger democracy. Every citizen should be able to vote consciously and informed, without being influenced by fake accounts or foreign propaganda.

## License

This project is open-source and available under the [MIT License](LICENSE).


# TikTok Bot Detection Project - RO

## Misiune

**Vreau, împreună, să ajutăm la găsirea botilor care au interferat alegerile prezidențiale, prin manipulare mediatică și socială pe TikTok.**

Încerc să ajut, fiindcă, din păcate, autoritățile sunt depășite. Există un dosar deschis la SIE (Serviciul de Informații Externe), care constată că au fost folosite zeci de mii de conturi false de pe TikTok, coordonate, posibili suspecti fiind China, Rusia, Iran, după cum spune Dragoș Pătraru în acest video: [Dragoș Pătraru - YouTube](https://www.youtube.com/live/Uqi7AvfkNvU?si=PvC1H54z1EX7mIoY&t=1079).

## Autor

Sunt un simplu programator, îngrijorat de soarta țării. Găsești mai multe informații despre mine pe [LinkedIn](https://www.linkedin.com/in/sorinnicumarian/).

**Email**: sorinnicumarian@gmail.com

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
