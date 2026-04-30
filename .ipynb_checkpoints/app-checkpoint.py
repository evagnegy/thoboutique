import panel as pn
import random


pn.extension(design="material") #needed to insure background is white (against dark mode of py.cafe or just my browser lol)
pn.extension('modal') #used for popups

#tracks what page youre on and what item is selected
state = pn.state
if 'page' not in state.cache:
    state.cache['page'] = 1
if 'selected_item' not in state.cache:
    state.cache['selected_item'] = None

# widgets
enter_button = pn.widgets.Button(
    name='Enter', 
    button_type='primary',
    sizing_mode='stretch_width',
    stylesheets=["""
        :host(.solid) .bk-btn-primary {
            background-color: #0f7e6a !important;
            border-color: #0f7e6a !important;
            border-radius: 0 !important;
            font-size: 15px !important;
        }
        :host(.solid) .bk-btn-primary:hover {
            background-color: #0c6355 !important;
            border-color: #0c6355 !important;
            border-radius: 0 !important;
            font-size: 15px !important;
        }
    """]
)

enter_button_fr = pn.widgets.Button(
    name='Entrez', 
    button_type='primary',
    sizing_mode='stretch_width',
    stylesheets=["""
        :host(.solid) .bk-btn-primary {
            background-color: #0f7e6a !important;
            border-color: #0f7e6a !important;
            border-radius: 0 !important;
            font-size: 15px !important;
        }
        :host(.solid) .bk-btn-primary:hover {
            background-color: #0c6355 !important;
            border-color: #0c6355 !important;
            border-radius: 0 !important;
            font-size: 15px !important;
        }
    """]
)

recipient_button = pn.widgets.Button(
    name='Recipient', 
    button_type='primary',
    sizing_mode='stretch_width',
    stylesheets=["""
        :host(.solid) .bk-btn-primary {
            background-color: #0f7e6a !important;
            border-color: #0f7e6a !important;
            border-radius: 0 !important;
            font-size: 15px !important;
        }
        :host(.solid) .bk-btn-primary:hover {
            background-color: #0c6355 !important;
            border-color: #0c6355 !important;
            border-radius: 0 !important;
            font-size: 15px !important;
        }
    """]
)

coordinator_button = pn.widgets.Button(
    name='Coordinator', 
    button_type='primary',
    sizing_mode='stretch_width',
    stylesheets=["""
        :host(.solid) .bk-btn-primary {
            background-color: #0f7e6a !important;
            border-color: #0f7e6a !important;
            border-radius: 0 !important;
            font-size: 15px !important;
        }
        :host(.solid) .bk-btn-primary:hover {
            background-color: #0c6355 !important;
            border-color: #0c6355 !important;
            border-radius: 0 !important;
            font-size: 15px !important;
        }
    """]
)

dropdown = pn.widgets.Select(
    name='', 
    options=['Please select department', 'War', 'Oil', 'London Drugs PhotoLab'],
    value='Please select department',
    sizing_mode='stretch_width',
    stylesheets=["""
        select {
            text-align: center !important;
            text-align-last: center !important;
        }
    """]
)

dropdown_enter_button = pn.widgets.Button(
    name='Enter', 
    button_type='primary',
    sizing_mode='stretch_width',
    stylesheets=["""
        :host(.solid) .bk-btn-primary {
            background-color: #0f7e6a !important;
            border-color: #0f7e6a !important;
            border-radius: 0 !important;
            font-size: 15px !important;
        }
        :host(.solid) .bk-btn-primary:hover {
            background-color: #0c6355 !important;
            border-color: #0c6355 !important;
            border-radius: 0 !important;
            font-size: 15px !important;
        }
    """]
)


# image panes
image_html = """
<div style="overflow: hidden; border-radius: 10px; max-width: 100%; width: 600px;">
    <img src="https://www.iboutique.ca/clients/ibout/images/Iboutique_Landing_Backgound_en.jpg?v=2" 
         style="width: 100%; margin-top: -21%; margin-bottom: -20%; display: block;">
</div>
"""

image_html_small = """
<div style="overflow: hidden; border-radius: 10px; max-width: 100%; width: 200px;">
    <img src="https://www.iboutique.ca/clients/ibout/images/Iboutique_Landing_Backgound_en.jpg?v=2" 
         style="width: 100%; margin-top: -21%; margin-bottom: -21%; display: block;">
</div>
"""


