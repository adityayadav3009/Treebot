import random
import streamlit as st

st.title("TREE BOT")
# dictionary

tree_data = {
    "Oak": {
        "questions": [
            "What is the average lifespan of an oak tree?",
            "Where are oak trees commonly found?",
            "What are the different species of oak trees?"
        ],
        "answers": [
            "The average lifespan of an oak tree is about 200 years.",
            "Oak trees are commonly found in North America, Europe, and Asia.",
            "There are over 600 species of oak trees."
        ]
    },
    "Pine": {
        "questions": [
            "How tall can pine trees grow?",
            "What are the uses of pine trees?",
            "Do all pine trees have needles?"
        ],
        "answers": [
            "Some pine trees can grow up to 200 feet tall.",
            "Pine trees are used for lumber, paper production, and Christmas trees.",
            "Yes, all pine trees have needles."
        ]
    },
    "Maple": {
        "questions": [
            "What is the national tree of Canada?",
            "What are the different types of maple trees?",
            "Do maple trees produce sap?"
        ],
        "answers": [
            "The national tree of Canada is the maple tree.",
            "There are several species of maple trees, including sugar maple, red maple, and silver maple.",
            "Yes, maple trees produce sap, which is used to make maple syrup."
        ]
    },
    "Birch": {
        "questions": [
            "What is the distinctive feature of birch trees?",
            "Where are birch trees commonly found?",
            "Are there any medicinal uses of birch trees?"
        ],
        "answers": [
            "Birch trees are known for their distinctive white bark.",
            "Birch trees are commonly found in temperate regions of the Northern Hemisphere.",
            "Birch trees have medicinal uses, such as the extraction of birch sap for its diuretic properties."
        ]
    },
    "Willow": {
        "questions": [
            "What are the physical characteristics of willow trees?",
            "Where do willow trees typically grow?",
            "Are there any cultural or symbolic associations with willow trees?"
        ],
        "answers": [
            "Willow trees have slender, flexible branches and narrow leaves.",
            "Willow trees are typically found near bodies of water, such as rivers and lakes.",
            "Willow trees have cultural and symbolic associations with healing, wisdom, and grief."
        ]
    },
    "Cherry": {
        "questions": [
            "What are the different types of cherry trees?",
            "When do cherry trees usually bloom?",
            "What are the culinary uses of cherries?"
        ],
        "answers": [
            "There are various types of cherry trees, including sweet cherry and sour cherry.",
            "Cherry trees usually bloom in spring, typically around March or April.",
            "Cherries are used in various culinary preparations, such as pies, jams, and beverages."
        ]
    }
}


def get_random_question(tree_type):
    questions = tree_data[tree_type]["questions"]
    return random.choice(questions)

def get_answer(question, tree_type):
    questions = tree_data[tree_type]["questions"]
    answers = tree_data[tree_type]["answers"]
    index = questions.index(question)
    return answers[index]

st.write("TreeBot: Hello! I can help you with questions about trees. Please choose a tree type from the available options.")
st.write("TreeBot: Available options: Oak, Pine, Maple , Birch ,Willow , Cherry")  

# Ask the user to select a tree type
tree_type = st.selectbox("Tree: ",("Oak", "Pine", "Maple", "Birch","Willow", "Cherry") )

# Validate the tree type
if tree_type not in tree_data:
    st.text("TreeBot: I'm sorry, I don't have information about that tree type.")
else:
    st.text("TreeBot: Ask me anything about"+ tree_type)

    
    user_input = st.text_input("User: ","random")


    if user_input.lower().strip() == "random":
        last_question = get_random_question(tree_type)
        st.write(last_question)
        st.text("TreeBot:" + get_answer(last_question, tree_type))

        

    elif user_input.endswith("?"):           # Generate and st.write bot's response

        last_question = user_input
        if last_question in tree_data[tree_type]["questions"]:
            st.write("TreeBot:" + get_answer(last_question, tree_type))
        else:
            st.write("TreeBot: I'm sorry, I don't have an answer to that question.")

    else:
        st.write("TreeBot: I'm sorry, I can only answer questions. Please ask a question.")

    # End the conversation if the user says goodbye
    if user_input.lower().strip() == "goodbye":
        st.write("TreeBot: Goodbye!")
        
