## Package/Library Overview

Name: Aryan Rahman

## 1. Which package/library did you select?

    I decided to use Pandas as a supporting library and Pygame as the primary library for this project. While Pandas is used to save, sort, and save leaderboard scores in a CSV file, Pygame is used to construct the game window, create the Tetris board, handle keyboard input, and control the game loop.


## 2. What is the package/library?

    1.    What purpose does it serve?

            The pygame library in Python is used for creating games and graphical applications. It helps display the game window, draw the board and blocks, show text such as the score and controls, detect keyboard input, and update the screen continuously while the game is running.

            In this project, pygame is used to create the Tetris window, move and rotate the tetromino pieces, show the next piece preview, display the score and leaderboard, and show the game-over popup when the board is full.

            The pandas library in Python is used for organizing, storing, and manipulating data in a table format. It is especially useful when working with structured data such as rows and columns.

            In this project, pandas is used for the leaderboard system. It reads scores from a CSV file, adds new scores after a game ends, sorts the scores from highest to lowest, and saves the updated leaderboard back into the file.

    2.    How do you use it?

            You first need to install the libraries, then import them into your Python files before using their functions and classes.

            In this project, pygame is imported in the main game files to manage graphics, events, timing, and text display.

            Example:
                import pygame

            Pandas is imported in the scoreboard file to manage the score table and CSV file.

            Example:
                import pandas as pd

    To install it?

            If you are using Visual Studio Code, open the terminal and type:

                pip install pygame
                pip install pandas

            If needed, update pip3 by typing:

                pip3 install --upgrade pip

            Then install the libraries by typing:

                pip3 install pygame
                pip3 install pandas

    Basic functions used when using pygame

    pygame.init()

            This function initializes the pygame modules needed for the game.

    pygame.display.set_caption(TITLE)

            This function sets the title of the game window.

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

            This creates the game window with the width and height given in the settings file.

    clock = pygame.time.Clock()

            This creates a clock object to help control how fast the game updates.

    clock.tick(FPS)

            This controls the frame rate of the game and makes the program refresh a fixed number of times per second.

    pygame.time.set_timer(FALL_EVENT, FALL_INTERVAL_MS)

            This is used to create a timed event so that the tetromino pieces automatically fall after a certain interval.

    pygame.draw.rect(...)

            This function is used many times in the project to draw the Tetris board, side panel, preview box, blocks, and popup boxes.

    pygame.font.Font(None, size)

            This function creates font objects that are used to display text such as the score, controls, leaderboard, and game-over message.

    pygame.display.flip()

            This updates the whole display every frame so that the user can see the latest version of the game screen.

    Example block of code

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == FALL_EVENT and not game.game_over:
                    game.tick_down()

                if event.type == pygame.KEYDOWN:
                    if game.game_over:
                        if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                            scoreboard.add_score("Player", game.score)
                            game.reset()
                        elif event.key == pygame.K_r:
                            game.reset()
                        continue

                    if event.key == pygame.K_LEFT:
                        game.move_left()
                    elif event.key == pygame.K_RIGHT:
                        game.move_right()
                    elif event.key == pygame.K_DOWN:
                        game.move_down(manual=True)
                    elif event.key == pygame.K_UP:
                        game.rotate()
                    elif event.key == pygame.K_r:
                        game.reset()

            In this example, the game keeps running inside an infinite loop until the user closes the window.

            pygame.event.get() collects all events happening during the game, such as quitting the window, pressing keys, or timed falling events.

            event.type is used to check what kind of event happened. In this project, it is used to close the game, move pieces, rotate pieces, restart the game, and make pieces fall automatically.

    Function used when using pandas

    pd.read_csv()

            This function reads the scores from the CSV file so that previous leaderboard data can be loaded when the game starts.

            Example:
                df = pd.read_csv(self.filename)

    pd.DataFrame()

            This function creates a new row of score data in table form before adding it to the existing leaderboard.

            Example:
                new_row = pd.DataFrame([{"player": player, "score": int(score)}])

    pd.concat()

            This function combines the old leaderboard data with the new score row.

    sort_values()

            This function sorts the leaderboard scores from highest to lowest.

    to_csv()

            This function saves the updated leaderboard data back into the CSV file.

    Example block of code

            def add_score(self, player: str, score: int) -> None:
                new_row = pd.DataFrame([{"player": player, "score": int(score)}])
                self.data = pd.concat([self.data, new_row], ignore_index=True)
                self.data = self.data.sort_values(by="score", ascending=False).reset_index(drop=True)
                self.data.to_csv(self.filename, index=False)

            In this example, pandas is used to create a new score entry, add it to the leaderboard, sort the scores, and save them into the CSV file.

            This is how the leaderboard in the Tetris game is updated after each game ends.


