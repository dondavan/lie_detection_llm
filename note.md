# Why environment is not working
Multiple python can be installed on your laptop, and they have sperated package managment.
VS code or terminal maybe configured to use different python, cause inconsistency in program running.

python3 --version
python --version
pip3 install transformers

changed python environment to 3.9
and pip3 installed all missing modules

col1, col2 = st.columns([3,1])
    col3, col4 = st.columns([5,1])

    ans_container = st.empty()
    input_container = col1.empty()
    submit_cont = col2.empty()
    progr_cont = st.empty()
    up_button_cont = col4.empty()
    down_button_cont = col3.empty()
 
# Next steps 

- initial credibility score show 
- try again if you failed next if you managed 
- connect submit button 
- put generate, load, chatloop in the beginning for the whole document so you don't need to redefine every page 

# git change
git pull
x

git add --all
git commit -m "im so hot"
git push

#what I will install
streamlit 
deta 
transformers

# start streamlit
python3 -m streamlit whatever

# requirement
deta==1.1.0
numpy==1.24.1
python-dotenv==0.21.1
streamlit==1.17.0
transformers==4.26.0

# leftover code 

 # Initialize session state variables if not already set
    if 'task_order' not in st.session_state:
        st.session_state.task_order = random.sample([1, 2], 2)  # Randomize the order of tasks 1 and 2
    if 'adversarial_order' not in st.session_state:
        st.session_state.adversarial_order = random.choice(["lie_to_truth", "truth_to_lie"])  # Randomize adversarial order
    if 'current_task' not in st.session_state:
        st.session_state.current_task = 0  # Start with the first task

    # Display the current task based on the `current_task` index
    current_task = st.session_state.current_task

    if current_task == 0:
        task_1_content()  # Task 1: Write a Lie or Truth
    elif current_task == 1:
        task_2_content()  # Task 2: Write a Lie or Truth
    elif current_task == 2:
        task_3_content()  # Task 3: Adversarial Example
    elif current_task == 3:
        task_4_content()  # Task 4: Adversarial Example with Specific Instructions
    else:
        # All tasks completed
        st.write("All tasks completed!")
        if st.button("Proceed to Next Section"):
            proceed_to_next_section()

def task_1_content():
    if st.session_state.task_order[0] == 1:
        st.title("Task 1: Write a Lie")
        st.write("**Please write a lie.**")
    else:
        st.title("Task 1: Write a Truth")
        st.write("**Please write a truth.**")

    user_input = st.text_area("Write your statement here:")
    if st.button("Submit Task 1"):
        st.session_state.task_1_input = user_input
        st.session_state.current_task += 1

def task_2_content():
    if st.session_state.task_order[1] == 1:
        st.title("Task 2: Write a Lie")
        st.write("**Please write a lie.**")
    else:
        st.title("Task 2: Write a Truth")
        st.write("**Please write a truth.**")

    user_input = st.text_area("Write your statement here:")
    if st.button("Submit Task 2"):
        st.session_state.task_2_input = user_input
        st.session_state.current_task += 1

def task_3_content():
    st.title("Task 3: Write an Adversarial Example")

    # Load statements if not already loaded
    if 'statements' not in st.session_state:
        st.session_state.statements = load_statements()

    # Draw a random statement for Task 3 if not already selected
    if 'task_3_statement' not in st.session_state:
        random_statement = st.session_state.statements.sample(n=1).iloc[0]
        st.session_state.task_3_statement = random_statement['text']
        st.session_state.task_3_condition = random_statement['condition']

    # Display the statement and instructions
    statement_text = st.session_state.task_3_statement
    condition = st.session_state.task_3_condition

    if condition == "deceptive":
        st.write("**Rewrite the following deceptive statement so that it appears truthful.**")
    else:
        st.write("**Rewrite the following truthful statement so that it appears deceptive.**")

    st.write(f"**Original Statement:** {statement_text}")

    # Input for the rewritten statement
    user_input = st.text_area("Write your adversarial example here:")

    if st.button("Submit Task 3"):
        st.session_state.task_3_input = user_input
        st.session_state.current_task += 1

def task_4_content():
    st.title("Task 4: Write an Adversarial Example with Specific Instructions")

    # Load statements if not already loaded
    if 'statements' not in st.session_state:
        st.session_state.statements = load_statements()

    # Draw a random statement for Task 4 if not already selected
    if 'task_4_statement' not in st.session_state:
        # Opposite condition of Task 3
        opposite_condition = "truthful" if st.session_state.task_3_condition == "deceptive" else "deceptive"
        random_statement = st.session_state.statements[st.session_state.statements['condition'] == opposite_condition].sample(n=1).iloc[0]
        st.session_state.task_4_statement = random_statement['text']
        st.session_state.task_4_condition = random_statement['condition']

    # Display the statement and instructions
    statement_text = st.session_state.task_4_statement
    condition = st.session_state.task_4_condition

     if condition == "deceptive":
        st.write("**Rewrite the following deceptive statement so that it appears truthful while ensuring that your rewrite means the same, is grammatically correct, and appears natural.**")
    else:
        st.write("**Rewrite the following truthful statement so that it appears deceptive while ensuring that your rewrite means the same, is grammatically correct, and appears natural.**")

    st.write(f"**Original Statement:** {statement_text}")

    # Input for the rewritten statement
    user_input = st.text_area("Write your adversarial example here:")

    if st.button("Submit Task 4"):
        st.session_state.task_4_input = user_input
        st.session_state.current_task += 1

def proceed_to_next_section():
    st.session_state.page = 'experiment'
    st.experimental_rerun()