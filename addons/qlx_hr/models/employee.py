# -*- coding: utf-8 -*-

from odoo import fields, models, api


class QualixHrEmployee(models.Model):
    _name = "hr.employee"
    _inherit = "hr.employee"

    start_date = fields.Date(string="Start Date", groups="hr.group_hr_user")
    end_date = fields.Date(string="End Date", groups="hr.group_hr_user") 
    trial_period = fields.Integer(string="Trial Period (Days)", help="Duration of the trial period in days", groups="hr.group_hr_user")
    trial_end_date = fields.Date(string="Trial End Date", compute='_compute_trial_end_date', store=True, groups="hr.group_hr_user")
    
    @api.depends('start_date', 'trial_period')
    def _compute_trial_end_date(self):
        for record in self:
            if record.start_date and record.trial_period:
                # Si on a une date de début et une période d'essai, on calcule la fin de la période d'essai
                record.trial_end_date = fields.Date.add(record.start_date, days=record.trial_period)
            else:
                record.trial_end_date = False  # Si l'un des champs est vide, la date de fin est vide

class QualixHrResumeLine(models.Model):
    _name = "hr.resume.line"
    _inherit = "hr.resume.line"

    establishment = fields.Char(string="Establishment", groups="hr.group_hr_user")

