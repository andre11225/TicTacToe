# TicTacToe with GUI

# The game board.
# 0 | 1 | 2   
#-----------
# 3 | 4 | 5 
#-----------
# 6 | 7 | 8 


from appJar import gui

# Variable Section
sec = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
x = 1

# Player scores
s1 = 0
s2 = 0


## Button Functions ============================================================

# 1
def press1():
        global x
        global s1
        global s2

        app.disableButton("1")
        
        if x == 1:
                app.setButton("1", "X")
                sec[0] = 'X'
                app.setLabel("f1", "Player 2 turn")
                app.setLabelBg("f1", "lightblue")
                x = 2
                
                # Player 1 victory conditions
                if sec[0] == 'X' and sec[1] == 'X' and sec[2] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                   
                elif sec[3] == 'X' and sec[4] == 'X' and sec[5] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[6] == 'X' and sec[7] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[3] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[1] == 'X' and sec[4] == 'X' and sec[7] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[5] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[4] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[4] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                
        else:
                app.setButton("1", "O")
                sec[0] = 'O'
                app.setLabel("f1", "Player 1 turn")
                app.setLabelBg("f1", "pink")
                x = 1

                # Player 2 victory conditions    
                if sec[0] == 'O' and sec[1] == 'O' and sec[2] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    app.setLabelBg("f1", "lightblue")
                 
                elif sec[3] == 'O' and sec[4] == 'O' and sec[5] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[6] == 'O' and sec[7] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[3] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[1] == 'O' and sec[4] == 'O' and sec[7] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[5] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[4] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[4] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    app.setLabelBg("f1", "lightblue")


# 2
def press2():
        global x
        global s1
        global s2
        
        app.disableButton("2")
        
        if x == 1:
                app.setButton("2", "X")
                sec[1] = 'X'
                app.setLabel("f1", "Player 2 turn")
                app.setLabelBg("f1", "lightblue")
                x = 2
                
                # Player 1 victory conditions
                if sec[0] == 'X' and sec[1] == 'X' and sec[2] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                   
                elif sec[3] == 'X' and sec[4] == 'X' and sec[5] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[6] == 'X' and sec[7] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[3] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[1] == 'X' and sec[4] == 'X' and sec[7] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[5] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[4] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[4] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")

                
        else:
                app.setButton("2", "O")
                sec[1] = 'O'
                app.setLabel("f1", "Player 1 turn")
                app.setLabelBg("f1", "pink")
                x = 1

                # Player 2 victory conditions    
                if sec[0] == 'O' and sec[1] == 'O' and sec[2] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                 
                elif sec[3] == 'O' and sec[4] == 'O' and sec[5] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[6] == 'O' and sec[7] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[3] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[1] == 'O' and sec[4] == 'O' and sec[7] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[5] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[4] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[4] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")

# 3
def press3():
        global x
        global s1
        global s2
        
        app.disableButton("3")
        
        if x == 1:
                app.setButton("3", "X")
                sec[2] = 'X'
                app.setLabel("f1", "Player 2 turn")
                app.setLabelBg("f1", "lightblue")
                x = 2
                
                # Player 1 victory conditions
                if sec[0] == 'X' and sec[1] == 'X' and sec[2] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                   
                elif sec[3] == 'X' and sec[4] == 'X' and sec[5] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[6] == 'X' and sec[7] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[3] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[1] == 'X' and sec[4] == 'X' and sec[7] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[5] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[4] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[4] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")

                
        else:
                app.setButton("3", "O")
                sec[2] = 'O'
                app.setLabel("f1", "Player 1 turn")
                app.setLabelBg("f1", "pink")
                x = 1

                # Player 2 victory conditions    
                if sec[0] == 'O' and sec[1] == 'O' and sec[2] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                 
                elif sec[3] == 'O' and sec[4] == 'O' and sec[5] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[6] == 'O' and sec[7] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[3] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[1] == 'O' and sec[4] == 'O' and sec[7] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[5] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[4] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[4] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")

