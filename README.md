Kome
=======

Japanese subtitle cleaner and automatic synchronization of subtitles with video, so that
subtitles are aligned to the correct starting point within the video.

Turn this:                       |  Into this:
:-------------------------------:|:-------------------------:
![](https://github.com/wanhuz/kome/assets/12682216/5384d6cd-9463-41a7-af21-2ca832021dd5)  |  ![](https://github.com/wanhuz/kome/assets/12682216/f78044dd-ab9b-4f75-9b66-f214cf856305) 


Install
-------
First, make sure ffmpeg is installed. On MacOS, this looks like:
~~~
brew install ffmpeg
~~~
(Windows users: make sure `ffmpeg` is on your path and can be referenced
from the command line!)

Then, download from releases page and extract the zip file.

Usage
-----
Run in terminal on kome directory:
~~~
kome.py src_video.mkv dest_video.mkv
~~~

Kome will extract subtitle from source video, clean it, synchronise the subtitle timing with the destination video and generate the  subtitle file in the destination directory.

There are additional parameter such as selecting different subtitle track from source video, selecting external subtitle file, etc. 

For more options, see 'kome.py -help'

Credits
-------
This project uses the following libraries:
- [ffmpeg](https://www.ffmpeg.org/) and the [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) wrapper, for extracting raw audio from video
- [sushi](https://github.com/tp7/Sushi) and Python 3 fork [sushi](https://github.com/FichteFoll/Sushi)

# License
Code in this project is [MIT licensed](https://opensource.org/licenses/MIT).