## 3. What are the functionalities of the package/library?

    Functionalities of Pygame

        Pygame has a lot of helpful options for creating games. The primary functions utilized in this project are:

            i. Create a display to launch the primary game window
            ii. Sketching the side panel, popup boxes, tetromino blocks, and board
            iii. Event handling to recognize user input, including restart instructions and arrow keys
            iv. Keyboard controls that let the user to rotate and move parts
            v. Font rendering to show leaderboard text, instructions, and score text
            vi. Scheduling the automated fall of parts at predetermined intervals
            vii. The board, side panel, and preview box are positioned using rectangles and layout tools.


    Functionalities of Pandas

        Several helpful data-handling features are offered by Pandas. The primary ones in this project are:

            i.Reading CSV files using read_csv()
            ii. Creating tabular data using DataFrame()
            iii. Combining rows using concat()
            iv. Sorting values using sort_values()
            v. Saving files using to_csv()


## 4. When was it created?

    Pygame was founded on October 28, 2000, and has since grown to become one of the most widely used Python tools for creating 2D games.
    One of the most popular Python libraries for data analysis and structured data management, Pandas was first made available on January 11, 2008.


## 5. Why did you select this package/library?

    I chose Pygame because it is easily accessible and has very straightforward formatting, which is a huge benefit for novices like me. Additionally, I required a library that could construct a graphical window, draw moving pieces, detect keyboard input, and control a real-time game loop because my project is a Tetris game. Because Pygame has all of these capabilities in one library, it was a wise decision.

    Pandas was my choice because the game required a leaderboard system. Managing scores in an organized manner, appropriately sorting them, and saving them to a CSV file were all made much simpler using pandas. Pygame and Pandas worked well to enable me to integrate data administration and graphics into a single project.


## 6. How did learning the package/library influence your learning of the language?

    Learning Pygame helped me understand Python more deeply because it showed me how Python can be used for interactive, real-time applications instead of only simple scripts. I had to work with loops, conditionals, classes, functions, constants, and multiple files in a practical project.

    Learning Pandas also improved my Python skills by teaching me how to manage data in a cleaner and more efficient way. I learned how Python can be used not only for graphics and gameplay, but also for reading, sorting, and saving structured information like leaderboard scores.

    Overall, these libraries helped me see that Python is flexible enough to support both game development and data handling in the same program.


## 7. How was your overall experience with the package/library?

    My overall experience with Pygame and Pandas was positive. Pygame gave me the tools to create a complete game interface with controls, movement, drawing, and timing. Pandas made the leaderboard system much easier to build and organize.

        1. When would I recommend these libraries to someone?

            I would suggest Pygame because it offers basic capabilities for graphics, animation, music, and keyboard controllers, making Python game production much simpler. It is easy to use for beginners, excellent for learning programming fundamentals, and enables you to make interactive games without requiring a complicated setup. Regarding pandas, I would suggest it since it greatly simplifies, expedites, and organizes data processing. Large data sets may be effectively cleaned, analyzed, and manipulated by users, which is particularly helpful in data science, business, and research.

        2. Would I continue using these libraries?

           Yes, I would keep using these libraries since Pandas makes handling and analyzing data lot faster and more structured, while Pygame makes creating interactive games simple. Both libraries are highly helpful for upcoming programming and data-related tasks, save time, and are easy to use for beginners.

           
## References

1. Pygame Documentation: i. https://en.wikipedia.org/wiki/Pygame
                         ii. https://www.pygame.org/docs/
2. Pandas Documentation: i. https://en.wikipedia.org/wiki/Pandas_(software)
                         ii. https://pandas.pydata.org/docs/