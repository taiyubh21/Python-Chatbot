# Mohammad Taiyub Hussain

# Define conversation pairs
# Inputs and responses
conversationPairs = [
    [
        # Different inputs will lead to similar responses
        r"Hi|Hello|Hey",
        ["Hello, how can I help you today?", "Hi, what would you like help with?"]
    ],
    [
        r"How are you?",
        ["I'm fine. How are you?", "I'm well, and you?"]
    ],
    [
        r"I'm okay|I'm fine|I'm doing well",
        ["That's good to hear!", "That's nice to hear!"]
    ],
    [
        r"Define AI|What is meant by Artificial Intelligence?|What does Artificial Intelligence mean?|"\
        r"Definition of Artificial Intelligence|What is Artificial Intelligence?|What does AI Mean?|AI|Artificial Intelligence|What is AI?",
        ["Artificial Intelligence is computer science technology that emphasizes creating intelligent machine that can mimic human behavior. "
        "Artificial Intelligence can behave like a human, think like a human, and is also capable of decision making.", 
        "It's the study of methods for making computers behave intelligently. Roughly speaking, a computer is intelligent to the extent that "
        "it does the right thing rather than the wrong thing. The right thing is whatever action is most likely to achieve the goal, or, in more "
        "technical terms, the action that maximizes expected utility. AI includes tasks such as learning, reasoning, planning, perception, language "
        "understanding, and robotics."]
    ],
    [
        r"Why do we need Artificial Intelligence?|Why is Artificial Intelligence necessary?|What is the purpose of Artificial Intelligence?|"\
        r"Why do we require Artificial Intelligence?|Why do we need AI?|Why is AI necessary?",
        ["The goal of Artificial intelligence is to create intelligent machines that can mimic human behavior. "
         "We need AI for today's world to solve complex problems, make our lives more smoothly by automating the routine work, "
         "saving the manpower, and to perform many more other tasks."]
    ],
    [
        r"Give some real world applications of AI|Name a few real world uses for AI|Describe some actual applications of AI|"\
        r"Give some examples of AI's practical applications|Give some instances where AI has been used in the real world|"\
        r"Name a few real world uses for AI|Where has Artificial Intelligence been used in real life|"\
        r"Give some real world applications of Artificial Intelligence|Name a few real world uses for Artificial Intelligence|Real world applications",
        ["There are various real-world applications of AI, and some of them are given below:\n - Google Search Engine: When we start writing "
         "something on Google, we immediately get the relevant recommendations from google, and this is because of different AI technologies."
         "\n - Ridesharing Applications: Different ride-sharing applications such as Uber uses AI and machine learning to determine the type of ride, "
         "minimize the time once the car is hailed by the user, price of the ride, etc.\n - Spam Filters in Email: The AI is also used for email spam "
         "filtering so that you can get the important and relevant emails only in your inbox.\n - Social Networking: Different social networking sites "
         "such as Facebook, Instagram, Pinterest, etc., use the AI technology for different purposes such as face recognition and friend suggestions."
         "\n - Product recommendations: When we search for a product on Amazon, we get the recommendation for similar products, and this is because of "
         "different ML algorithms. Similarly, on Netflix, we get personalized recommendations for movies and web series."]
    ],
    [
        r"What are the types of AI?|What varieties of AI are there?|What varieties of AI exist?|Which kinds of AI are there?|What are the types of Artificial Intelligence?|" \
        r"What varieties of Artificial Intelligence are there?|What varieties of Artificial Intelligence exist?|Which kinds of Artificial Intelligence are there?|" \
        r"Types of AI",
        ["Artificial intelligence can be divided into different types on the basis of capabilities and functionalities.\n Based on Capabilities:\n - Weak AI or Narrow AI: "
         "Weak AI is capable of performing some dedicated tasks with intelligence. Siri is an example of Weak AI.\n - General AI: The intelligent machines that can "
         "perform any intellectual task with efficiency as a human. \n - Strong AI: It is the hypothetical concept that involves the machine that will be better than "
         "humans and will surpass human intelligence.\n Based on Functionalities:\n - Reactive Machines: Purely reactive machines are the basic types of AI. "
         "These focus on the present actions and cannot store the previous actions.\n - Limited Memory: As its name suggests, it can store the past data or experience "
         "for the limited duration. The self-driving car is an example of such AI types.\n - Theory of Mind: It is the advanced AI that is capable of understanding human "
         "emotions, people, etc., in the real world.\n - Self-Awareness: Self Awareness AI is the future of Artificial Intelligence that will have their own consciousness, "
         "emotions, similar to humans."]
    ],
    [
        r"What is machine learning?|Describe machine learning|What exactly is machine learning?|Machine learning",
        ["It's the branch of AI that explores ways to get computers to improve their performance based on experience."]
    ],
    [
        r"When will AI systems become more intelligent than people?|When will AI systems surpass human intelligence?|"\
        r"When will Artificial Intelligence systems surpass human intelligence?",
        ["This is a hard one to answer for several reasons. First, the word 'will' assumes that this a question of forecasting, like forecasting the weather, "
         "whereas in fact it includes an element of choice: it's unlikely ever to happen if we humans decide not to pursue it, for example. Second, the phrase "
         "'more intelligent' assumes a single linear scale of intelligence, which doesn't really exist. Already machines are much better at some tasks than humans, "
         "and of course much worse at others. Third, if we grant that there is some useful notion of 'general-purpose' intelligence that can be developed in machines, "
         "then the question does begin to make sense; but it's still very hard to answer. Achieving this kind of intelligence would require significant breakthroughs "
         "in AI research and those are very hard to predict. Most AI researchers think it might happen in this century."]
    ],
    [
        r"What can AI do now?|What can Artificial Intelligence do now?",
        ["The range of tasks where machines perform at a creditable level is much wider than it was a few years ago. It includes playing board games and card games, "
         "answering simple questions and extracting facts from newspaper articles, assembling complex objects, translating text from one language to another, "
         "recognizing speech, recognizing many kinds of objects in images, and driving a car under most 'normal' driving conditions. There are many less obvious "
         "kinds of tasks carried out by AI systems, including detecting fraudulent credit-card transactions, evaluating credit applications, and bidding in complex "
         "ecommerce auctions. Many of the functions of a search engine are in fact simple forms of AI."]
    ],
    [
        r"What impact will AI have on human society in the near future?|What impact will AI have on human society?|"\
        r"What kind of an impact will AI have in the near future on human society?|In the near future, what effects will AI have on human society?|"\
        r"What kind of a future will there be for AI in terms of human society?|What impact will Artificial Intelligence have on human society in the near future?|"\
        r"What impact will Artificial Intelligence have on human society?|What kind of an impact will Artificial Intelligence have in the near future on human society?|"\
        r"Impact of AI",
        ["It is quite likely that some major innovations will emerge in the foreseeable future. The self-driving car is already under active development and testing, "
         "with some companies promising first deliveries in the near future. (Other companies are being more cautious, recognizing the difficulties involved.) "
         "With improvements in computer vision and legged locomotion, robots for unstructured environments become practical; these might include agricultural and "
         "service settings and helping humans (especially the elderly and infirm) with domestic chores. Finally, as machines improve their grasp of language, search "
         "engines and 'personal assistants' on mobile phones will change from indexing web pages to understanding web pages, leading to qualitative improvements in their "
         "ability to answer questions, synthesize new information, offer advice, and connect the dots. AI may also have a substantial impact on areas of science, such as "
         "systems biology, where the complexity and volume of information challenges human abilities."]
    ],
    [
        r"What is the biggest misconception about AI?|What is the biggest misunderstanding about AI?|AI misconception|Artificial Intelligence misconception",
        ["A misconception of AI oversets its capacity, so AI is promoted as neutral, accessible and accurate. There are limitations to all of those things. "
         "AI reflects the values of the people who have created it. It is not accessible to people across the world or within particular countries. "
         "And it is often not particularly accurate; it is only as good as the way it has been programmed or the data it has been trained on.", 
         "One of the biggest misconceptions is that people think of AI as one big tool that can solve all problems automatically. AI must be trained, "
         "similar to us humans when we study a new area of knowledge."]
    ],
    [
        r"Why is ethics a concern with AI?|Why is ethics a concern with Artificial Intelligence?|Why is AI ethically problematic?|"\
        r"Why should ethics be an issue with AI?|Why is ethics a problem with AI?|Ethics concern AI|Concern of ethics",
        ["Ethics is a concern with AI, mainly because it wasn't designed with it in mind. Designers are now reverse-engineering AI data sets to better "
         "incorporate ethics as a priority. The reason there's an ethical concern about bias when it comes to AI is that AI can only be as ethical as those "
         "who write the training data, program it and audit it."]
    ],
    [
        r"How can companies ensure their automated AI technology can be trusted?|How can businesses verify the reliability of their automated AI technology?|"\
        r"What steps can businesses take to guarantee the reliability of their automated AI technology?|Artificial Intelligence reliability in business",
        ["- Identify when AI can correct bias and when humans can correct AI (often AI mirrors flaws that already exist in human decision making).\n"
         "- Educate yourself and your employees by engaging in discussions and continuing to learn about AI industry ethical best practice.\n"
         " - Promote the diversity of employees within the AI field.\n - Critique decision making from an ethical lens and test fairness perceptions on humans."]
    ],
    [
        r"bye|goodbye|quit|exit",
        ["Goodbye", "Take care"]
    ]
]