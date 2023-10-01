import selene
import pytest
from selene import browser
from selene import be, have

def test_todo_list():
    browser.open('https://sky-todo-list.herokuapp.com/')

    browser.element('[type="text"]').type('Selene auto').press_enter()
    browser.should(have.text('Selene auto'))

test_todo_list()