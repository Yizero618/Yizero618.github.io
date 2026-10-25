# 王亦琳个人网站

静态网站，通过 GitHub Pages 从 `main` 分支根目录发布，无需构建。

- `/`：默认跳转至中文主页 `/CN/`；旧的 `/#/...` 作品集深链接跳转至 `/work/`
- `/CN/#product-projects`：中文简历中的产品项目入口，分为科大讯飞与 TCL 两个分支
- `/CN/#game-products`：产品项目下方的游戏产品区，三款游戏均可直接在本站试玩；英文入口位于 `/English/#game-products`
- `/games/tiny-room.html`：九关空间布置解谜《这也能住？》
- `/games/borrow-a-beam.html`：六关光线反射解谜《借我一束光》
- `/games/mellow-island.html`：含小屋场景及连续道路的《三小只的慢慢岛》
- `/iflytek/`：科大讯飞实习产品案例，来自 `iFlytek_Portfolio.html`
- `/work/`：TCL 产品分支，包含三个专题的完整案例、场景演示、项目资料检索与面试导览
- `/English/`：与 `/CN/` 结构和内容对应的英文简历，可进入中文交互案例
- `/CN/`：中文简历，支持打印 / 保存 PDF
- `/portfolio.html`：原有 40 页完整作品集
- `assets/personal.css`：两个页面共用样式；使用 Cinna、Froth、Creme、Latte、Chai 配色
- `assets/product-projects.css`：中文简历产品分支与中英文简历字级样式
- `assets/personal.js`：移动导航与打印交互
- `assets/pages/`、`assets/thumbs/`：原始作品集页面与缩略图

交互作品集基于 `Yilin_Portfolio.html` 整合，项目示意图内嵌于首页；资料导览目前只在浏览器本地检索。项目图片直接引用现有作品集文件，保持原始比例；中英文页面均提供语言切换入口。

修改 `/CN/` 的内容后，运行 `python3 scripts/sync_english.py`，根据同一页面结构更新英文译文。脚本会提示尚未翻译的新中文内容。

三款游戏的脚本、样式、插画和所需字体均内嵌在对应 HTML 中，无需服务器或第三方运行时资源。玩法与来源说明见 `games/README.md`。游戏进度保存在当前网站来源的浏览器存储中，原 Sites 网址或下载文件中的存档不会自动迁移到 GitHub Pages。
