import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit.components.v1 import html

# 페이지 설정
st.set_page_config(page_title="독일 여행 가이드", layout="wide")

# CSS로 스타일링
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
    }
    .hero {
        text-align: center;
        margin-bottom: 2rem;
    }
    .hero h1 {
        font-size: 3rem;
        color: #1f4e79;
        margin-bottom: 0.5rem;
    }
    .hero p {
        font-size: 1.2rem;
        color: #444;
    }
    .city-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        margin-top: 1rem;
    }
    .map-container {
        border-radius: 1rem;
        overflow: hidden;
        margin-top: 1rem;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 도시 데이터
travel_destinations = {
    "베를린": {
        "lat": 52.52,
        "lon": 13.405,
        "description": "🟢 독일의 수도이자 문화, 역사, 예술이 살아있는 도시입니다. 브란덴부르크 문, 베를린 장벽, 박물관 섬 등이 유명합니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Brandenburger_Tor_abends.jpg/640px-Brandenburger_Tor_abends.jpg"
    },
    "뮌헨": {
        "lat": 48.1351,
        "lon": 11.5820,
        "description": "🍺 바이에른주의 중심 도시로, 옥토버페스트와 알프스 자연경관으로 유명합니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/M%C3%BCnchen_-_Marienplatz_-_Rathaus_und_Frauenkirche.jpg/640px-M%C3%BCnchen_-_Marienplatz_-_Rathaus_und_Frauenkirche.jpg"
    },
    "함부르크": {
        "lat": 53.5511,
        "lon": 9.9937,
        "description": "⚓ 엘베 강 하구에 있는 항구 도시로, 미니아투어 원더랜드가 인기입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Hamburg_Hafenpanorama.jpg/640px-Hamburg_Hafenpanorama.jpg"
    },
    "하이델베르크": {
        "lat": 49.3988,
        "lon": 8.6724,
        "description": "🏰 고성, 고대 대학과 낭만적인 경치로 유명한 독일의 보석 같은 도시입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Heidelberg_Castle_panorama_2016.jpg/640px-Heidelberg_Castle_panorama_2016.jpg"
    },
    "쾰른": {
        "lat": 50.9375,
        "lon": 6.9603,
        "description": "⛪ 고딕 양식의 쾰른 대성당으로 유명하며, 라인 강에서 유람도 즐길 수 있습니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/K%C3%B6lner_Dom_von_Osten.jpg/640px-K%C3%B6lner_Dom_von_Osten.jpg"
    }
}

# Hero 영역
st.markdown("""
<div class="hero">
    <h1>🇩🇪 독일 여행 가이드</h1>
    <p>당신만의 독일 여행지를 찾아보세요! 🧳✨</p>
</div>
""", unsafe_allow_html=True)

# 도시 선택
city = st.selectbox("🌍 여행지를 선택하세요", list(travel_destinations.keys()))

# 도시 카드 표시
with st.container():
    st.markdown(f"""
    <div class="city-card">
        <h2>{city}</h2>
        <img src="{travel_destinations[city]['image']}" width="100%" style="border-radius: 1rem; margin-bottom: 1rem;">
        <p>{travel_destinations[city]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

# 지도 표시
map_center = [travel_destinations[city]["lat"], travel_destinations[city]["lon"]]
m = folium.Map(location=map_center, zoom_start=6)
folium.Marker(
    location=map_center,
    popup=city,
    tooltip=city
).add_to(m)

with st.container():
    st.markdown('<div class="map-container">', unsafe_allow_html=True)
    st_folium(m, width=700, height=450)
    st.markdown('</div>', unsafe_allow_html=True)

