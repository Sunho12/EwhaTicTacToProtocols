def get_move(self):
        '''
        Function to get move from other peer
        Get message using socket, and check if it is valid
        If is valid, send ACK message
        If is not, close socket and quit
        '''
        ###################  Fill Out  #######################
        msg = self.socket.recv(SIZE).decode() # get message using socket

        ip_address = '127.0.0.1'
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
        '''
        Check if the selected location is already taken or not
        '''

        '''
        Send message to peer
        '''
        
        '''
        Get ack
        '''
        
        loc = 5 # peer's move, from 0 to 8

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
        
        return True
        ######################################################  




def check_result(self,winner,get=False):
        '''
        Function to check if the result between peers are same
        get: if it is false, it means this user is winner and need to report the result first
        '''
        # no skeleton
        ###################  Fill Out  #######################

        


        return True
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
