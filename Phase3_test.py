import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import uuid

# Unique email generation
domain = "testing.com"
unique_id = uuid.uuid4().hex
email = f"{unique_id}@{domain}"

# General variables

firstName = "Johnie"
lastName = "Jhones"
password = "Tosca1234"
selectedCamera = "Digital SLR Camera"
city = "Cape Town"
address = "25 Jhonsen Street"
zipCode = "911"
phoneNumber = "2025202620"
driver = webdriver.Edge()
f = driver.find_element

# Register variables

Register_Xpath = "//a[normalize-space()='Register']"
Gender_Xpath = "//input[@id='gender-male']"
RegisterButton_Xpath = "//input[@id='register-button']"
Result_Xpath = "//div[@class='result']"
Continue_Xpath = "// input[ @ value = 'Continue']"
Logout_Xpath = "//a[normalize-space()='Log out']"
AccountRegistered = "Your registration completed"

# Loging variables

Login_Xpath = "//a[normalize-space()='Log in']"
Login2_Xpath = "//input[@value='Log in']"
Account_Xpath = "//a[@class='account']"

# Cart and checkout variables

SearchBar_Xpath = "//input[@id='small-searchterms']"
SearchBtn_Xpath = "//input[@value='Search']"
ProductClick_Xpath = "//a[normalize-space()='Digital SLR Camera 12.2 Mpixel']"
AddtoCart_Xpath = "//input[@id='add-to-cart-button-18']"
ShoppingCartBtn_Xpath = "//span[normalize-space()='Shopping cart']"
ItemInCart_Xpath = "//a[@class='product-name']"
ItemInCartQuantity_Xpath = "//input[@name='itemquantity6380790']"
TermsOfService_Xpath = "//input[@id='termsofservice']"
CheckoutBtn_Xpath = "//button[@id='checkout']"

CountryBtn_Xpath = "//option[@value='71']"
CityField_Xpath = "//input[@id='BillingNewAddress_City']"
AddressField_Xpath = "//input[@id='BillingNewAddress_Address1']"
ZipCodeField_Xpath = "//input[@id='BillingNewAddress_ZipPostalCode']"
PhoneNumberField_Xpath = "//input[@id='BillingNewAddress_PhoneNumber']"

BillingContinue_Xpath = "//input[@onclick='Billing.save()']"
ShoppingContinue_Xpath = "//input[@onclick='Shipping.save()']"
MethodContinue_Xpath = "//input[@onclick='ShippingMethod.save()']"
PaymentContinue_Xpath = "//input[@onclick='PaymentMethod.save()']"
PaymentInfoContinue_Xpath = "//input[@class='button-1 payment-info-next-step-button']"
ConfirmOrder_Xpath = "//input[@value='Confirm']"
CompleteBtn_Xpath = "(//input[@value='Continue'])[1]"
PurchaseCompleted = "Your order has been successfully processed!"
Purchase_Xpath = "//strong[normalize-space()='Your order has been successfully processed!']"


@pytest.fixture
def setUp():
    base_url = "https://demowebshop.tricentis.com/"
    driver.maximize_window()
    driver.get(base_url)

def test_register(setUp):

    driver.implicitly_wait(3)

    title = driver.title
    print("\nThe title of the webpage is: " + title)
    current_url = driver.current_url
    print("The current url is: " + current_url)

    register_button = f(By.XPATH, Register_Xpath)
    register_button.click()
    print("User has clicked the register button")

    gender_button = f(By.XPATH, Gender_Xpath)
    gender_button.click()
    print("User has selected their gender")

    first_name_field = f(By.ID, "FirstName")
    first_name_field.send_keys(firstName)
    print("User has clicked on first name field and entered their first name")

    last_name_field = f(By.ID, "LastName")
    last_name_field.send_keys(lastName)
    print("User has clicked on last name field and entered their last name")

    email_field = f(By.ID, "Email")
    email_field.send_keys(email)
    print("User has clicked on email field and entered their email")

    password_field = f(By.ID, "Password")
    password_field.send_keys(password)
    print("User has clicked on password field and entered their password")

    confirm_password_field = f(By.ID, "ConfirmPassword")
    confirm_password_field.send_keys(password)
    print("User has clicked on confirm password field and entered their password")

    register_buton = f(By.XPATH, RegisterButton_Xpath)
    register_buton.click()
    print("User has clicked the register button to finalize register")

    result = f(By.XPATH, Result_Xpath)
    print(result.text)
    assert result.text == AccountRegistered

    continue_button = f(By.XPATH, Continue_Xpath)
    continue_button.click()
    print("User has clicked continue after creating their account")

    logout_button = f(By.XPATH, Logout_Xpath)
    logout_button.click()
    print("User has logged out of their account")

