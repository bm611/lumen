"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .components import nav, hero


@rx.page(route="/", title="Lumen")
def index() -> rx.Component:
    return rx.container(
        nav(),
        hero(),
        size="4",
    )


style = {
    "font_family": "Grotesk",
    "background_color": "#f0f0f0",
}


app = rx.App(
    style=rx.Style(style),
    stylesheets=["/fonts/font.css"],
    theme=rx.theme(
        appearance="light",
    ),
)
