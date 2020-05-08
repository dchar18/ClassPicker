# ClassPicker
Automated Python script that logs into university's course registration portal and finds a specified course in a specified term

Disclaimer: this only works for the University of Illinois at Chicago's course registration portal

To get the script to work:
1. Download the Selenium package (including chromedriver, which is place in /usr/local/bin/)
2. Replace the fields in Login.py with personal credentials
3. When running the script, execute the command in the form of "python3 Picker.py [course number]" and optionally the name of the subject if it is not "computer science"
