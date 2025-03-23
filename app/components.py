import reflex as rx
from app.state import StoryState


def custom_button(text: str, icon: str) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text),
            class_name="items-center gap-1",
        ),
        class_name="px-3 py-1.5 rounded-lg text-sm bg-indigo-50 text-indigo-700 hover:bg-indigo-100 transition-all",
    )


def category_button(
    text: str, icon: str, bg_color: str, text_color: str, hover_color: str
) -> rx.Component:
    """Create a category button with consistent styling.

    Args:
        text: The button text
        icon: The icon name
        bg_color: Background color class (e.g., "indigo-100")
        text_color: Text color class (e.g., "indigo-800")
        hover_color: Hover background color class (e.g., "indigo-200")
    """
    return rx.button(
        rx.hstack(
            rx.icon(icon, size=14),
            rx.text(text),
            class_name="items-center justify-center",
        ),
        class_name=f"px-3 py-1.5 bg-{bg_color} text-{text_color} rounded-full text-sm hover:bg-{hover_color} transition-all whitespace-nowrap",
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
                    class_name="text-3xl md:text-4xl bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 bg-clip-text text-transparent relative hover:scale-105 transition-transform duration-300",
                ),
                class_name="flex justify-center items-center cursor-pointer",
                spacing="1",
                on_click=rx.redirect("/"),
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


def story_craft_card() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.icon(
                    "wand-sparkles",
                    size=24,
                    color="indigo",
                    class_name="",
                ),
                rx.text(
                    "Craft Your Tale",
                    class_name="text-xl md:text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent",
                ),
                class_name="mb-2 items-center justify-left w-full",
            ),
            rx.vstack(
                rx.text_area(
                    placeholder="Enter a story theme or topic...",
                    variant="soft",
                    class_name="w-full rounded-xl p-1 border-2 border-black focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all resize-none min-h-[100px] text-gray-700 bg-white/80 backdrop-blur-sm shadow-sm",
                    style={"font_family": "Grotesk"},
                ),
                align_items="start",
                width="100%",
                spacing="1",
            ),
            # Genre section with scrollable container
            rx.vstack(
                rx.hstack(
                    rx.icon("bookmark", size=18, color="indigo"),
                    rx.text(
                        "Choose a genre",
                        class_name="text-sm font-medium text-gray-700",
                    ),
                    class_name="items-center",
                    spacing="2",
                ),
                rx.box(
                    rx.flex(
                        category_button(
                            "Fantasy",
                            "sparkles",
                            "indigo-100",
                            "indigo-800",
                            "indigo-200",
                        ),
                        category_button(
                            "Adventure", "globe", "green-100", "green-800", "green-200"
                        ),
                        category_button(
                            "Mystery",
                            "message_circle_question",
                            "purple-100",
                            "purple-800",
                            "purple-200",
                        ),
                        category_button(
                            "Sci-Fi", "rocket", "blue-100", "blue-800", "blue-200"
                        ),
                        category_button(
                            "Fairytale", "star", "pink-100", "pink-800", "pink-200"
                        ),
                        class_name="space-x-2 overflow-x-auto py-2 flex-nowrap md:flex-wrap md:gap-y-2 justify-start",
                    ),
                    class_name="w-full overflow-x-auto scrollbar-hide",
                ),
                spacing="2",
                align_items="start",
                width="100%",
            ),
            # Story Tone section with scrollable container
            rx.vstack(
                rx.hstack(
                    rx.icon("music_2", size=18, color="amber"),
                    rx.text(
                        "Story Tone",
                        class_name="text-sm font-medium text-gray-700",
                    ),
                    class_name="items-center",
                    spacing="2",
                ),
                rx.box(
                    rx.flex(
                        category_button(
                            "Whimsical", "sun", "yellow-100", "yellow-800", "yellow-200"
                        ),
                        category_button(
                            "Dramatic", "flame", "red-100", "red-800", "red-200"
                        ),
                        category_button(
                            "Educational",
                            "graduation_cap",
                            "teal-100",
                            "teal-800",
                            "teal-200",
                        ),
                        category_button(
                            "Humorous",
                            "smile_plus",
                            "amber-100",
                            "amber-800",
                            "amber-200",
                        ),
                        category_button(
                            "Inspirational",
                            "lightbulb",
                            "violet-100",
                            "violet-800",
                            "violet-200",
                        ),
                        class_name="space-x-2 overflow-x-auto py-2 flex-nowrap md:flex-wrap md:gap-y-2 justify-start",
                    ),
                    class_name="w-full overflow-x-auto scrollbar-hide",
                ),
                spacing="2",
                align_items="start",
                width="100%",
                margin_top="4",
            ),
            class_name="w-full border border-gray-200 rounded-2xl p-4 md:p-6 space-y-4 bg-white shadow-sm hover:shadow-md transition-all",
        ),
        class_name="w-full mx-auto mt-2",
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
                story_craft_card(),
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
                    class_name="mt-4 cursor-pointer bg-gradient-to-r from-purple-500 to-indigo-500 text-white rounded-lg p-6 font-bold shadow-md shadow-purple-300/30 hover:shadow-lg hover:shadow-purple-300/40 hover:-translate-y-0.5 transition-all duration-200 relative overflow-hidden shimmer-button",
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
                    on_click=rx.redirect("/story"),
                ),
                class_name="w-full max-w-2xl mx-auto mt-2",
                spacing="2",
                align="center",
            ),
            spacing="3",
            align="start",
            class_name="py-12 md:py-20 md:items-center",
        ),
        class_name="w-full max-w-6xl mx-auto px-2",
    )


