# 游戏试玩

三款游戏均为自包含 HTML，样式、代码和运行所需素材已内嵌，无需安装依赖，也不依赖外部服务。

| 游戏 | 试玩文件 | 来源 |
| --- | --- | --- |
| 这也能住？ | [tiny-room.html](tiny-room.html) | [原 Sites 版本](https://tiny-room-nine-keys.ohmymikesmith.chatgpt.site/) |
| 借我一束光 | [borrow-a-beam.html](borrow-a-beam.html) | 本次用户提供的《借我一束光_可直接试玩(1).html》，保持原始字节 |
| 三小只的慢慢岛 | [mellow-island.html](mellow-island.html) | [原 Sites 版本](https://three-friends-mellow-island-1025.ohmymikesmith.chatgpt.site/) |

## 本地打开

下载任一 HTML 后，直接用现代浏览器打开即可；文件可以单独复制或改名。需要固定本地存档来源时，可在仓库根目录运行：

```sh
python3 -m http.server 8000
```

然后打开 `http://localhost:8000/games/tiny-room.html`、`http://localhost:8000/games/borrow-a-beam.html` 或 `http://localhost:8000/games/mellow-island.html`。

## 玩法与操作

**这也能住？** 九关小房间布置解谜。拖动家具，或先选家具再点格子摆放；留出入口、使用位置和通路，并满足后续关卡的采光与走廊要求，再点击“试住一下”。键盘可用方向键选格、Enter / 空格放置、R 旋转、Delete / 退格收回、Ctrl / Cmd + Z 撤销、Esc 取消选择或结束操作。

**借我一束光** 六关光线解谜。点击或轻触镜子改变光路，照亮所有植物，并避开熟睡的小猫；后续关卡加入书柜、固定镜子和双光源。Tab 选中镜子，Enter / 空格旋转；支持撤销、重置、递进提示和自由选关，没有倒计时。

**三小只的慢慢岛** 和吉伊、小八、乌萨奇散步、采集、钓鱼、种菜，准备野餐，也能进屋喝茶、看绘本和休息。WASD / 方向键移动，Shift 跑步，E 互动，空格跳跃，1 / 2 / 3 切换带队角色；B 背包、M 地图或室内导览、J 日记、R 回小屋或出门。也可点击地面和地点自动行走，手机使用摇杆与互动按钮。

## 存档与素材

存档只保存在当前浏览器的 `localStorage`，按网页来源（协议、域名、端口）隔离。原 Sites 与 GitHub Pages 的来源不同，原来的进度不会自动转移；换浏览器、清除网站数据也会影响存档。直接打开本地文件时，存储范围由浏览器决定，不保证随文件改名或移动而保留。三款游戏使用各自的存档键，不需要账号或后端。

《这也能住？》与《借我一束光》的图形由 SVG 绘制，内嵌 Adobe 思源黑体中文子集及完整 SIL Open Font License 1.1；英文通过系统字体栈显示，不分发 Helvetica 字体文件。《这也能住？》还保留字体来源与修改说明。

《三小只的慢慢岛》的岛屿和室内由 Canvas 绘制。吉伊、小八精灵取自用户提供的合照；乌萨奇采用已确认的手绘风格透明素材，同时保留用户指定参考图和合照作为加载回退。所有 PNG 均以原始字节内嵌，保留现有透明通道、朝向和绘制方式。
