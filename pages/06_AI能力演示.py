import streamlit as st
import requests
import json

st.set_page_config(page_title="AI能力演示", page_icon="🤖", layout="wide")

st.markdown("<div style='font-size:2rem;font-weight:700;color:#1E293B;'>🤖 AI 能力演示</div>", unsafe_allow_html=True)
st.markdown("<div style='color:#64748B;margin-bottom:2rem;'>医共体 AI 中台核心能力场景化演示 — 智能辅助诊疗与运营管理</div>", unsafe_allow_html=True)

# 尝试检测本地 Ollama
ollama_available = False
try:
    r = requests.get("http://localhost:11434/api/tags", timeout=2)
    if r.status_code == 200:
        ollama_available = True
        models = r.json().get("models", [])
except Exception:
    pass

st.markdown("### 🎯 演示场景选择")
scenario = st.selectbox("选择一个 AI 场景进行体验", [
    "🏥 智能急症分诊助手",
    "🩻 影像 AI 辅助诊断",
    "💊 合理用药审核",
    "📋 病历内涵质控",
    "📊 运营数据分析助手",
])

# 场景 1：智能急症分诊助手
if "智能急症分诊" in scenario:
    st.markdown("#### 场景说明")
    st.info("模拟患者到达急诊后的智能分诊流程。AI 根据患者主诉、生命体征，自动推荐分诊级别和就诊科室。")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**患者信息录入**")
        chief_complaint = st.text_area("主诉", "胸痛 30 分钟，伴大汗、呼吸困难")
        age = st.number_input("年龄", 18, 120, 62)
        gender = st.selectbox("性别", ["男", "女"])
        bp = st.text_input("血压", "165/95 mmHg")
        hr = st.number_input("心率", 30, 200, 105)
        spo2 = st.number_input("血氧饱和度", 50, 100, 92)
        run = st.button("🚀 启动 AI 分诊分析", type="primary")

    with col2:
        st.markdown("**AI 分诊结果**")
        if run:
            with st.spinner("AI 分析中..."):
                # 如果 Ollama 可用，尝试调用；否则使用预设回复
                if ollama_available:
                    try:
                        prompt = f"""你是一名急诊分诊 AI 助手。请根据以下患者信息进行分诊评估，输出：
1. 推荐分诊级别（1-5级，1级最危急）
2. 推荐就诊科室
3. 主要风险提示
4. 建议优先检查项目

患者信息：
- 主诉：{chief_complaint}
- 年龄：{age}岁，性别：{gender}
- 血压：{bp}，心率：{hr}次/分，血氧：{spo2}%

请用中文简洁输出。"""
                        resp = requests.post("http://localhost:11434/api/generate", json={
                            "model": models[0]["name"] if models else "llama3",
                            "prompt": prompt,
                            "stream": False,
                        }, timeout=30)
                        if resp.status_code == 200:
                            result = resp.json().get("response", "")
                            st.success(result)
                        else:
                            raise Exception("Ollama 返回错误")
                    except Exception as e:
                        st.warning(f"本地 AI 调用失败（{e}），使用预设演示结果：")
                        st.error("**🔴 分诊级别：I 级（危急）**")
                        st.markdown("- **推荐科室**：胸痛中心 / 心内科急诊")
                        st.markdown("- **主要风险**：急性冠脉综合征（ACS）高度可疑，需排除 STEMI")
                        st.markdown("- **优先检查**：心电图（10分钟内）、心肌损伤标志物（TnI/CK-MB）、胸部 CT（排除主动脉夹层）")
                        st.markdown("- **处置建议**：立即建立静脉通路，吸氧，心电监护，通知心内科值班医师")
                else:
                    st.error("**🔴 分诊级别：I 级（危急）**")
                    st.markdown("- **推荐科室**：胸痛中心 / 心内科急诊")
                    st.markdown("- **主要风险**：急性冠脉综合征（ACS）高度可疑，需排除 STEMI")
                    st.markdown("- **优先检查**：心电图（10分钟内）、心肌损伤标志物（TnI/CK-MB）、胸部 CT（排除主动脉夹层）")
                    st.markdown("- **处置建议**：立即建立静脉通路，吸氧，心电监护，通知心内科值班医师")
        else:
            st.markdown("<div style='color:#94A3B8;padding:2rem;text-align:center;'>👈 请在左侧录入患者信息后点击分析</div>", unsafe_allow_html=True)

