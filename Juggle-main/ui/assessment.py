import streamlit as st
from models.workstyle import WorkStyleProfile
from supabase_client import get_supabase

QUESTIONS = [
    {
        "key": "q1",
        "text": "1. You receive several tasks at once. What do you do?",
        "options": [
            {"text": "Plan everything before starting.",           "weight": 3},
            {"text": "Start with a quick task to build momentum.", "weight": 2},
            {"text": "Start with the task that is due soonest.",   "weight": 1},
        ],
    },
    {
        "key": "q2",
        "text": "2. How do you prefer to work?",
        "options": [
            {"text": "Long, focused sessions.",           "weight": 3},
            {"text": "Short sessions with quick progress.", "weight": 2},
            {"text": "I work best when there is a deadline.",   "weight": 1},
        ],
    },
    {
        "key": "q3",
        "text": "3. When a deadline is still far away, you usually:",
        "options": [
            {"text": "Start early and plan ahead.",           "weight": 3},
            {"text": "Do smaller parts when I have time.", "weight": 2},
            {"text": "Focus on it when the deadline gets closer.",   "weight": 1},
        ],
    },
    {
        "key": "q4",
        "text": "4. Which task would you choose first?",
        "options": [
            {"text": "A difficult task that needs planning.",           "weight": 3},
            {"text": "A short task that I can finish quickly.", "weight": 2},
            {"text": "A task that is due tomorrow.",   "weight": 1},
        ],
    },
    {
        "key": "q5",
        "text": "5. What motivates you to start working?",
        "options": [
            {"text": "Having a clear plan.",           "weight": 3},
            {"text": "Seeing quick progress.", "weight": 2},
            {"text": "Having an approaching deadline.",   "weight": 1},
        ],
    },
]

def show_assessment():
    st.title("Work Style Assessment")

    st.write(
        "Answer the questions below to determine how "
        "you prefer to manage your workload."
    )

    st.divider()

    answers = {}
    for q in QUESTIONS:
        answers[q["key"]] = st.radio(
            q["text"],
            q["options"],
            format_func=lambda opt: opt["text"],
            key=f"assessment_{q['key']}",
        )

        st.divider()

    if st.button("Finish Assessment", use_container_width=True):

        total = sum(choice["weight"] for choice in answers.values())

        if total >= 12:
            style = "Focused Planner"
            work_time = 90
            preference = "Most important tasks first"
        elif total >= 9:
            style = "Quick Starter"
            work_time = 30
            preference = "Short tasks first"
        else:
            style = "Deadline Driven"
            work_time = 60
            preference = "Urgent tasks first"

        user_id = st.session_state.get("user_id")

        if not user_id:
            st.error("Your session has expired. Please log in again.")
            return

        assessment_answers = {k: v["text"] for k, v in answers.items()}

        assessment_data = {
            "assessment_answers": assessment_answers,
            "work_style": style,
            "preferred_time": work_time,
            "task_preference": preference,
        }

        try:
            supabase = get_supabase()
            supabase.table("users").update(
                assessment_data
            ).eq("id", user_id).execute()
        except Exception:
            st.error(
                "Your assessment could not be saved. "
                "Please try again."
            )
            return

        profile = WorkStyleProfile(style, work_time, preference)

        st.session_state.user.set_work_style(profile)
        st.session_state.assessment_answers = assessment_answers
        st.session_state.assessment_completed = True
        st.session_state.work_style = style
        st.session_state.page = "Home"

        st.rerun()