# app.py
import panel as pn

pn.extension()

# Create a simple interactive app
slider = pn.widgets.IntSlider(name='Value', start=0, end=100, value=50)
text = pn.pane.Markdown('## Hello from Panel!')

def update_text(event):
    return f"## The slider value is: {event.new}"

interactive_text = pn.bind(update_text, slider)

# Create the app layout
app = pn.Column(
    text,
    slider,
    interactive_text
)

# Serve the app
app.servable()
