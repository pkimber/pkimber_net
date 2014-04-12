from block.service import (
    init_page,
    init_page_section,
    init_section,
)

from web.models import PAGE_HOME


def _create_page(page_name, page_num, template_name, is_home):
    return init_page(
        page_name.capitalize(),
        page_num,
        template_name=template_name,
        is_home=is_home,
    )
    return page


def _create_main_section():
    return init_section(
        'main'.capitalize(),
        'web',
        'Main',
        'web.main.create',
    )


def init_app_web():
    section_main = _create_main_section()
    home = _create_page(PAGE_HOME, 0, 'web/home_list.html', True)
    init_page_section(home, section_main)
    portfolio = _create_page('Portfolio', 1, 'web/portfolio_list.html', False)
    init_page_section(portfolio, section_main)
    technology = _create_page('Technology', 2, 'web/technology_list.html', False)
    init_page_section(technology, section_main)
    contact = _create_page('Contact', 3, 'web/contact_list.html', False)
    init_page_section(contact, section_main)