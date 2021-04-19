from pages.main import MainPage
import pytest


@pytest.mark.location
def test_geo_location(web_browser):
    """Make sure that location can be changed """
    page = MainPage(web_browser)
    page.location.click()
    page.input_location.send_keys("Краснодар")
    page.first_element_in_location.click()
    page.location_btn_success.click()
    page.wait_page_loaded(3)

    assert page.location.get_text() == "Краснодар"


@pytest.mark.pages
def test_pokupki_page(web_browser):
    """Make sure that page 'Покупки' works fine """
    page = MainPage(web_browser)
    page.pokupki.click()
    page.wait_page_loaded(3)

    assert 'https://pokupki.market.yandex.ru/' in page.get_current_url()


@pytest.mark.pages
def test_electronica_page(web_browser):
    """Make sure that page 'Электроника' works fine """
    page = MainPage(web_browser)
    page.elektronika.click()
    page.wait_page_loaded(3)

    assert 'https://market.yandex.ru/catalog--elektronika/54440' in page.get_current_url()
    assert page.h1.get_text() == 'Электроника'


@pytest.mark.pages
def test_dacha_i_sad_page(web_browser):
    """Make sure that page 'Дача и сад' works fine """
    page = MainPage(web_browser)
    page.dacha_i_sad.click()
    page.wait_page_loaded(3)

    assert 'https://market.yandex.ru/catalog--dacha-sad-i-ogorod/54495' in page.get_current_url()
    assert page.h1.get_text() == 'Дача и сад'


@pytest.mark.pages
def test_detskie_products_page(web_browser):
    """Make sure that page 'Детские товары' works fine """
    page = MainPage(web_browser)
    page.detskie_tovary.click()
    page.wait_page_loaded(3)

    assert 'https://market.yandex.ru/catalog--detskie-tovary/54421' in page.get_current_url()
    assert page.h1.get_text() == 'Детские товары'


@pytest.mark.pages
def test_products_drinks_page(web_browser):
    """Make sure that page 'Продукты питания' works fine """
    page = MainPage(web_browser)
    page.products_drinks.click()
    page.wait_page_loaded(3)

    assert 'https://market.yandex.ru/catalog--produkty-napitki/54434' in page.get_current_url()
    assert page.h1.get_text() == 'Продукты питания'


@pytest.mark.pages
def test_bytovaya_tekhnika_page(web_browser):
    """Make sure that page 'Бытовая техника' works fine """
    page = MainPage(web_browser)
    page.tehnica_bytovaia.click()
    page.wait_page_loaded(3)

    assert 'https://market.yandex.ru/catalog--bytovaia-tekhnika/54419' in page.get_current_url()
    assert page.h1.get_text() == 'Бытовая техника'


@pytest.mark.pages
def test_life_streams_page(web_browser):
    """Make sure that page 'Трансляции' works fine """
    page = MainPage(web_browser)
    page.live_streams.click()
    page.wait_page_loaded(3)

    assert 'https://market.yandex.ru/live' in page.get_current_url()


@pytest.mark.pages
def test_start_trade_page(web_browser):
    """Make sure that page 'Начать продавать на Маркете' works fine """
    page = MainPage(web_browser)
    page.start_trade_page.click()
    page.wait_page_loaded(3)

    assert 'https://partner.market.yandex.ru/welcome/partners' in page.get_current_url()


@pytest.mark.pages
def test_catalog_birds_products(web_browser):
    """Make sure that we can open this page from catalog """
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.zoo_products_catalog.click()
    page.birds_products.click()

    assert 'https://market.yandex.ru/catalog--tovary-dlia-ptits/62871' in page.get_current_url()
    assert page.h1.get_text() == 'Для птиц'


@pytest.mark.pages
def test_catalog_pokupki_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.pokupki_in_catalog.click()
    page.wait_page_loaded()

    assert 'https://pokupki.market.yandex.ru' in page.get_current_url()


@pytest.mark.pages
def test_catalog_uhod_za_litsom_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.beauty_in_catalog.click()
    page.uhod_za_litsom.click()

    assert 'https://market.yandex.ru/catalog--sredstva-po-ukhodu-za-litsom/17437151' in page.get_current_url()
    assert page.h1.get_text() == 'Уход за лицом'


@pytest.mark.pages
def test_catalog_gaming_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.computers_in_catalog.click()
    page.gaming_page.click()

    assert 'https://market.yandex.ru/catalog--tovary-dlia-geimerov/18072602' in page.get_current_url()
    assert page.h1.get_text() == 'Гейминг'


