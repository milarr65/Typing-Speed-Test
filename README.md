# TYPING SPEED TEST
Test your typing speed with this minimalistic python app. Built with NiceGUI.

## About this project
This app is an assignment of the Udemy course **_100 Days of Code: The Complete Python Pro Bootcamp._** We were given full creative freedom to develop the app. My version is based on [**Monkeytype**](https://monkeytype.com/), which is one of my favorite sites to procrastinate on hehe. So most of the functionality is the same.

Originally this was supposed to be built with tkinter, but I came across a youtube video that briefly talked about [**NiceGUI**](https://nicegui.io/) and after reading their docs I couldn't resist trying it. I'm actually super happy I did it, it's been fun learning to use this framework, even though I feel that my code is a bit of a mess, as I'm still a beginner programmer 😅.

## ℹ️ How it works
By default this test is using the top 200 most common words in the English language. But you can choose a bigger set of words in the settings menu. The available options are 200 words, 500, 1k, 3k and 5k. Remember that the bigger the sample size, the more "rare" words you'll get.

Word lists are provided by [google-10000-english](https://github.com/first20hours/google-10000-english) on Github

### 🚀 Difficulty

Each level of difficulty prioritizes words of different length, what does this mean? In easy mode, you'll get mostly short words along with some medium length ones. In medium mode, you'll mostly get medium length words, with some long words mixed in. In hard mode, as you can imagine, you'll get mostly long words.

It is recommended to select a longer test runtime to match medium or hard mode, in order to get better results after each test.

### 📊 Stats
- **_Wpm_** - Words per minute. The amount of correctly typed characters per minute.

- **_Raw_** - Same as wpm, but it takes into account incorrect characters.

- **_Accuracy_** - The percentage of correctly typed characters.

- **_Cpm_** - Characters per minute.

All stats are calculated after the test ends and are normalized to 60 seconds. Unfortunately nothing is calculated live during the test because I didn't have time to implement that :( In the future I might add live stats and maybe a chart similar to monkeytype's.

## 🖥️ How to run this in your computer

You need to have python installed (I'm using python 3.13.1)

1. Git clone this repository, or download as a zip file and extract its contents.
   
   ```
   git clone <link to this repo>
   ```

2. Open the directory in a dedicated terminal, or in your preferred text editor. (I use VSCode)

3. Create a virtual environment inside the directory
   ```
   python -m venv .venv
   .\.venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   
   ```

4. Install the necessary packages with pip
   ```
   pip install -r requirements.txt
   ```
5. Run main.py
    ```
    python main.py
    ```

> [!Note]

> By default the app will show up as a pop-up window in your computer. To run it as a webpage inside your browser: In main.py, set `native=False` inside `ui.run()`. 
> 
> Optional: If you want nicegui to reload the browser page every time it detects changes in the code set `reload=True`
  
  ```python
  ui.run(native=False, reload=True)
  ```
