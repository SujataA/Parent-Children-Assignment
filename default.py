# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import cStringIO

class CSVExporter(object):
    file_ext = "csv"
    content_type = "text/csv"

    def __init__(self, rows):
        self.rows = rows

    def export(self):
        if self.rows:
            s = cStringIO.StringIO()
            self.rows.export_to_csv_file(s, represent=True)
            return s.getvalue()
        else:
            return ''

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


def pc_report():
    query = ((db.children.mother == db.parent.id) and (db.children.father == db.parent.id))
    grid = SQLFORM.grid(db.children, orderby=[db.children.id],
                        csv=True, exportclasses=dict(csv=(CSVExporter, 'CSV')),
                        fields=[db.children.id, db.children.name, db.children.mother, db.children.father])
    return dict(grid=grid)          



