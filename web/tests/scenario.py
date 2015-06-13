# -*- encoding: utf-8 -*-
from block.models import (
    Page,
    PageSection,
    Section,
)

from web.models import PAGE_HOME


def _init_main_section():
    return Section.objects.init_section(
        'main',
        'Main',
        'web',
        'Main',
        'web.main.create',
    )


def init_app_web():
    section_main = _init_main_section()
    home = Page.objects.init_page(
        PAGE_HOME,
        '',
        PAGE_HOME.capitalize(),
        0,
        'web/home_list.html',
        is_home=True
    )
    PageSection.objects.init_page_section(home, section_main)
    portfolio = Page.objects.init_page(
        'portfolio',
        '',
        'Portfolio',
        1,
        'web/portfolio_list.html',
    )
    PageSection.objects.init_page_section(portfolio, section_main)
    technology = Page.objects.init_page(
        'technology',
        '',
        'Technology',
        2,
        'web/technology_list.html',
    )
    PageSection.objects.init_page_section(technology, section_main)
    contact = Page.objects.init_page(
        'contact',
        '',
        'Contact',
        3,
        'web/contact_list.html',
    )
    PageSection.objects.init_page_section(contact, section_main)
