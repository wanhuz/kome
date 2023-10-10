Kome
=======

Japanese subtitle cleaner and automatic synchronization of subtitles with video, so that
subtitles are aligned to the correct starting point within the video.

Turn this:                       |  Into this:
:-------------------------------:|:-------------------------:
![](https://github.com/wanhuz/kome/assets/12682216/5384d6cd-9463-41a7-af21-2ca832021dd5)  |  ![](https://github.com/wanhuz/kome/assets/12682216/f78044dd-ab9b-4f75-9b66-f214cf856305) 


Install
-------
First, Install Python 3 

Then, make sure ffmpeg is installed. On MacOS, this looks like:
~~~
brew install ffmpeg
~~~
(Windows users: make sure `ffmpeg` is on your path and can be referenced
from the command line!)

Then, download kome from releases page, extract the zip file. Run `pip install -r requirements.txt` from terminal in Kome directory.

Usage
-----
Run in terminal on kome directory:
~~~
kome.py src_video.mkv dest_video.mkv
~~~

Kome will extract subtitle from source video, clean it, synchronise the subtitle timing with the destination video and generate the  subtitle file in the destination directory.

There are additional parameter such as selecting different subtitle track from source video, selecting external subtitle file, etc. 

For more options, see 'kome.py -help'

Use case
-----
A use case for Kome is if you have a Japanese video with built-in subtitle but want to use the subtitle in another video (for example, use the subtitle from TV series to BD). 

This script will extract subtitle from source video, reshift the timing to destination video, clean hearing impaired subtitle and apply clean style to subtitle automatically for viewing.

Script steps
-----
1. Extract subtitle from source video.
2. Shift subtitle timing to destination video.
3. Clean subtitle to remove sound effect, character parantheses and misc symbol.
4. Apply cleaner style.
5. Output subtitle to destination video folder.

Caveat
-----
- This script cannot improve bad timing. If original lines are mistimed, they will be mistimed in the output file too.
- This script cannot completely remove sound effect. Some sound effect line do not have discernible pattern that this script can match and remove.
- Make sure to check the subtitle before uploading it for other to use. A Kanji to check is '音' in for example '走る音' as it does not have regular pattern to match to.

Todo
-----
1. Add option to disable styling
2. Add option to clean subtitle only

Credits
-------
This project uses the following libraries:
- [ffmpeg](https://www.ffmpeg.org/) and the [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) wrapper, for extracting raw audio from video
- [sushi](https://github.com/tp7/Sushi) and Python 3 fork [sushi](https://github.com/FichteFoll/Sushi)

# License
Code in this project is [MIT licensed](https://opensource.org/licenses/MIT).
