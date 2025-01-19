import pandas as pd
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException



# globale Chrome Settings und Variablen
service=Service("./chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--log-level=1")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
untilTimeout = 5


def authManual(driver):
    print("Starte manuelle Authentifizierung...")
    url = "https://borys.webuntis.com/WebUntis/?school=RBZ+Eckener+Schule+Flensburg#/basic/login"
    driver.get(url)
    input("Drücke [beliebig], sobald du angemeldet bist und das Skript fortfahren darf.")
    return driver

def authAuto(driver):
    with open("./credentials.txt", "r") as f:
        lines = f.readlines()
        username = lines[0].strip()
        password = lines[1].strip()
    school = "RBZ+Eckener+Schule+Flensburg"
    url = f"https://borys.webuntis.com/WebUntis/?school={school}#/basic/login"
    driver.get(url)
    inputs = WebDriverWait(driver, untilTimeout).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.un-input-group__input")))
    inputs[0].send_keys(username)
    inputs[1].send_keys(password)
    inputs[1].send_keys(Keys.RETURN)
    print("Über credentials.txt authentifiziert.")
    input("Drücke [beliebig], sobald du angemeldet bist und das Skript fortfahren darf.")
    return driver

def getWeekURLs(driver, date):
    driver.get(f"https://borys.webuntis.com/timetable-students-my/{date}")
    iframe = WebDriverWait(driver, untilTimeout).until(
        EC.presence_of_element_located((By.ID, "embedded-webuntis"))
    )
    #print("[LOG] iframe erkannt")
    driver.switch_to.frame(iframe)
    #print("[LOG] zu iframe gewechselt")
    WebDriverWait(driver, untilTimeout).until(
        EC.presence_of_element_located((By.CLASS_NAME, "timetableContent"))
    )
    anchor_tags = WebDriverWait(driver, untilTimeout).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
    )
    weekURLs = [
        anchor.get_attribute("href")
        for anchor in anchor_tags
        if anchor.get_attribute("href") and anchor.get_attribute("href").endswith("/class-registry")
    ]
    print(f"[LOG] Für die Woche mit Datum '{date}' wurden {len(weekURLs)} Unterrichtsstunden erkannt.")
    return weekURLs



def getURLsInfo(driver, weekURLs):
    xpaths= {
        "Inhalt": '//*[@id="root"]/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div[2]/textarea',
        "Fachbezeichnung": '//*[@id="root"]/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div/span',
        "Raumangabe": '//*[@id="root"]/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div[4]/div/span',
        "Uhrzeit": '//*[@id="root"]/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div[3]/span',
        "Datum": '//*[@id="root"]/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div[2]/span'
    }
    checkXPath = '//*[@id="root"]/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div'
    l = len(weekURLs)
    print(f"Es werden {l} Seiten für die Woche abgerufen.")
    info = []
    for x, url in enumerate(weekURLs, start=1):
        stundeninfos = {}
        print(f"Rufe Url {x} von {l} ab.")
        driver.get(url)
        for property, xpath in xpaths.items():
            if property == "Inhalt":
                try:
                    form_element = WebDriverWait(driver, untilTimeout).until(
                        EC.presence_of_element_located((By.XPATH, checkXPath))
                    )
                    try:
                        empty_indicator = form_element.find_element(By.CLASS_NAME, "empty-indicator")
                        stundeninfos[property] = "leer"
                    except NoSuchElementException:
                        stundeninfos[property] = driver.find_element(By.XPATH, xpath).text
                except:
                    print("[Error] - Vermutlich Timeout beim Suchen von <div class='form'> im DOM-Tree.")
                    stundeninfos[property] = "leer"

            else:
                print(f"[LOG] Lese {property} aus.")
                try:
                    result = WebDriverWait(driver, untilTimeout).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    stundeninfos[property] = result.text
                except:
                    stundeninfos[property] = "leer"
                    print(f"[Error] - Vermutlich Timeout beim Suchen von '{xpath}' im DOM-Tree.")
            info.append(stundeninfos)
            print(stundeninfos)
    return info



print("Automatische Authentifizierung erfordert, dass du deine Logindaten unverschlüsselt in der Datei 'credentials.txt' speicherst. Zeile 1: Benutzername, Zeile 2: Passwort.")
method = input("Möchtest du dich automatisch oder manuell anmelden? [a/m] ")
driver = webdriver.Chrome(service=service, options=options)

# Entfernen, wenn fertig
method = "a"


if method.lower() == "m":
    session = authManual(driver)
elif method.lower() == "a":
    session = authAuto(driver)
else:
    print("Ungültige Eingabe.")
    driver.quit()
    exit()

# Authentifizierung abgeschlossen. Ab jetzt mit Session arbeiten

print("Folgende Abfragen bitte fehlerfrei eingeben. Ich hab kein Error-Handling eingebaut, dafür bezahlt man mich nicht gut genug (gar nicht).")
startdate = input("Gib im Format YYYY-MM-DD an, ab wann du die Stundenplaninfos fetchen willst: ")
enddate = input("Gib im Format YYYY-MM-DD an, bis wann du die Stundenplaninfos fetchen willst ODER 'H' für das heutige Datum: ")
if enddate.lower() == "h":
    enddate = datetime.now().strftime("%Y-%m-%d")
interval = f"{startdate} - {enddate}"
cont = input(f"Du hast das Intervall {interval} gewählt. Fortfahren? [y/n] ")
if cont.lower() != "y":
    print("Abbruch.")
    driver.quit()
    exit()
sdo = datetime.strptime(startdate, "%Y-%m-%d")
edo = datetime.strptime(enddate, "%Y-%m-%d")
wday = sdo.weekday()
datelist = []
x = sdo

while sdo < edo:
    datelist.append(sdo.strftime("%Y-%m-%d"))
    sdo = sdo + timedelta(days=7)


allUrls = []
for date in datelist:
    urls = getWeekURLs(session, date)
    allUrls.extend(urls)
print(allUrls)
print(f"[LOG] im Intervall' {interval}' wurden {len(allUrls)} Unterrichtsstunden erkannt und ihre URLs wurden gesammelt.")
print(f"[LOG] Fahre fort und nutze URLs um Informationen abzurufen.")

data = getURLsInfo(session, allUrls)
session.quit()

print(f"[LOG] Erstelle mit 'Pandas'-Biliothek Excel-Datei aus Datensatz.")
df = pd.DataFrame(data)
filename = f"Untisdaten {interval}.xlsx"
df.to_excel(filename, index=False)
print(f"[LOG] Excel-Datei '{filename}' wurde erstellt.")