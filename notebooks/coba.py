# IF YOU RUNNING FROM HERE, U NEED TO USE ABSOLUTE PATH IN FUNCTION.PY (GITHUB CODESPACE)

import os
import function as fc

print("Current directory:", os.getcwd())


text = "Today was one of those days that filled me with pure joy. The weather was perfect, with clear skies and a gentle breeze that made everything feel fresh and new. I woke up early, feeling energized, and decided to take a walk around the neighborhood. The sunrise painted the sky with soft pinks and oranges, and I couldn’t help but pause and take it all in. There’s something so peaceful about those quiet mornings, just me and the world waking up. Later, I met up with a friend for coffee, and we spent hours laughing and reminiscing. It’s amazing how the simplest conversations can fill you with so much happiness, and I realized that joy isn’t about grand moments—it’s found in the small, everyday things. Whether it’s the feeling of the sun on your skin, the sound of a good friend’s laughter, or the peace that comes from just being present, today reminded me that joy is all around if we take the time to appreciate it. I ended the day feeling grateful for everything I have, from the simple moments to the wonderful people in my life. It was one of those days that will stay with me for a long time, a reminder that happiness doesn’t have to be complicated—it’s right here in front of us."

fc.predicting_input(text)
