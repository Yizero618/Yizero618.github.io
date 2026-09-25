"""Build the English resume from the Chinese page's shared HTML structure."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
page = (ROOT / "CN" / "index.html").read_text(encoding="utf-8")


def swap(original: str, translation: str) -> None:
    global page
    if original not in page:
        raise ValueError(f"Source text missing: {original}")
    page = page.replace(original, translation)


swap('<html lang="zh-CN">', '<html lang="en">')
swap(
    '王亦琳的中文简历：教育背景、AI 产品实习经历、研究发表、项目作品与专业技能。',
    'Elaine Wang’s resume: education, AI product internships, research publications, selected work, and skills.',
)
swap('王亦琳 — 中文简历 | AI 产品、研究与设计', 'Elaine Wang — Resume | AI Product, Research & Design')
swap('https://yizero618.github.io/CN/">\n  <link rel="alternate"', 'https://yizero618.github.io/English/">\n  <link rel="alternate"')
swap('<meta property="og:url" content="https://yizero618.github.io/CN/">', '<meta property="og:url" content="https://yizero618.github.io/English/">')
swap('跳转到正文', 'Skip to content')
swap('<a class="brand" href="/CN/"', '<a class="brand" href="/English/"')
swap('王亦琳中文简历首页', 'Elaine Wang resume home')
swap('王亦琳 · Elaine Wang', 'Elaine Wang · 王亦琳')
swap('aria-label="主导航"', 'aria-label="Main navigation"')
swap('aria-label="切换语言"', 'aria-label="Language"')
swap('aria-label="移动端导航"', 'aria-label="Mobile navigation"')
swap('<a href="/English/" lang="en" hreflang="en">EN</a>', '<a href="/English/" lang="en" hreflang="en" aria-current="page">EN</a>')
swap('<a href="/CN/" lang="zh-CN" hreflang="zh-CN" aria-current="page">中文</a>', '<a href="/CN/" lang="zh-CN" hreflang="zh-CN">中文</a>')
swap('<summary>目录</summary>', '<summary>Menu</summary>')

swap('个人简历 / Curriculum Vitae', 'Curriculum Vitae / Personal Profile')
swap('<h1 id="resume-title">王亦琳<span class="english-name" lang="en">Elaine Wang</span></h1>', '<h1 id="resume-title">Elaine Wang<span class="english-name" lang="zh-CN">王亦琳</span></h1>')
swap('用产品思维，连接技术与真实场景。', 'Connecting technology with real contexts through product thinking.')
swap(
    '关注生成式 AI、智能终端、AI 影像与教育科技。具备产品机会研究、需求分析、原型设计、数据复盘与跨团队推进经验；以环境设计与空间研究为基础，从人、场景与行为出发定义问题。',
    'I focus on generative AI, smart devices, AI imaging, and education technology. My experience spans product opportunity research, requirements analysis, prototyping, data review, and cross-functional coordination. With a foundation in environmental design and spatial research, I define problems through people, contexts, and behavior.',
)
swap('邮箱 · 189023227@qq.com', 'Email · 189023227@qq.com')
swap('微信 · Wyilin0618', 'WeChat · Wyilin0618')
swap('浏览项目预览 ↘', 'Browse project previews ↘')
swap('查看实习经历 ↓', 'View experience ↓')
swap('打印 / 保存 PDF', 'Print / Save as PDF')
swap('王亦琳个人照片', 'Portrait of Elaine Wang')
swap('教育、技能与荣誉', 'Education, skills, and honors')

swap('从教育场景到家庭终端，选择一个方向，走进具体的产品判断与交互方案。', 'Explore product decisions and interaction designs across education and the connected home.')
swap('进入科大讯飞产品项目', 'Open the iFLYTEK product project')
swap('进入 TCL 产品项目', 'Open the TCL product project')
swap('科大讯飞产品案例首页预览', 'Preview of the iFLYTEK product case study')
swap('AI 教育 · 产品规则 · 体验研究', 'AI education · Product rules · Experience research')
swap('把 AI 的能力，放进教师的日常。', 'Bringing AI into teachers’ everyday work.')
swap('智能终端 · 场景洞察 · AI 体验', 'Smart devices · Scenario insights · AI experiences')
swap('让技术围绕真实的生活场景。', 'Designing technology around real life at home.')
swap('让长故事，<br>有一个更轻的入口。', 'Long stories,<br>made lighter.')
swap('AI 快剪<br>助眠 · K 歌', 'AI Edit<br>Sleep · Sing')
swap('探索案例', 'Explore case study')
swap('查看 TCL 产品项目详情', 'View details of the TCL product project')
swap('查看科大讯飞产品项目详情', 'View details of the iFLYTEK product project')
swap('查看项目', 'View project')
swap('产品项目', 'Product Projects')

swap('教育背景', 'Education')
swap('实习经历', 'Experience')
swap('研究成果', 'Research')
swap('研究与发表', 'Research & Publications')
swap('设计作品', 'Selected Work')
swap('香港大学', 'The University of Hong Kong')
swap('管理科学与工程 · 硕士', 'Master’s program in Management Science and Engineering')
swap('安徽大学', 'Anhui University')
swap('环境设计 · 本科', 'Bachelor’s degree in Environmental Design')
swap('专业前 10%', 'Top 10% in major')
swap('能力与工具', 'Skills & Tools')
swap('产品与研究', 'Product & Research')
swap('产品机会研究、用户研究、竞品分析、PRD、需求管理、指标与验收标准', 'Product opportunity research, user research, competitive analysis, PRDs, requirements management, metrics, and acceptance criteria')
swap('AI 与技术协作', 'AI & Technical Collaboration')
swap('提示词设计、Agent 工作流、API、FastAPI、Swagger、HTML / CSS / JavaScript', 'Prompt design, agent workflows, APIs, FastAPI, Swagger, HTML / CSS / JavaScript')
swap('数据与分析', 'Data & Analysis')
swap('数据清洗、指标设计与业务复盘', 'data cleaning, metric design, and business review')
swap('Excel、SQL / MySQL、Python、', 'Excel, SQL / MySQL, Python, ')
swap('原型与视觉表达', 'Prototyping & Visual Communication')
swap('Figma、Axure、Canva、Visio、MindManager、Photoshop、Premiere、After Effects', 'Figma, Axure, Canva, Visio, MindManager, Photoshop, Premiere, After Effects')
swap('语言及资格证书', 'Languages and certificates')
swap('计算机二级', 'National Computer Rank Examination Level 2')
swap('普通话二甲', 'Putonghua Proficiency Test, Level 2-A')
swap('获奖与荣誉', 'Awards & Honors')
swap('全国三维数字化创新设计大赛 · 国家级二等奖', 'National 3D Digital Innovation Design Competition · National Second Prize')
swap('两岸新锐设计竞赛华灿奖 · 省级二等奖', 'Huacan Award, Cross-Strait Emerging Designers Competition · Provincial Second Prize')
swap('第十六届蓝桥杯大赛 · 省级二等奖', '16th Lanqiao Cup Competition · Provincial Second Prize')
swap('Anhui University学习优秀一等奖（前 5%）及多项校级奖学金', 'Anhui University First Prize for Academic Excellence (top 5%) and multiple university scholarships')

swap('TCL 软件工程中心 · 产品规划部', 'TCL Software Engineering Center · Product Planning Department')
swap('AI 产品经理实习生', 'AI Product Manager Intern')
swap('围绕电视、手机与家庭多终端生态开展生成式 AI 与影像产品洞察，结合用户场景、设备特点与技术成熟度判断产品机会。', 'Researched generative AI and imaging opportunities across TVs, mobile devices, and the connected-home ecosystem, assessing product opportunities through user scenarios, device strengths, and technical maturity.')
swap('担任电视端 AI 快剪专题负责人，协调预研、算法、客户端、嵌入式、设计与业务团队，推进方案评审、优先级判断与体验验证。', 'Owned the TV-based AI Quick Edit topic, coordinating early research, algorithm, client, embedded, design, and business teams to advance concept review, prioritization, and experience validation.')
swap('科大讯飞', 'iFLYTEK')
swap('面向批阅机、数智作业和智学网，承接教师、学生、运营与客服需求，负责需求分析、PRD、原型、业务规则和验收标准。', 'Worked across the grading device, digital homework, and Zhixuewang products, translating needs from teachers, students, operations, and customer support into requirements, PRDs, prototypes, business rules, and acceptance criteria.')
swap('维护需求池与版本清单，结合使用数据和一线反馈定位核心链路问题，推动需求从澄清、定义到交付与复盘。', 'Maintained the requirements backlog and release scope, using usage data and frontline feedback to identify friction in core journeys and move requirements from clarification and definition through delivery and review.')
swap('招商银行武汉分行', 'China Merchants Bank, Wuhan Branch')
swap('销售运营助理', 'Sales Operations Assistant')
swap('梳理活动上线流程与检查项，监控经营表现、客户标签和重点客户异动，协同销售推进潜力客户转化。', 'Organized campaign launch workflows and checks, monitored business performance, customer segments, and changes among key customers, and coordinated with sales on prospective customer follow-up.')
swap('湖北省城建设计院', 'Hubei Urban Construction Design Institute')
swap('项目运营助理', 'Project Operations Assistant')
swap('参与智慧路灯产品设计与项目推进，使用 Figma / Axure 完成原型与交互表达；运营多平台内容矩阵，累计产出原创内容 110 篇。', 'Contributed to smart streetlight product design and project coordination, creating prototypes and interaction flows in Figma / Axure; managed content across platforms and produced 110 original pieces.')
swap('武汉市拜斯达装饰公司', 'Best Decoration, Wuhan')
swap('产品运营助理', 'Product Operations Assistant')
swap('搭建全渠道用户反馈闭环，归类咨询、投诉与转化阻塞问题，推动服务流程和响应机制优化。', 'Built an omnichannel user-feedback loop, classified inquiries, complaints, and conversion barriers, and supported improvements to service flows and response processes.')

swap('公共交通公平性 · 独立作者 · Infrastructure Reports · 2025', 'Public transit equity · Sole author · Infrastructure Reports · 2025')
swap('整合社区边界、地铁、公交与住房等空间数据，对比深圳城中村与正式居住区的公共交通可达性和设施分布公平性。', 'Combined neighborhood boundaries, metro, bus, and housing data to compare public transit accessibility and the equity of facility distribution between urban villages and formal residential communities in Shenzhen.')
swap('智慧物流 · Proc. SPIE 13792 · ITSSC 2025', 'Smart logistics · Proc. SPIE 13792 · ITSSC 2025')
swap('围绕运输效率、路径优化和库存管理，研究物联网、机器学习与实时数据分析在智慧物流中的协同应用。', 'Studied how IoT, machine learning, and real-time data analysis can work together in smart logistics across transport efficiency, route optimization, and inventory management.')
swap('阅读论文 ↗', 'Read the paper ↗')
swap('从地方文化、公共空间到城市交通公平，我以研究理解场地与人的日常，再把洞察转化为可体验的设计。', 'From local culture and public space to transit equity, I study places and everyday life, then turn those insights into tangible design experiences.')
swap('以宣纸文化与山水意象串联小镇更新、公共空间和生态旅游。', 'Xuan paper culture and landscape imagery connect town renewal, public space, and ecotourism.')
swap('以慢食理念组织乡村院落、集市与共享活动，延续地方文化活力。', 'Slow Food principles shape village courtyards, markets, and shared activities that sustain local culture.')
swap('结合工业记忆与滨江生态策略，重连城市、社区和江岸。', 'Industrial memory and riverside ecology reconnect the city, community, and waterfront.')
swap('比较深圳城中村与正式居住区的公交可达性，识别交通服务差距。', 'Compares transit access in Shenzhen’s urban villages and formal neighborhoods to identify service gaps.')
swap('查看完整作品集', 'View the full portfolio')
swap('四个项目 · 完整方案与过程', 'Four projects · Full concepts and process')
swap('产品 · 研究 · 设计', 'Product · Research · Design')
swap('返回顶部 ↑', 'Back to top ↑')

# The Chinese name remains as a bilingual identity marker. Everything else is translated.
remaining = set(re.findall(r"[\u3400-\u9fff]+", page)) - {"王亦琳", "中文"}
if remaining:
    raise ValueError(f"Untranslated Chinese text: {sorted(remaining)}")
if re.search(r"[、。；，（）]", page):
    raise ValueError("Untranslated Chinese punctuation remains")

(ROOT / "English" / "index.html").write_text(page, encoding="utf-8")