def render_title(title: str) -> rx.Component:
    """Render the story title.

    Args:
        title: The title of the story

    Returns:
        A component displaying the title
    """
    return rx.box(
        rx.heading(
            title,
            class_name="text-3xl md:text-5xl lg:text-6xl tracking-wide font-bold bg-clip-text text-transparent bg-gradient-to-r from-purple-600 via-blue-500 to-indigo-600 mb-2 text-center",
        ),
        class_name="w-full px-4 py-6",
    )


def render_story() -> rx.Component:
    """Render the story with navigation between chapters.

    Returns:
        A component displaying the current chapter with navigation
    """
    return rx.box(
        rx.vstack(
            # Title Section
            rx.box(
                render_title(StoryState.story["title"]),
                class_name="flex items-center justify-center w-full",
            ),
            # Story content with card-like appearance
            rx.box(
                rx.vstack(
                    rx.heading(
                        rx.cond(
                            StoryState.current_chapter_index >= 0,
                            f"Chapter {StoryState.current_chapter['chapter_number']}: {StoryState.current_chapter['chapter_name']}",
                            "Loading chapter...",
                        ),
                        class_name="text-xl md:text-2xl font-bold mb-4 text-gray-800",
                    ),
                    rx.box(
                        rx.image(
                            StoryState.current_chapter["image"],
                            class_name="w-full h-auto rounded-2xl shadow-lg transform transition-transform duration-500 hover:scale-[1.02]",
                            alt=f"Illustration for Chapter {StoryState.current_chapter['chapter_number']}",
                        ),
                        class_name="mb-6 overflow-hidden rounded-2xl",
                    ),
                    rx.text(
                        StoryState.current_chapter["text"],
                        class_name="text-lg leading-relaxed text-gray-700 whitespace-pre-line",
                    ),
                    # Navigation buttons
                    rx.hstack(
                        rx.button(
                            rx.hstack(
                                rx.icon("arrow-left", size=16),
                                rx.text("Previous Chapter"),
                            ),
                            class_name="mt-8 px-4 py-2 bg-white text-purple-600 border border-purple-300 rounded-lg shadow hover:shadow-md transition-all disabled:opacity-50 disabled:cursor-not-allowed",
                            is_disabled=~StoryState.has_previous_chapter,
                            on_click=StoryState.go_to_previous_chapter,
                        ),
                        rx.spacer(),
                        rx.button(
                            rx.hstack(
                                rx.text("Next Chapter"),
                                rx.icon("arrow-right", size=16),
                            ),
                            class_name="mt-8 px-4 py-2 bg-gradient-to-r from-purple-500 to-indigo-500 text-white rounded-lg shadow hover:shadow-md hover:-translate-y-0.5 transition-all disabled:opacity-50 disabled:cursor-not-allowed",
                            is_disabled=~StoryState.has_next_chapter,
                            on_click=StoryState.go_to_next_chapter,
                        ),
                        class_name="w-full",
                    ),
                    # Chapter indicator
                    rx.hstack(
                        *[
                            rx.box(
                                class_name=rx.cond(
                                    StoryState.current_chapter_index == i,
                                    "w-2 h-2 rounded-full bg-purple-600",
                                    "w-2 h-2 rounded-full bg-gray-300",
                                ),
                            )
                            for i in range(
                                3
                            )  # Fixed number of chapters in our sample story
                        ],
                        class_name="mt-6 justify-center space-x-2",
                    ),
                    align="stretch",
                    class_name="p-4 md:p-8 bg-white rounded-3xl shadow-xl",
                ),
                class_name="w-full md:max-w-4xl mx-auto px-0 md:px-4",
            ),
            spacing="4",
            align="center",
            class_name="w-full py-4 md:py-8",
        ),
        class_name="w-full",
    )
