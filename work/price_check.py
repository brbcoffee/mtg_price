#!/usr/bin/env python

import sys
from subprocess import check_output

def return_file_contents_as_var(file_name):
    with open(file_name, 'r') as infile:
        result_list = infile.readlines()
    i = 0
    while i < len(result_list):
        result_list[i] = result_list[i].strip()
        i += 1
    return result_list

def return_normal_data_point_from_web_page(card):
    full_url = 'https://www.mtggoldfish.com/price' + card + '#paper'
    search_string = "type\'>PAPER"
    cmd = "curl --silent '%s' | grep -A1 \"%s\" | grep price-box-price | tr -dc '0-9.'" % (full_url, search_string)
    price_point = check_output(cmd, shell=True)
    #call(cmd, shell=True))
    print card + " " + price_point

def return_foil_data_point_from_web_page(card):
    full_url = 'https://www.mtggoldfish.com/price' + card + '#paper'
    search_string = "type\'>PAPER"
    cmd = "curl --silent '%s' | grep -A1 \"%s\" | grep price-box-price | tr -dc '0-9.'" % (full_url, search_string)
    price_point = check_output(cmd, shell=True)
    #call(cmd, shell=True))
    print card + " " + price_point


if __name__ == "__main__":
    normal_file = sys.argv[1]
    foil_file = sys.argv[2]
    normal_list = return_file_contents_as_var(normal_file)
    foil_list = return_file_contents_as_var(foil_file)
    print "Normal:"
    for card in normal_list:
        return_normal_data_point_from_web_page(card)
    print "Foil:"
    for card in foil_list:
        return_foil_data_point_from_web_page(card)
