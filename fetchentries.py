import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



# globale Chrome Settings und Variablen
service=Service(r"C:\tools\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--log-level=1")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
timeout = 5


def authManual(driver):
    print("Starte manuelle Authentifizierung...")
    url = "https://borys.webuntis.com/WebUntis/?school=RBZ+Eckener+Schule+Flensburg#/basic/login"
    driver.get(url)
    input("Drücke [beliebig], sobald du angemeldet bist.")
    return driver

def authAuto(driver):
    with open("./credentials.txt", "r") as f:
        lines = f.readlines()
        username = lines[0].strip()
        password = lines[1].strip()
    school = "RBZ+Eckener+Schule+Flensburg"
    url = f"https://borys.webuntis.com/WebUntis/?school={school}#/basic/login"
    driver.get(url)
    inputs = WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.un-input-group__input")))
    inputs[0].send_keys(username)
    inputs[1].send_keys(password)
    inputs[1].send_keys(Keys.RETURN)
    print("Über credentials.txt authentifiziert.")
    return driver

def getWeekURLs(driver, date):
    time.sleep(timeout)
    driver.get(f"https://borys.webuntis.com/timetable-students-my/{date}")
    iframe = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, "embedded-webuntis"))
    )
    print("iframe erkannt.")
    driver.switch_to.frame(iframe)
    print("zu iframe gewechselt.")
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CLASS_NAME, "timetableContent"))
    )
    anchor_tags = driver.find_elements(By.TAG_NAME, "a")
    weekURLs = [
        anchor.get_attribute("href")
        for anchor in anchor_tags
        if anchor.get_attribute("href") and anchor.get_attribute("href").endswith("/class-registry")
    ]
    print(f"URLs der Unterrichtseinheiten von Woche {date} erkannt.")
    return weekURLs



def getURLsInfo(driver, weekURLs):
    info = []
    xpaths= {
        "Fachbezeichnung": '//*[@id="root"]/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div/span',
        "Raumangabe": '//*[@id="root"]/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div[4]/div/span',
        "Uhrzeit": '//*[@id="root"]/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div[3]/span',
        "Datum": '//*[@id="root"]/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div[2]/span',
        "Inhalt": '//*[@id="root"]/div/div/div/div[2]/div/div[1]/section/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div[2]/textarea'
    }
    l = len(weekURLs)
    print(f"Es werden {l} Seiten für die Woche abgerufen.")
    for x, url in enumerate(weekURLs, start=1):
        stundeninfos = {}
        print(f"Rufe Url {x} von {l} ab.")
        driver.get(url)
        for property, xpath in xpaths.items():
            print(f"Lese {property} aus.")
            try:
                result = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                stundeninfos[property] = result.text
            except:
                stundeninfos[property] = "Error - Exception beim Lesen des bElements."
                print(f"Error - Exception beim Lesen des Elements {property} mit dem XPath {xpath}.")
            info.append(stundeninfos)
            print(stundeninfos)
    return info



print("Automatische Authentifizierung erfordert, dass du deine Logindaten unverschlüsselt in der Datei 'credentials.txt' speicherst.")
print("Da es dir suspekt sein sollte fremden Code mit deinen Logindaten zu füttern, kannst du dich auch selbst anmelden und den Rest dem Skript überlassen. (Es wäre einem böswilligen Hacker aber immernoch möglich so an deine Daten zu gelangen.)")
#method = input("Möchtest du dich automatisch oder manuell anmelden? [a/m] ")
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

print("Hole alle Informationen für die Schulwoche mit Datum 2024-05-27")
letzteMaiWocheURLs = getWeekURLs(session,"2024-05-27")
info = getURLsInfo(session, letzteMaiWocheURLs)
print(info)
session.quit()