@pytest.mark.pages
def test_catalog_children_sport_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.sport_products_catalog.click()
    page.children_sport.click()

    assert 'https://market.yandex.ru/catalog--detskii-sport/18072403' in page.get_current_url()
    assert page.h1.get_text() == 'Детский спорт'


@pytest.mark.pages
def test_catalog_interior_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.house_catalog.click()
    page.interior.click()

    assert 'https://market.yandex.ru/catalog--domashnii-interer/54497' in page.get_current_url()
    assert page.h1.get_text() == 'Интерьер'


@pytest.mark.pages
def test_catalog_tables_chairs_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.furniture_catalog.click()
    page.tables_chairs.click()

    assert 'https://market.yandex.ru/catalog--stoly-i-stulia/18049598' in page.get_current_url()
    assert page.h1.get_text() == 'Столы и стулья'


@pytest.mark.pages
def test_catalog_electric_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.building_catalog.click()
    page.electric.click()

    assert 'https://market.yandex.ru/catalog--elektrika/55183' in page.get_current_url()
    assert page.h1.get_text() == 'Электрика'


@pytest.mark.pages
def test_catalog_clock_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.jewelery_catalog.click()
    page.clock.click()

    assert 'https://market.yandex.ru/catalog--chasy/18057688' in page.get_current_url()
    assert page.h1.get_text() == 'Наручные часы'


@pytest.mark.pages
def test_catalog_optics_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.health_catalog.click()
    page.optics.click()

    assert 'https://market.yandex.ru/catalog--optika/56064' in page.get_current_url()
    assert page.h1.get_text() == 'Контактные линзы и очки'


@pytest.mark.pages
def test_catalog_telescopes_microscopes_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.hobby_catalog.click()
    page.telescopes_microscopes.click()

    assert 'https://market.yandex.ru/catalog--teleskopy-i-mikroskopy/18071678' in page.get_current_url()
    assert page.h1.get_text() == 'Телескопы и микроскопы'


@pytest.mark.pages
def test_catalog_business_finance_books_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.books_catalog.click()
    page.business_finances.click()

    assert 'https://market.yandex.ru/catalog--biznes-i-finansy/19436490' in page.get_current_url()
    assert page.h1.get_text() == 'Бизнес и финансы'


@pytest.mark.pages
def test_catalog_school_suits_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.for_school_office_catalog.click()
    page.school_suits.click()

    assert 'https://market.yandex.ru/catalog--shkolnaia-odezhda-i-obuv/17985882' in page.get_current_url()
    assert page.h1.get_text() == 'Школьная одежда и обувь'


@pytest.mark.pages
def test_catalog_accessories_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.clothes_shoes_catalog.click()
    page.accessories.click()

    assert 'https://market.yandex.ru/catalog--aksessuary-i-ukrasheniia/54600' in page.get_current_url()
    assert page.h1.get_text() == 'Аксессуары и украшения'


@pytest.mark.pages
def test_catalog_building_equip_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.equipment_catalog.click()
    page.building_eqip.click()

    assert 'https://market.yandex.ru/catalog--stroitelnoe-oborudovanie/54592' in page.get_current_url()
    assert page.h1.get_text() == 'Строительное оборудование'


@pytest.mark.pages
def test_catalog_audio_video_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.car_products_catalog.click()
    page.audio_video.click()

    assert 'https://market.yandex.ru/catalog--avtomobilnaia-audio-i-videotekhnika/54455' in page.get_current_url()
    assert page.h1.get_text() == 'Автомобильная аудио- и видеотехника'


@pytest.mark.pages
def test_catalog_condoms_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.adult_products_catalog.click()
    page.condoms.click()

    assert 'https://market.yandex.ru/catalog--prezervativy/18019246' in page.get_current_url()
    assert page.h1.get_text() == 'Презервативы'


@pytest.mark.pages
def test_catalog_discount_auto_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.discount_catalog.click()
    page.auto_discount.click()

    assert 'https://market.yandex.ru/catalog--tovary-dlia-avto-i-mototekhniki/16801126' in page.get_current_url()
    assert page.h1.get_text() == 'Авто с уценкой'


@pytest.mark.pages
def test_catalog_sales_page(web_browser):
    """Make sure that we can open this page from catalog"""
    page = MainPage(web_browser)
    page.catalog_btn.click()
    page.wait_page_loaded(3)
    page.sales_catalog.click()

    assert 'https://market.yandex.ru/catalog--tovary-so-skidkoi/61522' in page.get_current_url()
    assert page.h1.get_text() == 'Скидки и акции'


