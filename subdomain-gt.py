#!/usr/bin/python3
"""
#############################################################################
#          SUBDOMAIN:GT - SUB-DOMAIN INFORMATION GATHERING TOOL             #
#############################################################################
# Copyright 2021 Alchemists                                                 #
#############################################################################
# A SUBDOMAIN:GT - SUB-DOMAIN INFORMATION GATHERING TOOL (c) 2021           #
# This work is marked with CC0 1.0 Universal.                               #
# To view a copy of this license, visit                                     #
#                                                                           #
# http://creativecommons.org/publicdomain/zero/1.0                          #
#                                                                           #
# Unless required by applicable law or agreed to in writing, software       #
# distributed under the License is distributed on an "AS IS" BASIS,         #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
# See the License for the specific language governing permissions and       #
# limitations under the License.                                            #
#############################################################################
#                               ABOUT Alchemists                            #
#############################################################################
#           |   Github      |   Twitter     |   GMail                       #
############|###############|###############|################################
# Developer |   hexdee606   |   hexdee606   |   hexdee606                   #
# Tester    |   Itachi-91   |   Itachi_9197 |   itachiuchiha9197            #
# Tester    |   Paradox44   |   Paradox_044 |   paradoxhex44                #
# Tester    |   athena-077  |   athena_077  |   athena74047                 #
#############################################################################
# this script is written in Python3 using PyCharm Community Edition 2021    #
# for Linux operating system. We hope you enjoy our work.                   #
# This software program is written for educational purposes only if you     #
# received any legal notice from cyber cell/ police then we will not        #
# responsible for that. use this script for your own risk.                  #
#############################################################################
"""

# Import Some Important Repository
import os
import sys

try:
    import requests
except ImportError:
    print("################################################################")
    print("# {:<60} #".format("Installing missing repository..."))
    print("################################################################")
    try:
        if os.name == 'nt':
            _ = os.system('python3 -m pip3 install requests')
        else:
            _ = os.system('pip3 install requests')
    except Exception as e:
        try:
            _ = os.system('pip3 install requests')
        except Exception as ee:
            print("|--------------------------------------------------|")
            print("| ERROR #1 : SOMETHING WRONG HERE.                 |")
            print("|--------------------------------------------------|")
            print("|                    ERROR MESSAGE                 |")
            print("|--------------------------------------------------|")
            print(str(ee))
            print("|--------------------------------------------------|")
            sys.exit()

import requests


def clear():
    """
    This function help  to clear your terminal/ command prompt window.
    :return: clear terminal/ command prompt window.
    """
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def error_message(fatal_error, message):
    """
    This function is created to display error message in proper manner.
    :param fatal_error: is boolean, use for terminate program if fatal error is occurred.
    :param message: message want to display, we use this for exception techniques.
    :return: display error message in proper manner.
    """
    try:
        clear()
        print("|--------------------------------------------------|")
        print("| ERROR #1 : SOMETHING WRONG HERE.                 |")
        print("|--------------------------------------------------|")
        print("|                    ERROR MESSAGE                 |")
        print("|--------------------------------------------------|")
        print(str(message))
        print("|--------------------------------------------------|")
        if fatal_error:
            sys.exit()
        return True
    except Exception as err:
        print("|--------------------------------------------------|")
        print("| ERROR #2 : SOMETHING WRONG HERE.                 |")
        print("|--------------------------------------------------|")
        print("|                    ERROR MESSAGE                 |")
        print("|--------------------------------------------------|")
        print(str(err))
        print("|--------------------------------------------------|")
        sys.exit()


def welcome_message():
    print("################################################################")
    print("# {:<60} #".format("SUBDOMAIN:GT - SUB-DOMAIN INFORMATION GATHERING TOOL"))
    print("################################################################")
    print("# {:<17} : {:<40} #".format("Version", "0.0.0.2"))
    print("# {:<17} : {:<40} #".format("Build", "BETA-20210825P0745-Kali_Linux_2021.2"))
    print("# {:<17} : {:<40} #".format("License type", "CC0 1.0 Universal"))
    print("# {:<17} : {:<40} #".format("Coded using", "PyCharm 2021.1.3 (Community Edition)"))
    print("################################################################")
    print("# {:<17} : {:<40} #".format("Team Name", "Alchemists"))
    print("# {:<17} : {:<40} #".format("Developer", "Hexdee606"))
    print("# {:<17} : {:<40} #".format("Tester", "Paradox44"))
    print("# {:<17} : {:<40} #".format("Tester", "Itachi-91"))
    print("# {:<17} : {:<40} #".format("Tester", "athena-077"))
    print("################################################################")


clear()
welcome_message()
print("# {:<60} #".format("Downloading subdomain list . . ."))
print("################################################################")
try:
    git_url = "https://raw.githubusercontent.com/hexdee606/SubDomain-GT/master/subdomains.txt"
    with open("subdomains.txt", "wb") as git_file:
        git_response = requests.get(git_url)
        git_file.write(git_response.content)
except Exception as e:
    error_message(True, e)

total_scan_count = 0
subdomain_count = 0
try:
    clear()
    welcome_message()
    print("# {:<60} #".format("This script scans up to 1000 common subdomain"))
    print("################################################################")
    domain = input("Please Enter domain name [example: google.com]: ")
    clear()
    welcome_message()
    print("# {:<60} #".format("Discovered subdomains are: "))
    print("################################################################")
    print("# {:<60} #".format("To exit use Ctrl + C"))
    print("################################################################")
    msg_string = "Discovered subdomains for {} are: ".format(domain)
    print("# {:<60} #".format(msg_string))
    print("################################################################")

    file = open("subdomains.txt")
    content = file.read()
    subdomains = content.splitlines()
    discovered_subdomains = []
    for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"
        try:
            total_scan_count += 1
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            subdomain_count += 1
            print("# [{:<3}] {:<19} : {}".format(subdomain_count, "Discovered subdomain", url))
            discovered_subdomains.append(url)

    with open("discovered_subdomains.txt", "w") as f:
        for subdomain in discovered_subdomains:
            print(subdomain, file=f)
    print("################################################################")
    print("# {:<40} : {:<17} #".format("Total discovered subdomain", subdomain_count))
    print("# {:<40} : {:<17} #".format("Total subdomain scanned", total_scan_count))
    print("################################################################")
except KeyboardInterrupt:
    clear()
    welcome_message()
    print("# {:<60} #".format("We hope you enjoy"))
    print("################################################################")
    print("# {:<40} : {:<17} #".format("Total discovered subdomain", subdomain_count))
    print("# {:<40} : {:<17} #".format("Total subdomain scanned", total_scan_count))
    print("################################################################")
except Exception as e:
    error_message(True, e)
