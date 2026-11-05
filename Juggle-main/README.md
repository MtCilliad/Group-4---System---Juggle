# Juggle: Personalized Workload Management System

A to-do list that helps students organize tasks, track deadlines, manage their available time, and get personalized recommendations based on their work style and workload.

---

## Project Structure

```text
Juggle/
├── app.py
├── supabase_client.py
├── models/
│   ├── Task.py
│   ├── TaskTypes.py
│   ├── user.py
│   └── workstyle.py
├── services/
│   └── workload_analyzer.py
├── ui/
│   ├── activity.py
│   ├── assessment.py
│   ├── home.py
│   ├── login.py
│   ├── recommendation.py
│   ├── styles.py
│   ├── tasks.py
│   └── workload.py
├── .streamlit/
│   └── config.toml
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/juscode1/Juggle.git
cd Juggle
```

### 2. Install Dependencies

Make sure Python is installed on your computer. Install the required packages using pip:

```bash
pip install streamlit supabase
```

Install any additional packages required by the application.

### 3. Configure Supabase

Create a `secrets.toml` file inside the `.streamlit/` directory.

Add your Supabase credentials:

```toml
SUPABASE_URL = "https://qawnsthuwecizfypdhju.supabase.co"
SUPABASE_KEY = "sb_publishable_l4TAcdBzhTIP7gNl9COEWQ_nIB2qDH0"
```

### 4. Run the Application

Run the following command from the project root:

```bash
streamlit run app.py
```

The application should open in your default web browser.
