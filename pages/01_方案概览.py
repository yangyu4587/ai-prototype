import streamlit as st
import yaml

st.set_page_config(page_title="方案概览", page_icon="📋", layout="wide")

with open("config.yaml", "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

st.markdown("<div style='font-size:2rem;font-weight:700;color:#1E293B;'>📋 方案概览</div>", unsafe_allow_html=True)
st.markdown("<div style='color:#64748B;margin-bottom:2rem;'>科左后旗县域医共体数智化能力提升建设方案 — 整体介绍</div>", unsafe_allow_html=True)

# 项目背景
st.markdown("### 一、项目背景")
st.markdown("""
科左后旗位于内蒙古自治区通辽市，下辖 33 家医疗机构（含 1 家县级医院、15 家乡镇卫生院、17 家村卫生室），服务常住人口约 28 万人。
当前县域医共体信息化建设存在以下突出问题：
""")

pain_points = [
    ("🏥", "系统孤岛", "各医疗机构信息系统独立运行，数据无法互联互通，重复检查、重复用药问题突出"),
    ("📊", "数据分散", "缺乏统一的数据标准和治理体系，数据质量低，难以支撑管理决策"),
    ("👨‍⚕️", "基层薄弱", "乡镇卫生院信息化水平参差不齐，医生诊疗能力有限，患者向上级医院集中"),
    ("💰", "资源浪费", "人力资源、财务、物资管理粗放，缺乏统一的资源调配机制，运营成本居高不下"),
    ("🤖", "智能缺失", "尚未引入 AI 辅助诊疗能力，基层医生诊断水平难以快速提升"),
]

for icon, title, desc in pain_points:
    with st.container():
        c1, c2 = st.columns([1, 8])
        with c1:
            st.markdown(f"<div style='font-size:2rem;text-align:center;'>{icon}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"**{title}**：{desc}")
    st.markdown("---")

# 建设目标
st.markdown("### 二、建设目标")
goals = [
    ("🌐", "互联互通", "构建统一的医共体数据中心，实现县域内 33 家医疗机构数据互联互通与业务协同"),
    ("🏆", "能力提升", "打造智慧医疗服务平台，提升基层医疗机构诊疗能力与服务质量，实现'小病不出乡'"),
    ("📉", "降本增效", "建立 HRP 统一资源管理平台，实现人财物精细化管理，运营成本降低 30%"),
    ("🧠", "AI 赋能", "引入 AI 辅助诊疗能力，降低漏诊误诊率，提升患者就医体验与满意度"),
    ("📋", "标杆示范", "形成可复制、可推广的县域医共体数智化建设标杆模式"),
]

cols = st.columns(2)
for i, (icon, title, desc) in enumerate(goals):
    with cols[i % 2]:
        st.markdown(f"""
        <div style="background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:1rem;margin-bottom:1rem;">
            <div style="font-size:1.5rem;margin-bottom:0.5rem;">{icon} <b>{title}</b></div>
            <div style="color:#64748B;font-size:0.95rem;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# 核心指标
st.markdown("### 三、核心指标")
metrics = cfg["metrics"]
cols = st.columns(4)
for i, m in enumerate(metrics):
    with cols[i]:
        st.metric(label=f"{m['title']}", value=f"{m['value']}{m['unit']}")

st.markdown("### 四、建设范围")
st.markdown("""
| 层级 | 机构类型 | 数量 | 建设重点 |
|---|---|---|---|
| 县级 | 县医院（牵头医院） | 1 家 | 数据中台、HRP、AI 能力中心 |
| 乡级 | 乡镇卫生院 | 15 家 | HIS/LIS/EMR 升级、远程会诊接入 |
| 村级 | 村卫生室 | 17 家 | 轻量诊疗终端、健康档案采集 |
| **合计** | — | **33 家** | 统一标准、互联互通 |
""")

# 预期成效
st.markdown("### 五、预期成效")
st.markdown("""
- **患者端**：县域内就诊率提升至 90% 以上，平均候诊时间缩短 40%
- **医生端**：基层医生诊疗效率提升 35%，AI 辅助诊断准确率达 95%+
- **管理端**：运营数据实时可视，人财物统一调配，年度运营成本降低 30%
- **监管端**：医共体运行指标全面数字化，支持精细化绩效考核
""")
