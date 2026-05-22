import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="数据中心建设演示", page_icon="🗄️", layout="wide")

# 自定义 CSS
st.markdown("""
<style>
    .main-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.3rem;
    }
    .sub-title {
        font-size: 1rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        border-radius: 12px;
        padding: 1.2rem;
        color: white;
        text-align: center;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
    }
    .metric-label {
        font-size: 0.85rem;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# 标题区
st.markdown('<div class="main-title">🗄️ 医共体数据中心建设</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">构建统一数据中台，实现县域内 33 家医疗机构数据互联互通</div>', unsafe_allow_html=True)

# 核心指标卡片
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">33</div>
        <div class="metric-label">家医疗机构接入</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">500万</div>
        <div class="metric-label">日增量数据条数</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value"><200ms</div>
        <div class="metric-label">接口响应时间</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 两栏布局
left, right = st.columns(2)

with left:
    st.markdown("### 📋 五大建设内容")

    items = [
        ("📊", "数据标准制定", "高", "参照国家卫健委行业标准，统一数据元、数据集、数据字典"),
        ("🔑", "主数据管理", "高", "科室、人员、药品、诊断、收费项目等统一编码与映射"),
        ("🔄", "数据采集汇聚", "高", "ETL 工具抽取各机构业务数据，支持实时与批量采集"),
        ("🛡️", "数据治理", "中", "质量评分、脱敏加密、分级分类、生命周期管理"),
        ("🔌", "数据服务", "中", "API 接口封装，支撑上层应用敏捷开发"),
    ]

    for icon, title, level, desc in items:
        color = "#EF4444" if level == "高" else "#F59E0B"
        st.markdown(f"""
        <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:8px;padding:0.8rem;margin-bottom:0.6rem;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-weight:600;">{icon} {title}</span>
                <span style="background:{color};color:white;padding:2px 8px;border-radius:4px;font-size:0.75rem;">{level}优先级</span>
            </div>
            <div style="color:#64748B;font-size:0.85rem;margin-top:0.3rem;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    # 横向条形图：建设内容优先级
    df_priority = px.data.tips()
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        y=["数据标准制定", "主数据管理", "数据采集汇聚", "数据治理", "数据服务"],
        x=[95, 90, 88, 75, 70],
        orientation='h',
        marker_color=["#EF4444", "#EF4444", "#EF4444", "#F59E0B", "#F59E0B"],
        text=["95", "90", "88", "75", "70"],
        textposition="outside",
    ))
    fig1.update_layout(
        title="建设优先级评分",
        xaxis_title="优先级评分",
        yaxis_title="",
        height=280,
        margin=dict(l=20, r=40, t=40, b=20),
    )
    st.plotly_chart(fig1, use_container_width=True)

with right:
    st.markdown("### 📈 预期效果对比")

    # 分组柱状图：当前 vs 目标
    categories = ["数据标准化率", "数据质量评分", "接口可用性", "数据完整率"]
    current = [45, 60, 85, 70]
    target = [90, 85, 99, 95]

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(name="当前水平", x=categories, y=current, marker_color="#94A3B8"))
    fig2.add_trace(go.Bar(name="建设目标", x=categories, y=target, marker_color="#2563EB"))
    fig2.update_layout(
        barmode="group",
        title="关键指标：当前值 vs 目标值",
        yaxis_title="百分比(%)",
        height=300,
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    st.plotly_chart(fig2, use_container_width=True)

    # 关键提升幅度
    st.markdown("#### 🎯 核心提升幅度")
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="数据标准化率", value="90%", delta="+45%")
    with col_b:
        st.metric(label="数据质量评分", value="85分", delta="+25分")

    col_c, col_d = st.columns(2)
    with col_c:
        st.metric(label="接口可用性", value="99%", delta="+14%")
    with col_d:
        st.metric(label="数据完整率", value="95%", delta="+25%")

st.markdown("---")
st.markdown("### 🏗️ 数据中心架构")
st.markdown("""
```
┌─────────────────────────────────────────────────────────────┐
│                     【数据服务层】                             │
│    API 网关 │ 数据查询 │ 报表服务 │ AI 训练数据供给             │
├─────────────────────────────────────────────────────────────┤
│                     【数据治理层】                             │
│    质量评分 │ 脱敏加密 │ 分级分类 │ 元数据管理 │ 血缘追踪        │
├─────────────────────────────────────────────────────────────┤
│                     【数据存储层】                             │
│    CDR 临床库 │ ODR 运营库 │ RDR 科研库 │ 主数据 MDM          │
├─────────────────────────────────────────────────────────────┤
│                     【数据采集层】                             │
│    ETL 引擎 │ 实时同步 │ 消息队列 │ 日志采集 │ 接口适配        │
├─────────────────────────────────────────────────────────────┤
│                     【数据源层】                               │
│    HIS │ LIS │ PACS │ EMR │ HRP │ 公卫 │ 物联网 │ 外部系统     │
└─────────────────────────────────────────────────────────────┘
```
""")

st.success("✅ **建设成效**：数据中心建成后，医共体 33 家机构实现'数据同源、标准同标、服务同频'，为智慧医疗应用奠定坚实的数据底座。")
