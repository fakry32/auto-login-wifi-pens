# Code By : fakry32

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import requests
import time

def cek_koneksi():
    try:
        requests.get("https://www.google.com")
        return True
    except requests.ConnectionError:
        return False

def login(username, password):
    print("Koneksi internet tidak ada, akan mencoba login")
    username = "Masukkan Username Disini"
    password = "Masukkan Password Disini"

    print("Sedang login...")
    driver = webdriver.Chrome()
    driver.get("https://iac4.pens.ac.id:8009/index.php?zone=misc")

    username_field = driver.find_element(By.ID,"auth_user")
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID,"auth_pass")
    password_field.send_keys(password)

    login_button = driver.find_element(By.NAME,"accept")
    login_button.click()

    driver.quit()

def main():
    while True:
        if cek_koneksi():
            print("Koneksi internet ada")
        else:
            print("Tidak ada koneksi internet")
            
            login("username", "password")
        time.sleep(5)

if __name__ == "__main__":
    main()