@pytest.mark.pages
def test_scores_page(web_browser):
    """Make sure that we can open this page"""
    page = MainPage(web_browser)
    page.scores_page.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://plus.yandex.ru/' in page.get_current_url()


@pytest.mark.pages
def test_orders_page(web_browser):
    """Make sure that we can open this page"""
    page = MainPage(web_browser)
    page.orders_page.click()

    assert 'https://market.yandex.ru/my/orders' in page.get_current_url()
    assert page.h1.get_text() == 'Мои заказы'


@pytest.mark.pages
def test_wishlist_page(web_browser):
    """Make sure that we can open this page"""
    page = MainPage(web_browser)
    page.wishlist_page.click()

    assert 'https://market.yandex.ru/my/wishlist' in page.get_current_url()
    assert page.h1.get_text() == 'Избранное'


@pytest.mark.pages
def test_cart_page(web_browser):
    """Make sure that we can open this page"""
    page = MainPage(web_browser)
    page.cart_page.click()

    assert 'https://pokupki.market.yandex.ru/my/cart' in page.get_current_url()


@pytest.mark.sort
def test_check_sort_by_price(web_browser):
    """ Make sure that sort by price works fine

    NOTE: this function have a bug , test can be Failed"""

    page = MainPage(web_browser)
    page.search.send_keys("кружка")
    page.search_run_button.click()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    prices = page.products_prices.get_text()
    prices = [float(p.replace(' ', '')) for p in prices]

    assert prices == sorted(prices)


@pytest.mark.sort
def test_check_sort_by_default_popularity(web_browser):
    """ Make sure that sort by popularity by default value works fine"""
    page = MainPage(web_browser)
    page.search.send_keys("кружка")
    page.search_run_button.click()

    assert page.products_titles.count() > 0


@pytest.mark.sort
def test_check_sort_by_quality(web_browser):
    """ Make sure that sort by quality works fine"""
    page = MainPage(web_browser)
    page.search.send_keys("кружка")
    page.search_run_button.click()
    page.sort_products_by_quality.click()

    assert page.products_titles.count() > 0


@pytest.mark.sort
def test_check_sort_by_opinions(web_browser):
    """ Make sure that sort by opinions works fine"""
    page = MainPage(web_browser)
    page.search.send_keys("кружка")
    page.search_run_button.click()
    page.sort_products_by_opinions.click()

    assert page.products_titles.count() > 0


@pytest.mark.sort
def test_check_sort_by_discount(web_browser):
    """ Make sure that sort by discount works fine"""
    page = MainPage(web_browser)
    page.search.send_keys("кружка")
    page.search_run_button.click()
    page.sort_products_by_discount.click()

    assert page.products_titles.count() > 0


@pytest.mark.sort
def test_check_sort_by_date(web_browser):
    """ Make sure that sort by date works fine"""
    page = MainPage(web_browser)
    page.search.send_keys("кружка")
    page.search_run_button.click()
    page.sort_products_by_date.click()

    assert page.products_titles.count() > 0


@pytest.mark.search
def test_check_search(web_browser):
    """ Make sure main search works fine"""
    page = MainPage(web_browser)
    page.search.send_keys('iPhone 12')
    page.search_run_button.click()

    assert page.products_titles.count() > 0

    for title in page.products_titles.get_text():
        assert 'iphone' in title.lower()


@pytest.mark.search
def test_check_search_with_wrong_layout(web_browser):
    """ Make sure that wrong keyboard layout input works fine"""
    page = MainPage(web_browser)
    # Enter "смартфон" on english keyboard layout
    page.search.send_keys("cvfhnajy")
    page.search_run_button.click()

    assert page.products_titles.count() > 0

    for title in page.products_titles.get_text():
        assert 'смартфон' in title.lower()


@pytest.mark.search
def test_check_search_with_misprint(web_browser):
    """ Make sure that misprint input works fine"""
    page = MainPage(web_browser)
    # Enter "смартфон" with little misprint
    page.search.send_keys("смордфон")
    page.search_run_button.click()

    assert page.products_titles.count() > 0

    for title in page.products_titles.get_text():
        assert 'смартфон' in title.lower()


@pytest.mark.search
def test_check_search_with_incorrect_data(web_browser):
    """ Make sure that we got answer from website about our incorrect input"""
    page = MainPage(web_browser)
    # Enter incorrect data in search field
    page.search.send_keys("17adozzxss812")
    page.search_run_button.click()

    assert page.products_titles.count() < 1
    assert page.search_incorrect.get_text() == 'По вашему запросу ничего не найдено'


