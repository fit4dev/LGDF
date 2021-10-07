# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_margin = fields.Float(string='Margin %', translate=True, compute='_compute_product_margin')

    def _compute_product_margin(self):
        self.product_margin = ((self.list_price - self.standard_price) / self.standard_price)
