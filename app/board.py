import os 

class initBoard(object):
    """ type: class
    Select type of device for connect to BCI 
    Parameters
    ----------
    config : string
        Config file to load. Must be in app directory. 
        It's possible to use multiple configs for different use.
    """

    def __init__(self, config='../conf/app.ini'):
        import configparser

        self.config = configparser.ConfigParser()
        self.config.read(config)
        print(self.config.sections())
        print(self.config['BCI-CONFIGURATION']['bci.board_type'])
        
        self.board_name = self.config['BCI-CONFIGURATION']['bci.board_type']
        self.board = self.connect(self.board_name)
        self.connected = self.board.state

    def connect(self, board_type):
        board_type = board_type.lower()
        if board_type == 'simulator':
            try:
                from modules.boards.sim_board.board import initBoard #TODO: This is fucked up, should import from ../modules/boards/sim_board.board class initBoard, but it doesnt.
                print ("Attach {} module...".format(self.board_name))
                
                return bci.OpenBCISimulator(
                    self.config['BCI-CUSTOM-OPTS']['bci.sim_electrodes'],
                    self.config['BCI-CONFIGURATION']['bci.sampling_rate'],
                )

            except NameError as e:
                raise e

        elif board_type == 'cyton':
            pass
            
        elif board_type == 'ganglion':
            pass
            
        else: 
            raise ValueError("Incorrect board type: {} \n Please provide valid board name!".format(board_type))

if __name__ == "__main__":
    a = initBoard()
    a.board_name
