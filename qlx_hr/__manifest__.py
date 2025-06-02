# -*- coding: utf-8 -*-
{
    "name": "Qualix - HR",
    "description": "Qualix - HR customizations",
    "sequence": 10,
    "version": "1.0",
    "depends": [
        "hr",
        "hr_skills",
        'analytic',
        "hr_timesheet",
        'timesheet_grid',
        'gamification',
        ],
    "data": [
        "views/employee.xml",
        "views/timesheet.xml",
        "views/resume_tab.xml",
        "views/badges_tab.xml",
    ],
    "installable" : True,
    "application" : False,
}
