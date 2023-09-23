'''
NAME
    my_constants_1_2_1.py

DESCRIPTION
    Group constants described in uppercase text

AUTHOR   VERSION   DATE         COMMENT
gabor    1.2.1     2022-08-02   added #current directory, updated #strings
gabor    1.2.0     2022-05-28   added #time, updated #standard conversions
gabor    1.1.2     2022-05-15   updated #numbers and #strings
gabor    1.1.1     2022-05-13   updated #strings
gabor    1.1.0     2022-05-12   added #currencies and #separators, updated #strings
gabor    1.0.0     2022-05-08   creation
'''

from pathlib import Path

#currencies
DOLLAR = 'USD'
EURO = 'EUR'
POUND = 'PND'
SWISS_FRANK = 'CHF'

#current directory
CURRENT_DIR = Path(__file__).resolve().parent

#separators
BACKSLASH = '\\'
COMMA = ','
DASH = '-'
DOT = '.'
EXCLAMATION_MARK = '!'
HORIZONTAL_DOTS = '...'
QUESTION_MARK = '?'
SEMICOLON = ';'
SLASH = '/'
UNDERSCORE = '_'
VERTICAL_DOTS = ':'

#strings
AUTOMATIC = 'automatic'
BLANK = ''
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
DOUBLE_QUOTE = '"'
MANUAL = 'manual'
SINGLE_QUOTE = "'"
SPACE = ' '
VOWELS = 'aeiou'

#numbers
ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10
HUNDRED = 100
THOUSAND = 1000
HUNDRED_THOUSAND = 100000
MILLION = 1000000
PI = 3.1416

#standard conversions
HOUR_IN_DAY = 24          #hour
INCH_TO_CM = 2.54         #cm
KG_TO_POUND = 2.204623    #pound
KM_TO_MILE = 0.621371     #mile
KM_H_TO_M_S = 0.277778    #m/s
KM_H_TO_MILE_H = 0.621427 #mile/h
M_TO_YARD = 1.093613      #yard
M_S_TO_KM_H = 3.6         #km/h
MILE_TO_KM = 1.609344     #km
MILE_TO_YARD = 1760       #yard
MILE_H_TO_KM_H = 1.6092   #km/h
MIN_IN_HOUR = 60          #minute
POUND_TO_KG = 0.453592    #kg
SEC_IN_MIN = 60           #second
YARD_TO_M = 0.9144        #m
YARD_TO_MILE = 0.000568   #mile

#distances
CM_TO_CM = ONE
CM_TO_KM = ONE / HUNDRED_THOUSAND
CM_TO_M = ONE / HUNDRED
CM_TO_MILE = CM_TO_KM * KM_TO_MILE
CM_TO_MM = TEN
CM_TO_YARD = CM_TO_M * M_TO_YARD

M_TO_CM = HUNDRED
M_TO_KM = ONE / THOUSAND
M_TO_M = ONE
M_TO_MILE = M_TO_KM * KM_TO_MILE
M_TO_MM = THOUSAND

KM_TO_CM = HUNDRED_THOUSAND
KM_TO_KM = ONE
KM_TO_M = THOUSAND
KM_TO_MM = MILLION
KM_TO_YARD = KM_TO_M * M_TO_YARD
MM_TO_CM = ONE / TEN
MM_TO_KM = ONE / MILLION
MM_TO_M = ONE / THOUSAND
MM_TO_MILE = MM_TO_KM * KM_TO_MILE
MM_TO_MM = ONE
MM_TO_YARD = MM_TO_M * M_TO_YARD
MILE_TO_CM = MILE_TO_KM * KM_TO_CM
MILE_TO_M  = MILE_TO_KM * KM_TO_M
MILE_TO_MILE = ONE
MILE_TO_MM = MILE_TO_KM * KM_TO_MM
YARD_TO_CM = HUNDRED * YARD_TO_M
YARD_TO_KM = ONE / THOUSAND * YARD_TO_M
YARD_TO_MM = THOUSAND * YARD_TO_M
YARD_TO_YARD = ONE

#weight
G_TO_G = ONE
G_TO_KG = ONE / THOUSAND
G_TO_POUND = G_TO_KG * KG_TO_POUND
G_TO_MG = THOUSAND
G_TO_TON = ONE / MILLION
KG_TO_G = THOUSAND
KG_TO_KG = ONE
KG_TO_TON = ONE / THOUSAND
KG_TO_MG = MILLION
MG_TO_G = ONE / THOUSAND
MG_TO_KG = ONE / MILLION
MG_TO_POUND = MG_TO_KG * KG_TO_POUND
MG_TO_MG = ONE
MG_TO_TON = ONE / (THOUSAND * MILLION)
POUND_TO_G = POUND_TO_KG * KG_TO_G
POUND_TO_POUND = ONE
POUND_TO_TON = POUND_TO_KG * KG_TO_TON
POUND_TO_MG = POUND_TO_KG * KG_TO_MG
TON_TO_G = MILLION
TON_TO_KG = THOUSAND
TON_TO_POUND = TON_TO_KG * KG_TO_POUND
TON_TO_MG = THOUSAND * MILLION
TON_TO_TON = ONE

#speed
KM_H_TO_KM_H = ONE
M_S_TO_M_S = ONE
M_S_TO_MILE_H = M_S_TO_KM_H * KM_H_TO_MILE_H
MILE_H_TO_M_S = MILE_H_TO_KM_H * KM_H_TO_M_S
MILE_H_TO_MILE_H = ONE

#time
MIN_IN_DAY = MIN_IN_HOUR * HOUR_IN_DAY
SEC_IN_HOUR = SEC_IN_MIN * MIN_IN_HOUR
SEC_IN_DAY = SEC_IN_MIN * MIN_IN_HOUR * HOUR_IN_DAY