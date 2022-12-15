# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:51:13 2022

@author: Yasin
"""

from oyun_lib2 import Oyun

    
oyun = Oyun()
oyun.run()

    
"""
def draw_numbers(N=9,M=9):
    offset = 35

    
    for row in disp_harita:
        for col in row:
            if col == "O" or col == "*":
                n_text = font.render(str(col), True, pg.Color('green'))
                screen.blit(n_text, pg.Vector2((col * 80) + offset + 5,(row * 80) + offset - 2))
""" 