@pytest.mark.footer
def test_footer_choice_goods(web_browser):
    """Make sure that we can open this page in footer"""
    page = MainPage(web_browser)
    page.choice_goods_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://yandex.ru/support/market/choice-goods' in page.get_current_url()


@pytest.mark.footer
def test_footer_delivery(web_browser):
    """Make sure that we can open this page in footer"""
    page = MainPage(web_browser)
    page.pay_delivery_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://pokupki.market.yandex.ru/my/order/conditions' in page.get_current_url()
    assert page.h1.get_text() == "Доставка Яндекса"


@pytest.mark.footer
def test_footer_troubleshooting(web_browser):
    """Make sure that we can open this page in footer"""
    page = MainPage(web_browser)
    page.feedback_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://yandex.ru/support/market/troubleshooting' in page.get_current_url()
    assert page.h1.get_text() == "Решение проблем"


@pytest.mark.footer
def test_footer_about(web_browser):
    """Make sure that we can open this page in footer"""
    page = MainPage(web_browser)
    page.about_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://market.yandex.ru/about' in page.get_current_url()


@pytest.mark.footer
def test_footer_research_jobs(web_browser):
    """Make sure that we can open this page in footer"""
    page = MainPage(web_browser)
    page.research_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://yandex.ru/jobs/usability' in page.get_current_url()
    assert page.h2.get_text() == 'Исследования для пользователей'


@pytest.mark.footer
def test_footer_return(web_browser):
    """Make sure that we can open this page in footer"""
    page = MainPage(web_browser)
    page.return_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://yandex.ru/support/market/return' in page.get_current_url()
    assert page.h1.get_text() == 'Возврат товара'


@pytest.mark.footer
def test_footer_facebook(web_browser):
    """Make sure that we can open this page in footer"""
    page = MainPage(web_browser)
    page.facebook_footer.click()
    page.wait_page_loaded()

    assert 'https://www.facebook.com/yandex.market/' in page.get_current_url()


@pytest.mark.footer
def test_footer_vkontakte(web_browser):
    """Make sure that we can open this page in footer"""
    page = MainPage(web_browser)
    page.vk_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://vk.com/yandex.market' in page.get_current_url()


@pytest.mark.footer
def test_footer_instagram(web_browser):
    """Make sure that we can open this page in footer"""
    page = MainPage(web_browser)
    page.instagram_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[-1])
    page.wait_page_loaded()

    assert 'https://www.instagram.com/yandex.market/' in page.get_current_url()


@pytest.mark.cart
def test_add_new_item_in_cart_correctly(web_browser):
    """Make sure that we can add new item in my cart"""
    page = MainPage(web_browser)
    page.search.send_keys("кружка")
    page.search_run_button.click()
    page.add_in_cart_btn[1].click()
    page.wait_page_loaded()
    page.go_to_cart_after_adding.click()
    page.wait_page_loaded()

    assert 'https://pokupki.market.yandex.ru/my/cart' in page.get_current_url()
    assert page.items_in_my_cart.count() > 0


@pytest.mark.cart
def test_delete_item_from_cart_correctly(web_browser):
    """Make sure that we can delete item from my cart"""
    page = MainPage(web_browser)
    page.search.send_keys("кружка")
    page.search_run_button.click()
    page.add_in_cart_btn[1].click()
    page.wait_page_loaded()
    page.go_to_cart_after_adding.click()
    page.wait_page_loaded()
    page.remove_item_from_cart[0].click()
    page.wait_page_loaded()

    assert page.items_in_my_cart.count() < 1
    assert 'https://pokupki.market.yandex.ru/my/cart' in page.get_current_url()


@pytest.mark.cart
def test_order_btn_works_correctly(web_browser):
    """Make sure that we can execute our order in cart"""
    page = MainPage(web_browser)
    page.search.send_keys("кружка")
    page.search_run_button.click()
    page.add_in_cart_btn[1].click()
    page.wait_page_loaded()
    page.go_to_cart_after_adding.click()
    page.wait_page_loaded()
    page.execute_btn_in_cart.click()
    page.continue_like_guest.click()
    page.wait_page_loaded()

    assert 'https://pokupki.market.yandex.ru/my/checkout' in page.get_current_url()
    assert page.inscription_on_order_page.get_text() == 'Как доставить заказ?'
