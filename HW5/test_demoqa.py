import os
from selene import be, have
from selene.support.shared import browser


def test_demoqa():
    browser.open("https://demoqa.com/automation-practice-form")

    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')

    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Osh')
    browser.element('#userEmail').type('aaoshepkov@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9659944488')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').type('1979')
    browser.element('.react-datepicker__month-select').type('January')
    browser.element('[class="react-datepicker__day react-datepicker__day--031"]').click()
    browser.element('#subjectsInput').type('computer science').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').type(os.path.abspath('files/jenkins.png'))
    browser.element('#currentAddress').type('Planet Earth')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()

    browser.element('tbody').all('tr')[0].should(have.text('Alex Osh'))
    browser.element('tbody').all('tr')[1].should(have.text('aaoshepkov@gmail.com'))
    browser.element('tbody').all('tr')[2].should(have.text('Male'))
    browser.element('tbody').all('tr')[3].should(have.text('9659944488'))
    browser.element('tbody').all('tr')[4].should(have.text('31 January,1979'))
    browser.element('tbody').all('tr')[5].should(have.text('Computer Science'))
    browser.element('tbody').all('tr')[6].should(have.text('Sports'))
    browser.element('tbody').all('tr')[7].should(have.text('jenkins.png'))
    browser.element('tbody').all('tr')[8].should(have.text('Planet Earth'))
    browser.element('tbody').all('tr')[9].should(have.text('NCR Delhi'))