def test_login(setUp):

    driver.implicitly_wait(3)

    login_button = f(By.XPATH, Login_Xpath)
    login_button.click()
    print("\nUser has clicked the login button")

    email_field = f(By.ID, "Email")
    email_field.send_keys(email)
    print("User has clicked the email field and entered their email")

    password_field = f(By.ID, "Password")
    password_field.send_keys(password)
    print("User has clicked the password field and entered their password")

    login_button_2 = f(By.XPATH, Login2_Xpath)
    login_button_2.click()
    print("User has clicked login button")

    account_field = f(By.XPATH, Account_Xpath)
    print("User is logged in with email: " + account_field.text)
    assert account_field.text == email

def test_CartAndCheckout(setUp):

    driver.implicitly_wait(3)

    search_bar = f(By.XPATH, SearchBar_Xpath)
    search_bar.send_keys(selectedCamera)
    print("\nUser has clicked on the search bar and entered what they are looking for")

    search_bar_button = f(By.XPATH, SearchBtn_Xpath)
    search_bar_button.click()
    print("User has clicked on search button")

    product_click = f(By.XPATH, ProductClick_Xpath)
    product_click.click()
    print("User has clicked on the selected product to learn more")

    driver.execute_script("window.scrollBy(0, 400)")

    add_to_cart_button = f(By.XPATH, AddtoCart_Xpath)
    add_to_cart_button.click()
    print("User has added product to cart")

    driver.execute_script("window.scrollBy(0, -400)")

    shopping_cart_button = f(By.XPATH, ShoppingCartBtn_Xpath)
    shopping_cart_button.click()
    print("User has clicked on the shopping cart button")

    item_in_cart = f(By.XPATH, ItemInCart_Xpath)
    print("The items in the cart are: " + item_in_cart.text)
    print("The selected farient is: " + item_in_cart.text)

    #item_in_cart_quantity = f(By.XPATH, ItemInCartQuantity_Xpath)
    #print("There are " + item_in_cart_quantity.text + item_in_cart.text + " in the cart")

    tos_button = f(By.XPATH, TermsOfService_Xpath)
    tos_button.click()
    print("User has clicked on the terms of service button")

    checkout_button = f(By.XPATH, CheckoutBtn_Xpath)
    checkout_button.click()
    print("User has clicked on the checkout button")

    country_button = f(By.XPATH, CountryBtn_Xpath)
    country_button.click()
    print("User has selected their country")

    city_field = f(By.XPATH, CityField_Xpath)
    city_field.send_keys(city)
    print("User has entered their city")

    address_field = f(By.XPATH, AddressField_Xpath)
    address_field.send_keys(address)
    print("User has entered their address")

    zip_code_field = f(By.XPATH, ZipCodeField_Xpath)
    zip_code_field.send_keys(zipCode)
    print("User has entered their zip code")

    phone_number_field = f(By.XPATH, PhoneNumberField_Xpath)
    phone_number_field.send_keys(phoneNumber)
    print("User has entered their phone number")

    billing_continue_button = f(By.XPATH, BillingContinue_Xpath)
    billing_continue_button.click()
    print("User clicked continue to shipping")

    shipping_continue_button = f(By.XPATH, ShoppingContinue_Xpath)
    shipping_continue_button.click()
    print("User clicked continue to payment method")

    method_continue_button = f(By.XPATH, MethodContinue_Xpath)
    method_continue_button.click()
    print("User clicked continue to payment details")

    payment_continue_button = f(By.XPATH, PaymentContinue_Xpath)
    payment_continue_button.click()
    print("User clicked continue to payment information")

    payment_info_continue_button = f(By.XPATH, PaymentInfoContinue_Xpath)
    payment_info_continue_button.click()
    print("User clicked continue to finish payment")

    driver.execute_script("window.scrollBy(0, 500)")

    confirm_order_button = f(By.XPATH, ConfirmOrder_Xpath)
    confirm_order_button.click()
    print("User clicked confirm order to finish order")

    confirmation_text = f(By.XPATH, Purchase_Xpath)
    assert confirmation_text.text == PurchaseCompleted

    time.sleep(0.5)

    complete_button = f(By.XPATH, CompleteBtn_Xpath)
    complete_button.click()
    print("User finished order and got sent to home screen")

    logout_button = f(By.XPATH, Logout_Xpath)
    logout_button.click()
    print("User has logged out of their account")
    driver.quit()



