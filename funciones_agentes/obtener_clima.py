from time import sleep
from selenium.webdriver.common.by import By

def obtener_clima(driver, consulta):

    # Buscar el clima en Google
    driver.get(f"https://www.google.com/search?q=clima+{consulta}")

    sleep(20)

    try:
        # Obtener el nombre de la ciudad
        ciudad = driver.find_element(By.CSS_SELECTOR, "span[class='BBwThe']").text

        # Obtener la temperatura
        temperatura = driver.find_element(By.CSS_SELECTOR, "span[id='wob_tm']").text

        # Obtener la descripción del clima
        descripcion = driver.find_element(By.CSS_SELECTOR, "span[id='wob_dc']").text

        return f"Clima en {ciudad}: {temperatura}°C, {descripcion}."

    except Exception:
        return "No se pudo obtener el clima en este momento."