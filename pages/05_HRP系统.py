import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="HRP系统", page_icon="📦", layout="wide")

st.markdown("<div style='font-size:2rem;font-weight:700;color:#1E293B;'>📦 HRP 系统</div>", unsafe_allow_html=True)
st.markdown("<div style='color:#64748B;margin-bottom:2rem;'>医院资源规划系统 — 人财物一体化精细化管理平台</div>", unsafe_allow_html=True)

st.markdown("### 建设理念")
st.info("💡 HRP（Hospital Resource Planning）是医共体运营管理的核心支撑系统，通过对**人力资源、财务、物资、资产**的统一管理，实现从粗放式管理向精细化、数据化、智能化管理的转型。")

tabs = st.tabs(["👥 人力资源", "💰 财务管理", "📦 物资管理", "🏢 资产管理"])

with tabs[0]:
    st.markdown("### 人力资源管理")
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("#### 核心功能")
        st.markdown("- **统一人员档案**：医共体内所有人员（含编制/合同/派遣）统一建档，一岗一档");
        st.markdown("- **智能排班**：基于科室工作量预测的智能排班，支持弹性排班、跨机构支援调配");
        st.markdown("- **绩效考核**：多维度 KPI 考核（工作量、质量、患者满意度、科研教学），绩效透明可溯");
        st.markdown("- **职称晋升**：职称评审流程线上化，学分/论文/考核自动汇总");
        st.markdown("- **培训管理**：继续教育学分自动采集，线上线下培训课程统一管理");
    with col2:
        st.markdown("#### 管理效果")
        st.metric(label="人员调配响应", value="提升 3 倍", delta="跨院支援即时调配")
        st.metric(label="绩效核算周期", value="缩短 70%", delta="从月度到实时")
        st.metric(label="人力成本占比", value="优化 10%", delta="精准排班降本")

with tabs[1]:
    st.markdown("### 财务管理")
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("#### 核心功能")
        st.markdown("- **预算管理**：年度预算编制、分解、执行监控、调整审批全线上化");
        st.markdown("- **成本核算**：科室/病种/项目多级成本核算，DRG/DIP 成本分析");
        st.markdown("- **财务共享**：医共体财务共享中心，集中报账、集中支付、集中核算");
        st.markdown("- **收费管理**：统一收费项目字典，价格调整联动，收入日报自动汇总");
        st.markdown("- **运营分析**：收支结构分析、盈亏平衡点、科室运营效率排名");
    with col2:
        st.markdown("#### 管理效果")
        st.metric(label="财务核算效率", value="提升 50%", delta="共享中心集中处理")
        st.metric(label="预算执行偏差", value="<5%", delta="实时监控预警")
        st.metric(label="运营成本", value="降低 15%", delta="精细化成本管控")

with tabs[2]:
    st.markdown("### 物资管理")
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("#### 核心功能")
        st.markdown("- **耗材管理**：高值耗材扫码溯源、SPD 供应链模式、库存自动补货");
        st.markdown("- **药品管理**：药库-药房-科室三级库存、效期预警、滞销药品分析");
        st.markdown("- **采购管理**：集采平台对接、供应商评价、采购合同线上审批");
        st.markdown("- **库存优化**：安全库存智能计算、呆滞库存预警、科室消耗定额管理");
        st.markdown("- **供应链协同**：与供应商系统对接，实现订单自动下发、物流跟踪");
    with col2:
        st.markdown("#### 管理效果")
        st.metric(label="耗材周转天数", value="缩短 40%", delta="SPD 模式优化")
        st.metric(label="库存资金占用", value="降低 25%", delta="精准补货")
        st.metric(label="过期损耗", value="降低 90%", delta="效期智能预警")

with tabs[3]:
    st.markdown("### 资产管理")
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("#### 核心功能")
        st.markdown("- **资产台账**：医疗设备、房产、车辆等全量资产数字化台账，一物一码");
        st.markdown("- **折旧管理**：多种折旧方法自动计算，财务/税务折旧分离管理");
        st.markdown("- **设备运维**：设备巡检、保养、维修全生命周期管理，故障预警");
        st.markdown("- **资产盘点**：RFID/扫码盘点，账实差异自动比对，盘点效率提升 10 倍");
        st.markdown("- **效益分析**：设备使用率、收入贡献、投资回报分析，支撑采购决策");
    with col2:
        st.markdown("#### 管理效果")
        st.metric(label="盘点效率", value="提升 10 倍", delta="RFID 批量盘点")
        st.metric(label="设备完好率", value="≥98%", delta="预防性维护")
        st.metric(label="资产利用率", value="提升 20%", delta="共享调配")

st.markdown("---")
st.markdown("### HRP 运营仪表盘模拟")

# 模拟仪表盘数据
kpi_data = pd.DataFrame({
    "指标": ["人力成本占比", "药品耗材占比", "百元医疗收入能耗", "平均住院日", "床位周转次数", "门诊次均费用"],
    "当前值": [32, 45, 8.5, 9.2, 28, 185],
    "目标值": [28, 38, 7.0, 8.0, 35, 165],
    "单位": ["%", "%", "元", "天", "次/年", "元"],
})

fig = go.Figure()
fig.add_trace(go.Bar(name="当前值", x=kpi_data["指标"], y=kpi_data["当前值"], marker_color="#EF4444"))
fig.add_trace(go.Bar(name="目标值", x=kpi_data["指标"], y=kpi_data["目标值"], marker_color="#10B981"))
fig.update_layout(barmode="group", title="HRP 核心运营指标对比", yaxis_title="数值")
st.plotly_chart(fig, use_container_width=True)
