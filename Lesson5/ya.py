'''
найти книги по слову Python
собрать все карточки товаров
вывести в консоль инфо: название + автор + цена
'''


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


driver.get('https://www.labirint.ru/')
WebDriverWait(driver, 5)

search_locator = '#search-field'

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

#найти книги по слову Python
word_search = 'Python'
search_input.send_keys(word_search, Keys.RETURN)
WebDriverWait(driver, 10)

#Собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, 'div.product-card')


#вывести в консоль инфо: название + автор + цена
for book in books:
    title = ''
    author = ''
    price = ''
    try:
        author = book.find_element(By.CSS_SELECTOR, 'div.product-card__author').text
    except:
        author = 'Автор не указан'
    try:
        title = book.find_element(By.CSS_SELECTOR, 'a.product-card__name').text
    except:
        title = 'Название не указано'
    try:
        price = book.find_element(By.CSS_SELECTOR, 'div.product-card__price-current').text
    except:
        price = 'Цена не указана'
    try:
        price = book.find_element(By.CSS_SELECTOR, 'div.product-card__price-current').text
    except:
        price = 'Цена не указана'

    print(f'Автор: {author} Название: "{title}" Текущая цена: {price}')
print(f'По слову {word_search} всего найдено {len(books)}')

