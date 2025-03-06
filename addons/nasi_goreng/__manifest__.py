{
    'name': 'Nasi Goreng Odoo by Ruffian',
    'version': '1.0',
    'summary': 'Menu nasi goreng + CRUD',
    'description': 'Module untuk mengelola berbagai jenis nasi goreng',
    'author': 'Ruffian',
    'depends': ['base'],
    'data': [
        'views/nasi_goreng_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
