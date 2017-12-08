# -*- coding: utf-8 -*-
{
    'name': "Ayhrras Custom Sales Report",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','purchase','report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/report_delivery.xml',
        'views/report_invoice.xml',
        'views/header_footer_inherit.xml',
        'views/custom_sales_reports_report.xml',
        'views/report_charge_invoice.xml',
        'views/report_collection.xml',
        'views/report_charge_invoice_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}