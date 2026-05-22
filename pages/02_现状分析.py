import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="现状分析", page_icon="📊", layout="wide")

st.markdown("<div style='font-size:2rem;font-weight:700;color:#1E293B;'>📊 现状分析</div>", unsafe_allow_html=True)
st.markdown("<div style='color:#64748B;margin-bottom:2rem;'>科左后旗医共体业务现状与信息化现状深度分析</div>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🏥 业务现状", "💻 信息化现状"])

with tab1:
    st.markdown("### 一、医疗资源分布")

    col1, col2 = st.columns(2)
    with col1:
        df_org = pd.DataFrame({
            "机构类型": ["县医院", "乡镇卫生院", "村卫生室"],
            "数量": [1, 15, 17],
            "床位数": [350, 280, 0],
            "卫技人员": [420, 180, 45],
        })
        fig = px.bar(df_org, x="机构类型", y=["床位数", "卫技人员"], barmode="group",
                     title="各层级医疗机构资源分布", color_discrete_sequence=["#2563EB", "#10B981"])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = px.pie(df_org, values="数量", names="机构类型", hole=0.4,
                      title="医疗机构数量占比", color_discrete_sequence=["#2563EB", "#10B981", "#F59E0B"])
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### 二、就诊流向分析")
    df_flow = pd.DataFrame({
        "层级": ["县医院", "乡镇卫生院", "村卫生室", "县外就医"],
        "就诊人次占比(%)": [45, 25, 15, 15],
    })
    fig3 = px.funnel(df_flow, x="就诊人次占比(%)", y="层级", color="层级",
                     color_discrete_sequence=["#EF4444", "#F59E0B", "#10B981", "#64748B"])
    st.plotly_chart(fig3, use_container_width=True)
    st.info("💡 **关键发现**：县域内就诊率仅 85%，15% 患者外流；乡镇卫生院就诊占比偏低，基层首诊能力不足。")

    st.markdown("### 三、核心痛点")
    pain_data = pd.DataFrame({
        "痛点": ["重复检查", "重复用药", "患者外流", "基层能力不足", "运营成本高", "数据孤岛"],
        "影响程度": [85, 72, 68, 90, 78, 88],
        "紧迫性": [80, 70, 65, 95, 75, 90],
    })
    fig4 = px.scatter(pain_data, x="影响程度", y="紧迫性", text="痛点", size="影响程度",
                      color="紧迫性", color_continuous_scale="Blues",
                      title="痛点矩阵分析（影响程度 vs 紧迫性）")
    fig4.update_traces(textposition="top center")
    st.plotly_chart(fig4, use_container_width=True)