# 4
def press4():
        global x
        global s1
        global s2

        app.disableButton("4")
        
        if x == 1:
                app.setButton("4", "X")
                sec[3] = 'X'
                app.setLabel("f1", "Player 2 turn")
                app.setLabelBg("f1", "lightblue")
                x = 2
                
                # Player 1 victory conditions
                if sec[0] == 'X' and sec[1] == 'X' and sec[2] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                   
                elif sec[3] == 'X' and sec[4] == 'X' and sec[5] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[6] == 'X' and sec[7] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[3] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[1] == 'X' and sec[4] == 'X' and sec[7] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[5] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[4] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[4] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")

                
        else:
                app.setButton("4", "O")
                sec[3] = 'O'
                app.setLabel("f1", "Player 1 turn")
                app.setLabelBg("f1", "pink")
                x = 1

                # Player 2 victory conditions    
                if sec[0] == 'O' and sec[1] == 'O' and sec[2] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                 
                elif sec[3] == 'O' and sec[4] == 'O' and sec[5] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[6] == 'O' and sec[7] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[3] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[1] == 'O' and sec[4] == 'O' and sec[7] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[5] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[4] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[4] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")


# 5
def press5():
        global x
        global s1
        global s2

        app.disableButton("5")
        
        if x == 1:
                app.setButton("5", "X")
                sec[4] = 'X'
                app.setLabel("f1", "Player 2 turn")
                app.setLabelBg("f1", "lightblue")
                x = 2
                
                # Player 1 victory conditions
                if sec[0] == 'X' and sec[1] == 'X' and sec[2] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                   
                elif sec[3] == 'X' and sec[4] == 'X' and sec[5] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[6] == 'X' and sec[7] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[3] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[1] == 'X' and sec[4] == 'X' and sec[7] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[5] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[4] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[4] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")

                
        else:
                app.setButton("5", "O")
                sec[4] = 'O'
                app.setLabel("f1", "Player 1 turn")
                app.setLabelBg("f1", "pink")
                x = 1

                # Player 2 victory conditions    
                if sec[0] == 'O' and sec[1] == 'O' and sec[2] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                 
                elif sec[3] == 'O' and sec[4] == 'O' and sec[5] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[6] == 'O' and sec[7] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[3] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[1] == 'O' and sec[4] == 'O' and sec[7] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[5] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[4] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[4] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")

# 6
def press6():
        global x
        global s1
        global s2

        app.disableButton("6")
        
        if x == 1:
                app.setButton("6", "X")
                sec[5] = 'X'
                app.setLabel("f1", "Player 2 turn")
                app.setLabelBg("f1", "lightblue")
                x = 2
                
                # Player 1 victory conditions
                if sec[0] == 'X' and sec[1] == 'X' and sec[2] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                   
                elif sec[3] == 'X' and sec[4] == 'X' and sec[5] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[6] == 'X' and sec[7] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[3] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[1] == 'X' and sec[4] == 'X' and sec[7] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[5] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[4] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[4] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")

                
        else:
                app.setButton("6", "O")
                sec[5] = 'O'
                app.setLabel("f1", "Player 1 turn")
                app.setLabelBg("f1", "pink")
                x = 1

                # Player 2 victory conditions    
                if sec[0] == 'O' and sec[1] == 'O' and sec[2] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                 
                elif sec[3] == 'O' and sec[4] == 'O' and sec[5] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[6] == 'O' and sec[7] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[3] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[1] == 'O' and sec[4] == 'O' and sec[7] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[5] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[4] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[4] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")

# 7
def press7():
        global x
        global s1
        global s2

        app.disableButton("7")
        
        if x == 1:
                app.setButton("7", "X")
                sec[6] = 'X'
                app.setLabel("f1", "Player 2 turn")
                app.setLabelBg("f1", "lightblue")
                x = 2
                
                # Player 1 victory conditions
                if sec[0] == 'X' and sec[1] == 'X' and sec[2] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                   
                elif sec[3] == 'X' and sec[4] == 'X' and sec[5] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[6] == 'X' and sec[7] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[3] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[1] == 'X' and sec[4] == 'X' and sec[7] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[5] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[4] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[4] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")

                
        else:
                app.setButton("7", "O")
                sec[6] = 'O'
                app.setLabel("f1", "Player 1 turn")
                app.setLabelBg("f1", "pink")
                x = 1

                # Player 2 victory conditions    
                if sec[0] == 'O' and sec[1] == 'O' and sec[2] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                 
                elif sec[3] == 'O' and sec[4] == 'O' and sec[5] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[6] == 'O' and sec[7] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[3] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[1] == 'O' and sec[4] == 'O' and sec[7] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[5] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[4] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[4] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
        
