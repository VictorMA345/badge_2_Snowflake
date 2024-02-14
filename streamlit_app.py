import streamlit

streamlit.title("My parents new healthy diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 & Blueberry OatMeal")
streamlit.text("🥗 kale, spinach and Rocket Smoothie")
streamlit.text("🐔 Hard Boiled free range Eggs")
streamlit.text("🥑🍞 Avocado Toast")
   
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
