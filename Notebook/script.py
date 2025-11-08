# script.py
import subprocess

# Exportar notebook a HTML
subprocess.run([
    'jupyter', 'nbconvert', 
    '--to', 'html', 
    'Notebook/EDA.ipynb'
])

