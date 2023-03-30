from bcolors import bcolors
import new_game
import os
from credits import credits

try:
    os.system('clear')
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} ┌────────────────┐{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │                │{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │                │{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │           xxxxxxxxxxx{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │        xx             xx{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │       x   ┌─────────┐   x{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW} _   _                                          {bcolors.GREEN}   ____                        _  {bcolors.RESET} {bcolors.BOLD} │      xx   │  x   x  │   xx{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __   {bcolors.GREEN}  / ___| __ _ _ __ ___   ___  | | {bcolors.RESET} {bcolors.BOLD} │      x    │         │    x{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  {bcolors.GREEN} | |  _ / _` | '_ ` _ \ / _ \ | | {bcolors.RESET} {bcolors.BOLD} │      x    │   ___   │   x{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}|  _  | (_| | | | | (_| | | | | | | (_| | | | | {bcolors.GREEN} | |_| | (_| | | | | | |  __/ |_| {bcolors.RESET} {bcolors.BOLD} │       xx  └─────────┘ xx{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| {bcolors.GREEN}  \____|\__,_|_| |_| |_|\___| (_) {bcolors.RESET} {bcolors.BOLD} │          xxxxxxxxxxxxx{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                   |___/                        {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │           ┌────┬─────┐{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │           │    │     │{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │                │{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │                │{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │                │{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │                │{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │            ┌───┴───┐{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │            │       │{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │{bcolors.RESET}")
    print (f"{bcolors.BOLD} {bcolors.YELLOW}                                                {bcolors.GREEN}                                  {bcolors.RESET} {bcolors.BOLD} │{bcolors.RESET}")
    print (f"{bcolors.BOLD}                                                                            ─────────┴────────{bcolors.RESET}")
    input(bcolors.BOLD +"                                           Press INTRO to start \n \n                                           Press CTRL+C to exit" + bcolors.RESET)
    os.system('clear')
    new_game.new_game()
except:
    credits()