# 8
def press8():
        global x
        global s1
        global s2

        app.disableButton("8")
        
        if x == 1:
                app.setButton("8", "X")
                sec[7] = 'X'
                app.setLabel("f1", "Player 2 turn")
                app.setLabelBg("f1", "lightblue")
                x = 2
                
                # Player 1 victory conditions
                if sec[0] == 'X' and sec[1] == 'X' and sec[2] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                   
                elif sec[3] == 'X' and sec[4] == 'X' and sec[5] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[6] == 'X' and sec[7] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[3] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[1] == 'X' and sec[4] == 'X' and sec[7] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[5] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[4] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[4] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")

                
        else:
                app.setButton("8", "O")
                sec[7] = 'O'
                app.setLabel("f1", "Player 1 turn")
                app.setLabelBg("f1", "pink")
                x = 1

                # Player 2 victory conditions    
                if sec[0] == 'O' and sec[1] == 'O' and sec[2] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                 
                elif sec[3] == 'O' and sec[4] == 'O' and sec[5] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[6] == 'O' and sec[7] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[3] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[1] == 'O' and sec[4] == 'O' and sec[7] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[5] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[4] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[4] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")

# 9
def press9():
        global x
        global s1
        global s2

        app.disableButton("9")
        
        if x == 1:
                app.setButton("9", "X")
                sec[8] = 'X'
                app.setLabel("f1", "Player 2 turn")
                app.setLabelBg("f1", "lightblue")
                x = 2
                
                # Player 1 victory conditions
                if sec[0] == 'X' and sec[1] == 'X' and sec[2] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                   
                elif sec[3] == 'X' and sec[4] == 'X' and sec[5] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[6] == 'X' and sec[7] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[3] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[1] == 'X' and sec[4] == 'X' and sec[7] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[5] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[0] == 'X' and sec[4] == 'X' and sec[8] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    
                elif sec[2] == 'X' and sec[4] == 'X' and sec[6] == 'X':
                    s1 += 1
                    app.setLabel("s1", s1)
                    app.setLabel("f1", "PLAYER 1 WINS")
                    app.setLabelBg("f1", "pink")
                    

                
        else:
                app.setButton("9", "O")
                sec[8] = 'O'
                app.setLabel("f1", "Player 1 turn")
                app.setLabelBg("f1", "pink")
                x = 1

                # Player 2 victory conditions    
                if sec[0] == 'O' and sec[1] == 'O' and sec[2] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                 
                elif sec[3] == 'O' and sec[4] == 'O' and sec[5] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[6] == 'O' and sec[7] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[3] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                  
                elif sec[1] == 'O' and sec[4] == 'O' and sec[7] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[5] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                elif sec[0] == 'O' and sec[4] == 'O' and sec[8] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                   
                elif sec[2] == 'O' and sec[4] == 'O' and sec[6] == 'O':
                    s2 += 1
                    app.setLabel("s2", s2)
                    app.setLabel("f1", "PLAYER 2 WINS")
                    app.setLabelBg("f1", "lightblue")
                    
                    


# Reset button
def reset():
        global sec
        sec = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        global x
        x = 1
        for i in range(9):
                app.setButton(sec[i], sec[i])
                app.enableButton(sec[i])
                app.setLabel("f1", "Player 1 turn")
                app.setLabelBg("f1", "pink")


def reset2():
        global s1
        global s2
        s1 = 0
        s2 = 0
        app.setLabel("s1", s1)
        app.setLabel("s2", s2)
        
        
#===============================================================================


app=gui("Tic Tac Toe", "800x600")
app.setSticky("news")
app.setExpand("both")
app.setFont(20)

app.addButton("1", press1, row=0, column=0)
app.addButton("2", press2, row=0, column=1)
app.addButton("3", press3, row=0, column=2)

app.addButton("4", press4, row=1, column=0)
app.addButton("5", press5, row=1, column=1)
app.addButton("6", press6, row=1, column=2)

app.addButton("7", press7, row=2, column=0)
app.addButton("8", press8, row=2, column=1)
app.addButton("9", press9, row=2, column=2)

app.addLabel("s1", s1, row=0, column=4)
app.setLabelBg("s1", "pink")
app.addLabel("s2", s2, row=1, column=4)
app.setLabelBg("s2", "lightblue")

app.addButton("Reset Game", reset, row=3, column=4)
app.addButton("Reset Score", reset2, row=2, column=4)

app.addLabel("f1", "Player 1", row=3, colspan=3)
app.setLabelBg("f1", "pink")


app.go()





















