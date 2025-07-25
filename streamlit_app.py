import streamlit as st

st.set_page_config(page_title="British Expansion in India", layout="centered") 
st.title("📚 British Expansion in India (1600 - 1856)")

st.header("📌 1. East India Company Begins Trade") 
st.markdown("""

In 1600, Queen Elizabeth gave permission to the East India Company to trade with the East.

The company aimed to buy spices from the East and sell them in England.

In 1608, the company arrived in Surat and set up its first trading center. """)


st.header("⚔️ 2. Conflicts with Indian Rulers") 
st.markdown("""

British faced resistance from Indian rulers like the Mughals, Marathas, and Mysore kings.

Important battles:

Battle of Plassey (1757): British defeated Siraj-ud-Daulah and gained control of Bengal.

Battle of Buxar (1764): British defeated combined armies of Bengal, Awadh, and the Mughals. """)



st.header("🏰 3. Expansion Policies") 
st.markdown("""

Subsidiary Alliance by Lord Wellesley:

Indian rulers had to keep British troops and pay for them.

Example: Hyderabad, Awadh, Mysore.


Doctrine of Lapse by Lord Dalhousie:

If a ruler died without a male heir, his kingdom was annexed.

Example: Satara, Jhansi, Nagpur. """)



st.header("🔁 4. Annexations by Force and Diplomacy")

st.markdown("""

British used force, treaties, and clever politics to take over kingdoms.

Example: Punjab was annexed after defeating the Sikhs in 1849.

Awadh was annexed in 1856 on the grounds of misrule. """)


st.header("🏆 5. Causes of British Success") 

st.markdown("""

Superior weapons and army discipline.

Divide-and-rule policy: Used Indian rulers against each other.

Lack of unity among Indian kings.

Advanced communication (postal, telegraph) and transport (railways). """)


st.header("🗺️ 6. India in 1856")

st.markdown("""

By 1856, major Indian territories were under British rule.

Some princely states existed but under British control.

The annexation of Awadh angered many Indians and became a major reason for the Revolt of 1857. """)


st.header("📝 Quiz: Test Your Knowledge") 

questions = {
    "Who introduced the Doctrine of Lapse?": [
        "Lord Dalhousie", "Lord Wellesley", "Lord Hastings", "Lord Canning"
    ],
    "Which battle marked the beginning of British rule in India?": [
        "Battle of Plassey", "Battle of Buxar", "Battle of Panipat", "Battle of Haldighati"
    ],
    "What was the main cause of the First Anglo-Maratha War?": [
        "Raghunath Rao’s appeal for British support", "Doctrinal expansion", "Economic interest", "Religious conflict"
    ],
    "When did the East India Company gain Diwani rights?": [
        "1765", "1757", "1857", "1773"
    ]
}

correct_answers = {
    "Who introduced the Doctrine of Lapse?": "Lord Dalhousie",
    "Which battle marked the beginning of British rule in India?": "Battle of Plassey",
    "What was the main cause of the First Anglo-Maratha War?": "Raghunath Rao’s appeal for British support",
    "When did the East India Company gain Diwani rights?": "1765"
}



score = 0
for q, options in questions.items():
    st.write(f"**{q}**")
    user_answer = st.radio("Choose one:", options, key=q)
    if user_answer == correct_answers[q]:
        score += 1
st.success(f"Your score: {score}/{len(questions)}")

if st.button("Submit Quiz"):

   st.success(f"You scored {score}/3! 🎉")

if score == 3: 

   st.balloons() 
elif score == 0:

  st.error("Try again! You can do it! 💪")

