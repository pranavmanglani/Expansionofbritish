import streamlit as st

#Set page config

st.set_page_config(page_title="British Expansion in India", layout="wide")

st.title("🇮🇳 Expansion of British Power in India") 
st.markdown(""" This interactive app covers key topics like:

British Strategic Policies

Subsidiary Alliance

Anglo-Maratha Wars

Doctrine of Lapse

Annexation of Awadh

Dalhousie’s Policy of Expansion

Subjugation of Mysore

Annexation of the Sikh Kingdom

India in 1856



---

""")

Sidebar Navigation

section = st.sidebar.radio("Jump to Section", [ "British Strategic Policies", "Subsidiary Alliance", "Anglo-Maratha Wars", "Doctrine of Lapse", "Annexation of Awadh", "Subjugation of Mysore", "Annexation of the Sikh Kingdom", "Dalhousie’s Policy of Expansion", "India in 1856", "Quiz: Test Your Knowledge" ])

if section == "British Strategic Policies": st.header("British Strategic Policies") st.markdown("""

Started as traders, later aimed for power.

Used policies to avoid expensive wars.

Two-pronged strategy:

1. Peaceful annexation


2. Military conquest



Also annexed under pretexts like maladministration. """)


elif section == "Subsidiary Alliance": st.header("Subsidiary Alliance (by Lord Wellesley)") st.subheader("Terms") st.markdown("""

British troops stationed in Indian territory.

Indian rulers paid for them.

British Resident placed in courts.

Rulers couldn't ally or go to war without permission. """) st.subheader("Effects") col1, col2 = st.columns(2) with col1: st.markdown("Advantages for British") 
st.markdown(""" - Large armies without own expenses - More territories and resources - Foreign rivals excluded - Controlled Indian foreign policy """) with col2: st.markdown("Disadvantages for Indians") st.markdown(""" - Loss of independence - Drained resources - People suffered under neglectful rulers - Helped subjugate Marathas """)


elif section == "Anglo-Maratha Wars": st.header("Anglo-Maratha Wars") st.subheader("1st War (1775–82)") st.markdown("""

Cause: Civil war over succession (Madhav Rao II vs Raghunath Rao)

Result: Treaty of Salbai (peace for 20 years) """) st.subheader("2nd War (1803–05)") st.markdown("""

Cause: Death of Madhav Rao II, internal rivalry

Result: British victory, Sindhia & Bhonsle accepted Subsidiary Alliance """) st.subheader("3rd War (1817–18)") st.markdown("""

Cause: Peshwa Baji Rao II resisted British control

Result: British victory, Peshwa deposed, Maratha power ended """)


elif section == "Doctrine of Lapse": st.header("Doctrine of Lapse (by Lord Dalhousie)") st.markdown("""

States with no natural male heir would be annexed.

Rulers could not adopt sons without British permission.

States affected: Satara, Jhansi, Nagpur

Led to widespread resentment and contributed to 1857 Revolt """)


elif section == "Annexation of Awadh": st.header("Annexation of Awadh") st.markdown("""

Nawab protected under Subsidiary Alliance

Later annexed on grounds of maladministration

Treasury drained, ruler incompetent

People deeply resented annexation — key centre of 1857 Revolt """)


elif section == "Subjugation of Mysore": st.header("Subjugation of Mysore") st.markdown("""

Ruled by Hyder Ali and his son Tipu Sultan

Both were efficient and strong rulers

British fought four wars with Mysore

Tipu Sultan died in 4th Anglo-Mysore War (1799), Mysore annexed """)


elif section == "Annexation of the Sikh Kingdom": st.header("Annexation of the Sikh Kingdom") st.markdown("""

Strong state under Ranjit Singh

After his death, power struggles weakened the kingdom

British fought two wars (1845–49)

Annexed Punjab after Second Anglo-Sikh War """)


elif section == "Dalhousie’s Policy of Expansion": st.header("Dalhousie’s Policy of Expansion") st.markdown("""

Used:

1. War (Punjab)


2. Doctrine of Lapse (Satara, Jhansi, Nagpur)


3. Maladministration (Awadh)



Aim: Build a complete British empire in India """)


elif section == "India in 1856": st.header("India in 1856") st.markdown("""

Most of India was under British control

Remaining Indian rulers had only nominal power

Factors for British success:

Disunity among Indian rulers

Weak administration

British military, economic, and naval strength """)



elif section == "Quiz: Test Your Knowledge": st.header("🧠 Quiz: Test Your Knowledge") score = 0

q1 = st.radio("1. Who introduced the Subsidiary Alliance?", ["Lord Dalhousie", "Lord Wellesley", "Warren Hastings"])
if q1 == "Lord Wellesley": score += 1

q2 = st.radio("2. Which war ended Maratha power?", ["First Anglo-Maratha War", "Second Anglo-Maratha War", "Third Anglo-Maratha War"])
if q2 == "Third Anglo-Maratha War": score += 1

q3 = st.radio("3. Doctrine of Lapse was introduced by?", ["Lord Dalhousie", "Lord Wellesley", "Lord Cornwallis"])
if q3 == "Lord Dalhousie": score += 1

q4 = st.radio("4. Which state was annexed on the grounds of maladministration?", ["Nagpur", "Awadh", "Jhansi"])
if q4 == "Awadh": score += 1

q5 = st.radio("5. Who fought bravely in the Anglo-Sikh Wars?", ["Ranjit Singh", "The Sikhs", "Hyder Ali"])
if q5 == "The Sikhs": score += 1

q6 = st.radio("6. Which ruler died in the Fourth Anglo-Mysore War?", ["Hyder Ali", "Tipu Sultan", "Baji Rao II"])
if q6 == "Tipu Sultan": score += 1

q7 = st.radio("7. What was a result of the Treaty of Salbai?", ["Peace with Marathas", "Start of rebellion", "Dalhousie became Governor"])
if q7 == "Peace with Marathas": score += 1

st.markdown(f"### ✅ Your Score: {score}/7")
if score == 7:
    st.success("Excellent! You’ve mastered this topic.")
elif score >= 5:
    st.info("Good job! Review a few points for perfection.")
else:
    st.warning("You might want to revisit some sections.")

