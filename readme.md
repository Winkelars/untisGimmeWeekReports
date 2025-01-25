# Disclaimer
Bisher nur in Windows 10 mit Python-3.12 getestet.
Feedback, ob das Skript auf anderen Plattformen funktioniert, ist willkommen.
Kompatibilitätsprobleme werden am wahrscheinlichsten im Zusammenhang mit der Python-Bibliothek "Selenium" auftreten.

# Installation
## Windows
1. allgemeine Abhängigkeiten installieren
    - Wenn du noch nie von Git gehört hast, ist das ok, aber  
    - Über das PowerShell-Modul "WinGet" kann Git kann ganz einfach mit dem Befehl ```winget install Git.Git``` installiert werden - Bei den neusten Windows 11 Releases ist Winget eingentlich vorinstalliert. Ansonsten Google -> "Windows git installation"
    - Außerdem muss Python installiert werden. Dafür empfehle ich die neuste Version von der [offiziellen Website](https://www.python.org/downloads/) herunterzuladen und den Installationsanweisungen zu folgen.

2. Repo klonen
    - Mit dem Befehl ```git clone https://github.com/Winkelars/untisGimmeWeekReports {pfad}``` kopierst du das Projekt in das Verzeichnis, das du im Feld {pfad} auswählst. 

3. Python-Abhängigkeiten installieren
    - Wenn du Python öfter benutzt möchtest du als erstes wahrscheinlich eine virtuelle Umgebung aufsetzen - also z.B. via ```python -m venv venv``` die Umgebung anlegen und danach über ```./venv/Scripts/Activate.ps1``` die Umgebung betreten. Dann sollte "(venv)" in deinem PowerShell-Prompt zu sehen sein.
    - Über ```pip install -r requirements.txt``` installierst du automatisch Selenium und alle anderen Python-Abhängigkeiten des Skripts.

4. Chromeengine installieren
    - Man muss jetzt noch einen Webdriver installieren und in Selenium einbinden
    - Da ich im Code explizit den Chromedriver angesprochen habe, müsst ihr entweder ebenfalls chromedriver.exe verwenden, oder den Code anpassen, was auch nicht allzu schwierig wäre.
    - Downloads für den Chrome-Webdriver, bzw. "chromedriver" gibt es [hier](https://googlechromelabs.github.io/chrome-for-testing/).
    - legt "chromedriver.exe" entpackt mit in das Repoverzeichnis neben "readme.md" und "fetchentries.py".

### Anmerkung
Teile der Installation könnten in Zukunft automatisiert oder überflüssig gemacht werden. Wenn ich herausfände wie man alles über ein kleines Dockerimage laufen lässt, würde man nur Docker installieren und dann einmal das Image ausführen müssen.