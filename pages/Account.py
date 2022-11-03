# import streamlit as st
# st.set_page_config(layout="wide")

# st.title("Streamlit Forms & Salary Calculator")
# st.subheader("Account Information")


# with st.form(key='ac_info'):
#     col1, col2, col3 = st.columns([3, 2, 1])

#     with col1:
#         firstname = st.text_input("Firstname")
        
#     with col2:
#         lastname = st.text_input("lastname")

#     with col3:
#         st.text("       \n")
#         submit_salary = st.form_submit_button(label='Submit')

# if submit_salary:
#     with st.beta_expander("Results"):
#         daily = [amount * 8]
#         weekly = [amount * hour_per_week]
#         df = pd.DataFrame({'hourly': amount, 'daily': daily, 'weekly': weekly})
#         st.dataframe(df.T)

# # Method 1: Context Manager Approach (with)
# with st.form(key='form1'):
#     firstname = st.text_input("Firstname")
#     lastname = st.text_input("lastname")
#     dob = st.date_input("Date of Birth")

#     # Important
#     submit_button = st.form_submit_button(label='SignUp')

# # Results Can be either form or outside
# if submit_button:
#     st.success("Hello {} you ve created an account".format(firstname))

# # Method 2:
# form2 = st.form(key='form2')
# username = form2.text_input("Username")
# jobtype = form2.selectbox("Job", ["Farmer", "Independent Researcher", "Goverment Employee"])
# submit_button2 = form2.form_submit_button("Login")

# if submit_button2:
#     st.write(username.upper())
