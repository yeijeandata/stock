import streamlit as st
import pandas as pd
import folium   # 지도 시각화 라이브러리
from streamlit_folium import folium_static  # folium 을 stremlit 에 통합하기 위한 라이브러리

# 페이지 제목 설정
st.title('Streamlit 지도 시각화 예제')

# 샘플 데이터 생성 (서울의 주요 장소들)
data = {
    '장소': ['서울역', '남산타워', '경복궁', '롯데타워', '여의도 한강공원'],
    '위도': [37.5546, 37.5512, 37.5796, 37.5116, 37.5284],
    '경도': [126.9706, 126.9882, 126.9770, 127.1000, 126.9349],
    '방문자 수': [5000, 3500, 4200, 2800, 3200]
}

df = pd.DataFrame(data)

# 서울 중심 좌표
center_lat, center_lon = 37.5665, 126.9780  # 서울 시청 좌표(위도, 경도)

# 기본 맵 설정
st.subheader('서울 주요 장소 방문자 수')

# folium 지도 생성, OpenStreetMap 사용해서 구글 지도 맵과 비슷한 느낌으로 설정
m = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles='OpenStreetMap')


# 각 위치에 마커 추가
for idx, row in df.iterrows(): # df.iterrows() 는 데이터 프레임의 각 행을 반복하는 메소드
    # 방문자 수에 따라 원 크기 조정 (방문자 수/100을 반지름으로 사용)
    radius = row['방문자 수'] / 100  # 빨간점 원의 크기를 지정하기 위해 필요
    folium.CircleMarker(
        location=[row['위도'], row['경도']],
        radius=min(max(radius, 5), 15),  # 최소 5, 최대 15 크기로 원의 크기 제한
        popup=f"{row['장소']}<br>방문자 수: {row['방문자 수']}명",
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.7,
        tooltip=row['장소']
    ).add_to(m)

# Streamlit에 지도 표시
folium_static(m)

# 데이터 테이블도 표시
st.subheader('데이터 테이블')
st.dataframe(df)
