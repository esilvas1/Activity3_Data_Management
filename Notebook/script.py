import subprocess
import os
import webbrowser
from pathlib import Path

print("🔄 Iniciando conversión del notebook...")

# Convertir a HTML (funciona bien)
print("\n1️⃣ Generando HTML...")
result_html = subprocess.run([
    'jupyter', 'nbconvert', 
    '--to', 'html', 
    'Notebook/EDA.ipynb'
])

if result_html.returncode == 0:
    print("✅ HTML generado exitosamente: Notebook/EDA.html")
    
    # Optimizar HTML para PDF
    print("\n2️⃣ Optimizando HTML para exportación a PDF...")
    html_file = Path("Notebook/EDA.html")
    html_content = html_file.read_text(encoding='utf-8')
    
    # CSS personalizado para evitar que el código se corte en PDF
    custom_css = """
    <style>
    @media print {
        /* Ajustar código para que no se corte */
        .jp-InputArea pre,
        .jp-OutputArea pre,
        .jp-RenderedText pre,
        pre code {
            white-space: pre-wrap !important;
            word-wrap: break-word !important;
            overflow-wrap: break-word !important;
            font-size: 9px !important;
            line-height: 1.2 !important;
        }
        
        /* Ajustar contenedores */
        .jp-Cell,
        .jp-InputArea,
        .jp-OutputArea {
            page-break-inside: avoid;
            max-width: 100% !important;
            overflow: visible !important;
        }
        
        /* Reducir padding */
        .jp-InputArea,
        .jp-OutputArea {
            padding: 3px !important;
        }
        
        /* Ajustar tablas */
        table {
            font-size: 8px !important;
            width: 100% !important;
        }
        
        /* Ajustar imágenes */
        img {
            max-width: 100% !important;
            height: auto !important;
            page-break-inside: avoid;
        }
        
        /* Márgenes de página */
        @page {
            margin: 1cm;
            size: A4;
        }
        
        body {
            margin: 0;
            padding: 10px;
        }
        
        /* Evitar que los gráficos se corten */
        .jp-RenderedImage {
            page-break-inside: avoid;
        }
    }
    
    /* También para visualización en pantalla */
    .jp-InputArea pre,
    .jp-OutputArea pre,
    .jp-RenderedText pre {
        white-space: pre-wrap;
        word-wrap: break-word;
        overflow-wrap: break-word;
        max-width: 100%;
    }
    </style>
    """
    
    # Insertar el CSS antes del cierre de </head>
    if '</head>' in html_content:
        html_content = html_content.replace('</head>', f'{custom_css}\n</head>')
    
    # Guardar el HTML modificado
    html_file.write_text(html_content, encoding='utf-8')
    print("✅ HTML optimizado - el código Python ahora se ajustará automáticamente")
    
    html_path = os.path.abspath("Notebook/EDA.html")
    print(f"📂 Ruta: {html_path}")
else:
    print("❌ Error al generar HTML")
    exit(1)

# Abrir HTML en el navegador para imprimir como PDF
print("\n📄 Para generar PDF (el código ya NO se cortará):")
print("   1. Abriendo el HTML optimizado en tu navegador...")
print("   2. Presiona Ctrl+P (o Cmd+P en Mac)")
print("   3. Configura:")
print("      - Destino: 'Guardar como PDF'")
print("      - Márgenes: Predeterminados")
print("   4. Haz clic en 'Guardar'")

webbrowser.open(f'file:///{html_path}')

print("\n✅ Proceso completado exitosamente")
print("✨ El código Python se ajustará automáticamente en el PDF")
