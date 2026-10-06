import streamlit as st
import pandas as pd

from database import (
    initialize_database,
    add_student,
    get_student,
    get_machines,
    get_queue,
    add_to_queue,
    complete_current_laundry,
    remove_from_queue,
    get_all_queue_data
)

from queue_manager import (
    calculate_waiting_time,
    get_position
)

from prediction import predict_waiting_time


# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------

st.set_page_config(
    page_title="Smart Laundry System",
    page_icon="🧺",
    layout="wide"
)


# ---------------------------------------
# INITIALIZE DATABASE
# ---------------------------------------

initialize_database()


# ---------------------------------------
# HEADER
# ---------------------------------------

st.title("🧺 Smart Laundry Queue & Notification System")

st.write(
    "A Python-based smart system for managing hostel laundry queues."
)

st.divider()


# ---------------------------------------
# SIDEBAR
# ---------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Student Registration",
        "Laundry Queue",
        "My Status",
        "Admin Dashboard",
        "Analytics"
    ]
)


# =======================================
# STUDENT REGISTRATION
# =======================================

if page == "Student Registration":

    st.header("👨‍🎓 Student Registration")

    student_id = st.text_input(
        "Student ID"
    )

    name = st.text_input(
        "Student Name"
    )

    room_no = st.text_input(
        "Room Number"
    )

    if st.button("Register Student"):

        if not student_id or not name or not room_no:

            st.error("Please fill all fields.")

        else:

            success, message = add_student(
                student_id,
                name,
                room_no
            )

            if success:
                st.success(message)
            else:
                st.error(message)


# =======================================
# LAUNDRY QUEUE
# =======================================

elif page == "Laundry Queue":

    st.header("🧺 Join Laundry Queue")

    student_id = st.text_input(
        "Enter Student ID"
    )

    if student_id:

        student = get_student(student_id)

        if student:

            st.success(
                f"Welcome {student[2]}!"
            )

            machines = get_machines()

            machine_names = [
                machine[1]
                for machine in machines
            ]

            selected_machine = st.selectbox(
                "Select Washing Machine",
                machine_names
            )

            people_waiting, estimated_time = (
                calculate_waiting_time(
                    selected_machine
                )
            )

            st.info(
                f"People currently waiting: "
                f"{people_waiting}"
            )

            st.info(
                f"Estimated waiting time: "
                f"{estimated_time} minutes"
            )

            if st.button("Join Queue"):

                success, message = add_to_queue(
                    student_id,
                    selected_machine,
                    estimated_time
                )

                if success:
                    st.success(message)
                    st.balloons()
                else:
                    st.error(message)

        else:

            st.warning(
                "Student not found. Please register first."
            )


# =======================================
# MY STATUS
# =======================================

elif page == "My Status":

    st.header("📊 My Laundry Status")

    student_id = st.text_input(
        "Enter Student ID"
    )

    if student_id:

        student = get_student(student_id)

        if not student:

            st.error("Student not found.")

        else:

            queue_data = get_all_queue_data()

            my_queue = queue_data[
                (queue_data["student_id"] == student_id)
                &
                (queue_data["status"] == "Waiting")
            ]

            if my_queue.empty:

                st.info(
                    "You are not currently in a laundry queue."
                )

            else:

                row = my_queue.iloc[0]

                machine = row["machine_name"]

                position = get_position(
                    student_id,
                    machine
                )

                waiting_time = predict_waiting_time(
                    position - 1
                )

                st.success(
                    f"🧺 Machine: {machine}"
                )

                st.metric(
                    "Queue Position",
                    position
                )

                st.metric(
                    "Estimated Waiting Time",
                    f"{waiting_time} min"
                )

                # Notification
                if position <= 2:

                    st.warning(
                        "🔔 Your laundry turn is approaching!"
                    )

                elif position <= 4:

                    st.info(
                        "⏳ Please wait. Your turn is coming soon."
                    )

                else:

                    st.info(
                        "You are currently in the queue."
                    )


# =======================================
# ADMIN DASHBOARD
# =======================================

elif page == "Admin Dashboard":

    st.header("👨‍💼 Admin Dashboard")

    st.subheader("Current Laundry Queues")

    queue_data = get_all_queue_data()

    waiting_data = queue_data[
        queue_data["status"] == "Waiting"
    ]

    if waiting_data.empty:

        st.info(
            "No students are currently waiting."
        )

    else:

        st.dataframe(
            waiting_data,
            use_container_width=True
        )

    st.divider()

    st.subheader("Complete Laundry")

    machines = get_machines()

    machine_names = [
        machine[1]
        for machine in machines
    ]

    selected_machine = st.selectbox(
        "Select Machine",
        machine_names
    )

    if st.button("Mark Current Laundry Completed"):

        success, message = complete_current_laundry(
            selected_machine
        )

        if success:
            st.success(message)
            st.rerun()

        else:
            st.warning(message)

    st.divider()

    st.subheader("Remove Queue Entry")

    if not waiting_data.empty:

        queue_id = st.number_input(
            "Queue ID",
            min_value=1,
            step=1
        )

        if st.button("Remove Student"):

            remove_from_queue(queue_id)

            st.success(
                "Student removed from queue."
            )

            st.rerun()


# =======================================
# ANALYTICS
# =======================================

elif page == "Analytics":

    st.header("📈 Laundry Analytics")

    data = get_all_queue_data()

    if data.empty:

        st.info(
            "No laundry data available yet."
        )

    else:

        st.subheader(
            "Machine Usage"
        )

        machine_usage = (
            data["machine_name"]
            .value_counts()
        )

        st.bar_chart(
            machine_usage
        )

        st.subheader(
            "Queue Status"
        )

        status_count = (
            data["status"]
            .value_counts()
        )

        st.bar_chart(
            status_count
        )

        st.subheader(
            "Laundry Records"
        )

        st.dataframe(
            data,
            use_container_width=True
        )