# TikTok Bot Detection Project

## Mission

**Vreau, împreună, să ajutăm la găsirea botilor care au ajutat la manipularea mediatică și socială prin conturi false pe TikTok.**

Încerc să ajut, fiindcă, din păcate, autoritățile sunt depășite. Există un dosar deschis la SIE (Serviciul de Informații Externe), care constată că au fost folosite zeci de mii de conturi false de pe TikTok, coordonate, posibil, de China, Rusia, Iran, după cum spune Dragoș Pătraru în acest video: [Dragoș Pătraru - YouTube](https://www.youtube.com/live/Uqi7AvfkNvU?si=PvC1H54z1EX7mIoY&t=1079).

## About the Author

Sunt un simplu programator, îngrijorat de soarta țării. Găsești mai multe informații despre mine pe [LinkedIn](https://www.linkedin.com/in/sorinnicumarian/).

**Email**: sorinmarian.it@gmail.com

## About the Project

Acest proiect este, deocamdată, un simplu fișier Python care face requesturi printr-o librărie neoficială TikTok, numită [TikAPI](https://tikapi.io/), pentru a strange date despre anumite hashtaguri folosite de Calin Georgescu.

### How to Use

1. **TikAPI Account**: Pentru a folosi acest proiect, trebuie să creezi un cont trial pe TikAPI, la care poți adăuga un card Revolut pentru a beneficia de 2000 de requesturi într-o lună. Cheia salvati-o intr-un fisier separat numit config.json, sub numele de tikapi_key
   
2. **Fetching Video Data**: Scriptul actual adună informații despre video-uri și autori de pe TikTok, dar nu sunt încă foarte relevante pentru detectarea botilor. Cu ajutorul comunității și al celor care contribuie, putem găsi o direcție mai bună în acest sens.

3. **JSON Responses**: Deocamdată, scriptul caută câmpuri de bază cum ar fi vizualizările, comentariile și like-urile. Este necesar să adăugăm un filtru mai detaliat pentru a identifica conturile false.

4. **Future Improvements**:
   - **#TODO**: Se poate căuta în răspunsurile JSON pentru câmpuri mai relevante care pot ajuta la descoperirea botilor.
   - **#TODO**: Se poate căuta pe TikTok sau alte cazuri de interferență politică pentru câmpuri mai relevante ce ar putea contribui la identificarea botilor.

## Contribute

Daca doriti sa ajutati puteti sa ma contactati pe email, sau direct prin comentarii/Pull Requests pe Github.

## Conclusion

Sper ca, strângând aceste date și trimițându-le către o sursă media de încredere, să putem ajuta autoritățile să își facă meseria și să protejeze mai bine cetățenii, contribuind astfel la o democrație mai puternică. Este esențial ca fiecare persoană să poată vota conștient și informat, fără a fi manipulat de conturi false sau influențe externe.

## License

This project is open-source and available under the [MIT License](LICENSE).