# 场景 2：影像 AI 辅助诊断
elif "影像 AI" in scenario:
    st.markdown("#### 场景说明")
    st.info("模拟胸部 CT 影像的 AI 辅助诊断流程。AI 自动检测肺结节、骨折等异常征象。")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**检查信息**")
        modality = st.selectbox("检查类型", ["胸部 CT", "头部 CT", "DR 胸片", "腹部 CT"])
        indication = st.text_area("检查指征", "体检发现肺结节随访")
        st.file_uploader("上传 DICOM 影像（演示模式，无需上传）", type=["dcm"], disabled=True)
        run = st.button("🚀 启动 AI 影像分析", type="primary")

    with col2:
        st.markdown("**AI 诊断报告**")
        if run:
            with st.spinner("AI 分析中..."):
                st.success("**AI 影像分析完成**")
                st.markdown("""
**检测到的征象：**
- 🟡 **肺结节**：右肺上叶尖段见一实性结节，大小约 6mm×5mm，边界清晰
- 🟢 **钙化灶**：左肺下叶陈旧性钙化灶，考虑良性
- 🟢 **气胸/积液**：未见明显气胸或胸腔积液

**AI 风险评估：**
- Lung-RADS 分级：**2 级（良性发现）**
- 恶性概率：**<1%**
- 建议随访：12 个月后低剂量 CT 复查

**相似病例推荐：**
- 病例 #2847：6mm 实性结节，随访 2 年稳定
- 病例 #3156：7mm 磨玻璃结节，术后证实为原位腺癌
                """)
        else:
            st.markdown("<div style='color:#94A3B8;padding:2rem;text-align:center;'>👈 选择检查类型后点击分析</div>", unsafe_allow_html=True)

# 场景 3：合理用药审核
elif "合理用药" in scenario:
    st.markdown("#### 场景说明")
    st.info("模拟医生开具处方时的实时 AI 用药审核，自动提示药物相互作用、过敏风险、剂量异常等问题。")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**处方信息**")
        diagnosis = st.text_input("诊断", "2型糖尿病伴高血压")
        age = st.number_input("患者年龄", 1, 120, 68)
        allergy = st.text_input("过敏史", "磺胺类过敏")
        drugs = st.text_area("药品清单", "二甲双胍 0.5g tid\n氨氯地平 5mg qd\n阿司匹林 100mg qd")
        run = st.button("🚀 启动 AI 用药审核", type="primary")

    with col2:
        st.markdown("**AI 审核结果**")
        if run:
            with st.spinner("AI 审核中..."):
                st.success("**AI 用药审核完成 — 发现 1 个问题需关注**")
                st.markdown("""
**✅ 通过项：**
- 二甲双胍：剂量合理，与诊断匹配
- 氨氯地平：剂量合理，适用于高血压合并糖尿病

**⚠️ 警示项：**
- **阿司匹林**：患者 68 岁，长期服用需评估胃肠道出血风险
  - 建议：联合 PPI（如奥美拉唑）保护胃黏膜，或改用氯吡格雷

**📋 优化建议：**
- 建议加用他汀类药物（如阿托伐他汀 20mg qd）进行心血管一级预防
- 监测：肝功能、肾功能、糖化血红蛋白每 3 个月复查
                """)
        else:
            st.markdown("<div style='color:#94A3B8;padding:2rem;text-align:center;'>👈 录入处方信息后点击审核</div>", unsafe_allow_html=True)

# 场景 4：病历内涵质控
elif "病历内涵质控" in scenario:
    st.markdown("#### 场景说明")
    st.info("模拟 AI 对病历内容进行内涵质控，检查诊断与检验结果一致性、病程记录及时性、手术记录完整性等。")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**病历摘要**")
        diagnosis = st.text_input("入院诊断", "急性阑尾炎")
        symptom = st.text_area("主诉/现病史", "腹痛 1 天，转移性右下腹痛 6 小时。伴发热，T 38.5℃。")
        exam = st.text_area("体格检查", "右下腹麦氏点压痛、反跳痛阳性。血常规：WBC 13.2×10⁹/L。")
        record = st.text_area("病程记录", "患者今日腹痛加重，复查血常规 WBC 15.1×10⁹/L，考虑化脓性阑尾炎，拟行急诊手术。")
        run = st.button("🚀 启动 AI 内涵质控", type="primary")

    with col2:
        st.markdown("**AI 质控结果**")
        if run:
            with st.spinner("AI 质控中..."):
                st.success("**AI 内涵质控完成 — 得分 88/100**")
                st.markdown("""
**❌ 缺陷项：**
- 缺少 **鉴别诊断**：未排除右侧输尿管结石、妇科急腹症等
- 病程记录中 **手术知情同意** 描述不完整，缺替代方案说明
- 术后首次病程记录未在 **术后 6 小时内** 完成

**⚠️ 提示项：**
- 血象进行性升高（13.2→15.1），建议补充 **PCT/CRP** 评估感染严重程度
- 患者发热，建议补充 ** Covid-19/流感筛查** 记录

**✅ 亮点：**
- 主诉描述规范，时间线清晰
- 手术指征描述充分
                """)
        else:
            st.markdown("<div style='color:#94A3B8;padding:2rem;text-align:center;'>👈 录入病历信息后点击质控</div>", unsafe_allow_html=True)

