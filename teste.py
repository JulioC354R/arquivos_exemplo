import svgwrite

# Create a new SVG drawing with the Roboto font and bold style
dwg_roboto = svgwrite.Drawing('multi_zap_roboto.svg', profile='tiny', size=(300, 100))

# Add text to the SVG using the Roboto font in bold
dwg_roboto.add(dwg_roboto.text('MultiZap', insert=(10, 50), fill='black', font_size='40', font_family='Roboto', font_weight='bold'))

# Save the new SVG file
roboto_svg_file_path = '/mnt/data/multi_zap_roboto.svg'
dwg_roboto.save()

roboto_svg_file_path
