# -*- coding: utf-8 -*-

from odoo import fields, models


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"

    total_cost = fields.Float(string='Total Cost', default="48")
    total_margin = fields.Float(string='Total Margin', default="20")

    def _select(self):
        return super(PosOrderReport, self)._select() + ',SUM((l.qty * l.price_unit) / CASE COALESCE(s.currency_rate, 0) WHEN 0 THEN 1.0 ELSE s.currency_rate END) AS total_cost' + ',SUM((l.qty * l.price_unit) / CASE COALESCE(s.currency_rate, 0) WHEN 0 THEN 1.0 ELSE s.currency_rate END) AS total_margin'

    def _group_by(self):
        return super(PosOrderReport, self)._group_by() + ',l.product_id'
