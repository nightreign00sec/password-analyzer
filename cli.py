#coding:utf-8
from analyzer.entropy import calculate_entropy
from analyzer.entropy import char_set_detector

password = input("Enter a password to analyze:\t")

char_set_detector(password)
calculate_entropy(password)
