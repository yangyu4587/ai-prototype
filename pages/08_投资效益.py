import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="投资效益", page_icon="💰", layout="wide")

st.markdown("<div style='font-size:2rem;font-weight:700;color:#1E293B;'>💰 投资效益</div>", unsafe_allow_html=True)
st.markdown("<div style='color:#64748B;margin-bottom:2rem;'>投资概算、资金来源与预期效益综合分析</div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 投资概算", "📈 ROI 测算", "🎯 综合效益"])

with tab1:
    st.markdown("### 一、总投资概算")
    st.markdown("**项目总投资：1,200 万元**（含软件、硬件、实施、培训、运维）")

    breakdown = pd.DataFrame({
        "投资项目": ["软件平台", "硬件设备", "实施服务", "培训运维"],
        "金额(万元)": [480, 300, 240, 180],
        "占比(%)": [40, 25, 20, 15],
        "说明": [
            "数据中台、业务系统、HRP、AI 平台、集成平台等软件许可与开发",
            "服务器、存储、网络设备、安全设备、终端设备等",
            "项目管理、系统集成、数据迁移、定制开发、上线实施",
            "用户培训、知识转移、首年运维保障、技术支持",
        ],
    })

    col1, col2 = st.columns([3, 2])
    with col1:
        st.dataframe(breakdown, use_container_width=True, hide_index=True)
    with col2:
        fig = px.pie(breakdown, values="金额(万元)", names="投资项目", hole=0.4,
                     title="投资结构占比", color_discrete_sequence=["#2563EB", "#10B981", "#F59E0B", "#EF4444"])
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 二、分阶段投入")
    phase_invest = pd.DataFrame({
        "阶段": ["一期（1-6月）", "二期（7-12月）", "三期（13-18月）"],
        "投入(万元)": [450, 480, 270],
        "占比(%)": [37.5, 40, 22.5],
        "主要投向": [
            "数据中心、网络、HIS/LIS 升级",
            "PACS/EMR/HRP/远程医疗",
            "AI 中台、运营平台、验收优化",
        ],
    })
    st.dataframe(phase_invest, use_container_width=True, hide_index=True)

    st.markdown("### 三、资金来源")
    source = pd.DataFrame({
        "资金来源": ["中央财政转移支付", "自治区配套资金", "市级配套资金", "县级自筹资金"],
        "金额(万元)": [400, 300, 200, 300],
        "占比(%)": [33.3, 25, 16.7, 25],
    })
    fig2 = px.bar(source, x="资金来源", y="金额(万元)", text="金额(万元)",
                  title="资金来源构成", color="资金来源",
                  color_discrete_sequence=["#2563EB", "#10B981", "#F59E0B", "#EF4444"])
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.markdown("### 一、直接经济效益测算")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 成本节约项（年度）")
        savings = pd.DataFrame({
            "节约项": ["减少重复检查", "降低药品耗材占比", "人力成本优化", "胶片成本节约", "运营管理提效"],
            "年节约(万元)": [180, 220, 150, 80, 70],
        })
        fig3 = px.bar(savings, x="年节约(万元)", y="节约项", orientation="h",
                      title="年度成本节约预估", color="年节约(万元)",
                      color_continuous_scale="Greens")
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        st.markdown("#### 收益增加项（年度）")
        revenue = pd.DataFrame({
            "收益项": ["县域内就诊率提升", "医保结余奖励", "远程服务收入", "数据服务收入"],
            "年收益(万元)": [120, 100, 50, 30],
        })
        fig4 = px.bar(revenue, x="年收益(万元)", y="收益项", orientation="h",
                      title="年度收益增加预估", color="年收益(万元)",
                      color_continuous_scale="Blues")
        st.plotly_chart(fig4, use_container_width=True)

    total_annual_benefit = 700  # 180+220+150+80+70+120+100+50+30
    investment = 1200
    payback_months = int(investment / (total_annual_benefit / 12))

    st.markdown("### 二、ROI 核心指标")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label="年度综合效益", value="¥700万", delta="直接+间接")
    with c2:
        st.metric(label="投资回收期", value=f"{payback_months}个月", delta="约 1.7 年")
    with c3:
        st.metric(label="5 年 ROI", value="192%", delta="净收益 ¥2,300万")
    with c4:
        st.metric(label="年均降本增效", value="23%", delta="运营成本优化")

    st.markdown("### 三、投资回报周期模拟")
    years = list(range(0, 6))
    cumulative = [-1200, -650, 50, 850, 1650, 2450]
    annual = [-1200, 550, 700, 800, 800, 800]

    fig5 = go.Figure()
    fig5.add_trace(go.Bar(name="年度净现金流", x=years, y=annual, marker_color=["#EF4444"]+["#10B981"]*5))
    fig5.add_trace(go.Scatter(name="累计现金流", x=years, y=cumulative, mode="lines+markers",
                               line=dict(color="#2563EB", width=3), marker=dict(size=10)))
    fig5.update_layout(title="投资回报周期模拟（万元）", xaxis_title="年份", yaxis_title="金额(万元)",
                       legend=dict(orientation="h", yanchor="bottom", y=1.02))
    fig5.add_hline(y=0, line_dash="dash", line_color="gray")
    st.plotly_chart(fig5, use_container_width=True)

    # ROI 可调计算器
    st.markdown("### 四、ROI 可调计算器")
    st.markdown("拖动滑块，根据您的实际情况调整参数，查看 ROI 变化：")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        invest_slider = st.slider("总投资(万元)", 800, 1800, 1200, 50)
    with col_b:
        save_slider = st.slider("年成本节约(万元)", 300, 1000, 600, 20)
    with col_c:
        revenue_slider = st.slider("年收益增加(万元)", 100, 500, 300, 10)

    total_annual = save_slider + revenue_slider
    payback = invest_slider / (total_annual / 12)
    roi_5y = (total_annual * 5 - invest_slider) / invest_slider * 100

    st.markdown(f"""
    <div style="background:#EFF6FF;border-radius:12px;padding:1.5rem;margin-top:1rem;text-align:center;">
        <div style="display:flex;justify-content:space-around;">
            <div>
                <div style="font-size:2rem;font-weight:700;color:#2563EB;">{total_annual}万</div>
                <div style="color:#64748B;">年度综合效益</div>
            </div>
            <div>
                <div style="font-size:2rem;font-weight:700;color:#2563EB;">{payback:.1f}个月</div>
                <div style="color:#64748B;">投资回收期</div>
            </div>
            <div>
                <div style="font-size:2rem;font-weight:700;color:#2563EB;">{roi_5y:.0f}%</div>
                <div style="color:#64748B;">5 年 ROI</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("### 一、社会效益")
    social = [
        ("👨‍⚕️", "提升基层能力", "乡镇卫生院诊疗能力接近县级医院水平，患者留在基层的信心增强"),
        ("🏠", "促进分级诊疗", "县域内就诊率从 85% 提升至 90%+，实现'小病不出乡、大病不出县'"),
        ("💊", "减少重复医疗", "检验检查互认避免重复检查，减轻患者经济负担与身体伤害"),
        ("🩺", "均衡医疗资源", "远程医疗让基层患者享受上级专家服务，缩小城乡医疗差距"),
        ("📋", "提升公卫水平", "传染病监测、慢病管理数字化，公共卫生应急响应能力显著增强"),
    ]
    for icon, title, desc in social:
        st.markdown(f"**{icon} {title}**：{desc}")

    st.markdown("### 二、管理效益")
    management = [
        ("📊", "数据驱动决策", "管理驾驶舱实时呈现运营全貌，决策从经验驱动转向数据驱动"),
        ("⚖️", "精细绩效考核", "多维度量化考核，激励导向明确，医务人员积极性显著提升"),
        ("🔗", "流程标准化", "业务流程数字化再造，减少人为差错，提升管理透明度"),
        ("📉", "成本可控可降", "人财物统一调配，库存周转加快，运营成本持续优化"),
    ]
    for icon, title, desc in management:
        st.markdown(f"**{icon} {title}**：{desc}")

    st.markdown("### 三、技术效益")
    tech = [
        ("🏗️", "架构先进可扩展", "云原生微服务架构，支持未来业务持续扩展与技术迭代"),
        ("🔄", "标准规范统一", "遵循国家行业标准，为后续互联互通五级、智慧医院评级奠定基础"),
        ("📤", "模式可复制推广", "形成县域医共体数智化建设标准包，可向周边旗县快速复制"),
        ("🤖", "AI 能力持续进化", "AI 中台具备模型持续训练能力，诊断准确率随数据积累不断提升"),
    ]
    for icon, title, desc in tech:
        st.markdown(f"**{icon} {title}**：{desc}")

    st.markdown("---")
    st.success("""
    ✅ **综合评估结论**：
    本项目投资 1,200 万元，预期 20 个月内收回投资，5 年 ROI 达 192%。
    不仅带来显著的经济效益，更在提升基层医疗能力、促进分级诊疗、缩小城乡医疗差距等方面产生深远的社会价值，
    是一项兼具经济可行性与社会必要性的优质项目。
    """)
