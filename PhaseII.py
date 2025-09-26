import streamlit as st



st.title("Avatar: The Last Airbender Quiz")
st.write("Answer the questions below to find out which character you are most like!")

#Question 1 Info (radio) #NEW
bending_element = st.radio(
    "If you had a choice, what element would you want to bend?",
    ["Water", "Earth", "Fire", "Air"]
)

#Question 2 Info (multiselect) #NEW 
hobbies = st.multiselect(
    "Which activities do you enjoy?",
    ["Training", "Reading", "Traveling", "Eating"]
)

#Question 3 Info (radio) 
vacation_area = st.radio(
    "If you could take a vacation anywhere in the avatar world, where would it be?",
    ["Fire Nation", "Earth Kingdom", "Water Tribe", "Air Nomads"]
)

#Question 4 Info (number input) #NEW
peace = st.number_input(
    "On a scale of 0-10, how important is peace in the world to you?",
    min_value=0, max_value=10, value=1
)

#Question 5 Info (radio)
motivation = st.radio(
    "What motivates you the most from the following choices?",
    ["Knowledge", "Balance", "Power", "Independence"]
)


if st.button("See My Result!"):
    scores = {"Aang": 0, "Katara": 0, "Zuko": 0, "Toph": 0}

    # Question 1: Element (Done)
    if bending_element == "Water":
        scores["Katara"] += 1
    elif bending_element == "Earth":
        scores["Toph"] += 1
    elif bending_element == "Fire":
        scores["Zuko"] += 1
    else:
        scores["Aang"] += 1

    # Question 2: Hobbies (Done)
    if "Reading" in hobbies:
        scores["Katara"] += 1
    if "Training" in hobbies:
        scores["Zuko"] += 1
    if "Traveling" in hobbies:
        scores["Aang"] += 1
    if "Eating" in hobbies:
        scores["Toph"] += 1

    # Question 3: Vacation Spot (Done)
    if vacation_area == "Fire Nation":
        scores["Zuko"] += 1
    elif vacation_area == "Earth Kingdom":
        scores["Toph"] += 1
    elif vacation_area == "Water Tribe":
        scores["Katara"] += 1
    elif vacation_area == "Air Nomads":
        scores["Aang"] += 1 

    #Question 4: Peace in the world
    if 0 <= peace <= 2:
        scores["Zuko"] += 1
    elif 3 <= peace <= 5:
        scores["Toph"] += 1
    elif 6 <= peace <= 8:
        scores["Katara"] += 1
    elif 9 <= peace <= 10:
        scores["Aang"] += 1

        

    # Question 5: motivation
    if motivation == "Knowledge":
        scores["Katara"] += 1
    elif motivation == "Balance":
        scores["Aang"] += 1
    elif motivation == "Power":
        scores["Zuko"] += 1
    elif motivation == "Independence":
        scores["Toph"] += 1



    result = "Aang"
    highest = scores["Aang"]

    for character in scores:
        if scores[character] > highest:
            result = character
            highest = scores[character]


    st.success(f"You are most like {result}!")

    if result == "Aang":
        st.image("Images/aang.webp", width=300)
    elif result == "Katara":
        st.image("Images/katara.webp", width=300)
    elif result == "Zuko":
        st.image("Images/zuko.jpg", width=300)
    elif result == "Toph":
        st.image("Images/toph.jpg", width=300)
