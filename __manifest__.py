# -*- coding: utf-8 -*-
{
    'name': "Quiz Idle Timer",
    'version': '17.0.1.0.0',
    'depends': ['base','survey'],
    'category': '',
    'description': """
    If mouse and keyboard are idle for particular time,timer should start
    """,
    'data': [
            'views/res_config_settings.xml',
            'views/survey_quiz.xml',
             ],
    'assets':{
        'survey.survey_assets': [
            'quiz_idle_timer/static/src/js/quiz_idle.js',
        ],
    },
    'application': 'True',
    'installable': True,
}