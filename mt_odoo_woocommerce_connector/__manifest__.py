# -*- coding: utf-8 -*-
# ############################################################################
#
#     Metclouds Technologies Pvt Ltd
#
#     Copyright (C) 2022-TODAY Metclouds Technologies(<https://metclouds.com>)
#     Author: Metclouds Technologies(<https://metclouds.com>)
#
#     You can modify it under the terms of the GNU LESSER
#     GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#     You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#     (LGPL v3) along with this program.
#     If not, see <http://www.gnu.org/licenses/>.
#
# ############################################################################

{
    'name': 'Odoo WooCommerce Connector',
    'summary': 'Odoo WooCommerce Connector',
    'version': '1.0.0',
    'sequence': 6,
    'description': """Odoo WooCommerce Connector""",    
    'author': 'Metclouds Technologies Pvt Ltd',
    'category': 'Sales',
    'maintainer': 'Metclouds Technologies Pvt Ltd',
    'website': 'https://www.metclouds.com',
    'license': 'LGPL-3',
    'depends': ['base', 'web', 'sale_management', 'purchase', 'stock', 'contacts', 'delivery', 'hr_expense'],
    'external_dependencies': {
        'python': ['woocommerce'],
    },
    'data': [ 
        'security/ir.model.access.csv',
        'wizard/product_instance.xml',
        'wizard/sale_order_instance.xml',
        'wizard/customer_import.xml',
        'wizard/product_attribute_instance.xml',
        'wizard/product_category_instance.xml',
        'wizard/tax_instance.xml',
        'wizard/generate_refund.xml',
        'wizard/generate_invoice.xml',
        'wizard/woocomm_order_actions.xml',
        'wizard/shipping_method.xml',        
        'wizard/stock_quantity.xml',        
        'wizard/message_wizard.xml',
        'view/woocommerce_instances.xml',
        'view/woocommerce_product.xml',
        'view/woocommerce_sale_order.xml',
        'view/woocommerce_product_variants.xml',
        'view/woocommerce_attribute.xml',
        'view/woocommerce_customer.xml',
        'view/woocommerce_tax.xml',
        'view/woocommerce_product_category.xml',
        'view/woocommerce_refund.xml',
        'view/woocommerce_images.xml',
        'view/woocommerce_delivery.xml',
        'view/menu.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'mt_odoo_woocommerce_connector/static/src/scss/mt_woo_graph_widget.scss',
            'mt_odoo_woocommerce_connector/static/src/**/*.js',
            'mt_odoo_woocommerce_connector/static/src/**/*.xml',             
        ],
    },    
}
