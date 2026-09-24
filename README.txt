EdgeTech+ 2026 A0 HTML v6
============================

入口: poster.html
基于 v5 版式，单独存放，不覆盖 v5。

这一版的改动：
- 方案区主视觉改为 ESP32-S31 产品页上的软件栈概念图（Matter / ESP-IDF / ESP-GMF / ESP Private Agents 等）；
- 右侧标语不再压住 Matter 图标，方案卡片下方的空带分给了应用照片和说明；
- 四颗芯片的第一行统一为同一个无线图标；
- 规格统一为无线、CPU、内存 / GPIO、特长四行；ESP32-S31 写明クラシック Bluetooth；
- 方案为 Edge AI、HMI / GMF、RainMaker（含 ESP Private Agents）、MCP / Chatbot、Matter；
- 底部应用写软件方案和硬件功能，各约三句。

浏览器预览只缩放 1682×2378 画布。打印时整张画布放大到 A0（841×1189 mm）。
未做出血和 CMYK，不是印刷认证文件。

内容校对・技术核验（2026-09-24）
================================

本轮已完成两轮内容审校：第一轮重点核对日语、规格数据和应用依据；第二轮将文案调整为更适合日本技术展会海报的简洁表达。最终可见文案以 main 分支 poster.html 为准。

主要核验结论：
- ESP32-S31：保留 Wi-Fi 6、Bluetooth 5.4 / Classic Bluetooth、802.15.4、双核 RISC-V、最高 320 MHz、512 KB SRAM、60 GPIO、1000 Mbps Ethernet 等核心信息。当前官方 Datasheet 仍为 Preliminary，正式印刷前应再次确认最新版。
- ESP32-C5：保留 2.4 / 5 GHz Wi-Fi 6、Bluetooth LE、802.15.4、最高 240 MHz、384 KB SRAM、29 GPIO 等信息；应用定位调整为双频 IoT、网关、智能家电等，避免把无线摄像头作为主要推荐场景。
- ESP32-H21：保留 96 MHz、320 KB SRAM、19 GPIO、片上 DC-DC、最高 20 dBm 等信息；产品定位以低功耗 Bluetooth LE / 802.15.4 为主，Matter 作为上层应用能力呈现。
- ESP32-H4：保留 Bluetooth 5.4、Thread 1.4 / Zigbee 3.0、双核 RISC-V、最高 96 MHz、DSP、384 KB SRAM、40 GPIO、15 路触摸、外部 PSRAM、LE Audio / PAwR / Direction Finding，以及 Bluetooth 6.0 认证信息。
- 软件与应用：ESP-GMF、ESP-VISION、ESP-Matter、ESP Private Agents、Documentation MCP 等均按官方能力边界描述，避免把框架能力写成超出其职责的硬件能力。
- 日本法人：海报采用 2025年5月2日设立“楽鑫ジャパン株式会社”的表述。
- 日语风格：统一使用「エッジAI」「AIエージェント」「開発を加速」「低遅延」等更适合日本技术展会物料的表达。

官方核验来源：
- ESP32-S31 Series Datasheet: https://documentation.espressif.com/esp32-s31_datasheet_en.html
- ESP32-C5 Product Page: https://www.espressif.com/en/products/socs/esp32-c5
- ESP32-H21 Product Page: https://www.espressif.com/en/products/socs/esp32-h21
- ESP32-H4 Product Page: https://www.espressif.com/en/products/socs/esp32-h4
- ESP-GMF Documentation: https://docs.espressif.com/projects/esp-gmf/en/latest/
- ESP-VISION Documentation: https://docs.espressif.com/projects/esp-vision/en/latest/
- ESP-Matter Documentation: https://docs.espressif.com/projects/esp-matter/en/latest/
- ESP Private Agents Documentation: https://docs.agents.espressif.com/
- Espressif Documentation MCP Server: https://developer.espressif.com/blog/2026/04/doc-mcp-server/
- ESP-BLE-AUDIO (ESP32-H4): https://docs.espressif.com/projects/esp-idf/en/stable/esp32h4/api-reference/bluetooth/esp-ble-audio.html
- 楽鑫ジャパン株式会社: https://www.espressif.com/ja-jp/company/about-us/jp-company

官方品牌文案来源（2026-09-24）
==============================

海报中的装饰型英文 / 日文标语已统一替换为 Espressif 官方英文或日文页面、官方公司资料中实际使用的表述；产品标题和技术说明仍按海报场景保留，不强行改写为官网原句。

对应关系：
- BUILD SMART WITH ESPRESSIF
  来源：Espressif 英文官网首页 / About Espressif。
  https://www.espressif.com/en/home
  https://www.espressif.com/en/node/4770

- SHARE / CONNECT / INNOVATE
  来源：Espressif 官方年度报告、企业文化 / 招聘资料中持续使用的品牌表达。
  https://www.espressif.com/sites/all/themes/espressif/images/nusIoTBrochure/cn/Recruitment%20Brochure_25-26_EN.pdf?v=1

- Espressif と共にスマートに構築
  来源：Espressif 日文官网 About Espressif 页面。
  https://www.espressif.com/ja-jp/node/8844

- 私たちはアーティストの視点から技術を開発します。
  / WE DEVELOP TECHNOLOGY FROM AN ARTIST’S PERSPECTIVE.
  来源：Espressif 日文 / 英文官网 About Espressif 页面。
  https://www.espressif.com/ja-jp/node/8844
  https://www.espressif.com/en/node/4770

- ディープラーニング＆エッジコンピューティング
  / DEEP LEARNING & EDGE COMPUTING
  来源：Espressif 日文 / 英文官网 About Espressif 的技术能力栏目。
  https://www.espressif.com/ja-jp/node/8844
  https://www.espressif.com/en/node/4770

- ENGINEERING INTELLIGENT & CONNECTED SYSTEMS
  来源：Espressif 2026 官方公司介绍资料（About Company 2026）。
  https://www.espressif.com/sites/all/themes/espressif/images/about-espressif/About%20Company_2026_EN.pdf?v=2

