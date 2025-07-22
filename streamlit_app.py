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


st.header("🏆 5. Causes of British Success") st.markdown("""

Superior weapons and army discipline.

Divide-and-rule policy: Used Indian rulers against each other.

Lack of unity among Indian kings.

Advanced communication (postal, telegraph) and transport (railways). """)


st.header("🗺️ 6. India in 1856") st.markdown("""

By 1856, major Indian territories were under British rule.

Some princely states existed but under British control.

The annexation of Awadh angered many Indians and became a major reason for the Revolt of 1857. """)


st.header("📝 Quiz: Test Your Knowledge") questions = { "When did the East India Company arrive in Surat?": ["1608", "1757", "1764", "1856"], "What policy did Lord Dalhousie implement?": ["Doctrine of Lapse", "Subsidiary Alliance", "Divide and Rule", "None"], "Which state was annexed due to misrule in 1856?": ["Awadh", "Punjab", "Jhansi", "Hyderabad"], }

score = 0 for q, options in questions.items(): user_answer = st.radio(q, options, key=q) if (q == "When did the East India Company arrive in Surat?" and user_answer == "1608") or 
(q == "What policy did Lord Dalhousie implement?" and user_answer == "Doctrine of Lapse") or 
(q == "Which state was annexed due to misrule in 1856?" and user_answer == "Awadh"): score += 1

if st.button("Submit Quiz"): st.success(f"You scored {score}/3! 🎉") if score == 3: st.balloons() elif score == 0: st.error("Try again! You can do it! 💪")

