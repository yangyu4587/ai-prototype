import streamlit as st
import yaml

# 页面配置 —— 必须在所有 st 命令之前
st.set_page_config(
    page_title="科左后旗县域医共体数智化方案",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 加载配置
with open("config.yaml", "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

# 自定义 CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #64748B;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        border-radius: 12px;
        padding: 1.5rem;
        color: white;
        text-align: center;
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
    }
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1E293B;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #E2E8F0;
    }
    .highlight-box {
        background-color: #EFF6FF;
        border-left: 4px solid #2563EB;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 40px;
        padding-left: 16px;
        padding-right: 16px;
        border-radius: 8px 8px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# 侧边栏
with st.sidebar:
    st.markdown("### 🏥 远盟元康")
    st.markdown("**科左后旗县域医共体**")
    st.markdown("数智化能力提升建设方案")
    st.divider()

    st.markdown("#### 📋 方案目录")
    pages = [
        "01_方案概览",
        "02_现状分析",
        "03_总体架构",
        "04_业务系统",
        "05_HRP系统",
        "06_AI能力演示",
        "07_实施路线",
        "08_投资效益",
    ]

    for p in pages:
        label = p.split("_", 1)[1]
        st.page_link(f"pages/{p}.py", label=label)

    st.divider()
    st.markdown("#### 📊 方案指标")
    for m in cfg["metrics"]:
        st.metric(label=f"{m['icon']} {m['title']}", value=f"{m['value']}{m['unit']}")

    st.divider()
    st.caption("© 2026 远盟元康（南京）科技有限公司")

# 主内容区（仅当直接访问 app.py 时显示欢迎页）
st.markdown('<div class="main-header">科左后旗县域医共体数智化能力提升建设方案</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">以数据驱动为核心，构建覆盖全县域的数字化医疗健康服务体系</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
metrics = cfg["metrics"]
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{metrics[0]['value']}</div>
        <div class="metric-label">{metrics[0]['icon']} {metrics[0]['title']} ({metrics[0]['unit']})</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{metrics[1]['value']}</div>
        <div class="metric-label">{metrics[1]['icon']} {metrics[1]['title']} ({metrics[1]['unit']})</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{metrics[2]['value']}</div>
        <div class="metric-label">{metrics[2]['icon']} {metrics[2]['title']} ({metrics[2]['unit']})</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{metrics[3]['value']}%</div>
        <div class="metric-label">{metrics[3]['icon']} {metrics[3]['title']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">🎯 建设目标</div>', unsafe_allow_html=True)

goals = [
    "构建统一的医共体数据中心，实现县域内 33 家医疗机构数据互联互通",
    "打造智慧医疗服务平台，提升基层医疗机构诊疗能力与服务质量",
    "建立 HRP 统一资源管理平台，实现人财物精细化管理和降本增效",
    "引入 AI 辅助诊疗能力，降低漏诊误诊率，提升患者就医体验",
    "形成可复制、可推广的县域医共体数智化建设标杆模式",
]

for i, g in enumerate(goals, 1):
    st.markdown(f'<div class="highlight-box"><b>{i}.</b> {g}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">📐 建设内容总览</div>', unsafe_allow_html=True)

st.markdown("""
| 建设模块 | 核心内容 | 覆盖范围 |
|---|---|---|
| **数据中心** | 医共体统一数据中台、数据标准、数据治理 | 全县域 33 家机构 |
| **业务系统** | HIS / LIS / PACS / EMR 升级与互联互通 | 县医院、乡镇卫生院、村卫生室 |
| **HRP 系统** | 人力资源、财务、物资、资产统一管理 | 医共体牵头医院及成员单位 |
| **AI 赋能** | 智能辅助诊断、影像 AI、慢病管理助手 | 重点科室与基层医生 |
| **运营平台** | 大数据分析、绩效评价、监管决策支持 | 医共体管理委员会 |
""")

st.info("👈 **请点击左侧导航菜单，逐项浏览方案各章节内容。** 每页均支持交互操作，可替代传统 PPT 进行现场演示。")