hardstare1 = """
<div style="overflow: hidden; border-radius: 10px; max-width: 100%; width: 500px;">
    <img src="https://media.tenor.com/40K6BRt5aJUAAAAM/bear-stare-hard-stare.gif" 
         style="width: 100%; display: block;">
</div>
"""

hardstare2 = """
<div style="overflow: hidden; border-radius: 10px; max-width: 100%; width: 500px;">
    <img src="https://media2.giphy.com/media/v1.Y2lkPTZjMDliOTUydmtyYTV6MHdodXNhOHJrazk4d3NiNHB4MWc4NDUzanNndDVraTd4MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3dgcqvbzWg5oAPt0yY/200.gif" 
         style="width: 100%; display: block;">
</div>
"""

hardstare3 = """
<div style="overflow: hidden; border-radius: 10px; max-width: 100%; width: 500px;">
    <img src="https://i.pinimg.com/originals/04/b6/9c/04b69c2c65246b1a54d6ca4a0db98953.gif" 
         style="width: 100%; display: block;">
</div>
"""

out_of_stock_html = """
<div style="text-align: center; padding: 20px;">
    <h2 style="color: #e1241b; font-family: 'Avenir Light', Avenir, sans-serif;">Out of Stock</h2>
    <p style="font-size: 16px;">This item is currently unavailable.</p>
</div>
"""

# items
items = {
    'item1': {
        'name': 'Extra dairy heavy cheese',
        'image': 'https://t4.ftcdn.net/jpg/04/70/65/17/360_F_470651717_p6MAXj7Qlz4iSTPYvRdNzG8CxBQh1uPP.jpg',
        'caption': 'Extra dairy heavy cheese',
        'description': 'This artisan cheese is crafted from rich, full-fat cows milk and aged to develop its complex, creamy flavor profile with concentrated dairy proteins and natural lactose throughout. Each bite delivers an indulgent experience of pure dairy goodness, with the milks natural sugars and fats creating a smooth, luxurious texture that cheese lovers crave.'
    },
    'item2': {
        'name': 'Tickets to see Wicked with Danny',
        'image': 'https://i.etsystatic.com/13808400/r/il/cb9e18/6482109708/il_fullxfull.6482109708_nl02.jpg',
        'caption': 'Tickets to see Wicked with Danny',
        'description': 'Experience the magic of Wicked on Broadway with Danny, who will provide enthusiastic live commentary throughout the entire performance about Jonathan Baileys exceptional talent, charm, and various roles. This unique theatergoing experience includes non-stop insights into why Jonathan Bailey is the greatest actor of our generation, shared passionately from curtain up to final bow.'
    },
    'item3': {
        'name': 'Lindt Vegan Chocolate Bar',
        'image': 'https://m.media-amazon.com/images/I/61BG6DGAljL.jpg',
        'caption':'Lindt Vegan Chocolate Bar',
        'description': 'Treat yourself with Lindt’s irresistibly delicious oat-based chocolate with the Vegan Original Chocolate Bar. Crafted with premium vegan chocolate, this gourmet chocolate bar delivers a perfectly smooth and creamy texture for a delicious, full sensory chocolate experience.'
    },
    'item4': {
        'name': '$10 Shoppers Gift Card',
        'image': 'https://assetscontent.s3.ca-central-1.amazonaws.com/images/1623674755699-ATB_Shoppers.jpg',
        'caption': '$10 Shoppers Gift Card',
        'description': 'This $10 Shoppers Drug Mart gift card offers a modest shopping experience at a pharmacy chain that, while adequate, simply doesnt compare to the superior selection and value youd find at London Drugs. Its a functional but underwhelming option that will leave you wishing you had a London Drugs gift card instead.'
    },
    'item5': {
        'name': 'Hoselton Canada Aluminum Goose Sculpture Plate #944 Trinket Dish Canadian Art',
        'image': 'https://i.ebayimg.com/images/g/7jgAAOSwOsFhiHV7/s-l400.jpg',
        'caption': 'Hoselton Canada Aluminum Goose Sculpture Plate #944 Trinket Dish Canadian Art',
        'description': 'Crafted at Hoselton Studios, this plate crafted in aluminum depicts various wildlife and includes a stand for display.'
    },
    'item6': {
        'name': 'Bradley Cooper Autograph',
        'image': 'https://cdn.rrauction.com/auction/674/3475441_1.jpg',
        'caption': 'Bradley Cooper Autograph',
        'description': 'This authenticated autograph from Bradley Cooper features his signature scrawled across a standard photo.'
    },
    'item7': {
        'name': 'Low Sodium Cooking Book',
        'image': 'https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781593370442/the-everything-low-salt-cookbook-book-9781593370442_lg.jpg',
        'caption':'Low Sodium Cooking Book',
        'description': 'This low-sodium cookbook is filled with bland, under-seasoned recipes that strip away all the salty, savory goodness that makes food actually taste delicious. Every page is a reminder of what youll be missing without the generous amounts of salt, soy sauce, and flavorful seasonings that make your favorite high-sodium dishes so satisfying.'
    },
    'item8': {
        'name': 'Festive Collection Cinnamon and Candied Tamarind Vertuo Nespresso',
        'image': 'https://www.nespresso.com/ecom/medias/sys_master/public/46378059268126/festive-vl-cinnamon-pdp.png?impolicy=medium&imwidth=824&imdensity=1',
        'caption':  'Festive Collection Cinnamon and Candied Tamarind Vertuo Nespresso',
        'description': 'The delightful warmth of cinnamon and the sweet, jammy flavor of tamarind makes this coffee the perfect match for the season.'
    },
    'item9': {
        'name': 'Reagle Beagle Trivia without Graham',
        'image': 'https://thebeagle.ca/newsite/wp-content/uploads/2023/11/trivia-poster.jpg',
        'caption':  'Reagle Beagle Trivia without Graham',
        'description': 'Experience pub trivia night without Graham, the charismatic and beloved host youve come to enjoy, as hell be replaced by Landon for the evening. Instead of Grahams quick wit and engaging style, youll spend the night with Landons hosting, making this a decidedly less appealing trivia experience.'
    },
    'item10': {
        'name': 'Sour Cream and Onion Clean Beans',
        'image': 'https://www.nutraphase.com/cdn/shop/files/Sour_Cream_Onion.jpg?v=1753372594',
        'caption': 'Sour Cream and Onion Clean Beans',
        'description': 'Feel the unmistakable rumbling of a hungry tummy? Tame your cravings WITH the bold crunch, big flavour, and protein power of clean beans. These savoury roasted broad beans are everything you’d ever want in a quick bite, packed with high-quality protein to step up your snacking game. Grab a handful – or hey, the whole bag! – and dig into the delicious gluten-free goodness.'
    },
    'item11': {
        'name': 'Starbucks Protein Latte',
        'image': 'https://about.starbucks.com/uploads/sites/9/2025/09/Starbucks-Protein-Beverages-Trio-3.jpg',
        'caption':  'Starbucks Protein Latte',
        'description': 'Bold espresso with Protein-boosted Milk and vanilla syrup.'
    },
    'item12': {
        'name': 'Norman Rockwell Print',
        'image': 'https://i.imgur.com/fhATbav.jpeg',
        'caption': 'Norman Rockwell Print',
        'description': 'This Norman Rockwell print is the exact same one thats already hanging on your wall at home, making it a completely redundant addition to your collection.'
    }
}


