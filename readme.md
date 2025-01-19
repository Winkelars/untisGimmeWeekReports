# Disclaimer
Bisher nur in Windows 10 mit Python-3.12 getestet.
Feedback ob das Skript auf anderen Plattformen funktioniert, ist willkommen - Das sollte aber vor allem von Selenium abhängen.

# Installation
## Windows
1. allgemeine Abhängigkeiten installieren
    - Wenn du noch nie von Git gehört hast, musst du eventuell 1-2 Youtube-Videos zu dem Thema schauen.
    - Git kann ganz einfach über den Befehl: ```winget install Git.Git``` in PowerShell installiert werden, falls du winget hast.
    - Außerdem muss Python installiert werden. Dafür empfehle ich die neuste Version von der [offiziellen Website](https://www.python.org/downloads/) herunterzuladen und den Installationsanweisungen zu folgen.

2. Repo klonen
    - Mit dem Befehl ```git clone https://github.com/Winkelars/fetchStundenInfos {pfad}``` kopierst du das Projekt in ein Verzeichnis, das du selbst benennen kannst. 

3. Python-Abhängigkeiten installieren
    - Über ```pip install -r requirements.txt``` installierst du automatisch Selenium und alle andere Abhängigkeiten des Skripts.

4. Chromeengine installieren
    - Man muss jetzt noch irgendwie einen Webdriver installieren und in Selenium einbinden
    - Da ich im Code explizit den Chromedriver angesprochen habe, müsst ihr diesen ebenfalls verwenden.
    - Downloads für den Chrome-Webdriver, bzw. "chromedriver" gibt es [hier](https://googlechromelabs.github.io/chrome-for-testing/).
    - Glaube dann müsst ihr in "fetckkkhentries.py" halt einmal 