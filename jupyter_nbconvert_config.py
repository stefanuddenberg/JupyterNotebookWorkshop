c = get_config()
c.Exporter.preprocessors = ['pre_pymarkdown.PyMarkdownPreprocessor'] # new from SU -- 10-19-2017
#Export all the notebooks in the current directory to the sphinx_howto format.
c.NbConvertApp.notebooks = ['notebook1.ipynb']
c.NbConvertApp.export_format = 'python'

