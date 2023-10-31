import streamlit as st
import random
import pandas as pd


st.title("Welcome to My Random Grouping App!")
#st.header("Random Grouping")
st.subheader("This application randomly groups people to different groups given a name list and number of members per group.")


st.sidebar.markdown("**Name list**")
my_list = st.sidebar.text_area("Enter name list", "")

#st.sidebar.markdown("**Number of Group**")
#num_group = st.sidebar.slider("Select a value", 2,15)

st.sidebar.write("\n\n")

st.sidebar.markdown("**Number of memebers per group**")
num_member = st.sidebar.selectbox("Select an option", [3, 4, 5, 6, 7])

st.sidebar.write("\n\n")

bu = st.sidebar.button("Group Now!")

if my_list and bu:
 my_list = my_list.split()
 random.shuffle(my_list)
 groups = [my_list[i:i+num_member] for i in range(0, len(my_list), num_member)]
 dic = {}
 for i, group in enumerate(groups):
    dic["Group "+str(i+1)] = group
 group = []
 student = []
 for key, value in dic.items():
     st.subheader(key)
     for item in value:
       st.write(item)
       group.append(key)
       student.append(item)
     st.write("\n")
 my_dic = {"Student": student, "Group": group}
 my_df = pd.DataFrame(my_dic)
 my_df.to_excel('group.xlsx', index=False)
     
 