# 场景 5：运营数据分析助手
elif "运营数据分析" in scenario:
    st.markdown("#### 场景说明")
    st.info("模拟管理者通过自然语言向 AI 助手提问，获取医共体运营数据洞察。")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**提问示例**")
        question = st.selectbox("选择一个问题", [
            "本月各卫生院门诊量环比变化如何？",
            "哪个科室的药品耗材占比最高？",
            "DRG 付费下亏损病种有哪些？",
            "基层医生绩效排名 TOP10 是谁？",
        ])
        custom_q = st.text_input("或输入自定义问题", "")
        if custom_q:
            question = custom_q
        run = st.button("🚀 询问 AI 助手", type="primary")

    with col2:
        st.markdown("**AI 分析回复**")
        if run:
            with st.spinner("AI 分析中..."):
                if "门诊量" in question:
                    st.success("**AI 运营分析回复**")
                    st.markdown("""
**本月各卫生院门诊量环比变化：**

| 卫生院 | 上月门诊量 | 本月门诊量 | 环比变化 |
|---|---|---|---|
| 甘旗卡镇卫生院 | 3,240 | 3,580 | **+10.5%** 🟢 |
| 金宝屯镇卫生院 | 2,180 | 2,050 | **-6.0%** 🔴 |
| 吉尔嘎朗镇卫生院 | 1,560 | 1,720 | **+10.3%** 🟢 |
| 常胜镇卫生院 | 1,320 | 1,450 | **+9.8%** 🟢 |
| **全县合计** | **28,400** | **30,100** | **+6.0%** 🟢 |

**洞察：**
- 整体门诊量增长 6%，得益于近期家庭医生签约随访推动
- 金宝屯镇下降需关注，建议调研是否有人员变动或设备故障
                    """)
                elif "药品耗材" in question:
                    st.success("**AI 运营分析回复**")
                    st.markdown("""
**药品耗材占比排名（本月）：**

| 科室 | 药品耗材占比 | 环比 |
|---|---|---|
| 心血管内科 | **52.3%** | +2.1% 🔴 |
| 肿瘤科 | **48.7%** | -1.5% 🟢 |
| 骨科 | **45.2%** | +3.2% 🔴 |
| 神经内科 | **41.8%** | -0.8% 🟢 |

**建议：**
- 心血管内科占比超标（目标 <45%），建议重点审查高值耗材使用合理性
- 骨科增长较快，关注植入类耗材集采执行情况
                    """)
                elif "DRG" in question:
                    st.success("**AI 运营分析回复**")
                    st.markdown("""
**DRG 付费下亏损病种 TOP5：**

| 病种 | 例均费用 | DRG 支付标准 | 例均亏损 | 病例数 |
|---|---|---|---|---|
| GB23 复杂腹部手术 | ¥32,400 | ¥28,500 | **-¥3,900** | 12 |
| LA19 肺癌化疗 | ¥18,600 | ¥16,200 | **-¥2,400** | 28 |
| FC35 脑出血手术 | ¥45,200 | ¥42,000 | **-¥3,200** | 8 |

**建议：**
- 对亏损病种开展临床路径优化，缩短平均住院日
- 与医保局沟通，提交成本数据申请调整支付标准
                    """)
                else:
                    st.success("**AI 运营分析回复**")
                    st.markdown("""
**基层医生绩效排名 TOP10（本月）：**

| 排名 | 姓名 | 机构 | 绩效得分 | 关键指标 |
|---|---|---|---|---|
| 1 | 张伟 | 甘旗卡镇卫生院 | 96.5 | 门诊量 420 / 患者满意度 98% |
| 2 | 李芳 | 常胜镇卫生院 | 94.2 | 慢病随访完成率 100% |
| 3 | 王强 | 金宝屯镇卫生院 | 93.8 | 签约居民管理 680 人 |
| 4 | 刘洋 | 吉尔嘎朗镇卫生院 | 92.5 | 远程会诊参与 15 例 |
| 5 | 陈静 | 阿古拉镇卫生院 | 91.6 | 健康教育讲座 4 场 |

**分析：**
- TOP10 医生平均绩效得分 91.2，较上月提升 3.5 分
- 慢病管理和随访完成率是拉开差距的关键指标
                    """)
        else:
            st.markdown("<div style='color:#94A3B8;padding:2rem;text-align:center;'>👈 选择或输入问题后点击询问</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### AI 中台技术架构")
st.markdown("""
```
┌──────────────────────────────────────────┐
│           应用场景层                       │
│  智能分诊 │ 影像 AI │ 用药审核 │ 病历质控 │
├──────────────────────────────────────────┤
│           模型能力层                       │
│  医学 NLP │ CV 影像 │ 知识图谱 │ 推理引擎 │
├──────────────────────────────────────────┤
│           模型管理层                       │
│  模型训练 │ 版本管理 │ A/B 测试 │ 效果评估 │
├──────────────────────────────────────────┤
│           计算资源层                       │
│  本地 GPU 集群 │ 华为云 AI │ 边缘推理节点 │
└──────────────────────────────────────────┘
```
""")

if ollama_available:
    st.success(f"✅ 检测到本地 Ollama 服务，可用模型：{', '.join([m['name'] for m in models[:3]])}")
else:
    st.info("ℹ️ 未检测到本地 Ollama 服务，演示模式使用预设回复。如需接入真实 AI，请启动 Ollama 并加载医学模型。")
