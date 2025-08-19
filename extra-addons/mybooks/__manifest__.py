# -*- coding: utf-8 -*-
{
    "name": "mon-livre",
    "summary": "Gestion des livres module Devs",
    "description": """
Gestion des livres avec code à barre et gestion mobile de la bilbiotheque
    """,
    "author": "Nabi Lyes",
    "website": "https://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base", "mail","sale"],
    "data": [
        'security/ir.model.access.csv',
        "views/menus.xml",
        "views/books.xml",
        "reports/book_report.xml",
        "views/sale_order_custom.xml",
        #'views/views.xml',
        #'views/templates.xml',
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "auto_install": True,
}
