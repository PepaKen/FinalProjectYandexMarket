from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
import os


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://market.yandex.ru/'

        super().__init__(web_driver, url)

    h1 = WebElement(xpath='//h1')

    h2 = WebElement(xpath='//h2')

    first_element_in_location = WebElement(xpath="//a[@class='aSUR-uUgeo'][1]")

    location = WebElement(xpath="//div[@class='_6RmNBByo8N']")

    input_location = WebElement(xpath="//input[@class='_1pVZ3jklLF']")

    location_btn_success = WebElement(xpath="//button[@class='zsSJkfeAPw _16jABpOZ2- _36y1jOUHs5 LS3-2-cZ2Z']")

    pokupki = WebElement(xpath="//a[@class='_3Lwc_UVFq4 cHIkHPYoKi _1DpwW9o1wj']")

    elektronika = WebElement(xpath='//a[@href="/catalog--elektronika/54440"]')

    dacha_i_sad = WebElement(xpath='//a[@href="/catalog--dacha-sad-i-ogorod/54495"]')

    detskie_tovary = WebElement(xpath='//a[@href="/catalog--detskie-tovary/54421"]')

    products_drinks = WebElement(xpath='//a[@href="/catalog--produkty-napitki/54434"]')

    tehnica_bytovaia = WebElement(xpath='//a[@href="/catalog--bytovaia-tekhnika/54419"]')

    live_streams = WebElement(xpath="//a[@href='/live']")

    catalog_btn = WebElement(xpath="//button[@class='zsSJkfeAPw _16jABpOZ2- gjdzW5ajbI _3WgR56k47x']")

    zoo_products_catalog = WebElement(xpath="//button[@id='91540721-tab']/a")

    birds_products = WebElement(xpath="//a[@href='/catalog--tovary-dlia-ptits/62871']")

    pokupki_in_catalog = WebElement(xpath='//a[@href="https://pokupki.market.yandex.ru/"]')

    beauty_in_catalog = WebElement(xpath="//button[@id='91540461-tab']/a")

    uhod_za_litsom = WebElement(xpath='//a[@href="/catalog--sredstva-po-ukhodu-za-litsom/17437151?hid=8475933"]')

    computers_in_catalog = WebElement(xpath='//button[@id="91540057-tab"]/a')

    gaming_page = WebElement(xpath='//a[@href="/catalog--tovary-dlia-geimerov/18072602"]')

    sport_products_catalog = WebElement(xpath='//button[@id="91541780-tab"]/a')

    children_sport = WebElement(xpath='//a[text()="Детский спорт"]')

    house_catalog = WebElement(xpath='//button[@id="91540260-tab"]/a')

    interior = WebElement(xpath='//a[@href="/catalog--domashnii-interer/54497?hid=90714"]')

    furniture_catalog = WebElement(xpath='//button[@id="91540328-tab"]/a')

    tables_chairs = WebElement(xpath='//a[@href="/catalog--stoly-i-stulia/18049598?hid=11917790"]')

    building_catalog = WebElement(xpath='//button[@id="91540195-tab"]/a')

    electric = WebElement(xpath='//a[@href="/catalog--elektrika/55183?hid=91697"]')

    jewelery_catalog = WebElement(xpath='//button[@id="91542173-tab"]/a')

    clock = WebElement(xpath='//a[@href="/catalog--naruchnye-chasy/18057688/list?glfilter=2737816%3A12111177%2C12111164%2C12111170&hid=91259"]')

    health_catalog = WebElement(xpath='//button[@id="91540525-tab"]/a')

    optics = WebElement(xpath='//a[@href="/catalog--optika/56064?hid=90530"]')

    hobby_catalog = WebElement(xpath='//button[@id="91541844-tab"]/a')

    telescopes_microscopes = WebElement(xpath='//a[@href="/catalog--teleskopy-i-mikroskopy/18071678"]')

    books_catalog = WebElement(xpath='//button[@id="91541904-tab"]/a')

    business_finances = WebElement(xpath='//a[@href="/catalog--knigi-o-biznese-i-finansakh/19436490/list?glfilter=18664890%3A18665018&hid=18540670"]')

    for_school_office_catalog = WebElement(xpath='//button[@id="91542364-tab"]/a')

    school_suits = WebElement(xpath='//a[@href="/catalog--shkolnaia-odezhda-i-obuv/17985882"]')

    clothes_shoes_catalog = WebElement(xpath='//button[@id="91542039-tab"]/a')

    accessories = WebElement(xpath='//a[@href="/catalog--aksessuary-i-ukrasheniia/54600?hid=7811881"]')

    equipment_catalog = WebElement(xpath='//button[@id="91542311-tab"]/a')

    building_eqip = WebElement(xpath='//a[@href="/catalog--stroitelnoe-oborudovanie/54592?hid=91777"]')

    car_products_catalog = WebElement(xpath='//button[@id="91540397-tab"]/a')

    audio_video = WebElement(xpath='//a[@href="/catalog--avtomobilnaia-audio-i-videotekhnika/54455?hid=90403"]')

    adult_products_catalog = WebElement(xpath='//button[@id="91542242-tab"]/a')

    condoms = WebElement(xpath='//a[@href="/catalog--prezervativy/18019246/list?hid=13744375"]')

    discount_catalog = WebElement(xpath='//button[@id="91542488-tab"]/a')

    auto_discount = WebElement(xpath='//a[@href="/catalog--tovary-dlia-avto-i-mototekhniki/16801126?hid=90402"]')

    sales_catalog = WebElement(xpath='//button[@id="91542546-tab"]/a')

    scores_page = WebElement(xpath='//div[@class="_3MJ2bWXdtL"]/a')

    orders_page = WebElement(xpath='//a[@href="/my/orders?track=menu"]')

    wishlist_page = WebElement(xpath='//a[@href="/my/wishlist?track=head"]')

    cart_page = WebElement(xpath='//a[@href="//pokupki.market.yandex.ru/my/cart?purchase-referrer=beru_in_yamarket"]')

    search = WebElement(id='header-search')

    search_run_button = WebElement(xpath='//button[@type="submit"]')

    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    sort_products_by_price = WebElement(xpath='//button[@data-autotest-id="dprice"]')

    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')

    search_incorrect = WebElement(xpath='//div[@class="_2QX_1Ho2Fe"]')

    sort_products_by_quality = WebElement(xpath='//button[@data-autotest-id="quality"]')

    sort_products_by_opinions = WebElement(xpath='//button[@data-autotest-id="opinions"]')

    sort_products_by_discount = WebElement(xpath='//button[@data-autotest-id="discount_p"]')

    sort_products_by_date = WebElement(xpath='//button[@data-autotest-id="ddate"]')

    choice_goods_footer = WebElement(xpath='//a[@href="https://yandex.ru/support/market/choice-goods/product-search.html"]')

    pay_delivery_footer = WebElement(xpath='//a[@href="https://pokupki.market.yandex.ru/my/order/conditions"]')

    feedback_footer = WebElement(xpath='//a[@href="https://yandex.ru/support/market/troubleshooting/general.xml"]')

    about_footer = WebElement(xpath='//a[@href="/about"]')

    research_footer = WebElement(xpath='//a[@href="https://yandex.ru/jobs/usability"]')

    return_footer = WebElement(xpath='//a[@href="https://yandex.ru/support/market/return.html"]')

    facebook_footer = WebElement(xpath='//a[@data-autotest-social-name="facebook"]')

    vk_footer = WebElement(xpath='//a[@data-autotest-social-name="vk"]')

    instagram_footer = WebElement(xpath='//a[@data-autotest-social-name="instagram"]')

    add_in_cart_btn = ManyWebElements(xpath='//button[@class="zsSJkfeAPw _16jABpOZ2- gjdzW5ajbI LS3-2-cZ2Z _2Sz75Y384m _1XumhZyXqj _2VlTHnWxF8"]')

    go_to_cart_after_adding = WebElement(xpath='//a[@class="zsSJkfeAPw _2sWJL7-h2E _16jABpOZ2- _36y1jOUHs5 _2_x8rfeWTI _1GRkjutzG9"]')

    items_in_my_cart = ManyWebElements(xpath='//div[@class="b_1_MhGKBSdf b_2er7mzKEW5 b_1dVZ35q5yJ"]')

    remove_item_from_cart = ManyWebElements(xpath='//div[@class="b_3FCaH0jGWO b_1yIm0AlO3K"]')

    execute_btn_in_cart = WebElement(xpath='//button[@data-tid="9fad06c2 525ccbb1 71ca58cd"]')

    continue_like_guest = WebElement(xpath='//button[@class="b_2AMPZ4ui7z b_3CFK95wJ78 b_2ZBikcORqH b_390_8UTRcv"]')

    inscription_on_order_page = WebElement(xpath="//div[text()='Как доставить заказ?']")

    start_trade_page = WebElement(xpath='//a[@href="https://partner.market.yandex.ru/welcome/partners?utm_source=market&utm_medium=header&from=market"]')

































