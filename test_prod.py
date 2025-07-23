from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração do WebDriver (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

# Acessa a página de cadastro usando o caminho absoluto com o protocolo file://
driver.get("file:///C:/Users/julia_pavlick/Downloads/teste_de_sistemas/produto.html")

# Preenche o campo ID do Produto
id_input = driver.find_element(By.ID, "id_produto")
id_input.send_keys("00123")

# Preenche o campo Descrição
descricao_input = driver.find_element(By.ID, "descricao")
descricao_input.send_keys("Pão Francês 50g")

# Preenche o campo Marca
marca_input = driver.find_element(By.ID, "marca")
marca_input.send_keys("Padaria do Alemão")

# Preenche o campo Quantidade
quantidade_input = driver.find_element(By.ID, "quantidade")
quantidade_input.send_keys("120")

# Preenche o campo Preço
preco_input = driver.find_element(By.ID, "preco")
preco_input.send_keys("0.50")

# Clica no botão de Cadastrar
# submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
# submit_button.click()

# Aguarda um momento para visualizar o resultado (em uma aplicação real, você verificaria a resposta)
time.sleep(10)

# Fecha o navegador
driver.quit()
