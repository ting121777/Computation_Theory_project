# TOC Project 2019

## Finite State Machine
/home/os2018/Documents/TOC-Project-2019/fsm.png

## Usage
The initial state is set to `user`.

* user
	* Input: "*"(any word, sentence, symbol, number...etc)
		* Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
		* State: `user` -> `hello`

* hello
        * Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
        	* State: `hello` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
        	* State: `hello` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
        	* State: `hello` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
        	* State: `hello` -> `hello`

* usage
	* Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
        	* State: `usage` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
        	* State: `usage` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
        	* State: `usage` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
        	* State: `usage` -> `hello`

* joke
	* Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
        	* State: `joke` -> `usage`

        * Input: "joke"
                * Reply: "Me: Dad, I'm hungry.\nDad: Hi Hungry! I'm Dad!\nMe: Dad, I'm serious...\nDad: No! You're hungry!\nMe: Are you kidding?\nDad: No! I'm Dad~\n\nLOL!\nWant another joke?\nEnter [joke]"
        	* State: `joke` -> `joke1`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
        	* State: `joke` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
        	* State: `joke` -> `hello`

* joke1
	* Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
        	* State: `joke1` -> `usage`

        * Input: "joke"
                * Reply: "Your brain has two parts.\nOne is left, and the other is right.\nYour left brain has nothing right.\nYour right brain has nothing left\n\nWOW, it's sarcastic\nWant another joke?\nEnter [joke]"
        	* State: `joke1` -> `joke2`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
        	* State: `joke1` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
        	* State: `joke1` -> `hello`

* joke2
	* Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
        	* State: `joke2` -> `usage`

        * Input: "joke"
                * Reply: "Knowledge is power. France is bacon\n\nemmm...a little hard,huh?\nWant another...oops, I have no joke\nQAQ"
        	* State: `joke2` -> `joke3`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
        	* State: `joke2` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
        	* State: `joke2` -> `hello`

* joke3
	* Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
        	* State: `joke3` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
        	* State: `joke3` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
        	* State: `joke3` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
        	* State: `joke3` -> `hello`

* song
	* Input: "yes"
                * Reply: "You can't leave without rhythm?\nThen you must hear this:\nhttps://www.youtube.com/watch?v=tjA7nAHOAww\n\nLet's keep going.\nDo you feel helpless about your life?\n[yes/no]"
        	* State: `song` -> `Audio`

        * Input: "no"
                * Reply: "You don't care about rhythm?\nThen why you ask for my recommends?\nWell, never mind~\nLet's keep going.\nDo you feel helpless about your life?\n[yes/no]"
        	* State: `song` -> `q2`
	
	* Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
        	* State: `song` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
        	* State: `song` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
        	* State: `song` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "yes", "no", "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
        	* State: `song` -> `hello`

* Audio
        * Input: "yes"
                * Reply: "You are not alone, pal\nSometimes I doubt that I was living in a little square box\nTry this:\nhttps://www.youtube.com/watch?v=hs29SkJhRZM&index=22&list=LLhmtPcxRod4yltoJVnBdYSQ&t=0s\n\nAhh! Forget about that\nDo you have or want a sweet sweet memory?\n[yes/no]"
                * State: `Audio` -> `Grow`

        * Input: "no"
                * Reply: "You feel happy about your life, huh?\nCongratulations!!!\n\nSo, you have a sweet sweet memory, right?\n[yes/no]"
                * State: `Audio` -> `q3`

        * Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
                * State: `Audio` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
                * State: `Audio` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
                * State: `Audio` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "yes", "no", "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
                * State: `Audio` -> `hello`

* q2
        * Input: "yes"
                * Reply: "You are not alone, pal\nSometimes I doubt that I was living in a little square box\nTry this:\nhttps://www.youtube.com/watch?v=hs29SkJhRZM&index=22&list=LLhmtPcxRod4yltoJVnBdYSQ&t=0s\n\nAhh! Forget about that\nDo you have or want a sweet sweet memory?\n[yes/no]"
                * State: `q2` -> `Grow`

        * Input: "no"
                * Reply: "You feel happy about your life, huh?\nCongratulations!!!\n\nSo, you have a sweet sweet memory, right?\n[yes/no]"
                * State: `q2` -> `q3`

        * Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
                * State: `q2` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
                * State: `q2` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
                * State: `q2` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "yes", "no", "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
                * State: `q2` -> `hello`

* Grow
	* Input: "yes"
                * Reply: "Ah~\nSweet sweet memory~\nLet's back to 2002\n--though I was born in 2018, www\nhttps://www.youtube.com/watch?v=u9BVsezZM-8&list=LLhmtPcxRod4yltoJVnBdYSQ&index=29\n\nSo so sweet~\nWant some sweeter love song?\n[yes/no]"
                * State: `Grow` -> `2002`

        * Input: "no"
                * Reply: "No sweet memory?\nThat's fine\nI can help you make some~\nTry this, sweet sweet love song!\n[yes/no]"
                * State: `Grow` -> `q4`

        * Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
                * State: `Grow` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
                * State: `Grow` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
                * State: `Grow` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "yes", "no", "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
                * State: `Grow` -> `hello`

