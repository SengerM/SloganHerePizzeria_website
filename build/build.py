import dominate # https://github.com/Knio/dominate
import dominate.tags as tags
from pathlib import Path

def build_navigation_menu(pages:dict):
	with tags.nav():
		for fname, page_data in pages.items():
			tags.a(page_data['title'], href=fname)

def build_page(page_title:str, content_generator:callable, pages:dict):
	doc = dominate.document(title=page_title)
	
	with doc.head:
		tags.link(rel='stylesheet', href='css/main.css')
		tags.link(rel="preconnect", href="https://fonts.googleapis.com")
		tags.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True)
		tags.link(href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap", rel="stylesheet")
		tags.meta(content="width=device-width, initial-scale=1", name="viewport")
	
	with doc.body:
		with tags.header(id='page_header'):
			with tags.div(id='logo_container', style='height: 222px; display: flex; justify-content: center;'):
				with tags.a(href='index.html'):
					tags.img(
						src = 'https://thumbs.dreamstime.com/b/italian-pizza-restaurant-design-logo-symbols-food-drink-restaurants-italian-pizza-restaurant-design-logo-symbols-210928159.jpg',
						alt = 'Logo',
						style = 'object-fit: contain; height: 100%;',
					)
			build_navigation_menu(pages=pages)
			
		with tags.div(id='page_content'):
			content_generator()
			
			SOCIAL_NETWORKS = {
				'instagram': {
					'img': {
						'src': 'https://cdn-icons-png.flaticon.com/512/1384/1384031.png',
					},
				},
				'facebook': {
					'img': {
						'src': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Facebook_icon_%28black%29.svg/1200px-Facebook_icon_%28black%29.svg.png',
					},
				},
				'tick tock': {
					'img': {
						'src': 'https://cdn-icons-png.flaticon.com/512/3938/3938074.png',
					},
				},
			}
			
			with tags.footer(id='page_footer', style='margin: 55px 0 55px 0; display: flex; flex-direction: column; align-items: center; gap: 22px; flex-wrap: wrap;'):
				tags.div('© Pizza Paradiso 2023', style='flex-shrink: 0;')
				with tags.div(style='display: flex; flex-direction: row; gap: 22px; flex-wrap: wrap;'):
					for name,data in SOCIAL_NETWORKS.items():
						tags.img(
							src = data['img']['src'],
							style = 'filter: invert(1) opacity(.8); height: 22px;',
							title = name,
						)
				
				with tags.div(style='display: flex; flex-wrap: wrap; gap: 5px;'):
					tags.div('Cotizaciones divisas al día de la fecha')
					with tags.span(style='display: flex; flex-direction: row; gap: 5px; flex-wrap: wrap;'):
						for moneda in ['USD','BRL','EUR']:
							with tags.div(style='flex-shrink: 0;'):
								tags.span('●')
								tags.span(id=f'precio_{moneda}', 'cargando...')
								tags.span(f'ARS/{moneda}')
		
		tags.script(src='js/divisas.js')
	return doc

def generate_home():
	tags.h1('Un lugar distinto')
	
	tags.p('Sumérjase en una experiencia culinaria sin igual, donde la tradición italiana se fusiona con la elegancia contemporánea. Nuestro compromiso es ofrecer a nuestros distinguidos comensales una deliciosa sinfonía de sabores, ingredientes frescos y una presentación impecable en cada bocado. Desde las exquisitas recetas de nuestras pizzas artesanales hasta el servicio impecable en un entorno sofisticado, "Slogan Here" es el lugar donde los amantes de la buena comida se reúnen para disfrutar de la auténtica excelencia gastronómica. Bienvenidos a un viaje gastronómico que deleitará sus sentidos y elevará sus expectativas.')
	
	tags.img(
		src = 'https://www.coastlinenservices.com/wp-content/uploads/2019/07/shutterstock_741884605.jpg',
		style = 'width: 100%; max-height: 88vh; border-radius: 11px;',
	)

def generate_menu():
	tags.h1('Menu')
	
	MENU_ITEMS = [
		dict(
			img_src = 'https://www.indianhealthyrecipes.com/wp-content/uploads/2015/10/pizza-recipe-1.jpg',
			name = 'Pizza arcoiris',
			description = 'Grande de muzza con morrones de colores diversos, aceitunas negras y salsa de tomate.',
		),
		dict(
			img_src = 'https://upload.wikimedia.org/wikipedia/commons/9/91/Pizza-3007395.jpg',
			name = 'Paradisíaca',
			description = 'Grande de muzza con morrones, cebollas, aceitunas negras y salsa de tomate.',
		),
		dict(
			img_src = 'https://www.allrecipes.com/thmb/iXKYAl17eIEnvhLtb4WxM7wKqTc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/240376-homemade-pepperoni-pizza-Beauty-3x4-1-6ae54059c23348b3b9a703b6a3067a44.jpg',
			name = 'Calabrese',
			description = 'Grande de muzza con salame picante y queso gratinado.',
		),
		dict(
			img_src = 'https://www.allrecipes.com/thmb/fFW1o307WSqFFYQ3-QXYVpnFj6E=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/48727-Mikes-homemade-pizza-DDMFS-beauty-4x3-BG-2974-a7a9842c14e34ca699f3b7d7143256cf.jpg',
			name = 'Márgara',
			description = 'Grande de muzza con tomate y albahacas.',
		),
		dict(
			img_src = 'https://hips.hearstapps.com/hmg-prod/images/classic-cheese-pizza-recipe-2-64429a0cb408b.jpg?crop=0.6666666666666667xw:1xh;center,top&resize=1200:*',
			name = 'Margarita',
			description = 'La clásica pizza margarita.',
		),
		dict(
			img_src = 'https://www.recipetineats.com/wp-content/uploads/2020/05/Pepperoni-Pizza_5-SQjpg.jpg',
			name = 'Calabrota',
			description = 'Es como nuestra calabresa, pero más cargadota!',
		),
		dict(
			img_src = 'https://www.deliciousmagazine.co.uk/wp-content/uploads/2023/03/960-2023D031_MIED_PIZZA.jpg',
			name = 'Vegetariana',
			description = 'Pizza vegetariana con forma de huevo frito.',
		),
	]
	
	with tags.div(style='display: flex; flex-direction: row; gap: 22px; flex-wrap: wrap;'):
		for item in MENU_ITEMS:
			with tags.div(style='display: flex; flex-direction: column; gap: 5px; width: 30%; min-width: 222px;'):
				tags.span(
					item['name'],
					style = 'font-weight: bold; font-size: 155%;',
				)
				tags.p(item['description'])
				tags.img(
					src = item['img_src'],
					style = 'width: 88%; border-radius: 11px;',
				)

def generate_contacto():
	tags.h1('Contacto')

def generate_nosotros():
	tags.h1('Nosotros')
	
	with tags.div(style = 'width: 100%; height: 77vh;'):
		tags.img(
			src = 'https://d3h1lg3ksw6i6b.cloudfront.net/media/image/2021/07/08/490b92922df3407cb5b91d3122a43579_Pavillon-Ledoyen.jpg',
			style = 'width: 100%; height: 100%; object-fit: contain; overflow: hidden; border-radius: 11px;',
		)
	
	tags.p('La pizzería de lujo Slogan Here es un auténtico oasis culinario para los amantes de la pizza que buscan una experiencia gastronómica excepcional. Ubicada en el corazón de la ciudad, este elegante establecimiento irradia sofisticación desde el momento en que cruzas su umbral. El ambiente es una mezcla perfecta de modernidad y tradición italiana, con techos altos, iluminación tenue y una decoración que rinde homenaje a las raíces italianas de la pizzería. Cada detalle ha sido cuidadosamente diseñado para ofrecer a los comensales una sensación de lujo inigualable.')
	
	tags.p('La excelencia de La Dolce Piazza se refleja en su carta de pizzas gourmet, con ingredientes de la más alta calidad procedentes de Italia y una atención meticulosa al proceso de preparación. Los comensales pueden disfrutar de pizzas artesanales únicas, como la "Pizza Trufa Supreme", que combina trufa negra fresca, queso mozzarella de bufala y una salsa de tomate casera. Además, la extensa carta de vinos ofrece una selección impresionante de etiquetas italianas y otras opciones internacionales, cuidadosamente elegidas para maridar a la perfección con cada pizza.')

	tags.p('El servicio impecable en La Dolce Piazza es otra característica distintiva de esta pizzería de lujo. El personal altamente capacitado y atento está siempre disponible para asesorar a los clientes en la elección de platos y vinos, brindando una experiencia gastronómica personalizada. En resumen, La Dolce Piazza es el destino ideal para aquellos que buscan deleitarse con la pizza de la más alta calidad en un entorno lujoso y elegante, donde cada visita se convierte en un festín culinario inolvidable.')
			

if __name__ == '__main__':
	PAGES = {
		'index.html': {
			'title': 'Home',
			'content_generator': generate_home,
		},
		'menu.html': {
			'title': 'Menu',
			'content_generator': generate_menu,
		},
		'contacto.html': {
			'title': 'Contacto',
			'content_generator': generate_contacto,
		},
		'nosotros.html': {
			'title': 'Nosotros',
			'content_generator': generate_nosotros,
		},
	}

	for fname, page_data in PAGES.items():
		page = build_page(
			page_title = page_data['title'],
			content_generator = page_data['content_generator'],
			pages = PAGES,
		)
		with open(Path(__file__).parent.parent/fname, 'w') as ofile:
			print(page, file=ofile)
