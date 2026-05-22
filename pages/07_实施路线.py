import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="实施路线", page_icon="🗓️", layout="wide")

st.markdown("<div style='font-size:2rem;font-weight:700;color:#1E293B;'>🗓️ 实施路线</div>", unsafe_allow_html=True)
st.markdown("<div style='color:#64748B;margin-bottom:2rem;'>三期渐进式建设，18 个月完成医共体数智化全面转型</div>", unsafe_allow_html=True)

phases = [
    ("一期：基础夯实", "第 1-6 个月", "#2563EB", [
        ("数据中心建设", "搭建医共体统一数据中台，完成数据标准制定与主数据治理", "M1-M3"),
        ("网络基础设施", "医共体专网升级，县-乡-村三级网络全覆盖，安全设备部署", "M1-M2"),
        ("统一身份认证", "建设 SSO 单点登录平台，实现一账号通办所有系统", "M2-M3"),
        ("HIS 系统升级", "县医院 HIS 核心升级，乡镇卫生院 HIS 适配改造", "M3-M5"),
        ("LIS 系统升级", "检验系统标准化改造，接入区域检验中心", "M4-M6"),
        ("数据迁移对接", "完成历史数据清洗迁移，实现核心业务数据互联互通", "M5-M6"),
    ]),
    ("二期：能力提升", "第 7-12 个月", "#10B981", [
        ("PACS 影像云", "部署区域影像云平台，实现影像集中存储与共享调阅", "M7-M9"),
        ("EMR 互联互通", "电子病历系统升级，达到互联互通四级甲等标准", "M7-M10"),
        ("HRP 系统上线", "人财物一体化管理平台部署，覆盖县医院及乡镇卫生院", "M8-M11"),
        ("远程医疗平台", "建设远程会诊、远程影像、远程心电系统", "M9-M10"),
        ("集成平台深化", "ESB 总线全面贯通，业务流程自动化编排", "M9-M11"),
        ("数据治理深化", "建立数据质量监控体系，运营指标看板上线", "M10-M12"),
    ]),
    ("三期：智慧赋能", "第 13-18 个月", "#F59E0B", [
        ("AI 中台建设", "医学 NLP、影像 AI、知识图谱等模型训练与部署", "M13-M15"),
        ("AI 场景落地", "智能分诊、辅助诊断、合理用药、病历质控等场景上线", "M14-M16"),
        ("运营分析平台", "大数据运营分析平台，支持 DRG/DIP 绩效分析", "M14-M16"),
        ("健康管理门户", "居民健康管理小程序上线，家庭医生签约服务数字化", "M15-M17"),
        ("全面验收优化", "系统调优、用户培训、文档交付、等级评审准备", "M16-M18"),
        ("标杆推广准备", "形成建设标准与实施方法论，准备对外复制推广", "M17-M18"),
    ]),
]

for name, period, color, tasks in phases:
    with st.container():
        st.markdown(f"""
        <div style="background:{color}15;border-left:5px solid {color};border-radius:8px;padding:1.5rem;margin-bottom:1.5rem;">
            <div style="font-size:1.4rem;font-weight:700;color:{color};">{name}</div>
            <div style="color:#64748B;font-size:0.95rem;margin-top:0.3rem;">⏱️ {period}</div>
        </div>
        """, unsafe_allow_html=True)

        for i, (task, desc, time) in enumerate(tasks):
            c1, c2, c3 = st.columns([2, 6, 2])
            with c1:
                st.markdown(f"**{task}**")
            with c2:
                st.markdown(desc)
            with c3:
                st.markdown(f"<span style='color:{color};font-weight:600;'>{time}</span>", unsafe_allow_html=True)
            if i < len(tasks) - 1:
                st.markdown("<div style='border-bottom:1px dashed #E2E8F0;margin:0.5rem 0;'></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 项目里程碑甘特图")

df_gantt = pd.DataFrame([
    dict(Task="数据中心建设", Start="2026-06-01", Finish="2026-08-31", Phase="一期"),
    dict(Task="网络基础设施", Start="2026-06-01", Finish="2026-07-31", Phase="一期"),
    dict(Task="统一身份认证", Start="2026-07-01", Finish="2026-08-31", Phase="一期"),
    dict(Task="HIS 系统升级", Start="2026-08-01", Finish="2026-10-31", Phase="一期"),
    dict(Task="LIS 系统升级", Start="2026-09-01", Finish="2026-11-30", Phase="一期"),
    dict(Task="数据迁移对接", Start="2026-10-01", Finish="2026-11-30", Phase="一期"),
    dict(Task="PACS 影像云", Start="2026-12-01", Finish="2027-02-28", Phase="二期"),
    dict(Task="EMR 互联互通", Start="2026-12-01", Finish="2027-03-31", Phase="二期"),
    dict(Task="HRP 系统上线", Start="2027-01-01", Finish="2027-04-30", Phase="二期"),
    dict(Task="远程医疗平台", Start="2027-02-01", Finish="2027-03-31", Phase="二期"),
    dict(Task="集成平台深化", Start="2027-02-01", Finish="2027-04-30", Phase="二期"),
    dict(Task="数据治理深化", Start="2027-03-01", Finish="2027-05-31", Phase="二期"),
    dict(Task="AI 中台建设", Start="2027-06-01", Finish="2027-08-31", Phase="三期"),
    dict(Task="AI 场景落地", Start="2027-07-01", Finish="2027-09-30", Phase="三期"),
    dict(Task="运营分析平台", Start="2027-07-01", Finish="2027-09-30", Phase="三期"),
    dict(Task="健康管理门户", Start="2027-08-01", Finish="2027-10-31", Phase="三期"),
    dict(Task="全面验收优化", Start="2027-09-01", Finish="2027-11-30", Phase="三期"),
    dict(Task="标杆推广准备", Start="2027-10-01", Finish="2027-11-30", Phase="三期"),
])

color_map = {"一期": "#2563EB", "二期": "#10B981", "三期": "#F59E0B"}
fig = px.timeline(df_gantt, x_start="Start", x_end="Finish", y="Task", color="Phase",
                  color_discrete_map=color_map, title="项目实施甘特图")
fig.update_yaxes(autorange="reversed")
fig.update_layout(height=600)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 关键里程碑")
milestones = [
    ("M3", "2026-08", "数据中台上线", "完成数据标准制定，首批 3 家机构接入"),
    ("M6", "2026-11", "一期验收", "HIS/LIS 升级完成，核心业务互联互通"),
    ("M9", "2027-02", "影像云上线", "区域影像云正式运营，远程会诊开通"),
    ("M12", "2027-05", "二期验收", "EMR/HRP/远程医疗全面上线"),
    ("M15", "2027-08", "AI 中台就绪", "AI 模型训练完成，具备场景落地条件"),
    ("M18", "2027-11", "终验交付", "全部系统上线运营，通过等级评审"),
]

cols = st.columns(3)
for i, (code, time, title, desc) in enumerate(milestones):
    with cols[i % 3]:
        st.markdown(f"""
        <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:8px;padding:1rem;margin-bottom:1rem;">
            <div style="color:#2563EB;font-weight:700;font-size:0.9rem;">{code} · {time}</div>
            <div style="font-weight:600;margin:0.3rem 0;">{title}</div>
            <div style="color:#64748B;font-size:0.85rem;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
