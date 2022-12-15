# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 20:14:01 2022

@author: Yasin
"""

import random
import sys
import pygame as pg
import time

import math

from a_star import a_star, a_star_b

class Oyun:
    def __init__(self):
        self.harita = []
        self.harita_B = []
        self.N = 0
        self.M = 0
        self.Oi = 0
        self.Oj = 0
        self.Bi = 0
        self.Bj = 0
        self.Hi = 0
        self.Hj = 0
        self.win_flag = True
        self.lose_flag = True
        self.init()
        self.screen_size = 1260, 750
        self.width_cell = (self.screen_size[0] - 150 - 2 * 15) // self.M
        self.height_cell = (self.screen_size[1] - 2 * 15) // self.N
        self.screen = pg.display.set_mode(self.screen_size)
        pg.init()
        
    def _haritaApend(self):
        self.harita = []
        for i in range(self.N):
            temp = []
            for j in range(self.M):
                temp.append(0)
            self.harita.append(temp)
        self.harita_B = []
       
        for i in range(self.N):
            temp = []
            for j in range(self.M):
                temp.append(0)
            self.harita_B.append(temp)
 
    def init(self):
        self.inputs()
        self._haritaApend()

        self.Hi = self.N // 2
        self.Hj = self.M -1
        self.harita[self.Hi][self.Hj] = "H"

        self.Oi = self.N -1
        self.Oj = 0
        self.harita[self.Oi][self.Oj] = "O"

        self.Bi = 0
        self.Bj = 0
        self.harita[self.Bi][self.Bj] = "B"

        Ci = random.randint(0, self.N-1)
        Cj = random.randint(0, self.M-1)

        start = time.time()
        for i in range(int(self.N*self.M /5)):
            flag = 0
            while(flag == 0):
                flag = 0
                while not self.harita[Ci][Cj] == 0:
                    Ci = random.randint(0, self.N-1)
                    Cj = random.randint(0, self.M-1)
                self.harita[Ci][Cj] = "C"
                B_flag, _ = a_star(self.harita, self.Bi, self.Bj, self.Hi, self.Hj)
                O_flag, _ = a_star(self.harita, self.Oi, self.Oj, self.Hi, self.Hj, who="O")
                if O_flag == -1 or B_flag == -1:
                    self.harita[Ci][Cj] = 0       
                else:
                    flag = 1
            if (time.time() - start) > 1.5:
                self.init()
                return
            self.harita[Ci][Cj] = "C"
            
    def up(self):
        if self.harita[self.Oi][self.Oj] == " ^" or self.harita[self.Oi][self.Oj] == "O^":
            self.harita[self.Oi][self.Oj] = "*^"
        else:
            self.harita[self.Oi][self.Oj] = "* "
        if self.Oi == 0:
            self.Oi = self.N
        self.Oi = self.Oi-1
        if self.harita[self.Oi][self.Oj] == 0:
            self.harita[self.Oi][self.Oj] = "O"
        elif self.harita[self.Oi][self.Oj] == " ^":
            self.harita[self.Oi][self.Oj] = "O^"
        elif self.harita[self.Oi][self.Oj] == "* " or self.harita[self.Oi][self.Oj] == "*^" or self.harita[self.Oi][self.Oj] == "B" or self.harita[self.Oi][self.Oj] == "*B":
            self.Oi = self.Oi+1
            self.harita[self.Oi][self.Oj] = "O"
        elif self.harita[self.Oi][self.Oj] == "C":
            print("LOSE!")
            self.lose_flag = False
        
    def down(self):
        if self.harita[self.Oi][self.Oj] == " ^" or self.harita[self.Oi][self.Oj] == "O^":
            self.harita[self.Oi][self.Oj] = "*^"
        else:
            self.harita[self.Oi][self.Oj] = "* "
        if self.Oi == self.N-1:
            self.Oi = -1
        self.Oi = self.Oi+1
        if self.harita[self.Oi][self.Oj] == 0:
            self.harita[self.Oi][self.Oj] = "O"
        elif self.harita[self.Oi][self.Oj] == " ^":
            self.harita[self.Oi][self.Oj] = "O^"
        elif self.harita[self.Oi][self.Oj] == "* " or self.harita[self.Oi][self.Oj] == "*^" or self.harita[self.Oi][self.Oj] == "B" or self.harita[self.Oi][self.Oj] == "*B":
            self.Oi = self.Oi-1
            self.harita[self.Oi][self.Oj] = "O"
        elif self.harita[self.Oi][self.Oj] == "C":
            print("LOSE!")
            self.lose_flag = False

    def right(self):
        if self.harita[self.Oi][self.Oj] == " ^" or self.harita[self.Oi][self.Oj] == "O^":
            self.harita[self.Oi][self.Oj] = "*^"
        else:
            self.harita[self.Oi][self.Oj] = "* "
        if self.Oj == self.M-1:
            self.Oj = -1
        self.Oj = self.Oj+1
        if self.harita[self.Oi][self.Oj] == 0:
            self.harita[self.Oi][self.Oj] = "O"
        elif self.harita[self.Oi][self.Oj] == " ^":
            self.harita[self.Oi][self.Oj] = "O^"
        elif self.harita[self.Oi][self.Oj] == "* " or self.harita[self.Oi][self.Oj] == "*^" or self.harita[self.Oi][self.Oj] == "B" or self.harita[self.Oi][self.Oj] == "*B":
            self.Oj = self.Oj-1
            self.harita[self.Oi][self.Oj] = "O"
        elif self.harita[self.Oi][self.Oj] == "C":
            print("LOSE!")
            self.lose_flag = False

    def left(self):
        if self.harita[self.Oi][self.Oj] == " ^" or self.harita[self.Oi][self.Oj] == "O^":
            self.harita[self.Oi][self.Oj] = "*^"
        else:
            self.harita[self.Oi][self.Oj] = "* "
        if self.Oj == 0:
            self.Oj = self.M
        self.Oj = self.Oj-1
        if self.harita[self.Oi][self.Oj] == 0:
            self.harita[self.Oi][self.Oj] = "O"
        elif self.harita[self.Oi][self.Oj] == " ^":
            self.harita[self.Oi][self.Oj] = "O^"
        elif self.harita[self.Oi][self.Oj] == "* " or self.harita[self.Oi][self.Oj] == "*^" or self.harita[self.Oi][self.Oj] == "B" or self.harita[self.Oi][self.Oj] == "*B":
            self.Oj = self.Oj+1
            self.harita[self.Oi][self.Oj] = "O"
        elif self.harita[self.Oi][self.Oj] == "C":
            print("LOSE!")
            self.lose_flag = False
            
    def stuck(self):
        if (not self.harita[(self.Oi+1)%self.N][(self.Oj)%self.M] == 0) and (not self.harita[(self.Oi+1)%self.N][(self.Oj)%self.M] == "H"):
            if (not self.harita[(self.Oi-1)%self.N][(self.Oj)%self.M] == 0) and (not self.harita[(self.Oi-1)%self.N][(self.Oj)%self.M] == "H"):
                if (not self.harita[(self.Oi)%self.N][(self.Oj+1)%self.M] == 0) and (not self.harita[(self.Oi)%self.N][(self.Oj+1)%self.M] == "H"):
                    if (not self.harita[(self.Oi)%self.N][(self.Oj-1)%self.M] == 0) and (not self.harita[(self.Oi)%self.N][(self.Oj-1)%self.M] == "H"):
                        self.lose_flag = False
                        #self.display()
                        print("LOSE!")

    def inputs(self):
        self.N = 20
        while self.N < 4:
            self.N = int(input("4'ten büyük bir sayı girin:"))
        self.M = 30
        while self.M < 4:
            self.M = int(input("4'ten büyük bir sayı girin:"))
        return self.N, self.M

    def draw_numbers2(self):
        
        self.draw_background2()
        if self.height_cell > self.width_cell:
            font = pg.font.SysFont(None, self.width_cell)
            offset = 15 + int(self.width_cell / 3.3)
        else:
            font = pg.font.SysFont(None, self.height_cell)
            offset = 15 + int(self.height_cell / 3.3)
        row = 0 
        while row < self.N:
            col = 0
            while col < self.M:
                output = self.harita[row][col]
                if output == "O" or output == "* ":
                    n_text = font.render(str(output), True, pg.Color('green'))
                    self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                elif output == "B" or output == " ^":
                    n_text = font.render(str(output), True, pg.Color('cyan'))
                    self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))    
                elif output == "C":
                    n_text = font.render(str(output), True, pg.Color('red'))
                    self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                elif output == "H":
                    n_text = font.render(str(output), True, pg.Color('magenta'))
                    self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                elif output == "*^":
                    n_text = font.render(str("*"), True, pg.Color('green'))
                    n2_text = font.render(str("^"), True, pg.Color('cyan'))
                    self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                    self.screen.blit(n2_text, pg.Vector2((col * self.width_cell) + offset+15, (row * self.height_cell) + offset - 3))
                elif output == "*B":
                    n_text = font.render(str("B"), True, pg.Color('cyan'))
                    self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset+15, (row * self.height_cell) + offset - 3))
                elif output == "O^":
                    n_text = font.render(str("O"), True, pg.Color('green'))
                    self.screen.blit(n_text , pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                else:
                    n_text = font.render(" ", True, pg.Color('magenta'))
                    self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                col += 1
            row += 1
    
    def draw_numbers(self):
         
         self.draw_background()
         if self.height_cell > self.width_cell:
            font = pg.font.SysFont(None, self.width_cell)
            offset = 15 + int(self.width_cell / 3.3)
         else:
            font = pg.font.SysFont(None, self.height_cell)
            offset = 15 + int(self.height_cell / 3.3)
         row = 0
         while row < self.N:
             col = 0
             while col < self.M:
                 output = self.harita[row][col]
                 if output == "O":
                     pg.draw.rect(self.screen, pg.Color("white"), pg.Rect(self.width_cell*col + 15,self.height_cell*row + 15, self.width_cell, self.height_cell))
                     n_text = font.render(str(output), True, pg.Color('green'))
                     self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                 elif output == "B":
                     pg.draw.rect(self.screen, pg.Color("white"), pg.Rect(self.width_cell*col + 15,self.height_cell*row + 15, self.width_cell, self.height_cell))
                     n_text = font.render(str(output), True, pg.Color('cyan'))
                     self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))    
                 elif output == "H":
                     pg.draw.rect(self.screen, pg.Color("white"), pg.Rect(self.width_cell*col + 15,self.height_cell*row + 15, self.width_cell, self.height_cell))
                     n_text = font.render(str(output), True, pg.Color('magenta'))
                     self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                 elif output == "*B":
                     pg.draw.rect(self.screen, pg.Color("white"), pg.Rect(self.width_cell*col + 15,self.height_cell*row + 15, self.width_cell, self.height_cell))
                     n_text = font.render(str("B"), True, pg.Color('cyan'))
                     self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset+15, (row * self.height_cell) + offset - 3))
                 elif output == "O^":
                     pg.draw.rect(self.screen, pg.Color("white"), pg.Rect(self.width_cell*col + 15,self.height_cell*row + 15, self.width_cell, self.height_cell))
                     n_text = font.render(str("O"), True, pg.Color('green'))
                     self.screen.blit(n_text , pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                 if math.sqrt((self.Oi - row)**2) < 3 and math.sqrt((self.Oj - col)**2) < 3:
                     if output == "* ":
                         pg.draw.rect(self.screen, pg.Color("white"), pg.Rect(self.width_cell*col + 15,self.height_cell*row + 15, self.width_cell, self.height_cell))
                         n_text = font.render(str(output), True, pg.Color('green'))
                         self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                     elif output == " ^":
                         pg.draw.rect(self.screen, pg.Color("white"), pg.Rect(self.width_cell*col + 15,self.height_cell*row + 15, self.width_cell, self.height_cell))
                         n_text = font.render(str(output), True, pg.Color('cyan'))
                         self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))    
                     elif output == "C":
                         pg.draw.rect(self.screen, pg.Color("white"), pg.Rect(self.width_cell*col + 15,self.height_cell*row + 15, self.width_cell, self.height_cell))
                         n_text = font.render(str(output), True, pg.Color('red'))
                         self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                     elif output == "*^":
                         pg.draw.rect(self.screen, pg.Color("white"), pg.Rect(self.width_cell*col + 15,self.height_cell*row + 15, self.width_cell, self.height_cell))
                         n_text = font.render(str("*"), True, pg.Color('green'))
                         n2_text = font.render(str("^"), True, pg.Color('cyan'))
                         self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                         self.screen.blit(n2_text, pg.Vector2((col * self.width_cell) + offset+15, (row * self.height_cell) + offset - 3))
                     elif output == 0:
                         pg.draw.rect(self.screen, pg.Color("white"), pg.Rect(self.width_cell*col + 15,self.height_cell*row + 15, self.width_cell, self.height_cell))
                         n_text = font.render(str(""), True, pg.Color('green'))
                         self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                     #else:
                         #pg.draw.rect(self.screen, pg.Color("white"), pg.Rect(self.width_cell*col + 15,self.height_cell*row + 15, self.width_cell, self.height_cell))
                         #n_text = font.render(" ", True, pg.Color('magenta'))
                         #self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset, (row * self.height_cell) + offset - 3))
                 col += 1
             row += 1        
    
    def draw_background2(self):
        self.screen.fill(pg.Color("white"))
        pg.draw.rect(self.screen, pg.Color("black"), pg.Rect(15,15,self.screen_size[0] - 150 - 2 * 15,self.screen_size[1] -  2 * 15),5)
        
        i = 1
        while (i * self.width_cell) < (self.screen_size[0] - 150 - 2 * 15):
            pg.draw.line(self.screen, pg.Color("black"), pg.Vector2((i * self.width_cell) + 15, 15), pg.Vector2((i * self.width_cell) + 15, self.screen_size[1] - 15 - 3) , 5)
            i += 1
            
        i = 1
        while (i * self.height_cell) < (self.screen_size[1] - 2 * 15):
            pg.draw.line(self.screen, pg.Color("black"), pg.Vector2(15, (i * self.height_cell) + 15), pg.Vector2(self.screen_size[0] - 150 - 15 - 3, (i * self.height_cell) + 15), 5)
            i += 1
            
    def draw_background(self):
         self.screen.fill(pg.Color("black"))
         pg.draw.rect(self.screen, pg.Color("black"), pg.Rect(15,15,self.screen_size[0] - 150 - 2 * 15,self.screen_size[1] -  2 * 15),5)
         
         i = 1
         while (i * self.width_cell) < (self.screen_size[0] - 150 - 2 * 15):
             pg.draw.line(self.screen, pg.Color("black"), pg.Vector2((i * self.width_cell) + 15, 15), pg.Vector2((i * self.width_cell) + 15, self.screen_size[1] - 15 - 3) , 5)
             i += 1
             
         i = 1
         while (i * self.height_cell) < (self.screen_size[1] - 2 * 15):
             pg.draw.line(self.screen, pg.Color("black"), pg.Vector2(15, (i * self.height_cell) + 15), pg.Vector2(self.screen_size[0] - 150 - 15 - 3, (i * self.height_cell) + 15), 5)
             i += 1
             
    def shadow(self):
        pass
    
    def game_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP: #Up
                    self.up()
                    self.computer()
                elif event.key == pg.K_DOWN: #Down
                    self.down()
                    self.computer()
                elif event.key == pg.K_RIGHT: #Right
                    self.right()
                    self.computer()
                elif event.key == pg.K_LEFT: #Left
                    self.left() 
                    self.computer()
                elif event.key == pg.K_r: #Restart
                    self.init()

                result, _ = a_star(self.harita, self.Oi, self.Oj, self.Hi, self.Hj, who="O")
                if result == -1:
                    self.lose_flag = False
                    print("STUCK LOSE!")

        self.draw_background()
        self.draw_numbers2()
        pg.display.flip()

        if self.Hi == self.Oi and self.Hj == self.Oj:
            print("WIN!")
            self.win_flag = False


    def run(self):                
            while self.win_flag == True and self.lose_flag == True:
                self.game_loop()
            pg.quit()
            sys.exit()
            
    def computer(self):
        next_, self.harita_B = a_star_b(self.harita, self.harita_B, self.Bi, self.Bj, self.Hi, self.Hj)
        if next_ == -1:
                print("PC LOSE!")
        else:
            if self.harita[next_[0]][next_[1]] == 0 or self.harita[next_[0]][next_[1]] == "* ":
                if self.harita[self.Bi][self.Bj] == "B": 
                    self.harita[self.Bi][self.Bj] = " ^"
                elif self.harita[self.Bi][self.Bj] == "*B":
                    self.harita[self.Bi][self.Bj] = "*^"
                if self.harita[next_[0]][next_[1]] == 0:
                    self.harita[next_[0]][next_[1]] = "B"
                elif self.harita[next_[0]][next_[1]] == "* ":
                    self.harita[next_[0]][next_[1]] = "*B"
                self.Bi, self.Bj = next_[0], next_[1]
            elif self.harita[next_[0]][next_[1]] == "C":
                print("PC LOSE!")
            elif self.harita[next_[0]][next_[1]] == "H":
                print("PC WIN!")
                print("YOU LOSE!")
                self.lose_flag = False


oyun = Oyun()
oyun.run()
