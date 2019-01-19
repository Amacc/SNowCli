
author = 'adam McChesney'
copyright = '2018, Adam Mcchesney'
description = 'Just playing around with ***REMOVED*** commands'
exclude_patterns = ['_build','**/venv']
html_theme = 'sphinx_rtd_theme'
htmlhelp_basename = 'SnowCli'
master_doc= 'index'
project = 'snow***REMOVED***'
project_short_name ='snow***REMOVED***'
pygments_style = 'sphinx'
todo_include_todos = True
todo_link_only = True
latex_elements = {}
latex_documents = [
    (master_doc, f'{project_short_name}.tex', project,
     author, 'manual'),
]
man_pages = [
    (master_doc, project_short_name, project,
     [author], 1)
]
texinfo_documents = [
    (master_doc, project_short_name, project,
     author, project_short_name, description,
     'Miscellaneous'),
]
intersphinx_mapping = {'https://docs.python.org/': None}
