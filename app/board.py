import configparser


class initBoard(object):
    """ type: class
    Select type of device for connect to BCI 
    Parameters
    ----------
    config : string
        Config file to load. Must be in app directory. 
        It's possible to use multiple configs for different use.
    """

    def __init__(self, config='app.ini'):
        self.__config = configparser.ConfigParser()
        self.__config.read(config)
        
        self.board_name = self.__config['BCI-CONFIGURATION']['bci.board_type']
        self.board = self.connect(self.board_name)
        self.connected = self.board.state

    def connect(self, board_type):
        board_type = board_type.lower()
        if board_type == 'simulator':
            try:
                import modules.boards.sim_board.board as bci
                print ("Attach {} module...".format(self.board_name))
                
                return bci.OpenBCISimulator(
                    self.__config['BCI-CUSTOM-OPTS']['bci.sim_electrodes'],
                    self.__config['BCI-CONFIGURATION']['bci.sampling_rate'],
                )

            except NameError as e:
                raise e

        elif board_type == 'cyton':
            pass
            
        elif board_type == 'ganglion':
            pass
            
        else: 
            raise ValueError("Incorrect board type: {} \n Please provide valid board name!".format(board_type))

a = initBoard()
