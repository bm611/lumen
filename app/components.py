import reflex as rx


def custom_button(text: str, icon_name: str) -> rx.Component:
    """Create a custom button with desktop text and mobile icon.

    Args:
        text: The text to display on desktop
        icon_name: The name of the icon to display on mobile

    Returns:
        A button component with responsive display
    """
    return rx.button(
        rx.desktop_only(rx.text(text, class_name="text-xl")),
        rx.mobile_and_tablet(rx.icon(icon_name, size=20)),
        class_name="p-2 md:p-4 cursor-pointer",
        style={
            "background_color": "white",
            "color": "black",
            "border": "1px solid black",
            "border_radius": "0.5rem",
            "box_shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
            "_hover": {
                "background_color": "#f9f9f9",
                "transform": "scale(1.05)",
                "box_shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
            },
            "transition": "all 0.2s ease-in-out",
        },
        on_click=rx.redirect("https://github.com/bm611/lumen"),
    )


def nav() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.box(
                    rx.image("/45.svg", class_name="w-12 h-12 md:w-12 md:h-12"),
                    class_name="transform -translate-y-1",
                ),
                rx.text(
                    "Lumen",
                    class_name="text-3xl md:text-4xl font-bold tracking-wide text-gray-800",
                ),
                class_name="flex justify-center items-center",
                spacing="2",
            ),
            rx.hstack(
                custom_button("sync", "refresh-cw"),
                custom_button("github", "github"),
                class_name="flex justify-center items-center",
                spacing="2",
            ),
            class_name="flex justify-between items-center",
        ),
        class_name="mt-1 mx-auto w-full bg-white border border-gray-200 rounded-3xl p-4 md:p-6 shadow-xl",
    )


def hero() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Where Imagination Comes to Life",
                class_name="text-4xl md:text-6xl tracking-wide font-bold text-left md:text-center bg-clip-text text-transparent bg-gradient-to-r from-purple-600 via-blue-500 to-indigo-600 mb-2",
            ),
            rx.text(
                "Instantly generate magical stories tailored to your interests. "
                "Our AI creates unique adventures you'll treasure forever.",
                class_name="text-lg md:text-2xl text-left md:text-center text-gray-700 max-w-3xl mx-auto mb-8",
            ),
            rx.vstack(
                rx.box(
                    rx.input(
                        placeholder="Enter a story idea or theme...",
                        class_name="w-full h-14 px-4 py-2 text-lg md:text-2xl rounded-md border-2 border-black",
                        style={"background_color": "#f0f0f0"},
                    ),
                    class_name="w-full max-w-2xl relative",
                ),
                rx.button(
                    rx.hstack(
                        rx.icon("sparkles", size=22),
                        rx.text(
                            "Generate Story",
                            class_name="tracking-wide text-lg md:text-2xl",
                        ),
                        rx.icon("sparkles", size=22),
                        class_name="flex items-center",
                    ),
                    class_name="mt-4 bg-gradient-to-r from-purple-500 to-indigo-500 text-white rounded-lg p-6 font-bold shadow-md shadow-purple-300/30 hover:shadow-lg hover:shadow-purple-300/40 hover:-translate-y-0.5 transition-all duration-200 relative overflow-hidden shimmer-button",
                    style={
                        "position": "relative",
                        "_before": {
                            "content": "''",
                            "position": "absolute",
                            "top": "0",
                            "left": "-100%",
                            "width": "100%",
                            "height": "100%",
                            "background": "linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent)",
                            "animation": "shimmer 2s infinite",
                        },
                        "_after": {
                            "content": "''",
                            "position": "absolute",
                            "top": "-2px",
                            "left": "-2px",
                            "right": "-2px",
                            "bottom": "-2px",
                            "background": "linear-gradient(90deg, #8B5CF6, #6366F1, #8B5CF6)",
                            "border_radius": "0.5rem",
                            "z_index": "-1",
                            "animation": "border-glow 3s infinite",
                            "filter": "blur(8px)",
                            "opacity": "0.7",
                        },
                    },
                ),
                class_name="w-full max-w-2xl mx-auto mt-2",
                spacing="2",
                align="center",
            ),
            spacing="3",
            align="start",
            class_name="py-12 md:py-20 md:items-center",
        ),
        class_name="w-full max-w-6xl mx-auto px-4",
    )
