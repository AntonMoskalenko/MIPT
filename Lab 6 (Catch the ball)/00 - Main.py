import tkinter as tk
from random import randint, choice
import math


def main():
    global WIDTH, HEIGHT, root, canvas, balls, score, score_text, speed, player
    WIDTH = 600
    HEIGHT = 400
    score = 0

    # Canvas creation
    root = tk.Tk()

    player_info()

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
    exit_button = tk.Button(root, activeforeground='red', text='Exit', width=20, command=exit_button_click)

    canvas.pack()
    exit_button.pack()

    score_text = canvas.create_text(WIDTH, HEIGHT, text="Score: " + str(score),
                                    anchor=tk.SE, fill="red", font=('Arial', 15, 'bold'))

    speed = 50
    balls = []
    add_ball()

    canvas.bind('<Button-1>', click_handler)

    tick()

    root.mainloop()


def player_info():
    """Player identification"""

    q_label = tk.Label(root, fg='black', width=20, text='Please enter your name:')
    data_entry = tk.Entry(root, width=20)
    save_button = tk.Button(root, text='Save', command=lambda: save_button_click(q_label, save_button, data_entry))

    q_label.pack()
    data_entry.pack()
    save_button.pack()


class Ball:
    def __init__(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.r = randint(20, 50)
        self.x = randint(self.r, WIDTH - self.r)
        self.y = randint(self.r, HEIGHT - self.r)
        self.dx, self.dy = (+2, +3)
        self.ball_id = canvas.create_oval(self.x - self.r,
                                          self.y - self.r,
                                          self.x + self.r,
                                          self.y + self.r,
                                          fill=choice(colors))

    def view(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r > WIDTH or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r > HEIGHT or self.y - self.r <= 0:
            self.dy = -self.dy

    def inside_ball(self, x, y):
        if math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2) <= self.r:
            return True
        else:
            return False

    def kill(self):
        canvas.delete(self.ball_id)


def click_handler(event):
    """Clicking inside or ouside the ball - scoring"""
    global score, ball_id
    miss = 0
    if len(balls) == 0:
        score -= 10
    else:
        for ball in balls:
            if ball.inside_ball(event.x, event.y) is True:
                ball.kill()
                score += 10
            else:
                miss += 1
        if miss == len(balls):
            score -= 10
    canvas.itemconfigure(score_text, text="Score: " + str(score))


def tick():
    """Drawing canvas"""
    for ball in balls:
        ball.move()
        ball.view()
    root.after(speed, tick)


def add_ball():
    """Adding ball every 2,5 seconds"""
    global speed
    new_ball = Ball()
    balls.append(new_ball)
    if speed > 10: speed -= 5
    canvas.after(2500, add_ball)


def save_button_click(q_label, save_button, data_entry):
    """Recording player name and showing it on canvas"""
    global player
    player = data_entry.get()

    q_label.destroy()
    save_button.destroy()
    data_entry.destroy()

    canvas.create_text(0, HEIGHT, text="Player: " + player,
                       anchor=tk.SW, fill="red", font=('Arial', 15, 'bold'))


def exit_button_click():
    """Scoring is left as simple - no valuation of existing table
    (last record is always added"""

    root.destroy()
    file = open("TopScores.txt", "r+")

    score_table = file.readlines()
    if len(score_table) >= 5: score_table.pop(4)
    if len(str(score)) == 2:
        score_txt = '0' + str(score)
    else:
        score_txt = str(score)
    score_table.append("Score: " + str(score_txt) + "\tPlayer: " + player + "\n")
    score_table.sort(reverse=True)

    file.close()
    file = open("TopScores.txt", "w")
    file.writelines(score_table)


if __name__ == "__main__":
    main()