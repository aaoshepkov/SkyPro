import selene
import pytest
from selene import browser
from selene import be, have
import time

def test_todo_list():
    browser.open('https://sky-todo-list.herokuapp.com/')
    browser.element('.input[type="text"]').type('Selene auto').press_enter()
    time.sleep(3)
    test