# make popups
popup_html = pn.pane.HTML("", align='center')

popup_content = pn.Column(
    popup_html,
    styles={'padding': '20px'}
)

modal = pn.layout.Modal(popup_content)


title = pn.pane.Markdown(
            "# thoBoutique", 
            align='center', 
            styles={
                'font-size': '24px',
                'font-family': '"Avenir Next Ultra Light", "Avenir Light", Avenir, sans-serif'
            }
        )

title_header = pn.pane.Markdown(
            "#   thoBoutique", 
            align='start', 
            styles={
                'font-size': '14px',
                'font-family': '"Avenir Light", Avenir, sans-serif'
            },
            margin=(-27,0,0,30)
        )

title_small = pn.pane.Markdown(
            "# thoBoutique", 
            align='end', 
            styles={
                'font-size': '13px',
                'font-family': '"Avenir Light", Avenir, sans-serif'
            },
            margin=(-20,17,0,0)
        )

login = pn.pane.Markdown(
            "# LOGIN", 
            align='end', 
            styles={
                'font-size': '20px',
                'font-family': '"Avenir Next Ultra Light", "Avenir Light", Avenir, sans-serif',
                'color': '#0f7e6a'
            }
        )

# initialize app
app = pn.Column(
    sizing_mode='stretch_width', 
    max_width=600,
    styles={
        'margin': '0 auto',
        'padding-top': '70px'
    }
)

