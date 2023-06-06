def get_move(self):
        '''
        Function to get move from other peer
        Get message using socket, and check if it is valid
        If is valid, send ACK message
        If is not, close socket and quit
        '''
        ###################  Fill Out  #######################
        msg = self.socket.recv(SIZE).decode() # get message using socket

        ip_address = self.recv_ip
        msg_valid_check = check_msg(msg, ip_address)
         
        
        if not msg_valid_check: # Message is not valid
            self.socket.close()   
            quit(self)
            
        else:  # If message is valid - send ack, update board and change turn

            ack_msg = "ACK"
            self.socket.send(ack_msg.encode())

            loc = 5 # received next-move
            
            ######################################################   
            
            
            #vvvvvvvvvvvvvvvvvvv  DO NOT CHANGE  vvvvvvvvvvvvvvvvvvv
            self.update_board(self.computer, loc, get=True)
            if self.state == self.active:  
                self.my_turn = 1
                self.l_status_bullet.config(fg='green')
                self.l_status ['text'] = ['Ready']
            #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                


def send_debug(self):
        '''
        Function to send message to peer using input from the textbox
        Need to check if this turn is my turn or not
        '''

        if not self.my_turn:
            self.t_debug.delete(1.0,"end")
            return
        # get message from the input box
        d_msg = self.t_debug.get(1.0,"end")
        d_msg = d_msg.replace("\\r\\n","\r\n")   # msg is sanitized as \r\n is modified when it is given as input
        self.t_debug.delete(1.0,"end")
        
        ###################  Fill Out  #######################
        start_index = d_msg.find("(")
        end_index = d_msg.find(")")

        if start_index != -1 and end_index != -1:
            coordinates = d_msg[start_index+1:end_index]
            tmp = coordinates
            n1, n2 = d_msg.strip("()").split(",")

            n1 = int(n1)
            n2 = int(n2)
            if n1 == 0:
                loc = n2
            elif n1 == 1:
                loc = 2*n1+n2+1
            elif n1 == 2:
                loc = 3*n1+n2
        
        
        if self.board[loc] == 0:
            self.socket.close()
            self.quit()
        self.socket.sendto(d_msg.encode(),(self.send_ip, self.port))
        ack, addr = self.socket.recvfrom(SIZE)
        
        if ack.decode() != "ACK":
            return False

        ######################################################  
        
        #vvvvvvvvvvvvvvvvvvv  DO NOT CHANGE  vvvvvvvvvvvvvvvvvvv
        self.update_board(self.user, loc)
            
        if self.state == self.active:    # always after my move
            self.my_turn = 0
            self.l_status_bullet.config(fg='red')
            self.l_status ['text'] = ['Hold']
            _thread.start_new_thread(self.get_move,())
            
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        


def send_move(self,selection):
        '''
        Function to send message to peer using button click
        selection indicates the selected button
        '''
        row,col = divmod(selection,3)
        ###################  Fill Out  #######################

        # send message and check ACK
        msg = f"SEND ETTTP/1.0\r\nHost:{self.send_ip}\r\nNew-Move:({row},{col})\r\n\r\n"
        self.socket.send(msg.encode())

        ack_msg = self.socket.recv(SIZE).decode()

        if ack_msg == "ACK":
            return True
        else:
            self.socket.close()
            quit(self)

        ######################################################  





 def check_result(self,winner,get=False):
        '''
        Function to check if the result between peers are same
        get: if it is false, it means this user is winner and need to report the result first
        '''
        # no skeleton
        ###################  Fill Out  #######################

        if get:  #내가 졌을 때
            opponent_result = self.socket.recv(SIZE).decode().strip()
            if opponent_result == str(self):
                return True
            else:
                return False
        else:   #내가 이겼을 때
            self.socket.send(self.encode())
            opponent_result = self.socket.recv(SIZE).decode().strip()
            if opponent_result == str(winner):
                return True
            else:
                return False

        ######################################################  



def check_msg(msg, recv_ip):
    '''
    Function that checks if received message is ETTTP format
    '''
    ###################  Fill Out  #######################

    if not msg.startswith("SEND ETTTP/1.0\r\n"):
        return False
    
    ip_start = msg.find("Host:") + len("Host:")
    ip_end = msg.find("\r\n", ip_start)
    if ip_start == -1 or ip_end == -1:
        return False
    
    received_ip = msg[ip_start:ip_end].strip()
    if received_ip == recv_ip:
        return True

    return False
    ######################################################  
