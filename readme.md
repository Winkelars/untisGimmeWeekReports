# Disclaimer
Bisher nur in Windows 10 mit Python-3.12 und in WSL auf Ubuntu getestet.
Feedback, ob das Skript auf anderen Plattformen funktioniert, ist willkommen.


# Vorschau
- ![image](https://pixeldrain.com/api/file/iTvN5jDS)
- [video preview](https://pixeldrain.com/api/file/i3CatESg) 


# Installation
## Windows
1. allgemeine Abhängigkeiten installieren 
    - Git: Über das PowerShell-Modul "WinGet" kann man als Windowsuser den Befehl ```winget install Git.Git``` benutzen um den Installationsvorgang für Git zu starten - Bei den neusten Windows 11 Releases ist Winget eingentlich vorinstalliert. Alternativ Git wie jedes andere Programm googlen und installieren -> "Windows git installation"
    - Python: Dafür empfehle ich die [offizielle Website](https://www.python.org/downloads/) zu besuchen den Installationsanweisungen zu folgen. Über Winget ist die Installation aber ziemlich sicher auch möglich.

2. Repo klonen
    - Mit dem Befehl ```git clone https://github.com/Winkelars/untisGimmeWeekReports {pfad}``` kopierst du das Projekt in das Verzeichnis, das du an der Stelle {pfad} auswählst.
    - wechsle mit ```cd {pfad}``` jetzt in das Verzeichnis

3. Python-Abhängigkeiten installieren
    - Wenn du planst Python öfter zu benutzen, und allgemein einfach best-practice folgen willst, solltest du nun eine virtuelle Umgebung aufsetzen - ich empfehle also ```python -m venv venv``` auszuführen und danach über ```./venv/Scripts/Activate.ps1``` die Umgebung zu betreten. Danach sollte "(venv)" in deinem PowerShell-Prompt zu sehen sein.
    - Über ```pip install -r requirements.txt``` installierst du zuletzt automatisch alle anderen Python-Bibliotheken, die das Skript zu laufen braucht.

4. Starte das Tool mit ```python fetchentries.py```. Die nächsten Schritte werden in der Konsole erklärt.

### Anmerkung
Teile der Installation werden in Zukunft hoffentlich automatisiert oder überflüssig gemacht. Wenn ich herausfinde wie man alles über ein kleines Dockerimage laufen lässt, muss man bald nur Docker installieren und das Image via ```docker run image``` ausführen

# Build
Um eine .exe für Windows zu bauen können folgende Schritte befolgt werden:
- ```pip install -r build_requirements.txt```
- ```pyinstaller --onefile --name untisGimmeWeekReports main.py```