# header and sidebar
def create_header_and_sidebar():
    header = pn.Column(
        pn.pane.HTML(image_html_small),
        title_header,
        sizing_mode='stretch_width',
        styles={
            'background-color': '#ffffff',
            'border-bottom': '1px solid #dee2e6'
        }
    )
    
    # levels/ they dont do anything
    sidebar = pn.Column(
        pn.pane.Markdown("### Instant Awards", styles={'text-align': 'center', 'color': 'white'},margin=(-10, 0, 0, 0)),
        pn.layout.Divider(),
        pn.pane.Markdown("**Level 1**", styles={'cursor': 'pointer','color': 'white'},margin=(0, 0, 0, 20),),
        pn.pane.Markdown("**Level 2**", styles={'cursor': 'pointer','color': 'white'},margin=(-10, 0, 0, 20),),
        pn.pane.Markdown("**Level 3**", styles={'cursor': 'pointer', 'color': 'white'},margin=(-10, 0, 0, 20),),
        pn.pane.Markdown("**Level 4**", styles={'cursor': 'pointer', 'color': 'white'},margin=(-10, 0, 0, 20),),
        pn.pane.Markdown("**Level 4**", styles={'cursor': 'pointer', 'color': 'white'},margin=(-10, 0, 0, 20),),
        pn.pane.Markdown("**Level 5**", styles={'cursor': 'pointer', 'color': 'white'},margin=(-10, 0, 0, 20),),
        pn.pane.Markdown("**Level 6**", styles={'cursor': 'pointer', 'color': 'white'},margin=(-10, 0, 0, 20),),
        pn.pane.Markdown("**Level 7**", styles={'cursor': 'pointer', 'color': 'white'},margin=(-10, 0, 0, 20),),
        pn.pane.Markdown("**Level 8**", styles={'cursor': 'pointer', 'color': 'white'},margin=(-10, 0, 0, 20),),
        pn.pane.Markdown("**Level 9**", styles={'cursor': 'pointer', 'color': 'white'},margin=(-10, 0, 0, 20),),
        width=200,
        styles={
            'background-color': '#e1241b',
            'padding': '20px',
            'min-height': '100vh'
        }
    )
    
    return header, sidebar

# functions to handle page transitions
def show_page_1():
    app.clear()
    app.styles = {'margin': '0 auto', 'padding-top': '70px'}
    app.max_width = 600
    app.sizing_mode = 'stretch_width'
    
    app.extend([
        title,
        pn.pane.HTML(image_html),
        pn.Row(enter_button_fr, enter_button),
        modal  
    ])
    
def show_page_2():
    app.clear()
    app.styles = {'margin': '0 auto', 'padding-top': '70px'}
    app.max_width = 600
    app.sizing_mode = 'stretch_width'
    
    app.extend([
        title,
        pn.pane.HTML(image_html),
        pn.Row(coordinator_button, recipient_button),
        modal
    ])
    
def show_page_3():
    app.clear()
    app.styles = {'margin': '0 auto', 'padding-top': '70px'}
    app.max_width = 600
    app.sizing_mode = 'stretch_width'
    
    app.extend([
        pn.Row(login,pn.Spacer(width=200),pn.Column(
            pn.pane.HTML(image_html_small),
            title_small),
        ),
        pn.layout.Divider(),
        dropdown,
        dropdown_enter_button,
        modal
    ])
    
def show_page_4():
    # clear the app and reset its styles for page 4
    app.clear()
    app.styles = {'margin': '0', 'padding': '0'}
    app.max_width = None
    app.sizing_mode = 'stretch_both'
    
    header, sidebar = create_header_and_sidebar()
    
    # item selection
    def make_select_item(item_id):
        def select_item(event):
            state.cache['selected_item'] = item_id
            state.cache['page'] = 5
            show_page_5()
        return select_item
    
    # make rows of items (4 per row)
    item_rows = []
    current_row = []
    
    for i, (item_id, item_data) in enumerate(items.items()):
        item_btn = pn.widgets.Button(
            name='', 
            width=250, 
            height=250, 
            button_type='light',
            styles={'opacity': '0', 'position': 'absolute', 'z-index': '10'}
        )
        item_btn.on_click(make_select_item(item_id))
        
        item_column = pn.Column(
            pn.pane.Image(
                item_data["image"], 
                width=250, 
                height=250,
                styles={'cursor': 'pointer', 'border-radius': '10px'},
                link_url='javascript:void(0)'
            ),
            pn.pane.Markdown(f"**{item_data['caption']}**", align='center'),
            item_btn,
            align='center',
            width=280
        )
        
        current_row.append(item_column)
        
        # if more than 4 items in a row make new row
        if len(current_row) == 4 or i == len(items) - 1:
            item_rows.append(pn.Row(*current_row, sizing_mode='stretch_width', margin=(0, 0, 30, 0)))
            current_row = []
    
    main_content = pn.Column(
        *item_rows,
        sizing_mode='stretch_width',
        styles={'padding': '20px'}
    )
    
    content_row = pn.Row(
        sidebar,
        main_content,
        sizing_mode='stretch_width'
    )
    
    app.extend([
        header,
        content_row,
        modal 
    ])

