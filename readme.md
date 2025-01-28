# Disclaimer
Bisher nur in Windows 10 mit Python-3.12 und in WSL auf Ubuntu getestet.
Feedback, ob das Skript auf anderen Plattformen funktioniert, ist willkommen.
Bei Linux muss der Pfad von "chromedriver.exe" zu "chromedriver" im Skript umbenannt werden - Oder man benennt chromedriver zu chromedriver.exe um. - Ich weiß, das könnte man easy beheben. Ich bin bisher nur zu faul gewesen.
Kompatibilitätsprobleme werden am wahrscheinlichsten im Zusammenhang mit der Python-Bibliothek "Selenium" auftreten.

# Vorschau
- ![image](https://pixeldrain.com/api/file/iTvN5jDS)
- [video preview](https://pixeldrain.com/api/file/i3CatESg) 


# Installation
## Windows
1. allgemeine Abhängigkeiten installieren 
    - Git: Über das PowerShell-Modul "WinGet" kann man als Windowsuser den Befehl ```winget install Git.Git``` benutzen um den Installationsvorgang für Git zu starten - Bei den neusten Windows 11 Releases ist Winget eingentlich vorinstalliert. Alternativ Git wie jedes andere Programm googlen und installieren -> "Windows git installation"
    - Python: Dafür empfehle ich die [offizielle Website](https://www.python.org/downloads/) zu besuchen den Installationsanweisungen zu folgen. Über Winget ist die Installation aber ziemlich sicher auch möglich.

3. Repo klonen
    - Mit dem Befehl ```git clone https://github.com/Winkelars/untisGimmeWeekReports {pfad}``` kopierst du das Projekt in das Verzeichnis, das du an der Stelle {pfad} auswählst.
    - wechsle mit ```cd {pfad}``` jetzt in das Verzeichnis

4. Python-Abhängigkeiten installieren
    - Wenn du planst Python öfter zu benutzen, und allgemein einfach best-practice folgen willst, solltest du nun eine virtuelle Umgebung aufsetzen - ich empfehle also ```python -m venv venv``` auszuführen und danach über ```./venv/Scripts/Activate.ps1``` die Umgebung zu betreten. Danach sollte "(venv)" in deinem PowerShell-Prompt zu sehen sein.
    - Über ```pip install -r requirements.txt``` installierst du zuletzt automatisch alle anderen Python-Bibliotheken, die das Skript zu laufen braucht.

5. Webdriver installieren
    - Man muss jetzt noch einen Webdriver installieren und in Selenium einbinden
    - Da ich hardcoded den Chromedriver angesprochen habe, müsst ihr entweder ebenfalls chromedriver.exe verwenden, oder den Code anpassen, was nicht all zu schwierig wäre. Geckodriver ist der Name des Webdrivers für Firefox.
    - Downloads für den Chrome-Webdriver, bzw. für "chromedriver" gibt es [hier](https://googlechromelabs.github.io/chrome-for-testing/).
    - legt "chromedriver.exe" in entpackter Form mit in das Repoverzeichnis neben "readme.md" und "fetchentries.py".

6. Webbrowser installieren
    - Chromedriver muss mit deiner Chromeversion kompatibel sein - meist heißt das, die wählst bei Schritt 5 die neuste chromedriver-Version und achtest darauf, dass dein Chrome Up To Date ist.
    - Bei anderem Webdriver installiert ihr den entsprechenden Webbrowser mit der benötigten Version

### Anmerkung
Teile der Installation werden in Zukunft hoffentlich automatisiert oder überflüssig gemacht. Wenn ich herausfinde wie man alles über ein kleines Dockerimage laufen lässt, muss man bald nur Docker installieren und das Image via ```docker run image``` ausführen
