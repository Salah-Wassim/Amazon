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
    search_input_password.send_keys(search_value_password)

    # Cibler le bouton s'identifier
    search_btn_continue = driver.find_element_by_class_name("a-button-input")
    search_btn_continue.click()


def error(err):
    # Cas erreur mot de passe
    login_error = driver.find_element_by_id("auth-error-message-box")
    signin_url = driver.get("https://www.amazon.fr/ap/signin")

    if login_error or signin_url:
        while err and signin_url:
            # Cibler l'input password
            search_input_password_err = driver.find_element_by_id("ap_password")
            search_value_password_err = input("Input your password : ")
            search_input_password_err.send_keys(search_value_password_err)

            # Cibler le bouton s'identifier
            search_btn_continue_err = driver.find_element_by_class_name("a-button-input")
            search_btn_continue_err.click()
            return (login_error and signin_url) is False


def search():
    # Cibler la barre de recherche
    search_bar = driver.find_element_by_id("twotabsearchtextbox")
    search_value = input("Input your research : ")
    search_bar.send_keys(search_value)

    # Recuperer le bouton de recherche
    search_btn = driver.find_element_by_id("nav-search-submit-button")
    search_btn.click()


def recoverArticle():
    # Recupere tous les titres d'articles
    articles_title = driver.find_elements_by_class_name("a-text-normal")

    # Parcourir la liste des éléments ciblés
    for title in articles_title:
        print(title.text)


def categories():
    # Cibler liste déroulante "Toutes nos catégorie"
    search_drop_down = driver.find_element_by_id("searchDropdownBox")
    search_drop_down.click()

    # Cibler les catégories
    search_categories = driver.find_elements_by_tag_name("option")

    # Creation d'un tableaux
    categories_array = []

    # Recuperer la liste des categories et les insérer dans un tableaux
    for c in search_categories:
        categories_array.append(c.text)  # Convertir WebElements en String
    print(categories_array)

    # Valider le nom de la catégorie entré par l'utilisateur et faire la recherche
    err_name_categorie = True
    while err_name_categorie:
        choice_categorie_user = input("Input a categorie name : ")
        if choice_categorie_user in categories_array:
            # Cibler la barre de recherche
            search_bar_categorie = driver.find_element_by_id("twotabsearchtextbox")
            search_bar_categorie.send_keys(choice_categorie_user)
            # Recuperer le bouton de recherche
            search_btn = driver.find_element_by_id("nav-search-submit-button")
            search_btn.click()
            # Recupere tous les titres d'articles
            recover_articles = input("Do you want to retrieve your search results? (yes / no) : ")
            if recover_articles == "yes":
                recoverArticle()
            return err_name_categorie is False
        else:
            print("Input a valid name categorie")
        # print()


def choice():
    choice_search_user = input("Do you want select a categorie ? (yes / no) : ")
    if choice_search_user == "yes":
        categories()
    elif choice_search_user == "no":
        search()
        recover_articles = input("Do you want to retrieve your search results? (yes / no) : ")
        if recover_articles == "yes":
            recoverArticle()


def basket():
    choice_basket_user = input("Would you like to access the basket ? (yes / no) : ")
    if choice_basket_user == "yes":
        search_basket = driver.find_element_by_id("nav-cart")
        search_basket.click()


# Choix de l'utilisateur
choice_user = input("Do you want signin ? (yes / no) : ")
if choice_user == "yes":
    auth()
    choice()
    basket()
elif choice_user == "no":
    choice()