* q3
        * Input: "yes"
                * Reply: "Ah~\nSweet sweet memory~\nLet's back to 2002\n--though I was born in 2018, www\nhttps://www.youtube.com/watch?v=u9BVsezZM-8&list=LLhmtPcxRod4yltoJVnBdYSQ&index=29\n\nSo so sweet~\nWant some sweeter love song?\n[yes/no]"
                * State: `q3` -> `2002`

        * Input: "no"
                * Reply: "No sweet memory?\nThat's fine\nI can help you make some~\nTry this, sweet sweet love song!\n[yes/no]"
                * State: `q3` -> `q4`

        * Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
                * State: `q3` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
                * State: `q3` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
                * State: `q3` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "yes", "no", "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
                * State: `q3` -> `hello`

* 2002
        * Input: "yes"
                * Reply: "Nothing to say just take this!\nhttps://www.youtube.com/watch?v=HJ54P8T9m8U&list=LLhmtPcxRod4yltoJVnBdYSQ&index=20\n\nNice song, huh?\nHowever, some people can't say their love out loud\nJust because they love the one whose sex is same with them\nTake this\n[yes/no]"
                * State: `2002` -> `9420`

        * Input: "no"
                * Reply: "Don't like love song?\nMaybe your love can't say out loud\nMaybe you love the one whose sex is same with you\nBut, hey!\nI'm here with you\n\nPeople who is homophobia, just Fxxx you\n[yes/no]"
                * State: `2002` -> `q5`

        * Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
                * State: `2002` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
                * State: `2002` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
                * State: `2002` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "yes", "no", "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
                * State: `2002` -> `hello`

* q4
        * Input: "yes"
                * Reply: "Nothing to say just take this!\nhttps://www.youtube.com/watch?v=HJ54P8T9m8U&list=LLhmtPcxRod4yltoJVnBdYSQ&index=20\n\nNice song, huh?\nHowever, some people can't say their love out loud\nJust because they love the one whose sex is same with them\nTake this\n[yes/no]"
                * State: `q4` -> `9420`

        * Input: "no"
                * Reply: "Don't like love song?\nMaybe your love can't say out loud\nMaybe you love the one whose sex is same with you\nBut, hey!\nI'm here with you\n\nPeople who is homophobia, just Fxxx you\n[yes/no]"
                * State: `q4` -> `q5`

        * Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
                * State: `q4` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
                * State: `q4` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
                * State: `q4` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "yes", "no", "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
                * State: `q4` -> `hello`

* 9420
        * Input: "yes"
                * Reply: "Everybody has right to love anyone\nhttps://www.youtube.com/watch?v=yFE6qQ3ySXE\nFxxx You!!!\nWell, that's all\nI have no song to recommend"
                * State: `9420` -> `FU`

        * Input: "no"
                * Reply: "Well...I have no song to recommend\nQAQ"
                * State: `9420` -> `QQ`

        * Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
                * State: `9420` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
                * State: `9420` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
                * State: `9420` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "yes", "no", "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
                * State: `9420` -> `hello`

* q5
        * Input: "yes"
                * Reply: "Everybody has right to love anyone\nhttps://www.youtube.com/watch?v=yFE6qQ3ySXE\nFxxx You!!!\nWell, that's all\nI have no song to recommend"
                * State: `q5` -> `FU`

        * Input: "no"
                * Reply: "Well...I have no song to recommend\nQAQ"
                * State: `q5` -> `QQ`

        * Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
                * State: `q5` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
                * State: `q5` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
                * State: `q5` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "yes", "no", "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
                * State: `q5` -> `hello`

* FU
	* Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
                * State: `FU` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
                * State: `FU` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
                * State: `FU` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
                * State: `FU` -> `hello`

* QQ
        * Input: "usage"
                * Reply: "Enter [song] I'll recommend you some my favorite songs!\nEnter [joke] I'll tell you some really funny jokes!\n-- at least I like them~"
                * State: `QQ` -> `usage`

        * Input: "joke"
                * Reply: "Teacher: Did your father help you with your assignment?\nMe: Nope! He did it all by himself.\n\nhahaha! I imply nothing\nWant another joke?\nEnter [joke]"
                * State: `QQ` -> `joke`

        * Input: "song"
                * Reply: "Let me recommend you some song, emmm...\nYou can't leave without rhythm, right?\n[yes/no]?"
                * State: `QQ` -> `song`

        * Input: "*"(any word, sentence, symbol, number...etc, except for "usage", "joke" and "song")
                * Reply: "Hello there!\nI'm an fsm AI~\nTo get more usage detail, please enter [usage]!"
                * State: `QQ` -> `hello`

