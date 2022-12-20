import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPets:
    def test_login_user(self, browser):

        # Open PetFriends base page:
        browser.get("https://petfriends.skillfactory.ru/")

        # click on the new user button
        btn_newuser = browser.find_element(
            By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]"
        )
        btn_newuser.click()

        # click existing user button
        btn_exist_acc = browser.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
        btn_exist_acc.click()

        # add email
        field_email = browser.find_element(By.ID, "email")
        field_email.clear()
        field_email.send_keys("julika77@mail.ru")

        # add password
        field_pass = browser.find_element(By.ID, "pass")
        field_pass.clear()
        field_pass.send_keys("77777")

        # click submit button
        btn_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
        btn_submit.click()

        browser.implicitly_wait(5)
        assert browser.current_url == "https://petfriends.skillfactory.ru/all_pets"

    def test_go_to_my_pets(self, browser):
        # click menu my_pets
        wait = WebDriverWait(browser, 10)
        menu_my_pets = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@href='/my_pets']"))
        )
        menu_my_pets.click()
        browser.implicitly_wait(5)
        assert browser.current_url == "https://petfriends.skillfactory.ru/my_pets"

    def test_all_pets_is_present(self, browser):
        amount_of_pets = browser.find_element(
            By.XPATH, "//div[@class='.col-sm-4 left']"
        ).text.split("\n")
        amount = int(amount_of_pets[1][10:])

        all_my_pets = len(
            list(browser.find_elements(By.XPATH, '//th[@scope="row"]/img'))
        )
        assert all_my_pets == amount

    def test_half_pets_have_photo(self, browser):
        images = browser.find_elements(By.XPATH, '//th[@scope="row"]/img')
        count = 0
        for i in range(len(images)):
            if images[i].get_attribute("src") != "":
                count += 1
        assert count >= len(images) / 2

    @pytest.mark.xfail
    def test_all_pets_have_description(self, browser):
        browser.implicitly_wait(5)
        names = browser.find_elements(By.XPATH, "//tbody/tr/td[1]")
        breeds = browser.find_elements(By.XPATH, "//tbody/tr/td[2]")
        ages = browser.find_elements(By.XPATH, "//tbody/tr/td[3]")
        for i in range(len(names)):
            assert names[i].text != ""
            assert breeds[i].text != ""
            assert ages[i].text != ""

    def test_all_pets_have_different_name(self, browser):
        names = list(browser.find_elements(By.XPATH, "//tbody/tr/td[1]"))
        all_names = [name.text for name in names]
        set_names = set(all_names)
        assert len(set_names) == len(all_names)

    def test_duplicate_pets(self, browser):
        names = browser.find_elements(By.XPATH, "//tbody/tr/td[1]")
        all_names = [name.text for name in names]
        breeds = browser.find_elements(By.XPATH, "//tbody/tr/td[2]")
        all_breeds = [breed.text for breed in breeds]
        ages = browser.find_elements(By.XPATH, "//tbody/tr/td[3]")
        all_ages = [age.text for age in ages]
        list_all_pets = [
            (
                all_names[i],
                all_breeds[i],
                all_ages[i],
            )
            for i in range(len(all_names))
        ]
        set_pets = set(list_all_pets)
        assert len(set_pets) == len(list_all_pets)
