
# Table of Contents

1.  [Что было сделано](#orgb5e7ff4)
2.  [Пример работы](#org79bac53)



<a id="orgb5e7ff4"></a>

# Что было сделано

-   Добавлены поля в вывод
-   Сделан вывод в таблицу
-   Добавлены тесты и документация
-   Реализован сбор новостей


<a id="org79bac53"></a>

# Пример работы
```bash
    make all
```
```
    docker compose run --workdir / app /bin/bash -c "black src docs/source/*.py; isort --profile black src/*.py docs/source/*.py"
    docker compose run --workdir / app /bin/bash -c "pylint src; flake8 src; mypy src; black --check src"
    
    ------------------------------------
    Your code has been rated at 10.00/10
    
    Success: no issues found in 16 source files
    docker compose run app pytest --cov=/src --cov-report html:htmlcov --cov-report term --cov-config=/src/tests/.coveragerc -vv
    ============================= test session starts ==============================
    platform linux -- Python 3.10.8, pytest-7.1.3, pluggy-1.0.0 -- /usr/local/bin/python
    cachedir: .pytest_cache
    rootdir: /, configfile: pytest.ini
    plugins: anyio-3.6.2, cov-3.0.0, mock-3.8.2, aiohttp-1.0.4, asyncio-0.20.3
    asyncio: mode=auto
    collecting ... collected 29 items
    
    tests/test_reader.py::TestReader::test_find PASSED                       [  3%]
    tests/test_reader.py::TestReader::test_find_not_found PASSED             [  6%]
    tests/test_reader.py::TestReader::test_get_weather PASSED                [ 10%]
    tests/test_reader.py::TestReader::test_get_news PASSED                   [ 13%]
    tests/test_reader.py::TestReader::test_find_country PASSED               [ 17%]
    tests/test_reader.py::TestReader::test_find_country_none PASSED          [ 20%]
    tests/test_renderer.py::TestRenderer::test_render PASSED                 [ 24%]
    tests/test_renderer.py::TestRenderer::test_format_languages PASSED       [ 27%]
    tests/test_renderer.py::TestRenderer::test_format_currencies_rates PASSED [ 31%]
    tests/test_renderer.py::TestRenderer::test_format_news PASSED            [ 34%]
    tests/test_renderer.py::TestRenderer::test_format_population PASSED      [ 37%]
    tests/test_renderer.py::TestRenderer::test_format_news_line PASSED       [ 41%]
    tests/test_renderer.py::TestRenderer::test_format_news_line_long PASSED  [ 44%]
    tests/clients/test_country.py::TestClientCountry::test_get_base_url PASSED [ 48%]
    tests/clients/test_country.py::TestClientCountry::test_get_countries PASSED [ 51%]
    tests/clients/test_currency.py::TestClientCountry::test_get_base_url PASSED [ 55%]
    tests/clients/test_currency.py::TestClientCountry::test_get_countries PASSED [ 58%]
    tests/clients/test_news.py::TestClientCountry::test_get_base_url PASSED  [ 62%]
    tests/clients/test_news.py::TestClientCountry::test_get_countries PASSED [ 65%]
    tests/clients/test_weather.py::TestClientCountry::test_get_base_url PASSED [ 68%]
    tests/clients/test_weather.py::TestClientCountry::test_get_countries PASSED [ 72%]
    tests/collectors/test_country.py::TestCountryCollector::test_collect_country_success PASSED [ 75%]
    tests/collectors/test_country.py::TestCountryCollector::test_read_country_success PASSED [ 79%]
    tests/collectors/test_currency.py::TestCurrencyCollector::test_collect_currency_success PASSED [ 82%]
    tests/collectors/test_currency.py::TestCurrencyCollector::test_read_currency_success PASSED [ 86%]
    tests/collectors/test_news.py::TestClientNews::test_collect_news_success PASSED [ 89%]
    tests/collectors/test_news.py::TestClientNews::test_read_news_success PASSED [ 93%]
    tests/collectors/test_weather.py::TestWeatherCollector::test_collect_weather_success PASSED [ 96%]
    tests/collectors/test_weather.py::TestWeatherCollector::test_read_weather_success PASSED [100%]
    
    ---------- coverage: platform linux, python 3.10.8-final-0 -----------
    Name                                Stmts   Miss Branch BrPart  Cover
    ---------------------------------------------------------------------
    clients/__init__.py                     0      0      0      0   100%
    clients/base.py                        19      6      6      0    52%
    clients/country.py                      8      0      0      0   100%
    clients/currency.py                     9      0      0      0   100%
    clients/news.py                         9      0      0      0   100%
    clients/weather.py                      9      0      0      0   100%
    collect.py                              2      2      0      0     0%
    collectors/__init__.py                  0      0      0      0   100%
    collectors/base.py                     23      7      2      0    64%
    collectors/collector.py               149     42     58     11    67%
    collectors/models.py                   52      0      0      0   100%
    logger.py                              10      1      0      0    90%
    main.py                                12     12      4      0     0%
    reader.py                              41      0     19      3    95%
    renderer.py                            35      1     18      1    96%
    settings.py                            13      0      0      0   100%
    tests/__init__.py                       2      0      0      0   100%
    tests/clients/__init__.py               0      0      0      0   100%
    tests/clients/test_country.py          15      0      0      0   100%
    tests/clients/test_currency.py         17      0      0      0   100%
    tests/clients/test_news.py             14      0      0      0   100%
    tests/clients/test_weather.py          14      0      0      0   100%
    tests/collectors/__init__.py            0      0      0      0   100%
    tests/collectors/conftest.py            8      0      0      0   100%
    tests/collectors/test_country.py       12      0      0      0   100%
    tests/collectors/test_currency.py      13      0      0      0   100%
    tests/collectors/test_news.py          14      0      2      0   100%
    tests/collectors/test_weather.py       14      0      0      0   100%
    tests/conftest.py                       0      0      0      0   100%
    tests/test_reader.py                   46      0      0      0   100%
    tests/test_renderer.py                 49      0      8      0   100%
    ---------------------------------------------------------------------
    TOTAL                                 609     71    117     15    84%
    Coverage HTML written to dir htmlcov
    
    
    ============================== 29 passed in 0.54s ==============================
```
```bash
    docker compose run app python main.py --location London
```
```
    -------------------------------------------------------------------------
    |Страна           | United Kingdom of Great Britain and Northern Ireland|
    |Регион           |                                      Northern Europe|
    |Языки            |                                    English (English)|
    |Население страны |                                           65.110.000|
    |Курсы валют      |                                     GBP = 86.46 руб.|
    |Площадь          |                                             242900.0|
    |Столица          |                                               London|
    |Широта           |                                                 54.0|
    |Долгота          |                                                 -2.0|
    |Время            |                                     09.02.2023 07:06|
    |Часовой пояс     |                                                    0|
    |Погода           |                                                 2.48|
    |Описание погоды  |                                      overcast clouds|
    |Видимость        |                                                10000|
    |Влажность        |                                                   91|
    |Скорость ветра   |                                                  3.6|
    |Давление         |                                                 1030|
    -------------------------------------------------------------------------
    |Источник         |                                             BBC News|
    |Новость          |Lloyd's of London boss warns UK's financial reputatio|
    |                 |n is dented                                          |
    |Ссылка           |         https://www.bbc.co.uk/news/business-64553955|
    |Дата             |                                     08.02.2023 00:01|
    |Описание         |The UK must prove its stability after a year of polit|
    |                 |ical and market turbulence, says the Lloyd's of Londo|
    |                 |n boss.                                              |
    |Текст            |The UK's reputation for financial stability was dente|
    |                 |d by a year of political turmoil, says the boss of in|
    |                 |surance giant Lloyd's of London.  John Neal said conf|
    |                 |idence in the UK had been hit by a high … [+4903 char|
    |                 |s]                                                   |
    -------------------------------------------------------------------------
    |Источник         |                                                  CNN|
    |Новость          |'You People' Jonah Hill and Lauren London kiss faked,|
    |                 | costar says                                         |
    |Ссылка           |https://www.cnn.com/2023/02/08/entertainment/jonah-hi|
    |                 |ll-lauren-london-kiss/index.html                     |
    |Дата             |                                     08.02.2023 16:56|
    |Описание         |Did Jonah Hill and Lauran London really kiss in "You |
    |                 |People?"                                             |
    |Текст            |Did Jonah Hill and Lauran London really kiss in You P|
    |                 |eople?  Their costar Andrew Schulz recently claimed o|
    |                 |n his podcast The Brilliant Idiots with his cohost Ch|
    |                 |arlamagne Tha God that the two costars d… [+1157 char|
    |                 |s]                                                   |
    -------------------------------------------------------------------------
    |Источник         |                                          Gizmodo.com|
    |Новость          |Uranium Found at London Heathrow Airport Poses 'No Th|
    |                 |reat,' Police Say                                    |
    |Ссылка           |https://gizmodo.com/uranium-found-at-london-heathrow-|
    |                 |airport-in-december-1849976147                       |
    |Дата             |                                     11.01.2023 19:37|
    |Описание         |Police reassured Heathrow Airport passengers on Tuesd|
    |                 |ay that there is no threat at the airport after borde|
    |                 |r patrol discovered small amounts of uranium in metal|
    |                 | bars shipped to the UK from Pakistan in late Decembe|
    |                 |r. Read more...                                      |
    |Текст            |Police reassured Heathrow Airport passengers on Tuesd|
    |                 |ay that there is no threat at the airport after borde|
    |                 |r patrol discovered small amounts of uranium in metal|
    |                 | bars shipped to the UK from Pakistan in… [+2409 char|
    |                 |s]                                                   |
    -------------------------------------------------------------------------
```
