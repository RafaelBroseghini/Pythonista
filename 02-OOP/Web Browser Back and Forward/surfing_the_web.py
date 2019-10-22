#!/usr/bin/env python
"""
This python script imitates how
the 'back' and 'forward' functionality
in a Web Browser work.

Using two stacks, one is able to
re create this functionality by
popping and pushing from one stack
into the other and keeping a reference
to the current_url.
"""
from browser import Browser

def surf_the_web(browser):
  inp = input("Site you want to visit: ")
  browser.current_url = inp

  while inp != "None":
    current = inp

    browser.check_back_and_forth(inp)

    if inp == "back":
      browser.go_back()
    elif inp == "forward":
      browser.go_forward()
    else:
      if current != browser.current_url:
        browser.backward.push(browser.current_url)
        browser.current_url = current

    inp = input("Site you want to visit: ")

def main():
  chrome = Browser()
  surf_the_web(chrome)

if __name__ == "__main__":
  main()
