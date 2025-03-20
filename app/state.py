import reflex as rx

# Sample story data structure
sample_story = {
    "title": "The Mermaid of Whispering Reef",
    "chapters": [
        {
            "chapter_number": 1,
            "chapter_name": "A Day of Play",
            "image": "/sample.jpeg",
            "text": """Coralia, the mermaid of Whispering Reef, had a laugh that sounded like the gentle chime of seashells. Her fiery red hair flowed as she darted through vibrant coral gardens. Today was a day for joy as sunbeams danced through the clear turquoise water.

Three sleek dolphins - Echo, Ripple, and Wave - joined her merriment. Their playful clicks echoed through the reef as they chased each other in spiraling loops. Coralia's shimmering tail propelled her through the water as she twirled alongside her friends.

The reef bustled with colorful fish - iridescent parrotfish, striped angelfish, and even a grumpy pufferfish. This vibrant kingdom of constant wonder was Coralia's home, and she, the smiling mermaid, was always at its heart."""
        },
        {
            "chapter_number": 2,
            "chapter_name": "The Mysterious Echo",
            "image": "/sample.jpeg",
            "text": """As the sun began to set, casting golden ripples across the surface above, Coralia heard something unusual. It was a haunting melody that seemed to come from the deepest part of the ocean. None of her friends could hear it, but the sound pulled at her heart.

"I must find where it's coming from," she told Echo, her most trusted dolphin companion. The wise dolphin clicked cautiously, warning her of the dangers in the deep unknown waters beyond the reef.

But Coralia's curiosity was too strong. "I'll be careful," she promised, her emerald eyes reflecting determination. "I'll return before the moon reaches its highest point." With a flick of her iridescent tail, she swam toward the mysterious sound, unaware of the adventure that awaited."""
        },
        {
            "chapter_number": 3,
            "chapter_name": "The Ancient Guardian",
            "image": "/sample.jpeg",
            "text": """The melody led Coralia to an underwater cave hidden behind a curtain of swaying seaweed. Inside, the walls glittered with luminescent crystals that pulsed in rhythm with the haunting song.

At the center of the cave floated an ancient sea turtle, its shell embedded with the same glowing crystals. Its eyes, wise and ancient, seemed to hold the stories of a thousand ocean years.

"Welcome, young guardian of Whispering Reef," the turtle spoke, its voice resonating in Coralia's mind. "I have been waiting for you."

Coralia gasped. "Me? But I'm just a mermaid who loves to play with her friends."

The turtle's eyes twinkled. "You are much more than that, child of the sea. The reef chose you as its heart for a reason. Now, it needs your help. A darkness approaches, and only you can protect the harmony of these waters."

As the turtle spoke of an ancient prophecy, Coralia realized her carefree days were about to change. A great responsibility now rested on her shoulders, but looking at the crystal-adorned guardian, she knew she wouldn't face it alone."""
        }
    ]
}


# State for the story viewer
class StoryState(rx.State):
    """The state for the story viewer."""
    
    # The current story being displayed
    story: dict = sample_story
    
    # The current chapter index (0-based)
    current_chapter_index: int = 0
    
    @rx.var
    def current_chapter(self) -> dict:
        """Get the current chapter data."""
        return self.story["chapters"][self.current_chapter_index]
    
    @rx.var
    def has_previous_chapter(self) -> bool:
        """Check if there is a previous chapter."""
        return self.current_chapter_index > 0
    
    @rx.var
    def has_next_chapter(self) -> bool:
        """Check if there is a next chapter."""
        return self.current_chapter_index < len(self.story["chapters"]) - 1
    
    def go_to_previous_chapter(self):
        """Navigate to the previous chapter if available."""
        if self.has_previous_chapter:
            self.current_chapter_index -= 1
    
    def go_to_next_chapter(self):
        """Navigate to the next chapter if available."""
        if self.has_next_chapter:
            self.current_chapter_index += 1