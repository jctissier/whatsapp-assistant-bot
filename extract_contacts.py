from bs4 import BeautifulSoup


# Testing
def make_soup(filename):
    html = open(filename)
    return BeautifulSoup(html, "lxml")
#     data = make_soup(filename="scraped.html")
#     find_chats(html=data)


# Helpers
def filter_all_tags(soup, html_tag, att, att_name):
    return soup.findAll(html_tag, {att, att_name})


def filter_one_tag(soup, html_tag, att, att_name):
    return soup.find(html_tag, {att, att_name})


def find_chats(html, **kwargs):
    CHAT_BOXES_CLASS = "_2wP_Y"
    CHAT_NAME_SPAN = "_1wjpf"
    CHAT_TIME_SPAN = "_3T2VG"
    CHAT_UNREAD_SPAN = "OUeyt"

    chats_info = {}
    total_chats_unanswered = 0

    if not kwargs.get('testing'):
        html = BeautifulSoup(html, "lxml")
    chats = filter_all_tags(html, "div", "class", CHAT_BOXES_CLASS)
    print(len(chats))

    for i, chat in enumerate(chats):
        chat_name = filter_one_tag(chat, "span", "class", CHAT_NAME_SPAN).text
        chat_time = filter_one_tag(chat, "span", "class", CHAT_TIME_SPAN).text
        try:
            chat_unread = int(filter_one_tag(chat, "span", "class", CHAT_UNREAD_SPAN).text)
            total_chats_unanswered += 1
        except AttributeError:
            chat_unread = 0
        
        # start the chat numbering at 1
        chats_info[i+1] = {
                            "chat_name": chat_name,
                            "chat_time": chat_time,
                            "chat_unread": chat_unread
                        }

    print(chats_info)
    print("You have a total of " + str(len(chats)) + " chats")
    print("Chats with messages waiting: " + str(total_chats_unanswered))
