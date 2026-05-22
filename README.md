# 企业 AI 方案原型 — Streamlit 标准执行流程

> 以《科左后旗县域医共体数智化能力提升建设方案》为例，演示如何用 Claude Code + Streamlit 替代传统 PPT 方案。

---

## 一、环境准备（一次性）

### 1.1 安装依赖
```bash
pip install streamlit plotly pandas pyyaml
```

### 1.2 项目目录结构
```
ai-prototype/
├── app.py                 # 主入口
├── config.yaml            # 方案配置
├── .streamlit/config.toml # 主题配置
├── pages/                 # 各演示页面
├── data/                  # 演示数据
└── assets/                # 图片资源
```

---

## 二、标准执行流程（Step by Step）

### Step 1：启动应用
```bash
cd ai-prototype
streamlit run app.py
```
浏览器自动打开 `http://localhost:8501`

### Step 2：浏览主页
- 查看方案标题、核心指标卡片（4 个 KPI）
- 阅读建设目标（5 大目标）
- 查看建设内容总览表

### Step 3：逐页浏览（左侧导航）
点击左侧导航菜单，按顺序浏览：

| 顺序 | 页面 | 重点体验 |
|---|---|---|
| 1 | 方案概览 | 项目背景、建设目标、核心指标 |
| 2 | 现状分析 | 图表交互：切换"业务现状/信息化现状"标签 |
| 3 | 总体架构 | 五层架构展开、两大保障体系 |
| 4 | 业务系统 | 切换 HIS/LIS/PACS/EMR 四大标签 |
| 5 | HRP 系统 | 切换人力/财务/物资/资产标签 |
| 6 | AI 能力演示 | **重点**：选择场景、填写表单、点击分析 |
| 7 | 实施路线 | 查看甘特图、里程碑卡片 |
| 8 | 投资效益 | **重点**：拖动 ROI 计算器滑块 |

### Step 4：现场演示技巧
- **全屏模式**：按 `F11` 浏览器全屏
- **侧边栏收起**：点击左上角 `>` 收起侧边栏，扩大内容区
- **交互演示**：在 AI 能力页填写真实表单，展示 AI 输出
- **ROI 计算器**：现场调整参数，实时计算投资回报

### Step 5：部署分享
```bash
# 方式一：本地打包
zip -r ai-prototype.zip ai-prototype/

# 方式二：部署到 Streamlit Cloud（需注册）
# 1. 推送代码到 GitHub
# 2. 在 share.streamlit.io 导入仓库
# 3. 获得在线链接，客户可直接访问
```

---

## 三、定制修改指南

### 修改方案标题和公司
编辑 `config.yaml`：
```yaml
project:
  name: "你的方案名称"
  company: "你的公司名称"
```

### 修改页面内容
编辑 `pages/XX_页面名.py` 中的文本和图表数据。

### 替换架构图
将架构图图片放入 `assets/`，在页面中用 `st.image()` 引用。

### 接入真实 AI
在 `06_AI能力演示.py` 中配置 API Key 或本地 Ollama 地址。

---

## 四、常见问题

**Q：页面加载慢？**
A：Plotly 图表较多，首次加载约 3-5 秒。可压缩图表数据或改用 st.table。

**Q：中文显示乱码？**
A：确保 `config.toml` 中 `font = "sans serif"`，且系统安装了中文字体。

**Q：如何增加新页面？**
A：在 `pages/` 下新建 `XX_页面名.py`，Streamlit 会自动识别并按数字排序。
