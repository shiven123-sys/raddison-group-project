import streamlit as st
import pandas as pd
import plotly.express as px
import random

# ----- Page Config -----
st.set_page_config(page_title="InsightAI Dashboard", layout="wide", page_icon="🤖")

# ----- Header -----
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>InsightAI: Interactive Content Analytics</h1>", unsafe_allow_html=True)
st.markdown("---")

# ----- Sidebar -----
st.sidebar.header("Settings")
platform = st.sidebar.selectbox("Choose Platform", ["Google Analytics", "Meta Analytics", "TikTok Analytics"])
time_range = st.sidebar.selectbox("Time Range", ["Last 7 Days", "Last 14 Days", "Last 30 Days"])
show_trend = st.sidebar.checkbox("Show Engagement Trend", value=True)

# ----- User Query -----
st.subheader("Ask InsightAI for Recommendations")
user_query = st.text_input("Enter your question:")

# ----- Dummy Data Generators -----
def get_dummy_metrics():
    return {
        "Views": random.randint(1000, 10000),
        "Likes": random.randint(100, 1000),
        "Shares": random.randint(10, 100),
        "Comments": random.randint(5, 50),
        "Engagement Rate (%)": round(random.uniform(1.0, 10.0), 2)
    }

def generate_ai_insights(query, metrics):
    recommendations = [
        "Post more videos during peak hours (6-9 PM).",
        "Use interactive polls to boost engagement.",
        "Focus on trending topics your audience likes.",
        "Increase posting frequency to 3-4 times/week.",
        "Use shorter captions for better reach."
    ]
    return f"Insight for '{query}': {random.choice(recommendations)}"

# ----- Main Dashboard -----
if st.button("Get Insights") and user_query.strip() != "":
    metrics = get_dummy_metrics()
    insights = generate_ai_insights(user_query, metrics)

    # ----- Metrics Cards -----
    st.subheader("Platform Overview")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Views", metrics["Views"], delta=f"{random.randint(-100,100)}")
    col2.metric("Likes", metrics["Likes"], delta=f"{random.randint(-50,50)}")
    col3.metric("Shares", metrics["Shares"], delta=f"{random.randint(-10,10)}")
    col4.metric("Comments", metrics["Comments"], delta=f"{random.randint(-5,5)}")
    col5.metric("Engagement Rate", f"{metrics['Engagement Rate (%)']}%", delta=f"{round(random.uniform(-1,1),1)}%")

    st.markdown("---")

    # ----- Tabs -----
    tabs = st.tabs(["Metrics Charts", "Engagement Trend", "Recommendations"])

    # ----- Metrics Charts Tab -----
    with tabs[0]:
        df_metrics = pd.DataFrame({
            "Metric": ["Views", "Likes", "Shares", "Comments"],
            "Count": [metrics["Views"], metrics["Likes"], metrics["Shares"], metrics["Comments"]]
        })
        bar_fig = px.bar(df_metrics, x="Metric", y="Count", color="Metric", text="Count",
                         title=f"{platform} Metrics Overview", template="plotly_dark")
        bar_fig.update_traces(marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.8)
        st.plotly_chart(bar_fig, use_container_width=True)

        # Pie chart for engagement distribution
        pie_fig = px.pie(df_metrics, names="Metric", values="Count", title="Engagement Distribution", template="plotly_dark")
        st.plotly_chart(pie_fig, use_container_width=True)

    # ----- Engagement Trend Tab -----
    with tabs[1]:
        if show_trend:
            trend_df = pd.DataFrame({
                "Day": [f"Day {i}" for i in range(1, 8)],
                "Engagement Rate": [round(random.uniform(1.0, 10.0), 2) for _ in range(7)]
            })
            line_fig = px.line(trend_df, x="Day", y="Engagement Rate", markers=True,
                               title=f"Weekly Engagement Trend - {platform}", template="plotly_dark")
            st.plotly_chart(line_fig, use_container_width=True)
        else:
            st.info("Engagement trend is hidden. Check 'Show Engagement Trend' in sidebar to display.")

    # ----- Recommendations Tab -----
    with tabs[2]:
        st.subheader("AI Recommendations")
        st.info(insights)
        st.markdown("💡 **Tip:** Apply these insights to improve your content strategy!")

    st.markdown("---")
    st.success("Dashboard ready! it's all with the use of LLM and analytics tool.")