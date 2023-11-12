from abc import ABC,abstractmethod


class Base_CLS:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def display_menu(self):
        pass
    
    @abstractmethod
    def display_data(self):
        pass
    
    @abstractmethod
    def add_data(self):
        pass
    
    @abstractmethod
    def update_data(self):
        pass
    
    @abstractmethod
    def delete_data(self):
        pass
    
    @abstractmethod
    def search_id(self):
        pass
    
    @abstractmethod
    def search_name(self):
        pass