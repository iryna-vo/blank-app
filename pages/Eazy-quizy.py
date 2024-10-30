import streamlit as st


st.title("🎬 Quick & Funny Film Quiz 🎬")
st.subheader("Choose the right answer")

questions = [
    {
        "question": "In Shrek, what does Donkey say about waffles?",
        "options": ["A) I’m making waffles!", "B) Waffles are overrated.", "C) I hate waffles."],
        "answer": "A) I’m making waffles!",
        "image": r"C:\Users\irkav\Documents\JEDHA_2024-2025\Full_stack_DA\GitHub\Blank-app-Streamlit\blank-app\image\image1.jpg"  
    },
    {
        "question": "In Toy Story, what does Buzz Lightyear famously say?",
        "options": ["A) To the moon and back!", "B) To infinity and beyond!", "C) To space and time!"],
        "answer": "B) To infinity and beyond!",
        "image": r"C:\Users\irkav\Documents\JEDHA_2024-2025\Full_stack_DA\GitHub\Blank-app-Streamlit\blank-app\image\image2.jpg"  
    },
    {
        "question": "In The Lion King, what’s Timon’s motto?",
        "options": ["A) Take it easy!", "B) Live for today!", "C) Hakuna Matata!"],
        "answer": "C) Hakuna Matata!",
        "image": r"C:\Users\irkav\Documents\JEDHA_2024-2025\Full_stack_DA\GitHub\Blank-app-Streamlit\blank-app\image\image3.jpg"
    },
    {
        "question": "In The Matrix, which color pill does Neo take?",
        "options": ["A) Red", "B) Blue", "C) Green"],
        "answer": "A) Red",
        "image": r"C:\Users\irkav\Documents\JEDHA_2024-2025\Full_stack_DA\GitHub\Blank-app-Streamlit\blank-app\image\image4.jpg"   
    },
    {
        "question": "In Pirates of the Caribbean, what’s Jack Sparrow always searching for?",
        "options": ["A) The Kraken", "B) The Black Pearl", "C) Buried treasure"],
        "answer": "B) The Black Pearl",
        "image": r"C:\Users\irkav\Documents\JEDHA_2024-2025\Full_stack_DA\GitHub\Blank-app-Streamlit\blank-app\image\image5.jpg"   
    }
]

# Quiz functionality
for i, q in enumerate(questions):
    st.image(q["image"], use_column_width=True)   
    st.write(f"**{i + 1}. {q['question']}**")
    # User selects an answer
    user_answer = st.radio("", q['options'], key=i)
    
    # Check if the selected answer is correct
    if st.button(f"Submit Answer for Question {i + 1}"):
        if user_answer == q['answer']:
            st.success("✅ Well answer!")
        else:
            st.error("❌ Wrong answer!")

# End message
st.write("**Well done :) Bravo!**")