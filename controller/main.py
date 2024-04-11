# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class QuizTimeSelector(http.Controller):

    @http.route('/get_idle_time/timer', auth='public', type='json')
    def get_idle_time(self):
        enable_idle = request.env['ir.config_parameter'].sudo().get_param(
            'quiz_idle_timer.enable_idle')
        if enable_idle:
            idle_time = request.env['ir.config_parameter'].sudo().get_param(
                'quiz_idle_timer.idle_time')
            idle_seconds = request.env['ir.config_parameter'].sudo().get_param(
                'quiz_idle_timer.idle_seconds')
            data = {'idle_time': idle_time, 'idle_seconds': idle_seconds}
            return data
        return False
