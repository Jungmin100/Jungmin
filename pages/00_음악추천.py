import streamlit as st

# 페이지 설정
st.set_page_config(page_title="기분별 음악 추천기", layout="centered")

# 스타일
st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #ffffff;
        background: linear-gradient(90deg, #1db954, #191414);
        padding: 2rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
    }
    .music-card {
        background-color: #f5f5f5;
        padding: 1.2rem;
        border-radius: 1rem;
        margin-bottom: 1.5rem;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown("""
<div class="title">
    <h1>🎶 당신의 기분에 맞는 음악을 추천해드릴게요!</h1>
</div>
""", unsafe_allow_html=True)

# 기분 선택
mood = st.selectbox(
    "지금 당신의 기분이나 상황은 어떤가요?",
    ["기분이 좋을 때 😄", "우울할 때 😢", "공부할 때 📚", "운동할 때 🏋️", "드라이브 중 🚗", "비 오는 날 🌧️"]
)

# 추천 음악 딕셔너리
recommendations = {
    "기분이 좋을 때 😄": [
        {"title": "Happy", "artist": "Pharrell Williams", "url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"},
        {"title": "Good Day", "artist": "IU", "url": "https://www.youtube.com/watch?v=jeqdYqsrsA0"}
    ],
    "우울할 때 😢": [
        {"title": "Someone Like You", "artist": "Adele", "url": "https://www.youtube.com/watch?v=hLQl3WQQoQ0"},
        {"title": "비도 오고 그래서", "artist": "헤이즈", "url": "https://www.youtube.com/watch?v=dzYwXdpz-Zk"}
    ],
    "공부할 때 📚": [
        {"title": "Lofi Hip Hop Radio", "artist": "ChilledCow", "url": "https://www.youtube.com/watch?v=jfKfPfyJRdk"},
        {"title": "Rainy Jazz Cafe", "artist": "Cafe Music BGM channel", "url": "https://www.youtube.com/watch?v=Dx5qFachd3A"}
    ],
    "운동할 때 🏋️": [
        {"title": "Stronger", "artist": "Kanye West", "url": "https://www.youtube.com/watch?v=PsO6ZnUZI0g"},
        {"title": "Eye of the Tiger", "artist": "Survivor", "url": "https://www.youtube.com/watch?v=btPJPFnesV4"}
    ],
    "드라이브 중 🚗": [
        {"title": "Blinding Lights", "artist": "The Weeknd", "url": "https://www.youtube.com/watch?v=4NRXx6U8ABQ"},
        {"title": "Perfect Night", "artist": "LE SSERAFIM", "url": "https://www.youtube.com/watch?v=9q_qRYBRvGk"}
    ],
    "비 오는 날 🌧️": [
        {"title": "Rain", "artist": "태연 (TAEYEON)", "url": "https://www.youtube.com/watch?v=AUFzGiVsJ5c"},
        {"title": "Rainy Days", "artist": "V (BTS)", "url": "https://www.youtube.com/watch?v=r9e2-MJqhTc"}
    ]
}

# 음악 추천 출력
st.subheader(f"🔊 추천 음악 리스트 ({mood})")

for track in recommendations[mood]:
    st.markdown(f"""
    <div class="music-card">
        <strong>{track["title"]}</strong><br>
        👤 {track["artist"]}<br>
        🔗 [YouTube 바로가기]({track["url"]})
    </div>
    """, unsafe_allow_html=True)
