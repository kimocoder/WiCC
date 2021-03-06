#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    WiCC (Wifi Cracking Camp)
    GUI tool for wireless pentesting on WEP and WPA/WPA2 networks.
    Project developed by Pablo Sanz Alguacil, Miguel Yanes Fernández and Adan Chalkley,
    as the Group Project for the 3rd year of the Bachelor of Sicence in Computing in Digital Forensics and CyberSecurity
    at TU Dublin - Blanchardstown Campus
"""


class Interface:
    name = ""
    address = ""
    type = ""
    power = 0
    channel = 0

    def __init__(self, name, address, type, power, channel):
        """
        Constructor for the class Interface, corresponding to the available wireless interfaces
        :param name: name of the interface
        :param address: physical address
        :param type: mode that the interface is running on
        :param power: power (dB) of the interface
        :param channel: channel where it's running
        """
        self.name = name
        self.address = address
        self.type = type
        self.power = power
        self.channel = channel

    def __str__(self):
        """
        Creates a string with the info of the interface
        :return: string with info about the interface parameters
        """
        output = ""
        output.__add__("Name: " + self.name)
        output.__add__(" Address: " + self.address)
        output.__add__((" Type: " + self.type))
        output.__add__((" Power: " + self.power))
        output.__add__((" Channel: " + self.channel))
        return output

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_type(self):
        return self.type

    def get_power(self):
        return self.power

    def get_channel(self):
        return self.channel

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_type(self, type):
        self.type = type

    def set_power(self, power):
        self.power = power

    def set_channel(self, channel):
        self.channel = channel

    def get_list(self):
        """
        Creates a list with the parameters of the interface
        :return: list of parameters
        """
        list = []
        list.append(self.name)
        list.append(self.address)
        list.append(self.type)
        list.append(self.power)
        list.append(self.channel)
        return list
