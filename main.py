import streamlit as st
import random
import pandas as pd


st.title("Welcome to My Random App!")

st.markdown("There are three features in this application, **Random exercise(s)/project(s) to each group**, **Randomly seleect a person/group**, and **Random Grouping**.")

st.sidebar.markdown("**You can choose different app features here!**")
option = st.sidebar.selectbox("Select an option", ["Random exercise(s)/project(s) to each group/person", "Randomly seleect a person/group", "Random Grouping"])

st.sidebar.write("\n\n")

if option == "Random exercise(s)/project(s) to each group/person":
  st.sidebar.markdown("**Exercise list/Project list**")
  p_list = st.sidebar.text_area("Enter exercise list/project list", "")

  st.sidebar.markdown("**Number of people/group**")
  size = st.sidebar.slider("Select a value", 2,15)

  st.sidebar.markdown("**Number of exercises/projects per group**")
  num_ex = st.sidebar.slider("Select a value", 1,5)

  st.sidebar.markdown("**Number of maximum occurances of an exercise/project**")
  num_oc = st.sidebar.slider("Select a value", 1,4)

  bu = st.sidebar.button("Random Now!")

  if p_list and bu:
    p_list = p_list.split()
    dic = {} # to store group name as key and assigned exercises/projects as key
    alr = [] # to store already occured exercises/projects
    for i in range(1,size+1):
      l = [] # to store assigned exercises/projects for group i
      j = 0
      while j < num_ex:
        ex = random.choice(p_list)
        if (ex not in l) and (alr.count(ex)< num_oc):
          l.append(ex)
          alr.append(ex)
          j += 1 
        if alr.count(ex) == num_oc:
          p_list.remove(ex)
      dic["Group "+str(i)] = l
    group = []
    ex = []
    for key, value in dic.items():
      st.subheader(key)
      for item in value:
        st.write(item)
        group.append(key)
        ex.append(item)
      st.write("\n")
    my_dic = {"Group": group, "Exercise/Project": ex}
    my_df = pd.DataFrame(my_dic)
    my_df.to_excel('Project.xlsx', index=False)
        

if option == "Randomly seleect a person/group":
  st.sidebar.markdown("**Name list/Group list**")
  name_list = st.sidebar.text_area("Enter name list", "")

  bu = st.sidebar.button("Random Now!")

  if name_list and bu:
    name_list = name_list.split()
    random.shuffle(name_list)
    st.subheader("The randomly selected person/group is:")
    st.markdown(random.choice(name_list))


if option == "Random Grouping":
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

  
     
 

 
