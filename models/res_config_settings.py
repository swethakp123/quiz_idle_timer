# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_idle = fields.Boolean(string='Quiz Idle Time',
                                 store=True,
                                 config_parameter='quiz_idle_timer.enable_idle')
    idle_time = fields.Float(string="Idle Time",
                             store=True,
                             config_parameter='quiz_idle_timer.idle_time')

    idle_seconds = fields.Integer(string="Idle Time",
                                  store=True,
                                  config_parameter='quiz_idle_timer.idle_seconds')
