# Copyright <2023> Toni Gil - antonio.gil@hilltech.es
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Toni Gil",
    "summary": "Gestión de incidencias para el curso Aeodoo",
    "version": "16.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://aeodoo.org",
    "author": "Hilltech, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml"
    ],
}