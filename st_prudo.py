import streamlit as st
import math


def binomial_probability(n, k, p):
    # Calculate the binomial coefficient
    binom_coeff = math.comb(n, k)

    # Calculate the probability
    probability = binom_coeff * (p ** k) * ((1 - p) ** (n - k))

    return probability


st.text("בואו נשחק פרודו")

#initial
new_game = st.button("משחק חדש")

#if new game button is pressed
if new_game:
    st.text("Starting a new game!")

col1, col2, col3 = st.columns(3)

with col1:
    num_players = st.number_input("מספר שחקנים", 1, 7)
    total_dice = num_players*5
with col2:
    num_dice_out = st.number_input("כמה קוביות נפסלו", 0, 35)
with col3:
    your_dice_amount = st.number_input("כמה יש לך בכוס", 0, 5)
#declaration

st.text("הכרזה:")

col1, col2, col3 = st.columns(3)

with col1:
    value = st.number_input("איזה מספר על הקוביה", 1, 6)
with col2:
    amount = st.number_input("כמה קוביות", 0, 35)
with col3:
    your_relevant_amount = st.number_input("כמה רלוונטיים יש לך", 0, 5)

unknown_amount = amount - your_relevant_amount

TOTAL_PROB = 0
DICE_PROB = (1/3) if value !=1 else (1/6)
unknown_dice = total_dice - num_dice_out - your_dice_amount
for i in range(unknown_amount, unknown_dice):
    print (i)
    prob = binomial_probability(unknown_dice,i,DICE_PROB)
    print (prob)
    TOTAL_PROB += prob

st.text(f"ההסתברות להכרזה הזאת היא {round(100*TOTAL_PROB,2)}")