# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'fpinformatica.alumno'
    _description = 'Alumno de FP'

    name = fields.Char(string="Nombre", required=True)
    surname = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True)
    birth_date = fields.Date(string="Fecha de nacimiento", required=True)
    academic_year = fields.Char(string="Curso académico", default="23/24")
    email = fields.Char(string="Correo electrónico")
    phone = fields.Char(string="Teléfono")
    
    cycle = fields.Selection([
        ('DAM', 'DAM'), ('DAW', 'DAW'), ('ASIR', 'ASIR'), 
        ('SMR', 'SMR'), ('DUAL', 'DUAL')
    ], string="Ciclo Formativo", required=True)

    period = fields.Selection([
        ('abril', 'Abril'), ('septiembre', 'Septiembre')
    ], string="Periodo de práctica", required=True)

    # Notas
    grade = fields.Float(string="Nota numérica", required=True)
    grade_text = fields.Char(string="Nota texto", compute="_compute_grade_text", store=True)

    # Relación con empresa
    company_id = fields.Many2one('fpinformatica.empresa', string="Empresa FCT")

    @api.depends('grade')
    def _compute_grade_text(self):
        for record in self:
            if 5 <= record.grade < 7:
                record.grade_text = "Aprobado"
            elif 7 <= record.grade < 9:
                record.grade_text = "Notable"
            elif 9 <= record.grade <= 10:
                record.grade_text = "Sobresaliente"
            else:
                record.grade_text = "Suspenso o Sin Calificar"