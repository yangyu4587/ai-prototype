import streamlit as st

st.set_page_config(page_title="总体架构", page_icon="🏗️", layout="wide")

st.markdown("<div style='font-size:2rem;font-weight:700;color:#1E293B;'>🏗️ 总体架构</div>", unsafe_allow_html=True)
st.markdown("<div style='color:#64748B;margin-bottom:2rem;'>医共体数智化分层架构设计 — 五层体系 + 两大保障</div>", unsafe_allow_html=True)

st.markdown("### 架构总览")
st.markdown("""
```
┌─────────────────────────────────────────────────────────────────┐
│                        【展现层】                                  │
│   区域健康门户 │ 医生工作站 │ 管理驾驶舱 │ 患者小程序 │ 监管大屏     │
├─────────────────────────────────────────────────────────────────┤
│                        【应用层】                                  │
│   智慧医疗 │ 智慧服务 │ 智慧管理 │ 协同共享 │ 公共卫生 │ 家庭医生    │
├─────────────────────────────────────────────────────────────────┤
│                        【平台层】                                  │
│   数据中台 │ 业务中台 │ AI 中台 │ 集成平台 │ 统一认证 │ 远程医疗    │
├─────────────────────────────────────────────────────────────────┤
│                        【数据层】                                  │
│   临床数据中心(CDR) │ 运营数据中心(ODR) │ 科研数据中心(RDR)        │
│   主数据管理(MDM)   │ 数据治理与质控    │ 数据安全与隐私保护         │
├─────────────────────────────────────────────────────────────────┤
│                        【基础设施层】                               │
│   计算资源(云/本地) │ 存储资源 │ 网络通讯 │ 安全设备 │ 终端设备      │
└─────────────────────────────────────────────────────────────────┘
         ↑ 标准规范体系          ↑ 信息安全体系
```
""")

layers = [
    ("🖥️", "展现层", "面向患者、医护人员、管理人员的多端统一入口", [
        "区域健康门户：居民健康档案查询、预约挂号、报告查询",
        "医生工作站：集成 AI 辅助的门诊/住院/检查一体化工作界面",
        "管理驾驶舱：实时运营数据可视化，支持多维度钻取分析",
        "患者小程序：轻量级移动端服务，覆盖预约挂号、缴费、报告查询",
        "监管大屏：医共体管理委员会决策支持大屏",
    ], "#EFF6FF"),
    ("📱", "应用层", "六大智慧应用群，覆盖医疗、服务、管理全场景", [
        "智慧医疗：电子病历、临床路径、合理用药、AI 辅助诊断",
        "智慧服务：智能导诊、在线问诊、慢病随访、健康管理",
        "智慧管理：HRP 人财物统一、供应链、绩效考核、预算管理",
        "协同共享：双向转诊、远程会诊、检验检查互认、影像云",
        "公共卫生：疾病监测、疫苗管理、健康宣教、突发公卫应急",
        "家庭医生：签约管理、健康评估、上门服务、重点人群随访",
    ], "#ECFDF5"),
    ("⚙️", "平台层", "三大中台 + 三大平台，构建能力共享底座", [
        "数据中台：数据采集、清洗、建模、服务化封装",
        "业务中台：患者中心、医嘱中心、收费中心、物资中心",
        "AI 中台：医学 NLP、影像识别、知识图谱、智能推理引擎",
        "集成平台：ESB 企业服务总线，HL7/FHIR/DICOM 标准协议适配",
        "统一认证：单点登录(SSO)、身份联邦、权限管理、操作审计",
        "远程医疗：高清视频会诊、远程影像诊断、远程心电监护",
    ], "#FFFBEB"),
    ("🗄️", "数据层", "三大数据中心 + 数据治理体系，奠定数据资产基础", [
        "临床数据中心(CDR)：整合门急诊、住院、检验、检查、用药全量临床数据",
        "运营数据中心(ODR)：人财物运营数据汇聚，支撑精细化管理和绩效考核",
        "科研数据中心(RDR)：脱敏后的科研级数据集，支持真实世界研究",
        "主数据管理(MDM)：科室、人员、药品、诊断、收费项目等统一主数据",
        "数据治理与质控：数据标准、元数据管理、数据质量评分、质控规则引擎",
        "数据安全与隐私保护：分级分类、脱敏加密、访问控制、操作审计",
    ], "#F3E8FF"),
    ("🔧", "基础设施层", "混合云架构，弹性可扩展", [
        "计算资源：私有云 + 公有云混合部署，关键业务本地、弹性业务上云",
        "存储资源：分布式存储，支持结构化/非结构化/影像海量数据",
        "网络通讯：医共体专网 + 5G 医疗专网，保障低时延高可靠",
        "安全设备：下一代防火墙、入侵检测、WAF、堡垒机、漏洞扫描",
        "终端设备：医生工作站、护士 PDA、自助服务机、村医移动终端",
    ], "#F1F5F9"),
]

for icon, name, desc, items, bg in layers:
    with st.container():
        st.markdown(f"""
        <div style="background:{bg};border-radius:12px;padding:1.5rem;margin-bottom:1rem;border:1px solid #E2E8F0;">
            <div style="font-size:1.3rem;font-weight:700;margin-bottom:0.5rem;">{icon} {name}</div>
            <div style="color:#64748B;margin-bottom:1rem;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
        for item in items:
            st.markdown(f"- {item}")
    st.markdown("---")

st.markdown("### 两大保障体系")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style="background:#EFF6FF;border-radius:12px;padding:1.5rem;border:1px solid #BFDBFE;">
        <div style="font-size:1.2rem;font-weight:700;color:#1D4ED8;margin-bottom:0.5rem;">📋 标准规范体系</div>
        <ul style="color:#1E293B;">
            <li>数据标准：参照国家卫健委行业标准与 FHIR 国际标准</li>
            <li>接口标准：HL7 v2/v3、DICOM、IHE 集成规范</li>
            <li>安全标准：等保 2.0 三级、数据安全法、个人信息保护法</li>
            <li>运维标准：ITIL 服务管理、SLA 分级保障</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="background:#ECFDF5;border-radius:12px;padding:1.5rem;border:1px solid #A7F3D0;">
        <div style="font-size:1.2rem;font-weight:700;color:#047857;margin-bottom:0.5rem;">🔒 信息安全体系</div>
        <ul style="color:#1E293B;">
            <li>物理安全：机房环境监控、冗余供电、门禁管控</li>
            <li>网络安全：分区隔离、边界防护、流量监测</li>
            <li>应用安全：代码审计、渗透测试、漏洞管理</li>
            <li>数据安全：分级分类、加密脱敏、备份恢复、操作审计</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
