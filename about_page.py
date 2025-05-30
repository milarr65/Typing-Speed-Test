from nicegui import ui

def about_page():
        
  with ui.column().classes('items-center justify-start h-full') as about_content:  
    
    ui.label("ABOUT THIS PROJECT").classes('rm-md text-bold text-3xl')

    ui.markdown("This app is an assignment of the Udemy course **_100 Days of Code: The Complete Python Pro Bootcamp._** We were given full creative freedom to develop the app. My version is based on [Monkeytype](https://monkeytype.com/), which is one of my favorite sites to procrastinate on hehe. So most of the functionality is the same.")

    ui.markdown("Originally this was supposed to be built with tkinter, but I came across a youtube video that briefly talked about [NiceGUI](https://nicegui.io/) and after reading their docs I couldn't resist trying it. I'm actually super happy I did it, it's been fun learning to use this framework, even though I feel that my code is a bit of a mess because I'm still a beginner programmer 😅.")

    with ui.row().classes('items-center self-start text-2xl'):
      ui.icon('help_outline').classes('material-symbols-outlined')
      ui.label("How it works").classes('rm-md text-bold')

    with ui.column().classes('items-start'):
      with ui.row().classes('items-center text-lg'):
        ui.icon('format_align_left').classes('material-symbols-outlined')
        ui.label("Word Samples").classes('rm-md text-bold')

      ui.label('By default this test is using the top 200 most common words in the English language. But you can choose a bigger set of words in the settings menu. The available options are 200 words, 500, 1k, 3k and 5k. Remember that the bigger the sample size, the more rare words you\'ll get.')
      ui.markdown('Word lists provided by [google-10000-english](https://github.com/first20hours/google-10000-english) on Github')

    with ui.column().classes('items-start'):
      with ui.row().classes('items-center text-lg'):
        ui.icon('rocket').classes('material-symbols-outlined')
        ui.label('Difficulty').classes('rm-md text-bold')

    
      ui.label("Each level of difficulty prioritizes words of different length, what does this mean? In easy mode, you'll get mostly short words along with some medium length ones. In medium mode, you'll mostly get medium length words, with some long words mixed in. In hard mode, as you can imagine, you'll be getting mostly long words.")
      ui.label('It is recommended to select a longer test runtime to match medium or hard mode, in order to get better results after each test.')

    with ui.column().classes('items-start mb-2'):
      with ui.row().classes('items-center text-lg'):
        ui.icon('leaderboard').classes('material-symbols-outlined')
        ui.label('Stats').classes('rm-md text-bold')

      with ui.column().classes('gap-1'):
        ui.markdown("""
                    **_Wpm_** - Words per minute. The amount of correctly typed characters per minute.\n
                    **_Raw_** - Same as wpm, but it takes into account incorrect characters.\n
                    **_Accuracy_** - The percentage of correctly typed characters.\n
                    **_Cpm_** - Characters per minute.
                    """)

        ui.label("All stats are calculated after the test ends and are normalized to 60 seconds. Unfortunately nothing is calculated live during the test because I didn't have time to implement that. In the future I might add live stats and maybe a chart similar to monkeytype's.")

  return about_content