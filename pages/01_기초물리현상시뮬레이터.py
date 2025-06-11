pip install -r requirements.txt
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

st.set_page_config(layout="centered", page_title="기초 물리 시뮬레이션")

st.title("🎢 기초 물리 운동 시뮬레이션")
sim_type = st.sidebar.selectbox("시뮬레이션 선택", ["등속도 운동", "등가속도 운동", "작용-반작용", "피스톤 운동"])

fig, ax = plt.subplots()

# 공통
fps = 60
t_max = 5  # 최대 시간
frames = int(fps * t_max)
dt = 1 / fps

if sim_type == "등속도 운동":
    st.sidebar.subheader("속도 입력")
    v = st.sidebar.slider("속도 (m/s)", 0.1, 10.0, 2.0, 0.1)

    ax.set_xlim(0, v * t_max + 2)
    ax.set_ylim(-1, 1)
    obj, = ax.plot([], [], 'ro', markersize=15)

    def update(frame):
        x = v * frame * dt
        obj.set_data(x, 0)
        return obj,

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

elif sim_type == "등가속도 운동":
    st.sidebar.subheader("초기속도와 가속도 입력")
    v0 = st.sidebar.slider("초기 속도 v₀ (m/s)", -10.0, 10.0, 2.0, 0.1)
    a = st.sidebar.slider("가속도 a (m/s²)", -5.0, 5.0, 1.0, 0.1)

    ax.set_xlim(0, v0 * t_max + 0.5 * a * t_max**2 + 2)
    ax.set_ylim(-1, 1)
    obj, = ax.plot([], [], 'bo', markersize=15)

    def update(frame):
        t = frame * dt
        x = v0 * t + 0.5 * a * t**2
        obj.set_data(x, 0)
        return obj,

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

elif sim_type == "작용-반작용":
    st.sidebar.subheader("가속도 입력 (양/음 방향)")
    a1 = st.sidebar.slider("물체 A의 가속도 (m/s²)", -5.0, 5.0, 1.0, 0.1)
    a2 = -a1  # 작용 반작용 (동일 크기 반대 방향)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-1, 1)
    A, = ax.plot([], [], 'go', markersize=15, label="A")
    B, = ax.plot([], [], 'ro', markersize=15, label="B")
    ax.legend()

    def update(frame):
        t = frame * dt
        x1 = 0.5 * a1 * t**2
        x2 = 0.5 * a2 * t**2
        A.set_data(x1, 0.3)
        B.set_data(x2, -0.3)
        return A, B

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

elif sim_type == "피스톤 운동":
    st.sidebar.subheader("크랭크 각속도 조절")
    omega = st.sidebar.slider("회전 속도 ω (rad/s)", 0.1, 10.0, 2.0, 0.1)

    R, L = 1, 3
    ax.set_xlim(-2, 5)
    ax.set_ylim(-2, 2)
    ax.set_aspect("equal")
    crank_line, = ax.plot([], [], 'r', lw=3)
    rod_line, = ax.plot([], [], 'b', lw=3)
    piston = plt.Rectangle((0, -0.5), 0.4, 1, color='gray')
    ax.add_patch(piston)

    def update(frame):
        t = frame * dt
        theta = omega * t
        x_crank = R * np.cos(theta)
        y_crank = R * np.sin(theta)
        x_slider = x_crank + np.sqrt(L**2 - y_crank**2)
        crank_line.set_data([0, x_crank], [0, y_crank])
        rod_line.set_data([x_crank, x_slider], [y_crank, 0])
        piston.set_xy((x_slider - 0.2, -0.5))
        return crank_line, rod_line, piston

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

st.pyplot(fig)
