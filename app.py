import streamlit as st
import time
from system_metrics import get_system_metrics

st.set_page_config(page_title="System Health Dashboard", layout="wide")

st.title("🖥️ System Health Dashboard")
st.markdown("Live system metrics monitor. Refreshes every 5 seconds.")

placeholder = st.empty()

while True:
    metrics = get_system_metrics()

    with placeholder.container():
        st.subheader("🧠 Basic Info")
        col1, col2 = st.columns(2)
        col1.metric("Hostname", metrics["hostname"])
        col2.metric("OS Version", metrics["os_version"])

        st.subheader("🧮 CPU & Memory")
        col3, col4 = st.columns(2)
        col3.metric("CPU Usage (%)", f"{metrics['cpu_usage']}%")
        col4.metric("Memory Usage", f"{metrics['memory_used']} / {metrics['memory_total']} GB ({metrics['memory_percent']}%)")

        st.subheader("💾 Disk Usage")
        st.metric("Disk Usage", f"{metrics['disk_used']} / {metrics['disk_total']} GB ({metrics['disk_percent']}%)")

        st.subheader("⏱️ Uptime")
        st.write(f"{metrics['uptime']}")

    time.sleep(5)
