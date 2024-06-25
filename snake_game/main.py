from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
EXTERNAL_SQUARE_WIDTH = CANVAS_WIDTH
EXTERNAL_SQUARE_HEIGHT = CANVAS_HEIGHT
INNER_SQUARE_WIDTH = EXTERNAL_SQUARE_WIDTH - 40
INNER_SQUARE_HEIGHT = EXTERNAL_SQUARE_HEIGHT - 40

SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1

def main():
    '''
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # EXTERNAL SQUARE
    canvas.create_rectangle(0,0,EXTERNAL_SQUARE_WIDTH,EXTERNAL_SQUARE_HEIGHT,color='#9bba5a')
    
    # INNER SQUARE
    border_top_left_x = (EXTERNAL_SQUARE_WIDTH - INNER_SQUARE_WIDTH)/2
    border_top_left_y = (EXTERNAL_SQUARE_HEIGHT - INNER_SQUARE_HEIGHT)/2 
    
    canvas.create_rectangle(
        border_top_left_x,
        border_top_left_y,
        EXTERNAL_SQUARE_WIDTH - border_top_left_x,
        EXTERNAL_SQUARE_HEIGHT - border_top_left_y,
        color='#9bba5a', 
        outline = 'black')
    # TODO: your code here
    
    player = canvas.create_rectangle(
        border_top_left_x,
        border_top_left_y,
        border_top_left_x + SIZE,
        border_top_left_y + SIZE,
        color='black'
    )
    goal = canvas.create_rectangle(360,360,360 + SIZE, 360 + SIZE, color= 'pink')    
    
    new_x = border_top_left_x
    new_y = border_top_left_y
    change_x = SIZE
    change_y = 0
    goal_x = 360
    goal_y = 360
    score = 0
    delay_with_score = DELAY
    while True:
        key = canvas.get_new_key_press()
        if key == 'ArrowLeft':
            change_x = -SIZE
            change_y = 0
        if key == 'ArrowRight':
            change_x = SIZE
            change_y = 0
        if key == 'ArrowUp':
            change_y = -SIZE
            change_x = 0
        if key == 'ArrowDown':
            change_y = SIZE
            change_x = 0
        old_x = canvas.get_left_x(player)
        old_y = canvas.get_top_y(player)
        new_x += change_x
        new_y += change_y        
        canvas.moveto(player,new_x,new_y)

        x = canvas.get_left_x(player)
        y = canvas.get_top_y(player)

        if (
            (x + SIZE > EXTERNAL_SQUARE_WIDTH - border_top_left_x) or 
            (y + SIZE > EXTERNAL_SQUARE_HEIGHT - border_top_left_y) or 
            (x < border_top_left_x) or 
            (y < border_top_left_y)
        ):
            game_over_square = canvas.create_rectangle(
                border_top_left_x,
                border_top_left_y,
                EXTERNAL_SQUARE_WIDTH - border_top_left_x,
                EXTERNAL_SQUARE_HEIGHT - border_top_left_y,
                color='#8bc34a', 
                outline = 'black'
            )

            font_size = 24
            text_game_over = canvas.create_text(EXTERNAL_SQUARE_WIDTH/2 - font_size*3, 
                                   EXTERNAL_SQUARE_HEIGHT/2 - font_size*2,
                                   text=str('GAME OVER'),
                                   font_size=font_size)

            score_text = canvas.create_text(EXTERNAL_SQUARE_WIDTH/2 - font_size*3, 
                                   EXTERNAL_SQUARE_HEIGHT/2 - font_size,
                                   text=str(f"SCORE: {score}"),
                                   font_size=font_size)

            play_square = canvas.create_rectangle(
                EXTERNAL_SQUARE_WIDTH * 1/4 ,
                (EXTERNAL_SQUARE_HEIGHT * 3/5) ,
                EXTERNAL_SQUARE_WIDTH * 3/4,
                (EXTERNAL_SQUARE_HEIGHT * 4/5),
                color='white', 
                outline = 'black'
            )

            play_text = canvas.create_text(EXTERNAL_SQUARE_WIDTH * 1/4 + font_size, 
                                   (EXTERNAL_SQUARE_HEIGHT * 3/5) + font_size,
                                   text=str("PLAY AGAIN"),
                                   font_size=font_size)
            while True:
                click = canvas.get_last_click()
                if click:
                    x_mouse_position = canvas.get_mouse_x()
                    y_mouse_position = canvas.get_mouse_y()
                    overlappings_objects = canvas.find_overlapping(x_mouse_position,y_mouse_position,x_mouse_position,y_mouse_position)
                    if len(overlappings_objects) > 0:
                        for elem in overlappings_objects:
                            if elem == play_square or elem == play_text:
                                main()
            
                   
          

        if x == goal_x and y == goal_y:
            score += 5
            delay_with_score -= 0.01
            canvas.delete(goal)
            num_x = random.randint(border_top_left_x,EXTERNAL_SQUARE_HEIGHT-border_top_left_x-SIZE)
            while num_x % 20 != 0 and num_x != EXTERNAL_SQUARE_HEIGHT - border_top_left_y - SIZE:
                num_x = random.randint(border_top_left_x,EXTERNAL_SQUARE_HEIGHT-border_top_left_x-SIZE)
            goal_x = num_x
            num_y = random.randint(border_top_left_y,EXTERNAL_SQUARE_HEIGHT - border_top_left_y-SIZE)
            while num_y % 20 != 0 and num_y != EXTERNAL_SQUARE_HEIGHT - border_top_left_y-SIZE:
                num_y = random.randint(border_top_left_y,EXTERNAL_SQUARE_HEIGHT - border_top_left_y-SIZE)
            goal_y = num_y
            goal = canvas.create_rectangle(goal_x,goal_y,goal_x + SIZE, goal_y + SIZE, color= 'pink')    

        time.sleep(delay_with_score)
        canvas.mainloop()

    # Keep the canvas window open when running in local IDE.
    # Wait for the user to close the window.
    '''
if __name__ == '__main__':
    main()