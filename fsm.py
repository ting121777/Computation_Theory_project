from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

#    def is_going_to_state1(self, event):
#        if event.get("message"):
#            text = event['message']['text']
#            return text.lower() == 'go to state1'
#        return False

#    def is_going_to_state2(self, event):
#        if event.get("message"):
#            text = event['message']['text']
#            return text.lower() == 'go to state2'
#        return False

    def on_enter_hello(self, event):
        print("I'm entering hello")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!")

    def on_exit_hello(self, event):
        print('Leaving hello')

    def on_enter_usage(self, event):
        print("I'm entering usage")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~")

    def on_exit_usage(self, event):
        print('Leaving usage')

    def on_enter_song(self, event):
        print("I'm entering song")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?")

    def on_exit_song(self, event):
        print('Leaving song')

    def on_enter_joke(self, event):
        print("I'm entering joke")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]")

    def on_exit_joke(self, event):
        print('Leaving joke')

    def on_enter_joke1(self, event):
        print("I'm entering joke1")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Me: Dad, I'm hungry.\nDad: Hi Hungry! I'm Dad!\nMe: Dad, I'm serious...\nDad: No! You're hungry!\nMe: Are you kidding?\nDad: No! I'm Dad~\n\nLOL!\nWant another joke?\nEnter [joke]")

    def on_exit_joke1(self, event):
        print('Leaving joke1')

    def on_enter_joke2(self, event):
        print("I'm entering joke2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Your brain has two parts.\nOne is left, and the other is right.\nYour left brain has nothing right.\nYour right brain has nothing left\n\nWOW, it's sarcastic\nWant another joke?\nEnter [joke]")

    def on_exit_joke2(self, event):
        print('Leaving joke2')

    def on_enter_joke3(self, event):
        print("I'm entering joke3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Knowledge is power. France is bacon\n\nemmm...a little hard,huh?\nWant another...oops, I have no joke\nQAQ")

    def on_exit_joke3(self, event):
        print('Leaving joke3')

    def on_enter_Audio(self, event):
        print("I'm entering Audio")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "You can't leave without rhythm?\nThen you must hear this:\nhttps://www.youtube.com/watch?v=tjA7nAHOAww\n\nLet's keep going.\nDo you feel helpless about your life?\n[yes/no]")

    def on_exit_Audio(self, event):
        print('Leaving Audio')

    def on_enter_q2(self, event):
        print("I'm entering q2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "You don't care about rhythm?\nThen why you ask for my recommends?\nWell, never mind~\nLet's keep going.\nDo you feel helpless about your life?\n[yes/no]")

    def on_exit_q2(self, event):
        print('Leaving q2')

    def on_enter_Grow(self, event):
        print("I'm entering Grow")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "You are not alone, pal\nSometimes I doubt that I was living in a little square box\nTry this:\nhttps://www.youtube.com/watch?v=hs29SkJhRZM&index=22&list=LLhmtPcxRod4yltoJVnBdYSQ&t=0s\n\nAhh! Forget about that\nDo you have or want a sweet sweet memory?\n[yes/no]")

    def on_exit_Grow(self, event):
        print('Leaving Grow')

    def on_enter_q3(self, event):
        print("I'm entering q3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "You feel happy about your life, huh?\nCongratulations!!!\n\nSo, you have a sweet sweet memory, right?\n[yes/no]")

    def on_exit_q3(self, event):
        print('Leaving q3')

    def on_enter_2002(self, event):
        print("I'm entering 2002")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Ah~\nSweet sweet memory~\nLet's back to 2002\n--though I was born in 2018, www\nhttps://www.youtube.com/watch?v=u9BVsezZM-8&list=LLhmtPcxRod4yltoJVnBdYSQ&index=29\n\nSo so sweet~\nWant some sweeter love song?\n[yes/no]")

    def on_exit_2002(self, event):
        print('Leaving 2002')

    def on_enter_q4(self, event):
        print("I'm entering q4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "No sweet memory?\nThat's fine\nI can help you make some~\nTry this, sweet sweet love song!\n[yes/no]")

    def on_exit_q4(self, event):
        print('Leaving q4')

    def on_enter_9420(self, event):
        print("I'm entering 9420")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Nothing to say just take this!\nhttps://www.youtube.com/watch?v=HJ54P8T9m8U&list=LLhmtPcxRod4yltoJVnBdYSQ&index=20\n\nNice song, huh?\nHowever, some people can't say their love out loud\nJust because they love the one whose sex is same with them\nTake this\n[yes/no]")

    def on_exit_9420(self, event):
        print('Leaving 9420')

    def on_enter_q5(self, event):
        print("I'm entering q5")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Don't like love song?\nMaybe your love can't say out loud\nMaybe you love the one whose sex is same with you\nBut, hey!\nI'm here with you\n\nPeople who is homophobia, just Fxxx you\n[yes/no]")

    def on_exit_q5(self, event):
        print('Leaving q5')

    def on_enter_FU(self, event):
        print("I'm entering FU")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Everybody has right to love anyone\nhttps://www.youtube.com/watch?v=yFE6qQ3ySXE\nFxxx You!!!\nWell, that's all\nI have no song to recommend")

    def on_exit_FU(self, event):
        print('Leaving FU')

    def on_enter_QQ(self, event):
        print("I'm entering QQ")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Well...I have no song to recommend\nQAQ")

    def on_exit_QQ(self, event):
        print('Leaving QQ')