def show_page_5():
    app.clear()
    app.styles = {'margin': '0', 'padding': '0'}
    app.max_width = None
    app.sizing_mode = 'stretch_both'
    
    header, sidebar = create_header_and_sidebar()
    
    item_id = state.cache['selected_item']
    item = items[item_id]
    
    back_button = pn.widgets.Button(
        name='← Back to Items',
        button_type='primary',
        stylesheets=["""
            :host(.solid) .bk-btn-primary {
                background-color: #0f7e6a !important;
                border-color: #0f7e6a !important;
                border-radius: 0 !important;
                font-size: 15px !important;
            }
            :host(.solid) .bk-btn-primary:hover {
                background-color: #0c6355 !important;
                border-color: #0c6355 !important;
                border-radius: 0 !important;
                font-size: 15px !important;
            }
        """]
    )
    
    select_item_button = pn.widgets.Button(
        name='Select Item',
        button_type='primary',
        stylesheets=["""
            :host(.solid) .bk-btn-primary {
                background-color: #0f7e6a !important;
                border-color: #0f7e6a !important;
                border-radius: 0 !important;
                font-size: 15px !important;
            }
            :host(.solid) .bk-btn-primary:hover {
                background-color: #0c6355 !important;
                border-color: #0c6355 !important;
                border-radius: 0 !important;
                font-size: 15px !important;
            }
        """]
    )
    
    def go_back(event):
        state.cache['page'] = 4
        show_page_4()
    
    def on_select_item(event):
        # show gif for 5th item, out of stock for all others
        if item_id == 'item5':
            popup_html.object = """
<div style="overflow: hidden; border-radius: 10px; max-width: 100%; width: 500px;">
    <img src="https://media.tenor.com/zvgmnvp8x30AAAAM/cars-tow-mater.gif" 
         style="width: 100%; display: block;">
</div>
"""
            modal.open = True
        else:
            popup_html.object = out_of_stock_html
            modal.open = True
    
    back_button.on_click(go_back)
    select_item_button.on_click(on_select_item)
    
    main_content = pn.Column(
        back_button,
        pn.Row(
            pn.pane.HTML(f'<img src="{item["image"]}" style="max-width: 400px; max-height: 600px; border-radius: 10px; margin: 20px 0; object-fit: contain;">'),
            pn.Column(
                pn.pane.Markdown(f"# {item['name']}"),
                pn.layout.Divider(),
                pn.pane.Markdown(item['description']),
                select_item_button,
                sizing_mode='stretch_width',
            )
        ),
        sizing_mode='stretch_width',
        styles={'padding': '20px'}
    )
    
    content_row = pn.Row(
        sidebar,
        main_content,
        sizing_mode='stretch_width'
    )
    
    app.extend([
        header,
        content_row,
        modal
    ])

# button click handlers
def on_enter_click(event):
    state.cache['page'] = 2
    show_page_2()

def on_wrong_button_click(event):
    popup_html.object = random.choice([hardstare1, hardstare2, hardstare3])
    modal.open = True
    
def on_recipient_click(event):
    state.cache['page'] = 3
    show_page_3()
    
def on_dropdown_button_click(event):
    if dropdown.value and dropdown.value != 'Please select department':
        if dropdown.value in ['War', 'Oil']:  
            popup_html.object = random.choice([hardstare1, hardstare2, hardstare3])
            modal.open = True
        elif dropdown.value == 'London Drugs PhotoLab':  
            state.cache['page'] = 4
            show_page_4()

# link buttons to handlers
enter_button.on_click(on_enter_click)
enter_button_fr.on_click(on_wrong_button_click)
recipient_button.on_click(on_recipient_click)
coordinator_button.on_click(on_wrong_button_click)
dropdown_enter_button.on_click(on_dropdown_button_click)

# initialize app with page 1
show_page_1()

# Serve the app - this is needed for py.cafe and most other deployers
app.servable()