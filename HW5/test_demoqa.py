from selene import be, have
from selene.support.shared import browser


def test_demoqa():
    # Открытие Google
    browser.open("https://demoqa.com/automation-practice-form")

    # Заполнение формы имя и проверка
    browser.element('[placeholder="First Name"]').should(be.blank).type('Alex')
    #browser.element('[placeholder="First Name"]').should(have.text('Alex'))
    # Заполнение формы фамилия и проверка
    browser.element('[placeholder="Last Name"]').should(be.blank).type('Osh')
    #browser.element('[placeholder="Last Name"]').should(have.text('Osh'))
    # Проверка наличия текста на странице
    browser.element('[placeholder="name@example.com"]').should(be.blank).type('aaoshepkov@gmail.com')

    browser.element('[for="gender-radio-1"]').click()
    browser.element('[placeholder="Mobile Number"]').should(be.blank).type('9659944488')
    browser.element('[id="dateOfBirthInput"]').click().press()
    browser.element('[class="subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3"]').should(be.blank).type('Python, Selene, AQA')
    test

def test_google_search_negative():
    # Открытие Google
    browser.open("https://www.google.com")

    # Поиск по запросу "yashaka/selene"
    browser.element('#APjFqb').should(be.blank).type('nvdjsnvkhsbdlkewjfoiahsdukfb').press_enter()

    # Проверка наличия текста на странице
    browser.element('#result-stats').should(have.text("Результатов: примерно 0"))
