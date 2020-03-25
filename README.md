# So, what is this?
It's a Discord "bot" which runs on the OS via the power of Python. There is no Discord API used.

# Usage
* The default prefix for all commands is `awaaz`.
* To play music during a call, simply run `awaaz play <song>`
* To check the version number which is basically an arbitrary value and to of no use for the user, run `awaaz -v`
* To spam to get shady DMs out of sight, run `awaaz spam`
* execute `awaaz anti-fbi` in your shady DMs to free yourself of any legal troube

# Configuration
This software has two components to it: The Python part, and the JS Chromium extension. The Python section is located in the `python` directory (intuitive naming scheme, right?) whistl the JS component is stored in `chrome_extension`. Simply load the unpacked extension into your favorite Chromium-based browser and run `main.py`, and have fun!

## Music Playback in a call
In order to play music through a DM call, you will need to pipe your output audio into the input. If you're on Linux, then I would recommend using a combination of PulseAudio and Audacity, [as outlined in this StackExchange thread](https://unix.stackexchange.com/questions/82259/how-to-pipe-audio-output-to-mic-input). If on Windows, try VoiceMeter Banana. If on macOS, perhaps look into Sunflower.

## Mouse Coordinate Variables
Hover your mouse pointer over the following locations respectably while running `vars_script.py`:

* yt1ThumbX & yt1ThumbY - The location of where the first thumbnail on a [YouTube search page](https://www.youtube.com/results?search_query=omar+waseem+pov+street+photography) is

After obtaining the coordinates, change the values of the variables in `actions.py`

# Limitations
* currently cannot auto-join call upon request; manual intervention required
* there can be no command in the chat as the latest message sent by any party before the execution of the python script, or else it'll freak
* sometimes, it registers one command twice (so if you posted `awaaz play Payitaht Abdulhamid Muzikleri Gazi Osman Pasha`, it might play that track twice)
* the computer which the software is running on cannot be used by the user unless for joining calls and deleting a table
* audio being piped is sometimes not clear, though I am not sure if that is an Internet connection issue or PulseAudio/Audacity
* chat must be fully populated

# Debugging
Kill `main.py` from the terminal emulator and refresh the page in the browser. Then run again.

# Bug Tracker
Please post in the ["Issues"](https://github.com/ansarirayyan/awaaz/issues) section of this GitHub repository

# Disclaimer
* I do not associate myself with any of the groups mentioned or implied above unless explicitly stated
* Do not take anything above as legal advice
