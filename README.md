# 王亦琳个人网站

静态网站，通过 GitHub Pages 从 `main` 分支根目录发布，无需构建。

- `/`：默认跳转至中文主页 `/CN/`；旧的 `/#/...` 作品集深链接跳转至 `/work/`
- `/work/`：中文交互作品集，包含三个 TCL 专题的完整案例、场景演示、项目资料检索与面试导览
- `/English/`：与 `/CN/` 结构和内容对应的英文简历，可进入中文交互案例
- `/CN/`：中文简历，支持打印 / 保存 PDF
- `/portfolio.html`：原有 40 页完整作品集
- `assets/personal.css`：两个页面共用样式；使用 Cinna、Froth、Creme、Latte、Chai 配色
- `assets/personal.js`：移动导航与打印交互
- `assets/pages/`、`assets/thumbs/`：原始作品集页面与缩略图

交互作品集基于 `Yilin_Portfolio.html` 整合，项目示意图内嵌于首页；资料导览目前只在浏览器本地检索。项目图片直接引用现有作品集文件，保持原始比例；中英文页面均提供语言切换入口。

修改 `/CN/` 的内容后，运行 `python3 scripts/sync_english.py`，根据同一页面结构更新英文译文。脚本会提示尚未翻译的新中文内容。
