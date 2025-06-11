import streamlit as st
import folium
from streamlit_folium import st_folium

# 독일의 주요 여행지 데이터
travel_destinations = {
    "베를린": {
        "lat": 52.52,
        "lon": 13.405,
        "description": "독일의 수도이자 문화, 역사, 예술이 살아있는 도시입니다. 브란덴부르크 문, 베를린 장벽, 박물관 섬 등이 유명합니다."
    },
    "뮌헨": {
        "lat": 48.1351,
        "lon": 11.5820,
        "description": "바이에른주의 중심 도시로 맥주 축제 '옥토버페스트'로 유명하며, 알프스와 가까워 자연과 도시를 함께 즐길 수 있습니다."
    },
    "함부르크": {
        "lat": 53.5511,
        "lon": 9.9937,
        "description": "엘베 강 하구에 있는 항구 도시로, 현대적인 건축과 아름다운 항구 풍경이 인상적입니다. 미니아투어 원더랜드도 인기가 많습니다."
    },
    "하이델베르크": {
        "lat": 49.3988,
        "lon": 8.6724,
        "description": "고성, 대학, 낭만적인 경치로 유명한 도시입니다. 고풍스러운 건축과 네카 강이 어우러진 아름다운 풍경을 자랑합니다."
    },
    "쾰른": {
        "lat": 50.9375,
        "lon": 6.9603,
        "description": "고딕 양식의 쾰른 대성당이 있는 도시로, 라인 강 유역에서 문화를 즐기기에 좋은 장소입니다."
    }
}

# Streamlit 앱 제목
st.title("🇩🇪 독일 여행지 가이드")

# 도시 선택
city = st.selectbox("방문하고 싶은 도시를 선택하세요:", list(travel_destinations.keys()))

# 선택한 도시 정보 출력
st.subheader(f"📍 {city}")
st.write(travel_destinations[city]["description"])

# Folium 지도 생성
map_center = [travel_destinations[city]["lat"], travel_destinations[city]["lon"]]
m = folium.Map(location=map_center, zoom_start=6)
folium.Marker(
    location=map_center,
    popup=city,
    tooltip=f"{city} 위치 보기"
).add_to(m)

# Streamlit에 Folium 지도 표시
st_folium(m, width=700, height=500)