with tab2:
    # ===== 需求2：层级筛选器（放在tab2最顶部）=====
    st.markdown("### 一、机构信息化水平排名")

    filter_col, _ = st.columns([1, 3])
    with filter_col:
        selected_level = st.selectbox(
            "筛选机构层级",
            ["全部", "县医院", "乡镇卫生院", "村卫生室"],
            help="选择要查看的机构层级，表格和图表将联动更新"
        )

    # ===== 需求1：33家机构排名表 =====
    # 模拟33家机构数据
    institutions_data = []

    # 县医院（1家）
    institutions_data.append({"机构名称": "科左后旗人民医院", "层级": "县医院", "信息化评分": 78})

    # 乡镇卫生院（15家）
    township_names = [
        "甘旗卡镇卫生院", "金宝屯镇卫生院", "吉尔嘎朗镇卫生院", "常胜镇卫生院",
        "阿古拉镇卫生院", "努古斯台镇卫生院", "海鲁吐镇卫生院", "阿都沁苏木卫生院",
        "茂道吐苏木卫生院", "巴胡塔苏木卫生院", "散都苏木卫生院", "查金台牧场卫生院",
        "胜利农场卫生院", "孟根达坝牧场卫生院", "乌兰敖道渔场卫生院"
    ]
    township_scores = [62, 58, 55, 60, 52, 48, 50, 45, 47, 53, 46, 44, 49, 43, 41]
    for name, score in zip(township_names, township_scores):
        institutions_data.append({"机构名称": name, "层级": "乡镇卫生院", "信息化评分": score})

    # 村卫生室（17家）
    village_names = [
        "甘旗卡村卫生室", "金宝屯村卫生室", "吉尔嘎朗村卫生室", "常胜村卫生室",
        "阿古拉村卫生室", "努古斯台村卫生室", "海鲁吐村卫生室", "阿都沁村卫生室",
        "茂道吐村卫生室", "巴胡塔村卫生室", "散都村卫生室", "查金台村卫生室",
        "胜利村卫生室", "孟根达坝村卫生室", "乌兰敖道村卫生室", "伊和淖尔村卫生室", "白兴吐村卫生室"
    ]
    village_scores = [35, 32, 38, 30, 28, 25, 33, 27, 29, 31, 26, 24, 30, 23, 22, 28, 25]
    for name, score in zip(village_names, village_scores):
        institutions_data.append({"机构名称": name, "层级": "村卫生室", "信息化评分": score})

    df_inst = pd.DataFrame(institutions_data)

    # 计算排名（按层级分组排名）
    df_inst["层级排名"] = df_inst.groupby("层级")["信息化评分"].rank(ascending=False, method="min").astype(int)
    df_inst["总排名"] = df_inst["信息化评分"].rank(ascending=False, method="min").astype(int)

    # 根据筛选条件过滤
    if selected_level != "全部":
        df_filtered = df_inst[df_inst["层级"] == selected_level].copy()
    else:
        df_filtered = df_inst.copy()

    # 显示表格
    st.dataframe(
        df_filtered.sort_values("信息化评分", ascending=False),
        use_container_width=True,
        hide_index=True,
        column_config={
            "机构名称": st.column_config.TextColumn("机构名称", width="large"),
            "层级": st.column_config.TextColumn("层级", width="medium"),
            "信息化评分": st.column_config.ProgressColumn(
                "信息化评分",
                help="满分100分，基于系统覆盖、数据质量、互联互通等维度综合评估",
                format="%d",
                min_value=0,
                max_value=100,
            ),
            "层级排名": st.column_config.NumberColumn("层级内排名", width="small"),
            "总排名": st.column_config.NumberColumn("总排名", width="small"),
        }
    )

    # 统计信息
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    with stat_col1:
        st.metric(label="机构数量", value=len(df_filtered))
    with stat_col2:
        st.metric(label="平均评分", value=f"{df_filtered['信息化评分'].mean():.1f}")
    with stat_col3:
        st.metric(label="最高评分", value=df_filtered["信息化评分"].max())
    with stat_col4:
        st.metric(label="最低评分", value=df_filtered["信息化评分"].min())

    st.markdown("---")

    # ===== 需求3：雷达图 + 差距分析 =====
    st.markdown("### 二、数据互联互通评估")

    connectivity = {
        "评估维度": ["数据标准化", "系统接口", "共享交换", "业务协同", "统一认证", "数据质量"],
        "当前得分": [45, 50, 35, 40, 30, 40],
        "目标得分": [90, 90, 85, 85, 80, 85],
    }
    df_conn = pd.DataFrame(connectivity)
    df_conn["差距"] = df_conn["目标得分"] - df_conn["当前得分"]

    col_left, col_right = st.columns(2)

    with col_left:
        # 雷达图（保留原有对比）
        fig6 = go.Figure()
        fig6.add_trace(go.Scatterpolar(
            r=df_conn["当前得分"].tolist() + [df_conn["当前得分"].iloc[0]],
            theta=df_conn["评估维度"].tolist() + [df_conn["评估维度"].iloc[0]],
            fill="toself", name="当前水平", line_color="#EF4444"
        ))
        fig6.add_trace(go.Scatterpolar(
            r=df_conn["目标得分"].tolist() + [df_conn["目标得分"].iloc[0]],
            theta=df_conn["评估维度"].tolist() + [df_conn["评估维度"].iloc[0]],
            fill="toself", name="建设目标", line_color="#10B981"
        ))
        fig6.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            title="数据互联互通能力雷达图",
            height=350,
        )
        st.plotly_chart(fig6, use_container_width=True)

    with col_right:
        # 新增：差距分析柱状图
        fig_gap = go.Figure()
        fig_gap.add_trace(go.Bar(
            x=df_conn["评估维度"],
            y=df_conn["差距"],
            marker_color=["#EF4444" if g > 50 else "#F59E0B" if g > 30 else "#10B981" for g in df_conn["差距"]],
            text=df_conn["差距"],
            textposition="outside",
        ))
        fig_gap.update_layout(
            title="各维度提升空间（目标 - 当前）",
            yaxis_title="差距分值",
            height=350,
            showlegend=False,
        )
        st.plotly_chart(fig_gap, use_container_width=True)

    # 差距分析表格
    st.markdown("#### 📋 各维度详细差距")
    gap_df = df_conn[["评估维度", "当前得分", "目标得分", "差距"]].copy()
    gap_df["提升幅度"] = (gap_df["差距"] / gap_df["当前得分"] * 100).round(1).astype(str) + "%"

    # 根据筛选的层级动态调整当前得分（模拟不同层级的差异）
    if selected_level == "县医院":
        gap_df["当前得分"] = [65, 70, 55, 60, 50, 60]
    elif selected_level == "乡镇卫生院":
        gap_df["当前得分"] = [45, 48, 30, 38, 25, 35]
    elif selected_level == "村卫生室":
        gap_df["当前得分"] = [25, 20, 10, 15, 8, 18]

    gap_df["差距"] = gap_df["目标得分"] - gap_df["当前得分"]
    gap_df["提升幅度"] = (gap_df["差距"] / gap_df["当前得分"] * 100).round(1).astype(str) + "%"

    st.dataframe(
        gap_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "评估维度": st.column_config.TextColumn("评估维度", width="medium"),
            "当前得分": st.column_config.NumberColumn("当前得分", width="small"),
            "目标得分": st.column_config.NumberColumn("目标得分", width="small"),
            "差距": st.column_config.NumberColumn("差距", width="small"),
            "提升幅度": st.column_config.TextColumn("提升幅度", width="small"),
        }
    )

    # 系统覆盖情况（根据筛选层级调整）
    st.markdown("---")
    st.markdown("### 三、系统覆盖情况")

    systems = ["HIS", "LIS", "PACS", "EMR", "HRP", "集成平台", "数据中心"]

    if selected_level == "全部":
        county = [100, 100, 100, 100, 60, 40, 20]
        township = [80, 60, 40, 50, 10, 10, 5]
        village = [30, 10, 0, 10, 0, 0, 0]

        df_sys = pd.DataFrame({
            "系统": systems,
            "县医院(%)": county,
            "乡镇卫生院(%)": township,
            "村卫生室(%)": village,
        })

        fig5 = go.Figure()
        fig5.add_trace(go.Bar(name="县医院", x=systems, y=county, marker_color="#2563EB"))
        fig5.add_trace(go.Bar(name="乡镇卫生院", x=systems, y=township, marker_color="#10B981"))
        fig5.add_trace(go.Bar(name="村卫生室", x=systems, y=village, marker_color="#F59E0B"))
        fig5.update_layout(barmode="group", title="各层级信息系统覆盖率对比", yaxis_title="覆盖率(%)")
    elif selected_level == "县医院":
        df_sys = pd.DataFrame({"系统": systems, "覆盖率(%)": [100, 100, 100, 100, 60, 40, 20]})
        fig5 = px.bar(df_sys, x="系统", y="覆盖率(%)", title="县医院信息系统覆盖率",
                      color="覆盖率(%)", color_continuous_scale="Blues")
    elif selected_level == "乡镇卫生院":
        df_sys = pd.DataFrame({"系统": systems, "覆盖率(%)": [80, 60, 40, 50, 10, 10, 5]})
        fig5 = px.bar(df_sys, x="系统", y="覆盖率(%)", title="乡镇卫生院信息系统覆盖率",
                      color="覆盖率(%)", color_continuous_scale="Greens")
    else:  # 村卫生室
        df_sys = pd.DataFrame({"系统": systems, "覆盖率(%)": [30, 10, 0, 10, 0, 0, 0]})
        fig5 = px.bar(df_sys, x="系统", y="覆盖率(%)", title="村卫生室信息系统覆盖率",
                      color="覆盖率(%)", color_continuous_scale="Oranges")

    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("### 四、信息化投入与缺口")
    df_invest = pd.DataFrame({
        "年份": ["2022", "2023", "2024", "2025(规划)"],
        "实际投入(万元)": [180, 220, 260, 1200],
        "累计系统数": [8, 12, 16, 35],
    })
    fig7 = px.bar(df_invest, x="年份", y="实际投入(万元)", text="实际投入(万元)",
                  title="年度信息化投入对比", color="年份",
                  color_discrete_sequence=["#94A3B8", "#94A3B8", "#94A3B8", "#2563EB"])
    st.plotly_chart(fig7, use_container_width=True)
    st.success("✅ 本轮建设将一次性投入 1200 万元，实现跨越式升级，补齐历年信息化短板。")
