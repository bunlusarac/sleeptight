<div align="center">
	<img src="sleep.jpg"/>
	<p><em>Nothing like a good night's sleep</em></p>
</div>

## Summary
sleeptight is a Python/Selenium WebDriver script that joins your online YTU courses for you while you are sleeping peacefully. It handles automatized leaving/joining to course meetings so that you don't have to worry about any nonattendance penalties. Please note that this is heavily WIP.

![screenshot](screenshot.png)

## Installation
You have to install Selenium and psutil to run sleeptight. You can use pip with requirements file:

`pip install -r requirements.txt` 

You also have to [download ChromeDriver binary](https://sites.google.com/chromium.org/driver/) and put it in the same directory with the sleeptight script.

Finally, you need to let ChromeDriver open Zoom binary automatically by checking the "Always open these types of links in the associated app" when ChromeDriver prompts you to open Zoom when you run sleeptight for the first time. You can also set Zoom to join audio automatically.

## Course ID
When you run the script, it will ask for the course ID. Course ID is the 5-digit ID at the end of the URL of the Online Lesson/Canlı Ders page of the course. For example if the URL is `...ViewOnlineLessonProgramForStudent/12345`, the course ID is 12345.

## Config
sleeptight creates a config file called stconfig which contains your login credentials so you don't have to enter it every time. If you entered wrong mail/password, you can delete stconfig (it will ask again for credentials and recreate stconfig) or you can edit it manually with an editor.

