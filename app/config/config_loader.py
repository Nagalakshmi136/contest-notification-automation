import configparser
from app.utils.urls import CONFIG_FILE_PATH

# Initialize the configparser
config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH)

# Parsing configurations:

#code chef
CODECHEF_CONTESTS_XPATH = config['codechef']['contests_xpath']

#code forces
CODEFORCES_CONTESTS_XPATH = config['codeforces']['contests_xpath']
CODEFORCES_DATE_FORMAT = config['codeforces']['date_format']

# #coding ninjas
CODINGNINJAS_CONTESTS_XPATH = config['codingninjas']['contests_xpath']
CODINGNINJAS_DATE_FORMAT = config['codingninjas']['date_format']

#gfg
GFG_CONTESTS_XPATH = config['gfg']['contests_xpath']
GFG_DATE_FORMAT = config['gfg']['date_format']

#leet code
LEETCODE_CONTESTS_XPATH = config['leetcode']['contests_xpath']

# WhatsApp configurations
WHATSAPP_SEARCH_BOX_XPATH = config["WhatsApp"]["search_box_xpath"]
WHATSAPP_MESSAGE_TEXTFIELD_XPATH = config["WhatsApp"]["message_textfield_xpath"]
