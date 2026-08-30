{
    'name': "Custom Website Block Demo",
    'summary': "Custom website block demo for the Odoo Experience 2026",
    'description': """
    Provides a snippet to display the weather forecast.
    Presents the features of interactions and options in the context of the website builder.
    """,
    'installable': True,

    'author': "ROLE & ALUP (Odoo)",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website/Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/snippets/snippets.xml',
        'views/snippets/s_weather.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'custom_website_block_demo/static/src/interactions/**/*',
            ('remove', 'custom_website_block_demo/static/src/interactions/**/*.edit.js'),
        ],
        'website.assets_inside_builder_iframe': [
            'custom_website_block_demo/static/src/**/*.edit.js',
        ],
        'website.website_builder_assets': [
            'custom_website_block_demo/static/src/builder/**/*',
        ],
    },
    'license': 'LGPL-3',
}
