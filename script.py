from selenium import webdriver

# Creer une variable pour déclencher le driver
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.amazon.fr/")

## Cibler le lien "Bonjour, Identifiez vous ...."
# search_nav_signin = driver.find_element_by_id("nav-link-accountList")
# search_nav_signin.click()

# Cibler le bouton "Accepter les cookies"
search_btn_cookies = driver.find_element_by_id("sp-cc-accept")
search_btn_cookies.click()

choice_user = input("Do you want signin ? (yes / no) : ")


def auth():
    # Clibler l'url de la page d'authentification
    search_btn_signin = driver.find_element_by_id("nav-link-accountList")
    search_btn_signin.click()

    # Cibler l'input email
    search_input_email = driver.find_element_by_id("ap_email")
    search_value_email = input("Input your email : ")
    search_input_email.send_keys(search_value_email)

    # Cibler le bouton continuer
    search_btn_continue = driver.find_element_by_class_name("a-button-input")
    search_btn_continue.click()

    # Cibler l'input password
    search_input_password = driver.find_element_by_id("ap_password")
    search_value_password = input("Input your password : ")
    search_input_password.send_keys(search_value_email)

    # Cibler le bouton s'identifier
    search_btn_continue = driver.find_element_by_class_name("a-button-input")
    search_btn_continue.click()

    # Cas erreur mot de passe
    login_error = driver.find_element_by_id("auth-error-message-box")

    if login_error:
        while login_error:
            # Cibler l'input password
            search_input_password = driver.find_element_by_id("ap_password")
            search_value_password = input("Input your password : ")
            search_input_password.send_keys(search_value_email)
            # Cibler le bouton s'identifier
            search_btn_continue = driver.find_element_by_class_name("a-button-input")
            search_btn_continue.click()


def search():
    # Cibler la barre de recherche
    search_bar = driver.find_element_by_id("twotabsearchtextbox")
    search_value = input("Input your research : ")
    search_bar.send_keys(search_value)

    # Recuperer le bouton de recherche
    search_btn = driver.find_element_by_id("nav-search-submit-button")
    search_btn.click()

    # Recupere tous les titres d'articles
    articles_title = driver.find_elements_by_class_name("a-text-normal")

    # Parcourir la liste des éléments ciblés
    for title in articles_title:
        print(title.text)


def categories():
    # Cibler liste déroulante "Toutes nos catégorie"
    search_drop_down = driver.find_element_by_id("searchDropdownBox")
    search_drop_down.click()


# Choix de l'utilisateur
if choice_user == "yes":
    auth()
elif choice_user == "no":
    choice_search_user = input("Do you want select a categorie ? (yes / no)")
    if choice_search_user == "yes":
        categories()
    else:
        search()

