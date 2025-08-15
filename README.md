# TYPING SPEED TEST

This project is an assignment of the Udemy course **_100 Days of Code: The Complete Python Pro Bootcamp._** We were given full creative freedom to develop the app (no starting code). My version is based on [**Monkeytype**](https://monkeytype.com/), which is one of my favorite sites to procrastinate on hehe. So most of the functionality is the same.

Originally this was supposed to be built with tkinter, but I came across a youtube video that briefly talked about [**NiceGUI**](https://nicegui.io/) and after skimming through their docs I couldn't resist trying it. I'm actually super happy I did it, it's been fun learning to use it, even though I feel that my code is a bit of a mess 😅.

## Video


https://github.com/user-attachments/assets/455c099f-17ed-44d8-ade2-a139f93e1861





## ℹ️ How it works

### 🚀 Difficulty

There are thre levels of difficulty, each prioritizes different words:

- Easy: Favors short words and mixes in some medium words.
- Medium: Favors medium-lenght words and mixes in some long and short words.
- Hard: Favors long words and mixes in some medium-length words.

It is recommended to select a longer test runtime to match medium or hard mode, in order to get better results after each test.

### 📈 Word Variety

Since each word list contains a large number of words (ten thousand words) this setting limits how many words the program will shuffle through. 

In other words, the smaller the word variety you choose, the more *"common"* or *"popular"* words you'll get. Alternatively, selecting a larger sample size will include more *"rare"* words.

Choose from sample sizes including **200,** **500,** **1,000**, **3,000**, or **5,000** of the most common English words.


I used the lists from [google-10000-english](https://github.com/first20hours/google-10000-english) repo on Github.

### 📊 Stats

- **_Wpm_** - Words per minute. The amount of correctly typed words per minute.

- **_Raw_** - Same as wpm, but it takes into account incorrect characters.

- **_Accuracy_** - The **_percentage_** of correctly typed characters.

- **_Cpm_** - Characters per minute.

All stats are calculated after the test ends and are normalized to 60 seconds. Unfortunately nothing is calculated live during the test because I didn't have time to implement that :( In the future I might add live stats and maybe a chart similar to monkeytype's.

## 🖥️ How to run this in your computer

You need to have python installed (I'm using python 3.13.1)

1. Git clone this repository, or download as a zip file and extract its contents.

   ```shell
   git clone https://github.com/milarr65/Typing-Speed-Test.git
   ```

2. Open the directory in a dedicated terminal, or in your preferred text editor. (I use VSCode)

3. Create a virtual environment inside the directory

   ```shell
   python -m venv .venv
   .\.venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux

   ```

4. Install the necessary packages with pip
   ```shell
   pip install -r requirements.txt
   ```
5. Run main.py
   ```shell
   python main.py
   ```

> [!Note]
> By default the app will show up as a pop-up window in your computer. To run it as a webpage inside your browser: Go to main.py, set `native=False` inside `ui.run()`.
>
> Optional: If you want nicegui to reload the browser page every time it detects changes in the code set `reload=True`
>
> ```python
> ui.run(native=False, reload=True)
> ```
