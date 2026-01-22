# -*- coding: utf-8 -*-
{
    'name': "FPINFORAMATICA",
    'summary': "Gestión de prácticas FCT (Alumnos y Empresas)",
    'description': "Módulo para gestionar la asignación de alumnos de FP a empresas.",
    'author': "Grupo DAM2",
    'website': "https://www.tusitio.com",
    'category': 'Education',
    'version': '0.1',

    # Módulos necesarios para que este funcione
    'depends': ['base'],

    # Lista de archivos a cargar (EL ORDEN IMPORTA)
    'data': [
        'security/security.xml',          # 1. Primero los grupos
        'security/ir.model.access.csv',   # 2. Luego los permisos
        'views/menus.xml',                # 3. Definición de acciones y menús
        'views/empresa_views.xml',        # 4. Vistas de empresa
        'views/alumno_views.xml',         # 5. Vistas de alumno
        'reports/report_fct.xml',         # 6. Informes
    ],
    
    'application': True,
    'installable': True,
}