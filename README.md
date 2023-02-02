# CP6-Project-PlotUI
## 프로젝트 소개
CSV파일의 데이터를 읽고 그래프로 표현하여 분석하는 프로그램입니다.
### 개발 기간
* 22.12.26 - 23.02.07
### 개발 환경
* Python 3.9
* PyQt5
* QtDisigner 5.15
* IDE : VisualStudioCode
### 주요 기능
#### FileLoad
* csv파일을 선택하면 파일의 이름과 csv파일 내부의 데이터 목록이 TreeWidget에 표시됩니다.
#### GraphPlot
* TreeWidget의 데이터 목록을 Drag하여 우측 GraphPlot에 Drop하면 그래프가 표시됩니다.
* GraphPlot에서 확대/축소 기능을 사용할 수 있습니다.
* 여러개의 데이터를 Drop하여 Graph들의 값들을 비교할 수 있습니다.
* GraphPlot의 하단 부분에 재생버튼으로 표시된 Graph들의 값을 실시간으로 확인할 수 있습니다.
* 반복재생/일시정지 기능을 사용할 수 있습니다.
* 표현된 GraphPlot을 이미지파일로 저장할 수 있습니다.
### 진행 중인 기능
* TabWidget
* Graph Split
* Split Graph 동기화 (여러개로 나누어진 그래프들의 값들을 실시간으로 비교)
* 시간축/재생바 수동 이동
* 대용량 데이터 사용
* GraphPlot 초기화
* CheckBox On/Off를 활용해 트리위젯에서 데이터 목록의 Value 표시
### License
* MIT License
