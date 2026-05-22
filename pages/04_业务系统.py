import streamlit as st

st.set_page_config(page_title="业务系统", page_icon="💻", layout="wide")

st.markdown("<div style='font-size:2rem;font-weight:700;color:#1E293B;'>💻 业务系统</div>", unsafe_allow_html=True)
st.markdown("<div style='color:#64748B;margin-bottom:2rem;'>HIS / LIS / PACS / EMR 四大核心业务系统升级方案</div>", unsafe_allow_html=True)

tabs = st.tabs(["🏥 HIS", "🧪 LIS", "🩻 PACS/RIS", "📋 EMR"])

with tabs[0]:
    st.markdown("### 医院信息系统 (HIS)")
    st.markdown("**定位**：覆盖门急诊、住院、药品、收费全流程的核心业务系统")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("#### 升级内容")
        modules = [
            ("📝", "门诊挂号收费", "支持多渠道预约（微信/电话/现场），智能分诊，统一号源管理，移动支付全覆盖"),
            ("🛏️", "住院管理", "电子入院证、床位统筹调配、住院费用一日清单、出院结算一站式"),
            ("💊", "药品管理", "智能药库、处方前置审核、抗菌药物分级管理、药品追溯码全程跟踪"),
            ("💳", "医保结算", "国家医保接口标准适配、DRG/DIP 预分组、异地结算直连、医保智能监控"),
        ]
        for icon, title, desc in modules:
            st.markdown(f"**{icon} {title}**：{desc}")
    with col2:
        st.markdown("#### 预期效果")
        st.metric(label="挂号候诊时间", value="缩短 50%", delta="-15分钟")
        st.metric(label="收费窗口压力", value="降低 60%", delta="移动支付占比 80%")
        st.metric(label="处方合格率", value="≥98%", delta="前置审核拦截")

with tabs[1]:
    st.markdown("### 检验信息系统 (LIS)")
    st.markdown("**定位**：实现检验全流程数字化、智能化、标准化管理")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("#### 升级内容")
        modules = [
            ("🧫", "标本管理", "条码闭环追踪、TAT 时效监控、不合格标本自动退回、生物安全预警"),
            ("📑", "检验申请", "医生电子申请、智能项目推荐、重复检验自动提示、危急值自动预警"),
            ("✅", "结果审核", "自动审核规则引擎、历史结果对比、 delta 检查、审核日志追溯"),
            ("📤", "报告发布", "多渠道报告推送（短信/微信/APP）、报告自助打印、区域检验结果互认"),
        ]
        for icon, title, desc in modules:
            st.markdown(f"**{icon} {title}**：{desc}")
    with col2:
        st.markdown("#### 预期效果")
        st.metric(label="标本周转时间", value="缩短 35%", delta="TAT 平均 2小时")
        st.metric(label="自动审核率", value="≥75%", delta="释放检验师精力")
        st.metric(label="危急值响应", value="<10分钟", delta="自动推送闭环")

with tabs[2]:
    st.markdown("### 影像归档与通信系统 (PACS/RIS)")
    st.markdown("**定位**：构建区域影像云平台，实现影像数据集中存储与共享调阅")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("#### 升级内容")
        modules = [
            ("☁️", "影像云存储", "县域影像数据集中上云，支持 10年+ 在线调阅，原始 DICOM 无损压缩存储"),
            ("🖊️", "诊断报告", "结构化报告模板、语音录入、AI 辅助征象识别、报告质量评分"),
            ("🌐", "远程阅片", "基层拍片/上级诊断模式，支持移动端远程审签，诊断时效提升 3 倍"),
            ("🤖", "AI 辅助诊断", "肺结节筛查、骨折检测、冠脉分析、病灶自动测量与随访对比"),
        ]
        for icon, title, desc in modules:
            st.markdown(f"**{icon} {title}**：{desc}")
    with col2:
        st.markdown("#### 预期效果")
        st.metric(label="影像共享率", value="100%", delta="县域内互认")
        st.metric(label="胶片成本", value="降低 80%", delta="云胶片替代")
        st.metric(label="AI 检出率", value="≥95%", delta="漏诊率下降")

with tabs[3]:
    st.markdown("### 电子病历系统 (EMR)")
    st.markdown("**定位**：实现病历全生命周期电子化、结构化、智能化管理")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("#### 升级内容")
        modules = [
            ("✍️", "病历书写", "结构化模板、智能语音录入、医学术语联想、病历相似病历推荐"),
            ("🔍", "病历质控", "环节质控+终末质控双保险、AI 内涵质控、缺陷自动提醒、质控评分排名"),
            ("🛤️", "临床路径", "病种路径库、路径执行监控、变异分析、路径入组率自动统计"),
            ("📊", "数据上报", "自动抽取填报国家卫统/单病种/重点专科等报表，数据直报零手工"),
        ]
        for icon, title, desc in modules:
            st.markdown(f"**{icon} {title}**：{desc}")
    with col2:
        st.markdown("#### 预期效果")
        st.metric(label="病历甲级率", value="≥98%", delta="AI 质控拦截")
        st.metric(label="书写效率", value="提升 40%", delta="语音+模板")
        st.metric(label="互联互通评级", value="四级甲等", delta="标准化改造")

st.markdown("---")
st.markdown("### 系统互联互通关系")
st.markdown("""
```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│   HIS   │◄──►│   LIS   │◄──►│ PACS/RIS│◄──►│   EMR   │
└────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘
     │              │              │              │
     └──────────────┴──────────────┴──────────────┘
                    │
              ┌─────┴─────┐
              │  集成平台  │
              │  (ESB)   │
              └─────┬─────┘
                    │
         ┌─────────┼─────────┐
         ▼         ▼         ▼
      ┌──────┐  ┌──────┐  ┌──────┐
      │数据中台│  │  AI  │  │统一认证│
      └──────┘  └──────┘  └──────┘
```
""")
