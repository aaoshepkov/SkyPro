import os
from selene import be, have
from selene.support.shared import browser


def test_demoqa():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Osh')
    browser.element('#userEmail').type('aaoshepkov@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('79659944488')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').type('1979')
    browser.element('.react-datepicker__month-select').type('January')
    browser.element('[class="react-datepicker__day react-datepicker__day--031"]').click()
    browser.element('#subjectsInput').type('computer science').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('files/jenkins.png')) #как работает модуль send_keys  и то что внутри него?
    browser.element('#currentAddress').type('Planet Earth')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()
#как лучше искать инфу по документации на selene? например, как найти инфу по полной проверке страницы и элементов на ней?
    # дальше должен быть сам тест с условиями should.have, should.be
    browser.element(all())
