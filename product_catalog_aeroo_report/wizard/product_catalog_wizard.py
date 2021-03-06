# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, api, models


class ProductCatalog(models.TransientModel):
    _name = 'product_catalog'
    _description = 'Wizard to generate the Product Catalog Report with Aeroo'

    product_catalog_report_id = fields.Many2one(
        'product.product_catalog_report',
        'Product Catalog',
        required=True
    )
    taxes_included = fields.Boolean(
        'Taxes Included',
    )
    use_planned_price = fields.Boolean(
        string='Use Planned Price',
        help="Use planned price instead of list price (if planned price module"
        " is not installed, nothing is going to change)")

    @api.onchange('product_catalog_report_id')
    def change_product_catalog_report(self):
        self.taxes_included = self.product_catalog_report_id.taxes_included

    @api.multi
    def generate_report(self):
        self.ensure_one()
        return self.product_catalog_report_id.with_context(
            taxes_included=self.taxes_included,
            use_planned_price=self.use_planned_price).generate_report()
