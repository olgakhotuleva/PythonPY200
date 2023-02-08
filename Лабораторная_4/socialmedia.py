import abc
from abc import ABC, abstractmethod


class Socialmedia(ABC):

    @abstractmethod
    def remove(self):
        print("Этот метод удаляет аккаунт пользователя")

    @abstractmethod
    def create_clone_page(self):
        print("Этот метод создает копию страницы пользователя")

