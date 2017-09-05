#!/usr/bin/env python

import sys
from subprocess import check_output

def return_file_contents_as_var(file_name):
    with open(file_name, 'r') as infile:
        result_list = infile.readlines()
    if len(result_list) == 1:
        return result_list[0].strip()
    i = 0
    while i < len(result_list):
        result_list[i] = result_list[i].strip()
        i += 1
    return result_list

def return_normal_data_point_from_web_page(card, headers_string):
    full_url = 'http://shop.tcgplayer.com/magic' + card
    cmd = "curl --silent '%s' %s | grep -A10  '>Market Price' | grep -A1 Normal | grep '$' | tr -dc '0-9.'" % (full_url, headers_string)
    price_point = check_output(cmd, shell=True)
    #call(cmd, shell=True))
    print card + " " + price_point

def return_foil_data_point_from_web_page(card, headers_string):
    full_url = 'http://shop.tcgplayer.com/magic' + card
    cmd = "curl --silent '%s' %s | grep -A10  '>Market Price' | grep -A1 Foil | grep '$' | tr -dc '0-9.'" % (full_url, headers_string)
    price_point = check_output(cmd, shell=True)
    #call(cmd, shell=True))
    print card + " " + price_point


if __name__ == "__main__":
    normal_file = sys.argv[1]
    foil_file = sys.argv[2]
    headers_file = sys.argv[3]

    normal_list = return_file_contents_as_var(normal_file)
    foil_list = return_file_contents_as_var(foil_file)
    headers_string = return_file_contents_as_var(headers_file)
    print "Normal:"
    for card in normal_list:
        return_normal_data_point_from_web_page(card, headers_string)
    print "Foil:"
    for card in foil_list:
        return_foil_data_point_from_web_page(card, headers_string)




#   normal_list = File.readlines(normal_file)
#foil_list = File.readlines(foil_file)
#header_string = File.read(headers_file).strip