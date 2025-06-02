# -*- coding: utf-8 -*-

from odoo import fields, models, api


class QualixHrTimesheet(models.Model):
    _name = "account.analytic.line"
    _inherit = "account.analytic.line"

    hourly_cost = fields.Monetary(
        store = True,
        readonly = True,
        compute = "_compute_hourly_cost",
        groups="hr.group_hr_user"
    )
    
    @api.depends('employee_id', 'unit_amount')
    def _compute_hourly_cost(self):
        for record in self:
            if record.employee_id:
                if record.employee_id.hourly_cost:
                    if not record.hourly_cost:
                        record['hourly_cost'] = record.employee_id.hourly_cost

                    record['amount'] = record.hourly_cost * record.unit_amount
